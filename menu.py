# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Functions to create a menu interation system


def menuDesc(menuName, key):
    """Function that prints out a description for the path chosen"""
    print(key)
    print(f"\t{menuName[key]}")

def pathMenu(menuName):
    """Function that will take a dictionary, menuName, and converts it to a
    text-based menu
    """
    # Prints keys
    for key in menuName:
        print("\tPath " + key)
    # Input for choosing the menu
    choice = input("What path shall thoust choose? ")
    # Creates a list of keys for error checking
    choices = list(menuName)
    # Loop that checks if the user enter an invalid input
    while str(choice) not in choices:
        print(f"I got, {str(choices)[1:-1]} watchu want?")
        choice = input("")
        # Repeats input for choosing the menu
    for key in choices:
        if choice == key:
            # Prints out users choice
            print(f"You have chose Path {key}")
            menuDesc(menuName, choice)

def pathChoose():
    """Function to determine the next path the player will take"""
    print(pathMenu)
    for path in locations.paths:
        if str(path) == pathMenu:
            print(pathMenu)

startMenu = ["Play", "Quit", "Controls"]
difficultyChooser = ["Hard", "Normal", "Easy"]
escapeRoom = {
    "Cabinet":"",
    "Chest":"",
    "Bookcase":"",
    "Painting":"",
    "Desk":"",
}
