# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# File to import files to play the game
import menu
import properties as prop
import locations as loc
import map as mp
import tabulate as tab

map = []
mp.listGen(loc.escapeRoom, map)
array = mp.arrayGen(map)
array = mp.randCenterStart(array)
print(tab.tabulate(array, tablefmt="simple"))

menu.choosenPath(loc.escapeRoom)
