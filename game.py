# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# File to import files to play the game
import player
import map as mp
import format as form
import os


def titleScreenSelctions():
    option = input("").lower()
    if option in ["play", "p"]:
        play():
    elif option in ["help", "h"]:
        helpMenu()
    elif option in ["quit", "q"]:
        sys.exit()


def titleScreen():
    os.system('cls')
    print("")

def helpScreen():
    None

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
    print(player.findPos())
    # takes input
    userIn = input().lower()
    # checks input for "up" or "w"
    try:
        if userIn in ["up", "w"]:
            # moves player up
            player.moveUp()
            # error handling if player tries to go out of map
            if player.y < 0:
                os.system("cls")
                print("Why you tryna go there?")
                player.y += 1
                # prints out table
                mp.highlighPos(player.y, player.x, escapeRoom)
            else:
                # prints out table
                os.system("cls")
                mp.highlighPos(player.y, player.x, escapeRoom)
        # checks input for "down" or "s"
        elif userIn in ["down", "s"]:
            # moves player down
            player.moveDown()
            # error handling if player tries to go out of map
            if player.y > arrayMaxY:
                os.system("cls")
                print("Why you tryna go there?")
                player.y -= 1
                # prints out table
                mp.highlighPos(player.y, player.x, escapeRoom)
            else:
                # prints out table
                os.system("cls")
                mp.highlighPos(player.y, player.x, escapeRoom)
        # checks input for "right" or "d"
        elif userIn in ["right", "d"]:
            # moves player right
            player.moveRight()
            # error handling if player tries to go out of map
            if player.x > arrayMaxX:
                os.system("cls")
                print("Why you tryna go there?")
                player.x -= 1
                # prints out table
                mp.highlighPos(player.y, player.x, escapeRoom)
            else:
                # prints out table
                os.system("cls")
                mp.highlighPos(player.y, player.x, escapeRoom)
        # checks input for "left" or "a"
        elif userIn in ["left", "a"]:
            # moves player left
            player.moveLeft()
            # error handling if player tries to go out of map
            if player.x < 0:
                os.system("cls")
                print("Why you tryna go there?")
                player.x += 1
                # prints out table
                mp.highlighPos(player.y, player.x, escapeRoom)
            else:
                # prints out table
                os.system("cls")
                mp.highlighPos(player.y, player.x, escapeRoom)
        # checks input for "i" or "inventory"
        elif userIn in ["inventory", "i"]:
            os.system("cls")
            mp.highlighPos(player.y, player.x, escapeRoom)
            print("\nOpening Inventory...\nInventory:")
            player.invGen()  # generates and prints inv
        # checks input for "q or "quit"
        elif userIn in ["quit", "q"]:
            print("thank you for playing")
            flag = False  # breaks loop
        # if input is none of the above then ask for it again
        else:
            os.system("cls")
            mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
            print("Invalid input, please try again")
    except:
        os.system("cls")
        mp.highlighPos(player.y, player.x, escapeRoom)  # prints out table
        print("Invalid input, please try again")
