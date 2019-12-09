# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# File to import files to play the game
import menu
import properties as prop
import locations as loc
import map as mp
import tabulate as tab
import numpy as np
import properties as prop


print("Hello what is your name?")
name = input("Name: ").title()
player = prop.Player(name, ["Gun"])
sepFormat = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
# print(sepFormat)
# player.description()
# print(sepFormat)

flag = True

map = []
mp.listGen(loc.escapeRoom, map)
array = mp.randArrayGen(map)
array = mp.CenterStart(array)
# print(tab.tabulate(array, tablefmt="simple"))
# print(np.where(array == 'desk'))

while flag:
    print(tab.tabulate(array, tablefmt="simple"))
    print("W: UP\nS: DOWN\nA: RIGHT\nD: LEFT")
    print("Where would you like to go?")
    userIn = input().lower()
    if userIn in ["up", "w"]:
        print("going up")
        player.moveUp()
        player.findPos()
    elif userIn in ["down", "s"]:
        print("going down")
        player.moveDown()
        player.findPos()
    elif userIn in ["right", "d"]:
        print("going right")
        player.moveRight()
        player.findPos()
    elif userIn in ["left", "a"]:
        print("going left")
        player.moveLeft()
        player.findPos()
    elif userIn == "quit":
        print("thank you for playing")
        flag = False
    else:
        print("invalid input, please try again")
