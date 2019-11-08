# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Functions to create a menu interaction system


def choosenPath(menuName):
    """Function that will take a dictionary, menuName, and converts it to a
    text-based menu
    """
    for key in menuName:  # Prints keys
        if key == "description":
            print(f"{menuName[key].capitalize()}")
        else:
            print("\t- " + key.title())
    # Input for choosing the menu
    option = input("Where would you like to search? ")
    option = option.lower()
    options = list(menuName)  # Creates a list of keys for error checking
    options.remove("description")  # removes description from options
    # Loop that checks if the user enter an invalid input or quit
    while option not in options or option == "quit":
        if option == "quit":  # if quit, quit
            print("I'll see you later ;)")
            break
        else:  # else print options and ask for input
            print(f"I got, {str(options)[1:-1]} watchu want?")
            option = input("")
    for i in options:
        if option == i:  # Checks which path player chooses
            print(f"You search the {option} and see\n")
            menuLDesc(menuName, option)  # prints out next menu


def menuLDesc(menuName, key):
    """Function that takes a dictionary, menuName, and converts it to a
    text-based menu for the key, key, only works if the key value paired of the
    key is a list
    """
    print(f"{key.title()}:")  # prints the option player choose
    for items in menuName[key]:  # prints the options that goes with the option
        print(f"\t- {items}")
    option = input("What would you like to search? ")  # takes another input
    option = option.lower()
    # Checks if user entered a valid input or quit
    while option not in menuName[key] or option == "quit":
        if option == "quit":  # if quit, quit
            print("Have a good night hun")
            break
        else:  # else print options and ask for input
            print(f"I got, {str(menuName[key])[1:-1]} watchu want?")
            option = input("")
    for i in menuName[key]:  # checks which path the player chose
        if option == "go back":  # if go back, reruns previous menu
            choosenPath(menuName)

escapeRoom = {
    "description": "you find yourself in a room, in it you see...",
    "cabinet": ["go back"],
    "chest": ["go back"],
    "bookcase": ["go back"],
    "painting": ["go back"],
    "desk": ["go back"],
}

choosenPath(escapeRoom)
