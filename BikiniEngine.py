from os import system, name
from time import sleep

def clear():
        if name == "nt":
            system("cls")
        else:
            system("clear")

def draw(art,text, speed_of_text):
    system("clear")
    with open(art, 'r', encoding='utf-8') as file:
        art = file.read()
    print(f"""{art}""")
    def print_smooth(text):
        for char in text:
            print(char, end="", flush=True)
            sleep(speed_of_text)
        print()
    print_smooth(text)
    user_mesage = str(input("»» "))
    return user_mesage


#def draw_with_selection(text,art, selection):
#    system("clear")
#    with open(art, 'r', encoding='utf-8') as file:
#        art = file.read()
#    print(f"""{art}""")
#    def print_smooth(text):
#        for char in text:
#            print(char, end="", flush=True)
#            sleep(0.05)
#        print()
#    print_smooth(text)

