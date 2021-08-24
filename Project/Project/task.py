import sys


# Write a function for each scene
# Use paper to map out how your game will play before
# you begin

def die():
    """Death scene, uses sys.exit to end the program
    can reuse this multiple times"""
    print("you died :(")
    sys.exit()


def start():
    """First scene calls itself with the else to deal with
     unexpected input"""
    print("You are in a dark cave there are passages "
          "that go to the left and right")
    user = input("Which way do you go [left] or [right]?")
    if user == "left":
        win()
    elif user == "right":
        bear()
    else:
        print("Not a valid choice")
        start()


def bear():
    """Bear scene don't fight the bear"""
    print("There is an angry bear sleeping on a pile of gold"
          "do you fight it or go back to safety?")
    user = input("What do you choose [fight] or [safety]?")
    if user == "fight":
        print("The bear wakes up. It doesn't end well.")
        die()
    elif user == "safety":
        print("Good choice that bear looked pretty scary.")
        start()


def win():
    """Winning scene uses sys.exit() to end the program"""
    print("You escaped from the cave well done")
    sys.exit()


# Run the program by calling the first scene start()

start()
