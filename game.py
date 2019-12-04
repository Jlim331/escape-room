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

map = []
mp.listGen(loc.escapeRoom, map)
array = mp.randArrayGen(map)
array = mp.CenterStart(array)
print(np.where(array == 'desk'))
print(tab.tabulate(array, tablefmt="simple"))
print(np.where(array == 'desk'))
# menu.choosenPath(loc.escapeRoom)
