# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# Map to see options and elements
import numpy as np
import locations as loc
import math as m
import tabulate as tab

def listGen(dictionary, list):
    """Appends the key of a dictionary to a list"""
    for i in dictionary:
        list.append(i)

def arrayGen(list):
    """Creates an array from a list and automatically determins the number of
    rows and col"""
    elem = len(list)
    sqrtElem = m.sqrt(elem)
    elemCheck = isinstance(sqrtElem, int)
    if elemCheck == False:
        sqrtElem = int(m.ceil(sqrtElem))
    else:
        sqrtElem = int(sqrtElem)
    diffElem = int(m.pow(sqrtElem, 2)) - elem
    for i in range(diffElem):
        list.append("")
    array = np.array(list).reshape(sqrtElem, sqrtElem)
    return array

def centerStart(array):
    global center
    center = m.ceil(float(len(array)) / 2)
    center = center - 1
    centerTile = array[center, center]
    array = np.where(array==centerTile, "start", array)
    # array[2][2] = centerTile
    return array


map = []
listGen(loc.escapeRoom, map)
array = arrayGen(map)
array = centerStart(array)
print(tab.tabulate(array, tablefmt="simple"))

print(center)
