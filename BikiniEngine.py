from os import system, name
from time import sleep
#from playsound import playsound

########################################################################
###############################VISUAL PART##############################
########################################################################

def clear():
        if name == "nt":
            system("cls")
        else:
            system("clear")

def draw(art,text, speed_of_text):
    system("clear")
    with open(f"art/{art}", 'r', encoding='utf-8') as file:
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


def animation(art):
    with open(f"anim/{art}", 'r', encoding='utf-8') as file:
        art = file.read()
    for i in range(2):
        clear()
        sleep(0.5)
        print(f"""{art}""")
        sleep(0.5)

#def sound(sound):
#    playsound(f"sounds/{sound}")





