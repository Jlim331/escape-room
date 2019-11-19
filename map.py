# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# Map to see options and elements
import numpy as np
import locations as loc

def listGen(dictionary, list):
    """Appends the key of a dictionary to a list"""
    for i in dictionary:
        list.append(i)

def arrayGen(list, row, col):
    """Creates an array with row amount of rows and col amount of columns from
    a list
    """
    array = np.array(list).reshape(row, col)
    return array

map = []
listGen(loc.escapeRoom, map)
print(map)

array = arrayGen(map, 3, 3)
print(array)
