import BikiniEngine

user_massage = BikiniEngine.draw("start_screen.txt", "GAME FOR EXAMPLE", 0.05)
if user_massage == "exit":
    exit()
elif user_massage == "start":
    BikiniEngine.draw("first_screen.txt", "This game was created as an example. Now I will show you what the Bikini engine is capable of.", 0.05)
    BikiniEngine.draw("human.txt", "This is a Vladik", 0.05)
    BikiniEngine.draw("human.txt", "He very bad person.", 0.05)
    BikiniEngine.draw("human.txt", "His mama digging under Denis. ", 0.05)
    t = BikiniEngine.draw("human.txt", "Shall we help Vladik’s mom, or not? ", 0.05)
    if t == "yes":
        BikiniEngine.draw("mama_kill_denis.txt", "We buried Denis in the courtyard of School No. 25. ", 0.05)
        BikiniEngine.draw("the_end_screen.txt", "The end!", 0.05)
    else:
        BikiniEngine.draw("vladik_die.txt", "Vladik burst into tears and fell down the stairs.", 0.05)
        BikiniEngine.draw("the_end_screen.txt", "The end!", 0.05)
elif user_massage == "help":
    BikiniEngine.clear()
    BikiniEngine.draw("help_screen.txt", "undestand?", 0.05)
