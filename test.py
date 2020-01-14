# Josh Lim
# Comp Sci 30 P4
# 01/09/2020
# File to test code
import map
from player import Player
from collections import OrderedDict
import action as act


def intro():
    print("Welcome to escape room")
    name = input("Name: ").title
    return name

player = Player(intro())

escapeRoom = map.map
arrayMaxX = map.findMax(escapeRoom) + 1  # finds max x
arrayMaxY = map.findMax(escapeRoom)  # finds max y

def getAvailaibleAction(room, player):
    actions = OrderedDict()


def play():
    print(arrayMaxX)
    print(arrayMaxY)
    while not player.win and not player.giveUp:
        room = map.tileAt(player.y, player.x)
        print("x: {}\ty: {}\tx: {}\ty: {}\t".format(room.x, room.y, player.x, player.y))
        print(room.name)
        print(room.desc)
        availableActions = room.availableActions(arrayMaxX, arrayMaxY)
        for a in availableActions:
            print("{}: {}".format(a.hotKey[0], a.name))
        userIn = input("\nAction: ")
        for a in availableActions:
            if userIn in a.hotKey:
                player.doAction(a, room, **a.kwargs)

play()
