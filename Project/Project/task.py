import sys


def die():
    """Death scene, uses sys.exit to end the program
    can reuse this multiple times"""
    print("you died :(")
    sys.exit()


def scene1():
    """Scene 1"""
    print("You are somewhere")
    print("You can make a good choice or a bad choice")
    choice = input("Do you make the [good] choice or the [bad] choice?")

    if choice == "good":
        print("That was a good choice. You keep walking")
        scene2()

    elif choice == "bad":
        print("That was a bad choice. You get eaten by a bear.")
        die()

    else:
        print("Please choose [good] or [bad]")
        scene1()


def scene2():
    """Scene 2"""
    print("Welcome to scene 2")
    choice = input("Do you make the [good] choice or the [bad] choice?")

    if choice == "good":
        print("That was a good choice")
        scene3()

    elif choice == "bad":
        print("That was a bad choice")
        die()

    else:
        print("Please choose [good] or [bad]")
        scene1()


# Call scene1() to run the game
scene1()
