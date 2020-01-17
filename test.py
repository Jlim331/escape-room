# Josh Lim
# Comp Sci 30 P4
# 01/09/2020
# File to run code
import map
from player import Player
import action as act
import os


def intro():
    print("Welcome to escape room")
    name = input("Name: ").title
    os.system('cls')
    return name


player = Player(intro())


escapeRoom = map.map
arrayMaxX = map.findMax(escapeRoom) + 1  # finds max x
arrayMaxY = map.findMax(escapeRoom)  # finds max y


def play():
    while not player.win and not player.giveUp:
        actionFlag = False
        room = map.tileAt(player.y, player.x)
        if player.win == True:
            break
        elif player.giveUp == True:
            break
        # elif player.turnCounter >= 91:
        #     print("You have surpassed 90 turns and ran out of time, you lose")
        #     break
        else:
            print("Turn " + str(player.turnCounter))
            map.highlightPos(player.y, player.x, escapeRoom)
            print("\n" + room.desc + "\n")
            availableActions = room.availableActions(arrayMaxX, arrayMaxY)
            print("What would you like to do? \n")
            for a in availableActions:
                print("{}: {} \t ".format(a.hotKey[0].title(), a.name.title())
                ,end = "")
                if a.name == "search":
                    print("")
            userIn = input("\nAction: ")
            os.system('cls')
            for a in availableActions:
                if userIn in a.hotKey:
                    player.turnCounter += 1
                    action = a
                    actionFlag = True
            if not actionFlag:
                print("Invalid input")
            else:
                player.doAction(action, room, **a.kwargs)
                room.modifyPlayer(player)


play()
