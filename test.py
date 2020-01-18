# Josh Lim
# Comp Sci 30 P4
# 01/09/2020
# File to run code
import map
from player import Player
import action as act
import os


def intro():
    """Function for intro sequence and accepting name"""
    print("Welcome to escape room")
    name = input("Name: ").title  # gets the name of the player
    os.system('cls')  # clears the terminal
    return name  # returns the name of the player


player = Player(intro())  # creates an instance of player class
escapeRoom = map.map  # sets game map to equal escape escape room
arrayMaxX = map.findMax(escapeRoom) + 1  # finds max x
arrayMaxY = map.findMax(escapeRoom)  # finds max y


def play():
    """Function to run the game"""
    # while the player hasn't won nor gave up...
    while not player.win and not player.giveUp:
        # sets action flag to false to tell if player has inputed a action or
        # an invalid input
        actionFlag = False
        room = map.tileAt(player.y, player.x)  # gets where the player is
        if player.win is True:  # if player won
            break
        elif player.giveUp is True:  # if player gave up
            break
        elif player.turnCounter >= 91:  # if player exceeds 91 turns
            print("You have surpassed 90 turns and ran out of time, you lose")
            break
        else:
            print("Turn " + str(player.turnCounter))  # prints turn counter
            # highlights the players position on the map
            map.highlightPos(player.y, player.x, escapeRoom)
            print("\n" + room.desc + "\n")  # prints the tile description
            # generates available actions
            availableActions = room.availableActions(arrayMaxX, arrayMaxY)
            print("What would you like to do? \n")
            for a in availableActions:  # prints out available actions
                print(
                    "{}: {} \t ".format(a.hotKey[0].title(), a.name.title()),
                    end=""
                    )
                # prints actions on a new line if the last key was search
                if a.name == "search":
                    print("")
            userIn = input("\nAction: ")  # gets the user input
            os.system('cls')  # clears terminal
            # checks if user input is equal to available actions hot key
            for a in availableActions:
                if userIn in a.hotKey:
                    player.turnCounter += 1  # adds one to turn counter
                    action = a  # sets the action object to a
                    actionFlag = True  # sets the action flag to true
            # if player enter an invalid input or no input
            if not actionFlag:
                print("Invalid input")
            # if player enter a valid input
            else:
                player.doAction(action, room, **a.kwargs)  # execute action
                room.modifyPlayer(player)  # modify player


play()  # plays game
