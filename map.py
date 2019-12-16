# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# Map to see options and elements
import numpy as np
import math as m
import tabulate as tab
import format as form
global map  # globalize map to be used in other files


class MapTile:
    """Map Class to create tiles for the game"""
    def __init__(self, name, desc, inv):
        self.name = name  # initiates with the name of the tile

    def __str__(self):
        return self.name  # returns just the tile name for the array


class winTile(MapTile):
    """Class to create the winning tile"""
    def __init__(self, name):
        self.name = name  # initiates with the name of the tile


class startTile(MapTile):
    """Class to create the starting tile"""
    def __init__(self, name):
        self.name = name  # initiates with the name of the tile


class endTile(MapTile):
    """Class to create the "giving up" tile"""
    def __init__(self, name):
        self.name = name  # initiates with the name of the tile


startTile = startTile("start")  # Creates start tile
endTile = endTile("exit door")  # Creates end tile
winTile = winTile("locked door")  # Creates win tile

# Creates array for the game
map = np.array([
    ["cabinet", "chest", "bookcase", endTile.__str__()],
    ["painting", startTile.__str__(), "desk", ""],
    ["shelve", "table", "chair", winTile.__str__()]
])


def highlighPos(y, x, array):
    """Function that takes an x and y cord of an array and highlights that
    item"""
    highlightTile = "~" + array[y][x] + "~"
    # replaces old tile with new tiles
    highlighted = np.where(array == array[y][x], highlightTile, array)
    # prints out the table but with the highlighted tile higlighted
    print(tab.tabulate(highlighted, tablefmt="grid"))


def findMax(array):
    """finds the max num of row in an array"""
    max = len(array) - 1
    max = int(max)
    return max


def listGen(dictionary, list):
    """Appends the key of a dictionary to a list"""
    for i in dictionary:  # appends each key of the dictionary to a list
        list.append(i)


def removename(list):
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


def randArrayGen(list):
    """Creates an array from a list and determines the number of row and col"""
    removeDesc(list)
    np.random.shuffle(list)
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
