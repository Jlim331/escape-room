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
    def __init__(self, name, desc, x, y):
        self.name = name
        self.desc = desc
        self.x = x
        self.y = y


class winTile(MapTile):
    """Class to create the winning tile"""
    def __init__(self, name, desc, x, y):
        super().__init__(name, desc, x, y)


class startTile(MapTile):
    """Class to create the starting tile"""
    def __init__(self, name, desc, x, y):
        super().__init__(name, desc, x, y)


class endTile(MapTile):
    """Class to create the "giving up" tile"""
    def __init__(self, name, desc, x, y):
        super().__init__(name, desc, x, y)


startTile = startTile("start", "fill in desc", 1, 1)
exitTile = endTile("exit door", "fill in desc", 3, 0)
winTile = winTile("locked door", "fill in desc", 3, 2)
cabinetTile = MapTile("cabinet", "fill in desc", 0, 0)
chestTile = MapTile("chest", "fill in desc", 1, 0)
bookcaseTile = MapTile("bookcase", "fill in desc", 2, 0)
paintingTile = MapTile("painting", "fill in desc", 0, 1)
deskTile = MapTile("desk", "fill in desc", 2, 1)
emptyTile = MapTile(" ", "fill in desc", 3, 1)
shelveTile = MapTile("shelve", "fill in desc", 0, 2)
tableTile = MapTile("table", "fill in desc", 1, 2)
chairTile = MapTile("chair", "fill in desc", 2, 2)


# Creates array for the game
map =[
    [cabinetTile, chestTile, bookcaseTile, exitTile],
    [paintingTile, startTile, deskTile, emptyTile],
    [shelveTile, tableTile, chairTile, winTile]
]

def tileAt(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return map [y][x]
    except:
        return None


def tileExists(x, y):
    return map.get((x, y))


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

def choicePrinter(playerx, playery, tilex, tiley, tileOption):
    if playerx == tilex and playery ==tiley:
        for option in tileOption:
            print(option)
