# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# File containing all tiles and map property
import numpy as np
import math as m
import tabulate as tab
import format as form
import action as act
global map  # globalize map to be used in other files


class MapTile:
    """Map Class to create tiles for the game"""
    def __init__(self, name, desc, event, x, y):
        self.name = name
        self.desc = desc
        self.event = event
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def search(self):
        return self.event

    def adjacentMoves(self, maxX, maxY):
        moves = []
        if self.y - 1 >= 0:
            moves.append(act.MoveUp())
        if self.y + 1 <= maxY:
            moves.append(act.MoveDown())
        if self.x + 1 <= maxX:
            moves.append(act.MoveRight())
        if self.x - 1 >= 0:
            moves.append(act.MoveLeft())
        return moves

    def defaultActions(self, maxX, maxY):
        moves = self.adjacentMoves(maxX, maxY)
        moves.append(act.ViewInv())
        moves.append(act.Quit())
        return moves

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        return moves

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def tilePos(self):
        return "x = {}, y = {}".format(self.x, self.y)


class WinTile(MapTile):
    """Class to create the winning tile"""
    def __init__(self):
        self.searchFlag = False
        super().__init__(name = "locked door",
                         desc = "fill in desc",
                         event = """
                         You see a locked door with three locks, do you wish to open the door?
                         """,
                         x = 3,
                         y = 2)

    def search(self):
        self.searchFlag = True
        return self.event

    def openDoor(self, player):
        if self.searchFlag == True:
            if player.inventory.count("key") == 3:
                player.win = True
                return """
                Congratulation on finding three keys
                You win!
                """
            else:
                return """
                You need to collect 3 keys to unlock this door
                """
        else:
            return None

winTile = WinTile()


class StartTile(MapTile):
    """Class to create the starting tile"""
    def __init__(self):
        super().__init__(name = "start",
                         desc = """
                                     Welcome to the escape room!!!
                          The games objective is to find all three keys in the
                             room before turn 50 or else you lose the game.
                                        What would you like to do?
                         """,
                         event = "Nothing to see here :)",
                         x = 1,
                         y = 1)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.StartTileSearch())
        return moves

startTile = StartTile()

class EndTile(MapTile):
    """Class to create the "giving up" tile"""
    def __init__(self):
        self.searchFlag = False
        super().__init__(name = "exit",
                         desc = "fill in desc",
                         event = """
                         You see a door with an exit sign on top, do you wish to open the door?
                         WARNING - THIS WILL BE TREATED AS YOU GIVING UP ON THE GAME - WARNING
                         """,
                         x = 3,
                         y = 0)

    def search(self):
        self.searchFlag = True
        return self.event

    def openDoor(self, player):
        if self.searchFlag == True:
            self.giveUp = False
            return """
            Thank you for playing, you lose
            """

endTile = EndTile()

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
    def __init__(self, item):
        self.item = item
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
            player.inventory.append(self.item)
            player.inventory.remove("chest key")
            return """
            You opened the chest and found a key
            """
        else:
            return """
            You need a key to open this chest.
            """

chestTile = ChestTile("key")

