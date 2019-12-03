# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# Map to see options and elements
import numpy as np
import math as m
import tabulate as tab


def listGen(dictionary, list):
    """Appends the key of a dictionary to a list"""
    for i in dictionary:  # appends each key of the dictionary to a list
        list.append(i)


def removeDesc(list):
    """Function to remove the key description from a list"""
    for i in list:  # searches for description and removes it
        if i == "description":
            list.remove("description")


def arrayGen(list):
    """Creates an array from a list and determines the number of row and col"""
    removeDesc(list)
    elem = len(list)  # finds how many items are in a list
    sqrtElem = m.sqrt(elem)  # finds the squareroot of elem
    if isinstance(sqrtElem, int) is False:  # checks if sqrt is an integer
        sqrtElem = int(m.ceil(sqrtElem))  # rounds up sqrtElem
    else:
        sqrtElem = int(sqrtElem)
    # finds the difference between elem and sqrt and then appendss for the diff
    diffElem = int(m.pow(sqrtElem, 2)) - elem
    for i in range(diffElem):
        list.append("")
    # creates a numpy array with the list and sqrtElem being the row and col
    array = np.array(list).reshape(sqrtElem, sqrtElem)
    return array


def randCenterStart(array):
    """Randomize the array, then appends to the center of the array 'start' and
    then appends the old center value to a blank value, array must contain a
    blank value"""
    center = m.ceil(float(len(array)) / 2)  # finds the center of the array
    center = center - 1
    centerTile = array[center, center]  # finds the value of the center tile
    # replaces the corner value with the center tile
    array[-1][-1] = centerTile
    np.random.shuffle(array)  # shuffles array
    array[center][center] = "start"  # replaces the center tile with start
    return array


def CenterStart(array):
    """Appends to the center of the array 'start' and then appends the old
    center value to a blank value, array must contain a blank value"""
    center = m.ceil(float(len(array)) / 2)  # finds the center of the array
    center = center - 1
    centerTile = array[center, center]  # finds the value of the center tile
    # replaces the corner value with the center tile
    array[-1][-1] = centerTile
    array[center][center] = "start"  # replaces the center tile with start
    return array
