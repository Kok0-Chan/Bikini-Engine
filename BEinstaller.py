import os
import time
import sys

directory = ""
name_folder = ""


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def type_print(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def progress_bar(label, seconds=2.0, width=40):
    """Прогресс-бар: заполняется за seconds секунд."""
    steps = 60
    sleep_per_step = seconds / steps
    for i in range(steps + 1):
        filled = int(width * i / steps)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(100 * i / steps)
        sys.stdout.write(f"\r  {label:<12} [{bar}] {percent:3d}%")
        sys.stdout.flush()
        time.sleep(sleep_per_step)
    print()


def robot_spin(seconds=1.5):
    """Крутящийся робот — свистоперделка."""
    frames = [
        r"""
     .--.
    |o_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
""",
        r"""
     .--.
    |o_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
""",
        r"""
     .--.
    |O_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
""",
        r"""
     .--.
    |o_O |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
""",
    ]
    end = time.time() + seconds
    idx = 0
    while time.time() < end:
        clear()
        print("  Установка... подождите")
        print(frames[idx % len(frames)])
        idx += 1
        time.sleep(0.15)


start_screen = r"""
████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█  *************************                                                   █
█  *BIKINI ENGINE INSTALLER*                                                   █
█  *************************                                                   █
█                                                                              █
█                                              .--.                            █
█  [1] - select directory                     |o_o |                           █
█                                             |:_/ |      +----------------+   █
█  [2] - name your game                      //   \ \     | BIKINI ENGINE  |   █
█                                           (|     | )    |   v0.01        |   █
█                                          /'\_   _/`\    +----------------+   █
█                                          \___)=(___/                         █
█                                                                              █
█                                                                              █
█                                                                              █
█                                                                              █
█                                                                              █
█                                                                              █
████████████████████████████████████████████████████████████████████████████████"""

start_screen_2 = r"""
████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█                                                                              █
█                                                                              █
█    *******************************************                               █
█    *To begin the installation, type <install>*                               █
█    *******************************************                               █
█                                                                              █
█                                                                              █
█                                                                              █
█                                        .--.                                  █
█                                       |o_o |                                 █
█                                       |:_/ |      +----------------+         █
█                                      //   \ \     | NICE!          |         █
█                                     (|     | )    |                |         █
█                                    /'\_   _/`\    +----------------+         █
█                                    \___)=(___/                               █
█                                                                              █
█                                                                              █
████████████████████████████████████████████████████████████████████████████████"""

dir_screen = r"""
████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█                                                                              █
█                                                                              █
█                                                                              █
█      ******************************************************************      █
█      *Please specify the path where the project folder will be created*      █
█      ******************************************************************      █
█                                                                              █
█                                                                              █
█                                          <yo>                                █
█                                     .--.                                     █
█                                    |o_o |                                    █
█                                    |:_/ |                                    █
█                                   //   \ \                                   █
█                                  (|     | )                                  █
█                                 /'\_   _/`\                                  █
█                                 \___)=(___/                                  █
█                                                                              █
████████████████████████████████████████████████████████████████████████████████"""

name_screen = r"""
████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█                                                                              █
█                                                                              █
█                                                                              █
█                                                                              █
█                       ********************************                       █
█                       *Enter the name of your project*                       █
█                       ********************************                       █
█                                                                              █
█                                                                              █
█                                  <Cool name for a game. I’d play it>         █
█                              .--.                                            █
█                             |>_< |                                           █
█                             |:_/ |                                           █
█                            //   \ \                                          █
█                           (|     | )                                         █
█                          /'\_   _/`\                                         █
█                          \___)=(___/                                         █
████████████████████████████████████████████████████████████████████████████████"""


# ---------- Шаблоны файлов проекта ----------
MAIN_PY = '''import os
from engine import run_script

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base)
    run_script("qwerty.txt", "art")
'''

ENGINE_PY = '''import os
import time


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def type_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def parse_line(line):
    command = line.partition("<")[0].strip().lower()
    if "<" in line and ">" in line:
        arguments = line.split("<", 1)[1].split(">", 1)[0]
        return command, arguments
    return None


def collect_choice(lines, start_idx):
    options = []
    current = None
    i = start_idx
    while i < len(lines):
        parsed = parse_line(lines[i])
        if parsed:
            cmd, arg = parsed
            if cmd == "choice" and arg == "end":
                return options, i + 1
            if cmd == "option":
                current = (arg, [])
                options.append(current)
                i += 1
                continue
        if current is not None:
            current[1].append(lines[i])
        i += 1
    return options, i


def run_lines(lines, art_dir):
    pictures = ""
    i = 0
    while i < len(lines):
        parsed = parse_line(lines[i])
        if not parsed:
            i += 1
            continue
        command, arguments = parsed

        if command == "set_pictures":
            path = os.path.join(art_dir, arguments.strip())
            try:
                with open(path, "r", encoding="utf-8") as f:
                    pictures = f.read()
            except FileNotFoundError:
                pictures = f"[нет файла арта: {path}]"

        elif command == "draw":
            clear()
            print(pictures)
            type_print(arguments)
            print()
            ans = input("»» ").strip()
            if ans == "quit" or ans == "":
                return

        elif command == "choice":
            if arguments == "end":
                i += 1
                continue
            question = arguments
            options, next_i = collect_choice(lines, i + 1)
            if not options:
                i = next_i
                continue
            while True:
                clear()
                print(pictures)
                type_print(question)
                print()
                for n, (label, _body) in enumerate(options, start=1):
                    print(f"  {n}. {label}")
                print()
                ans = input("»» ").strip()
                if ans.lower() == "quit":
                    return
                if ans.isdigit() and 1 <= int(ans) <= len(options):
                    _label, body = options[int(ans) - 1]
                    run_lines(body, art_dir)
                    break
                print("Нет такого варианта.")
                time.sleep(1)
            i = next_i
            continue

        elif command == "end":
            return

        i += 1


def run_script(script_path, art_dir):
    with open(script_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    run_lines(lines, art_dir)
'''

QWERTY_TXT = '''set_pictures<start.txt>
draw<Добро пожаловать в новую игру!>

choice<Куда пойдёшь?>
option<Налево>
    draw<Ты пошёл налево и нашёл клад!>
option<Направо>
    draw<Ты пошёл направо и встретил дракона.>
option<Нахуй>
    draw<Приключение окончено.>
choice<end>

draw<Конец.>
end<>
'''

START_ART = r"""
+--------------------+
|   НОВАЯ ИГРА       |
|   Bikini Engine    |
+--------------------+
"""


def install_project(base_dir, game_name):
    """Создаёт проект: папка игры, art/, main.py, engine.py, qwerty.txt."""
    project_dir = os.path.join(base_dir, game_name)
    art_dir = os.path.join(project_dir, "art")

    # 1. Папки
    progress_bar("Папки", seconds=1.2)
    os.makedirs(project_dir, exist_ok=False)
    os.makedirs(art_dir, exist_ok=True)

    # 2. art/start.txt
    progress_bar("Арт", seconds=0.8)
    with open(os.path.join(art_dir, "start.txt"), "w", encoding="utf-8") as f:
        f.write(START_ART)

    # 3. main.py
    progress_bar("main.py", seconds=0.8)
    with open(os.path.join(project_dir, "main.py"), "w", encoding="utf-8") as f:
        f.write(MAIN_PY)

    # 4. engine.py
    progress_bar("engine.py", seconds=1.0)
    with open(os.path.join(project_dir, "engine.py"), "w", encoding="utf-8") as f:
        f.write(ENGINE_PY)

    # 5. qwerty.txt
    progress_bar("qwerty.txt", seconds=0.6)
    with open(os.path.join(project_dir, "qwerty.txt"), "w", encoding="utf-8") as f:
        f.write(QWERTY_TXT)

    return project_dir


# ---------- Основной цикл установщика ----------
while True:
    clear()

    # Если и путь, и имя заданы — предлагаем установку
    if len(directory) > 0 and len(name_folder) > 0:
        print(start_screen_2)
        a = input("-> ").strip().lower()
        clear()

        if a != "install":
            print("Введите <install> для начала установки.")
            time.sleep(1.5)
            continue

        # --- Свистоперделка ---
        robot_spin(seconds=1.5)
        clear()
        type_print("  Проверка путей...", delay=0.01)
        time.sleep(0.5)

        base_dir = os.path.abspath(directory)
        try:
            project_dir = install_project(base_dir, name_folder)
        except FileExistsError:
            clear()
            print(f"Ошибка: папка уже существует: {os.path.join(base_dir, name_folder)}")
            break
        except FileNotFoundError:
            clear()
            print(f"Ошибка: неверный путь (родительская папка не существует): {base_dir}")
            break
        except Exception as e:
            clear()
            print(f"Ошибка установки: {e}")
            break

        # --- Финальный экран ---
        clear()
        type_print("  Установка завершена!", delay=0.02)
        print()
        print(f"  Проект: {project_dir}")
        print(f"  Запуск: python \"{os.path.join(project_dir, 'main.py')}\"")
        print()
        time.sleep(0.5)
        break

    # --- Главное меню ---
    print(start_screen)
    a = input("-> ").strip()
    clear()

    if a == "1":
        clear()
        print(dir_screen)
        directory = input("-> ").strip()
        clear()

    elif a == "2":
        clear()
        print(name_screen)
        name_folder = input("-> ").strip()
        clear()

    else:
        print("Введите 1 или 2.")
        time.sleep(1)