class BookcaseTile(MapTile):
    def __init__(self, item):
        self.item = item
        self.searchFlag = False
        super().__init__(name = "bookcase",
                         desc = "fill in desc",
                         event = """
                         You see a bookcase filled with a variety of books with the
                         most common color being red
                         """,
                         x = 2,
                         y = 0)

    def search(self):
        self.searchFlag = True
        return self.event

    def readBook1(self):
        if self.searchFlag == True:
            return """
            Minecraft: Combat Handbook: Ultimate Collector's Edition by Erik Aronsen
                The Masterpiece from Amazon #1 Bestselling Minecraft Authors Creative Community.
                This time we're delighted to present A Stunning Master Work - Minecraft Combat
                Handbook:Collector's Edition Our goal is to show you the most Incredible
                Possibilities and unlockyour Creative Abilities to Master Minecraft World
                together with us!
            """
        else:
            return None

    def readBook2(self):
        if self.searchFlag == True:
            return """
            THE ESSENTIAL CALVIN AND HOBBES by Bill Watterson
                Beginning with the day Hobbes sprang into Calvin's tuna fish trap, the first
                two Calvin and Hobbes collections, Calvin and Hobbes and Something Under The Bed
                Is Drooling, are brought together in this treasury. Including black-and-white
                dailies and color Sundays, The Essential Calvin and Hobbes also features an
                original full-color 16-page story.
            """
        else:
            return None

    def readBook3(self):
        if self.searchFlag == True:
            return """
            Diary of a Wimpy Kid Book 1 by Jeff Kinney
                It’s a new school year, and Greg Heffley finds himself thrust into middle school,
                where undersized weaklings share the hallways with kids who are taller, meaner,
                and already shaving. The hazards of growing up before you’re ready are uniquely
                revealed through words and drawings as Greg records them in his diary.
            """
        else:
            return None

    def readBook4(self):
        if self.searchFlag == True:
            return """
            Goosebumps: Welcome to Camp Nightmare by R L Stine
                The food isn't great. The counselors are strange. And the camp director seems
                demented. Okay, so Billy can handle all that. But then his fellow campers start
                to disappear. What's going on? Why won't his parents answer his letters? What's
                lurking out there after dark? Camp Nightmoon is turning into Camp Nightmare! And
                Billy might be next...
            """
        else:
            return None

    def readBook5(self, player):
        if self.searchFlag == True:
            player.inventory.append(self.item[0])
            return """
            Little Red Riding Hood by Gaby Goldsack
                he classic tale of Little Red Riding Hood comes to life in this vibrant retelling
                perfect for beginning readers.  Designed to encourage vocabulary development and
                help children read aloud, this story uses larger font types and vivid, contemporary
                illustrations to help early learning skills. It's a perfect addition to any children's
                library.

                As you opened the book a key fell out!
            """
        else:
            return None

    def readBook6(self):
        if self.searchFlag == True:
            return """
            Captain Underpants and the Tyrannical Retaliation of the Turbo Toilet 2000 by Dav Pilkey
                Just when you thought it was safe to flush . . .

                The Turbo Toilet 2000 strikes back! The carnivorous commode known for devouring everything
                in its path has built up a real appetite . . . for REVENGE! Join Captain Underpants for another
                epic showdown of Wedgie Power vs. Potty Power as our tighty-whitey-wearing superhero GOES TO ELEVEN!
            """
        else:
            return None

    def readBook7(self, player):
        if self.searchFlag == True:
            player.inventory.append(self.item[1])
            return """
            The 39 Clues Book One: The Maze of Bones by Rick Riordan
                Minutes before she died Grace Cahill changed her will, leaving her decendants an impossible decision:
                "You have a choice - one million dollars or a clue."

                You found a 39 clue card!
            """
        else:
            return None

bookcaseTile = BookcaseTile(["key", "Card # 6: Thomas Jefferson"])

class PaintingTile(MapTile):
    def __init__(self):
        super().__init__(name = "painting",
                         desc = "fill in desc",
                         event = """
                         You see a painting
                         """,
                         x = 0,
                         y = 1)

paintingTile = PaintingTile()

class DeskTile(MapTile):
    def __init__(self):
        super().__init__(name = "desk",
                        desc = "fill in desc",
                        event = """
                        You see a desk
                        """,
                        x = 2,
                        y = 1)

deskTile = DeskTile()

class EmptyTile(MapTile):
    def __init__(self):
        super().__init__(name = "",
                         desc = "fill in desc",
                         event = """
                         There is nothing to see here
                         """,
                         x = 3,
                         y = 1)

emptyTile = EmptyTile()

class ShelveTile(MapTile):
    def __init__(self):
        super().__init__(name = "shelve",
                         desc = "fill in desc",
                         event = """
                         You see a shelve
                         """,
                         x = 0,
                         y = 2)

shelveTile = ShelveTile()

class TableTile(MapTile):
    def __init__(self):
        super().__init__(name = "table",
                        desc = "fill in desc",
                        event = """
                        You see a table
                        """,
                        x = 1,
                        y = 2)

tableTile = TableTile()

class ChairTile(MapTile):
    def __init__(self):
        super().__init__(name = "chair",
                         desc = "fill in desc",
                         event = """
                         You see a chair
                         """,
                         x = 2,
                         y= 2)

chairTile = ChairTile()

map =[
    [cabinetTile, chestTile, bookcaseTile, endTile],
    [paintingTile, startTile, deskTile, emptyTile],
    [shelveTile, tableTile, chairTile, winTile]
]


def tileAt(y, x):
    if x < 0 and y < 0:
        return None
    try:
        return map [y][x]
    except:
        return None


def tileExist(x, y, maxX, maxY):
    if x >= 0 and y >= 0:
        if x <= maxX and y <= maxY:
            return True
    else:
        return False

def highlighPos(y, x, array):
    """Function that takes an x and y cord of an array and highlights that
    item"""
    highlightTile = "~" + array[y][x].name + "~"
    # replaces old tile with new tiles
    highlighted = np.where(array == array[y][x], "You are here", array)
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


def removeName(list):
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
