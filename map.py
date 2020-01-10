# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# File containing all tiles and map property
import numpy as np
import math as m
import tabulate as tab
import format as form
global map  # globalize map to be used in other files


class MapTile:
    """Map Class to create tiles for the game"""
    def __init__(self, name, desc, event, x, y):
        self.name = name
        self.desc = desc
        self.event = event
        self.x = x
        self.y = y

    def search(self):
        return self.event

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def tilePos(self):
        return "x = {}, y = {}".format(self.x, self.y)


class WinTile(MapTile):
    """Class to create the winning tile"""
    def __init__(self):
        super().__init__(name = "locked door",
                         desc = "fill in desc",
                         event = """
                         You see a locked door with three locks, do you wish to open the door?
                         """,
                         x = 3,
                         y = 2)


class StartTile(MapTile):
    """Class to create the starting tile"""
    def __init__(self):
        super().__init__(name = "start",
                         desc = """
                                     Welcome to the escape room!!!
                          The games objective is to find all three keys in the
                             room before turn 50 or else you lose the game.
                         """,
                         event = "Nothing to see here :)",
                         x = 1,
                         y = 1)


class EndTile(MapTile):
    """Class to create the "giving up" tile"""
    def __init__(self):
        super().__init__(name = "exit",
                         desc = "fill in desc",
                         event = """
                         You see a door with an exit sign on top, do you wish to open the door?
                         WARNING - THIS WILL BE TREATED AS YOU GIVING UP ON THE GAME - WARNING
                         """,
                         x = 0,
                         y = 3)


class CabinetTile(MapTile):
    def __init__(self, item):
        self.searchFlag = False
        self.item = item
        super().__init__(name = "cabinet",
                         desc = "fill in desc",
                         event = """
                         You see a generic cabinet with some clothes hanged,
                         a mirror and a drawer. What would you like to do?
                         """,
                         x = 0,
                         y = 0)

    def search(self):
        self.searchFlag = True
        return self.event

    def searchClothes(self):
        if self.searchFlag == True:
            return """
            You searched through the clothes and noticed some Balenciaga,
            Supreme, Gucci, Louis Voutton, but didn't find any keys at all.
            """
        else:
            return None

    def lookMirror(self):
        if self.searchFlag == True:
            return """
            You look in the mirror and notice a reflection that resembles yourself
            """
        else:
            return None

    def openDrawer(self, player):
        if self.searchFlag == True:
            player.inventory.append(self.item)
            return """
            You open the drawer and found a key!
            """
        else:
            return None

cabinetTile = CabinetTile("key")

class ChestTile(MapTile):
    def __init__(self):
        super().__init__(name = "chest",
                         desc = "fill in desc",
                         event = """
                         You see a chest
                         What would you like to do?
                         """,
                         x = 1,
                         y = 0)

    def openChest(self, player):
        if "chest key" in player.inventory:
            player.inventory.append("key")
            player.inventory.remove("chest key")
            return """
            You opened the chest and found a key
            """
        else:
            return """
            You need a key to open this chest.
            """

chestTile = ChestTile()

class BookcaseTile(MapTile):
    def __init__(self):
        self.searchFlag = False
        super().__init__(name = "bookcase",
                         desc = "fill in desc",
                         event = """
                         You see a bookcase filled with a bunch of red books,
                         textbook and magazine
                         """,
                         x = 2,
                         y = 0)

    def search(self):
        self.searchFlag = True
        return self.event


class PaintingTile(MapTile):
    def __init__(self):
        super().__init__(name = "painting",
                         desc = "fill in desc",
                         x = 0,
                         y = 1)


class DeskTile(MapTile):
    def __init__(self):
        super().__init__(name = "desk",
                        desc = "fill in desc",
                        x = 2,
                        y = 1)


class EmptyTile(MapTile):
    def __init__(self):
        super().__init__(name = "",
                         desc = "fill in desc",
                         x = 3,
                         y = 1)


class ShelveTile(MapTile):
    def __init(self):
        super().__init__(name = "shelve",
                         desc = "fill in desc",
                         x = 0,
                         y = 2)


class TableTile(MapTile):
    def __init__(self):
        super().__init__(name = "table",
                        desc = "fill in desc",
                        x = 1,
                        y = 2)


class ChairTile(MapTile):
    def __init__(self):
        super().__init__(name = "chair",
                         desc = "fill in desc",
                         x = 2,
                         y= 2)

# map =[
#     [CabinetTile(), ChestTile(), BookcaseTile(), EndTile()],
#     [PaintingTile(), StartTile(), DeskTile(), EmptyTile()],
#     [ShelveTile(), TableTile(), ChairTile(), WinTile()]
# ]


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
