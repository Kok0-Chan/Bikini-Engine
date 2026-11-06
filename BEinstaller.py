import os
directory = ""
name_folder = ""

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
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

while True:
    clear()
    if len(directory) > 0 and len(name_folder) > 0:
        print(start_screen_2)
        a = str(input("-> "))
        clear()
        try:
            os.mkdir(directory)
            os.mkdir(directory + "/art")
            os.mkdir(directory + "/anim")
            print(f"Folder '{directory}' created successfully.")
            full_directory = os.path.join(directory, name_folder)
            with open(full_directory + ".py", "w", encoding="utf-8") as f:
                f.write("""HelloWorld(print)""")
            print(f"file '{full_directory}' created successfully.")
            break
        except FileExistsError:
            print("Error: Folder already exists.")
            break
        except FileNotFoundError:
            print("Error: Invalid path (parent directory does not exist).")
            break
    print(start_screen)
    a = int(input("-> "))
    clear()
    if a == 1:
        clear()
        print(r"""
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
████████████████████████████████████████████████████████████████████████████████""")
        directory = str(input("-> "))
        clear()
    elif a == 2:
        clear()
        print(r"""
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
████████████████████████████████████████████████████████████████████████████████""")
        name_folder = str(input("-> "))
