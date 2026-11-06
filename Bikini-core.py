import os
from time import sleep


user_flags = True
user_answer = ""




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
    with open("qwerty.txt", "r", encoding="utf-8") as f: #Добавь позже чтобы можно было любой файл скрипта тут открывать
        while True:                                      #Основной цикл
            line = f.readline()                          #Чтение построчно скрипта
            command = line.partition("<")[0].lower()     #Перевод всех команд в нижний регистр
            if '<' in line and '>' in line:              #Получение аргумента из символов <>
                arguments = line.split('<')[1].split('>')[0]
            else:
                continue

            match command:                               #Все возможные команды
                case "draw":
                    while True:
                        clear()
                        print(pictures)
                        print_smooth(arguments)
                        print()
                        user_answers()
                        if user_flags == False:
                            break

                case "set_pictures":
                    pictures = arguments
                case "":
                    print(25)
                case "choice":
                    call_choise = arguments.split(",")
                    print()




            if not line:  # Достигнут конец файла (EOF)
                break
            #print(line.rstrip('\n'))
            #print(command)
            #print(arguments)
        break


