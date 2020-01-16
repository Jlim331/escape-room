# Josh Lim
# Comp Sci 30 P4
# 01/09/2020
# File to test code
import map
from player import Player
from collections import OrderedDict
import action as act
import os
import re


def intro():
    print("Welcome to escape room")
    name = input("Name: ").title
    os.system('cls')
    return name

player = Player(intro())

escapeRoom = map.map
arrayMaxX = map.findMax(escapeRoom) + 1  # finds max x
arrayMaxY = map.findMax(escapeRoom)  # finds max y

def getAvailaibleAction(room, player):
    actions = OrderedDict()


def play():
    while not player.win and not player.giveUp:
        actionFlag = False
        room = map.tileAt(player.y, player.x)
        if player.win == True:
            break
        elif player.giveUp == True:
            break
        else:
            print(room.name.title().center(96, "-"))
            print(room.desc)
            availableActions = room.availableActions(arrayMaxX, arrayMaxY)
            for a in availableActions:
                print("{}: {} \t ".format(a.hotKey[0].title(), a.name.title()), end = "")
                if a.name == "search":
                    print("")
            userIn = input("\nAction: ")
            os.system('cls')
            for a in availableActions:
                if userIn in a.hotKey:
                    action = a
                    actionFlag = True
            if not actionFlag:
                print("Invalid input")
            else:
                player.doAction(action, room, **a.kwargs)
                room.modifyPlayer(player)


play()
