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
            print("Type quit, to end game")
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
            print(f"\n\nYou search the {option} and see")
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
            print("Goodbye")
            break
        else:  # else print options and ask for input
            print(f"I got, {str(menuName[key])[1:-1]} watchu want?")
            option = input("")
    for i in menuName[key]:  # checks which path the player chose
        if option == "go back":  # if go back, reruns previous menu
            choosenPath(menuName)


def printNDict(dictName):
    """Prints out content in a nested dictionary with up to 2 layers,
    takes dictName as the dictionary name.
    """
    for dictName, key in dictName.items():
        """loops through the keys in the nested dictionary, dictName, and then
        prints the nested dictionary names along with its values.
        """
        print(dictName.title() + ":")  # prints nested dictionary name
        for items in key:
            """loops through nested dictionary key values and and prints the
            key along with the value with a tab before.
            """
            print(f"\t{items.title()} - {key[items]}")
