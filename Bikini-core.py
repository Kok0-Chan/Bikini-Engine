import os
from time import sleep
import itertools


user_flags = True
user_answer = ""
pictures = ""
user_flags = True
user_answer = ""
pictures = ""
choice_depth = 0



def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def user_answers():
    global user_flags       #Флаг для завершения основного цикла
    global user_answer      #Ввод пользователя
    user_answer = input("»» ")
    match user_answer:      #Все варианты ответа ввода пользователя
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
    for char in text:
        print(char, end="", flush=True)
        sleep(0.05)



while True:
    # Открываем файл со скриптом (пока жёстко qwerty.txt)
    with open("qwerty.txt", "r", encoding="utf-8") as f:

        # Основной цикл читаем файл построчно, пока не кончится
        while True:

            # Читаем одну строку из файла
            line = f.readline()

            # Если строка пустая - файл закончился, выходим из внутреннего цикла
            if not line:
                break

            # Всё, что стоит ДО первого символа "<" — это имя команды.
            # .strip() убирает пробелы/переводы строк, .lower() приводит к нижнему регистру
            command = line.partition("<")[0].strip().lower()

            # Если в строке есть и "<", и ">" — вытаскиваем аргумент между ними
            if '<' in line and '>' in line:
                # split('<', 1) делит строку по ПЕРВОМУ "<" на две части,
                # берём [1] (то, что после "<"), затем split('>', 1)[0] берёт всё до первого ">"
                arguments = line.split('<', 1)[1].split('>', 1)[0]
            else:
                # Строка без аргумента в "<>" — пропускаем (это не команда)
                continue

            # Определяем, что за команда, и выполняем её
            match command:

                # --- Команда "draw" — вывести картинку + текст и ждать ввода ---
                case "draw":
                    while True:
                        clear()                      # очищаем экран я заеался уже нахуй
                        print(pictures)              # печатаем текущую картинку
                        print_smooth(arguments)      # плавно печатаем текст из <>
                        print()                      # пустая строка после текста
                        user_answers()               # ждём ответа пользователя
                        if user_flags == False:      # если пользователь ввёл quit или пусто
                            break                    # выходим из цикла draw

                # --- Команда "set_pictures" — задать текущую картинку ---
                case "set_pictures":
                    pictures = arguments             # запоминаем картинку в глобальную переменную

                # --- Команда "choice" — граница блока-развилки --- нихуя я нарисовал
                case "choice":
                    if arguments == "start":
                        choice_depth += 1            # открыли блок choice
                    elif arguments == "end":
                        if choice_depth > 0:
                            choice_depth -= 1        # закрыли блок choice
                        else:
                            print("Ошибка: choice<end> без choice<start>")
                    else:
                        print(f"Неизвестный аргумент choice: {arguments}")

                # --- Пустая команда (строка вида "<...>" без имени) ---
                case "":
                    print(25)                        # заглушка, как было в оригинале

            # Если команда "end" — достигнут конец скрипта, выходим из внутреннего цикла
            if command == "end":
                break

        # Внешний цикл тоже прерываем — файл прочитан один раз
        break

