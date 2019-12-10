# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# File to import files to play the game
import player
import map as mp
import format as form


print("Hello what is your name?")  # initiates game with an intro
name = input("Name: ").title()  # store input
player = player.Player(name, ["Test"])  # creates player class

flag = True  # flag to keep while loop going

escapeRoom = mp.map  # sets map array to a variable
arrayMaxX = mp.findMax(escapeRoom) + 1  # finds max x
arrayMaxY = mp.findMax(escapeRoom)  # finds max y


mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
while flag:
    # prints options
    print("W: GO UP\tA: GO RIGHT\tQ: quit")
    print("D: GO LEFT\tS: GO DOWN\tI: Inventory")
    print("What would you like to do?")
    # takes input
    userIn = input().lower()
    # checks input for "up" or "w"
    if userIn in ["up", "w"]:
        # moves player up
        player.moveUp()
        # error handling if player tries to go out of map
        if player.y < 0:
            print(
                form.Colors.RED + "Why you tryna go there?" + form.Colors.END
            )
            player.y += 1
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
        else:
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
    # checks input for "down" or "s"
    elif userIn in ["down", "s"]:
        # moves player down
        player.moveDown()
        # error handling if player tries to go out of map
        if player.y > arrayMaxY:
            print(
                form.Colors.RED + "Why you tryna go there?" + form.Colors.END
            )
            player.y -= 1
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
        else:
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
    # checks input for "right" or "d"
    elif userIn in ["right", "d"]:
        # moves player right
        player.moveRight()
        # error handling if player tries to go out of map
        if player.x > arrayMaxX:
            print(
                form.Colors.RED + "Why you tryna go there?" + form.Colors.END
            )
            player.x -= 1
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
        else:
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
    # checks input for "left" or "a"
    elif userIn in ["left", "a"]:
        # moves player left
        player.moveLeft()
        # error handling if player tries to go out of map
        if player.x < 0:
            print(
                form.Colors.RED + "Why you tryna go there?" + form.Colors.END
            )
            player.x += 1
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
        else:
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
    # checks input for "i" or "inventory"
    elif userIn in ["inventory", "i"]:
        print("\nOpening Inventory...\nInventory:")
        player.invGen()  # generates and prints inv
    # checks input for "q or "quit"
    elif userIn in ["quit", "q"]:
        print("thank you for playing")
        flag = False  # breaks loop
    # if input is none of the above then ask for it again
    else:
        print(
            form.Colors.RED + "Invalid input, please try again" +
            form.Colors.END
        )
        mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
