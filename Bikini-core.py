import os
from time import sleep


# ---------- Глобальные переменные ----------
user_flags = True       # флаг работы основного цикла (False = выходим из draw)
user_answer = ""        # последний ввод пользователя
pictures = ""           # текущая картинка (задаётся через set_pictures)
flags = set()           # активные флаги (set_flag / clear_flag)


# ---------- Служебные функции ----------

def clear():
    """Очищает экран (под Windows и Linux/Mac)."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def user_answers():
    """Читает ответ пользователя после draw. 'quit' или пустой ввод — выход."""
    global user_flags
    global user_answer
    user_answer = input("»» ")
    match user_answer:
        case "quit":
            user_flags = False
        case "help":
            print(25)
        case _:
            if user_answer == "":
                user_flags = False
            else:
                print("Please enter a valid answer.")


def print_smooth(text):
    """Печатает текст по буквам с задержкой (эффект печатной машинки)."""
    for char in text:
        print(char, end="", flush=True)
        sleep(0.05)


def parse_line(line):
    """
    Разбирает строку вида 'command<arguments>' в кортеж (command, arguments).
    Если в строке нет <...> — возвращает None (это не команда).
    """
    command = line.partition("<")[0].strip().lower()
    if '<' in line and '>' in line:
        arguments = line.split('<', 1)[1].split('>', 1)[0]
        return command, arguments
    return None


def collect_choice(lines, start_idx):
    """
    Собирает ветки choice, начиная со строки start_idx (сразу после 'choice<Вопрос>').
    НЕ выполняет команды — просто раскладывает строки по вариантам.

    Возвращает:
      options — список пар (подпись_варианта, [строки_тела])
      index_после_choice_end — индекс строки, следующей за 'choice<end>'
    """
    options = []
    current = None          # текущая собираемая ветка: (подпись, [строки])
    i = start_idx

    while i < len(lines):
        parsed = parse_line(lines[i])

        if parsed:
            cmd, arg = parsed

            # Встретили choice<end> — развилка закончилась
            if cmd == "choice" and arg == "end":
                return options, i + 1

            # Встретили option<...> — начинаем новую ветку
            if cmd == "option":
                current = (arg, [])
                options.append(current)
                i += 1
                continue

        # Обычная строка — добавляем в тело текущей ветки (если она уже открыта)
        if current is not None:
            current[1].append(lines[i])

        i += 1

    # Если choice<end> не нашли — возвращаем что собрали
    return options, i


def run_lines(lines):
    """
    Выполняет список строк скрипта.
    Рекурсивно вызывает себя для выбранной ветки choice,
    поэтому вложенные choice работают.
    """
    global pictures, user_flags

    i = 0
    while i < len(lines):
        parsed = parse_line(lines[i])

        # Строка без <...> — не команда, пропускаем
        if not parsed:
            i += 1
            continue

        command, arguments = parsed

        match command:

            # ---------- draw: показать картинку + текст и ждать ввода ----------
            case "draw":
                while True:
                    clear()
                    print(pictures)
                    print_smooth(arguments)
                    print()
                    user_answers()
                    if user_flags == False:
                        break

            # ---------- set_pictures: задать текущую картинку ----------
            case "set_pictures":
                pictures = arguments

            # ---------- set_flag: включить флаг ----------
            case "set_flag":
                flags.add(arguments.strip().lower())

            # ---------- clear_flag: выключить флаг ----------
            case "clear_flag":
                flags.discard(arguments.strip().lower())

            # ---------- choice: развилка (игра спрашивает игрока) ----------
            case "choice":

                # Одиночный choice<end> без пары — просто пропускаем
                if arguments == "end":
                    i += 1
                    continue

                # choice<Вопрос> — начало развилки.
                # arguments здесь — текст вопроса, который увидит игрок.
                question = arguments

                # Собираем все option-ветки до choice<end>
                options, next_i = collect_choice(lines, i + 1)

                # Если вариантов нет — некорректный скрипт, идём дальше
                if not options:
                    print("Развилка без вариантов!")
                    i = next_i
                    continue

                # --- Меню: спрашиваем игрока, пока он не введёт корректный номер ---
                while True:
                    clear()
                    print(pictures)
                    print_smooth(question)
                    print()
                    for n, (label, _body) in enumerate(options, start=1):
                        print(f"  {n}. {label}")
                    print()

                    ans = input("»» ").strip()

                    # Выход из игры
                    if ans.lower() == "quit":
                        user_flags = False
                        return

                    # Корректный номер — выполняем ТОЛЬКО выбранную ветку
                    if ans.isdigit() and 1 <= int(ans) <= len(options):
                        chosen_label, chosen_body = options[int(ans) - 1]
                        run_lines(chosen_body)   # рекурсивный вызов
                        break

                    # Некорректный ввод — просим ещё раз
                    print("Нет такого варианта. Введи число.")
                    sleep(1)

                # Продолжаем выполнение после choice<end>
                i = next_i
                continue

            # ---------- end: конец скрипта ----------
            case "end":
                return

        i += 1


# ---------- Точка входа ----------
if __name__ == "__main__":
    # Читаем весь файл скрипта в список строк
    with open("qwerty.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    # Запускаем выполнение
    run_lines(all_lines)