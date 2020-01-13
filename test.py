# Josh Lim
# Comp Sci 30 P4
# 01/09/2020
# File to test code
import map
from player import Player
import action


def intro():
    print("Welceom to escape room")
    name = input("Name: ").title
    return name

player = Player(intro())

escapeRoom = map.map
arrayMaxX = map.findMax(escapeRoom) + 1  # finds max x
arrayMaxY = map.findMax(escapeRoom)  # finds max y

def play():
    while not player.win or not player.giveUp:
        room = map.tileExist(player.x, player.y)
        print(room.name)
        print(room.desc)
        availableActions = room.availableActions()
        for action in availableActions:
            print("{}: {} \t".format(action.hotKey[0].title(), action.name.capitalize()), end = "")
        userIn = input("\nAction: ")
        for action in availableActions:
            if userIn in action.hotKey:
                print("i")
                player.doAction(action)

play()
