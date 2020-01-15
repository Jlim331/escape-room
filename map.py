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
        self.searchFlag = False
        self.name = name
        self.desc = desc
        self.event = event
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def modifyPlayer(self, player):
        pass

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

    def search(self):
        self.searchFlag = True
        print(self.event)

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
        self.player = None
        self.open = False
        super().__init__(name = "locked door",
                         desc = "You see a locked door with three locks",
                         event = """
                         Upon examination it looks like each lock needs a key to open the door,
                         do you wish to attempt open the door?
                         """,
                         x = 3,
                         y = 2)

    def modifyPlayer(self, player):
        if self.open:
            if player.inventory.count("key") == 3:
                player.win = True
                print("""
                Congratulation on finding three keys
                You win!
                """)
            else:
                print("""
                You need to collect 3 keys to unlock this door
                """)
                self.open = False

    def openDoor(self):
        self.open = True
        self.searchFlag = False


    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.WinTileSearch())
        if self.searchFlag == True:
            moves.append(act.WinTileOpenDoor())
        return moves

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
        self.open = False
        super().__init__(name = "exit",
                         desc = "You see a bright exit sign on top of a door",
                         event = """
                         You see a door with an exit sign on top, do you wish to open the door?
                         WARNING - THIS WILL BE TREATED AS YOU GIVING UP ON THE GAME - WARNING
                         """,
                         x = 3,
                         y = 0)

    def modifyPlayer(self, player):
        if self.open:
            player.giveUp = True
            print("""
            You lose
                """)

    def openDoor(self):
        self.open = True

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.EndTileSearch())
        if self.searchFlag == True:
            moves.append(act.EndTileOpenDoor())
        return moves

endTile = EndTile()

class CabinetTile(MapTile):
    def __init__(self, item):
        self.item = item
        self.openDrawerFlag = False
        self.searchFlag = False
        self.keyFlag = False
        super().__init__(name = "cabinet",
                         desc = "You see a brown cabinet with two doors open",
                         event = """
                         You see a generic cabinet with some clothes hanged,
                         a mirror and a drawer. What would you like to do?
                         """,
                         x = 0,
                         y = 0)

    def modifyPlayer(self, player):
        if self.openDrawerFlag:
            if self.keyFlag:
                print("""
                you opened the drawer and see nothing
                """)
            else:
                print("""
                You opened the drawer and found a key!
                """)
                player.inventory.append("key")
                self.keyFlag = True
                self.openDrawerFlag = False

    def searchClothes(self):
        print("""
        You searched through the clothes and noticed some Balenciaga,
        Supreme, Gucci, Louis Voutton, but didn't find any keys at all.
        """)

    def lookMirror(self):
        print("""
        You look in the mirror and notice a reflection that resembles yourself
        """)

    def openDrawer(self):
        self.openDrawerFlag = True

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.CabinetTileSearch())
        if self.searchFlag == True:
            moves.extend([act.CabinetTileSearchClothes(), act.CabinetTileLookMirror(), act.CabinetTileOpenDrawer()])
        return moves


cabinetTile = CabinetTile("key")

class ChestTile(MapTile):
    def __init__(self, item):
        self.item = item
        self.openChestFlag = False
        self.openFlag = False
        super().__init__(name = "chest",
                         desc = "you see a chest in the corner, covered with dust",
                         event = """
                         You see a chest
                         What would you like to do?
                         """,
                         x = 1,
                         y = 0)

    def modifyPlayer(self, player):
        if self.openChestFlag:
            if self.openFlag:
                print("""
                You opened the chest and see nothing
                """)
            else:
                if "chest key" in player.inventory:
                    print("""
                    You opened the chest and found a key!
                    """)
                    player.inventory.append("key")
                    player.inventory.remove("chest key")
                    self.openChestFlag = False
                    self.openFlag = True
                else:
                    print("""
                    You need to find the chest key to open this chest
                    """)

    def openChest(self):
        self.openChestFlag = True

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.ChestTileSearch())
        if self.searchFlag == True:
            moves.append(act.ChestTileOpenChest())
        return moves

chestTile = ChestTile("key")

class BookcaseTile(MapTile):
    def __init__(self, item):
        self.item = item
        self.openBookFlag = False
        self.keyFlag = False
        super().__init__(name = "bookcase",
                         desc = "you see a bookcase standing tall and strong",
                         event = """
                         You see a bookcase filled with a variety of books with the
                         most common color being red
                         """,
                         x = 2,
                         y = 0)

    def modifyPlayer(self, player):
        if self.openBookFlag:
            if self.keyFlag:
                None
            else:
                print("""
                As you opened the book a key fell out!
                """)
                player.inventory.append("key")
                self.openBookFlag = False
                self.keyFlag = True

    def readBook1(self):
        print("""
        Minecraft: Combat Handbook: Ultimate Collector's Edition by Erik Aronsen
            The Masterpiece from Amazon #1 Bestselling Minecraft Authors Creative Community.
            This time we're delighted to present A Stunning Master Work - Minecraft Combat
            Handbook:Collector's Edition Our goal is to show you the most Incredible
            Possibilities and unlockyour Creative Abilities to Master Minecraft World
            together with us!
            """)

    def readBook2(self):
        print("""
        THE ESSENTIAL CALVIN AND HOBBES by Bill Watterson
            Beginning with the day Hobbes sprang into Calvin's tuna fish trap, the first
            two Calvin and Hobbes collections, Calvin and Hobbes and Something Under The Bed
            Is Drooling, are brought together in this treasury. Including black-and-white
            dailies and color Sundays, The Essential Calvin and Hobbes also features an
            original full-color 16-page story.
            """)

    def readBook3(self):
        print("""
        Diary of a Wimpy Kid Book 1 by Jeff Kinney
            It’s a new school year, and Greg Heffley finds himself thrust into middle school,
            where undersized weaklings share the hallways with kids who are taller, meaner,
            and already shaving. The hazards of growing up before you’re ready are uniquely
            revealed through words and drawings as Greg records them in his diary.
            """)

    def readBook4(self):
            print("""
            Goosebumps: Welcome to Camp Nightmare by R L Stine
                The food isn't great. The counselors are strange. And the camp director seems
                demented. Okay, so Billy can handle all that. But then his fellow campers start
                to disappear. What's going on? Why won't his parents answer his letters? What's
                lurking out there after dark? Camp Nightmoon is turning into Camp Nightmare! And
                Billy might be next...
                """)

    def readBook5(self):
        self.openBookFlag = True
        print("""
        Little Red Riding Hood by Gaby Goldsack
            he classic tale of Little Red Riding Hood comes to life in this vibrant retelling
            perfect for beginning readers.  Designed to encourage vocabulary development and
            help children read aloud, this story uses larger font types and vivid, contemporary
            illustrations to help early learning skills. It's a perfect addition to any children's
            library
            """)


    def readBook6(self):
        print("""
        Captain Underpants and the Tyrannical Retaliation of the Turbo Toilet 2000 by Dav Pilkey
            Just when you thought it was safe to flush . . .

            The Turbo Toilet 2000 strikes back! The carnivorous commode known for devouring everything
            in its path has built up a real appetite . . . for REVENGE! Join Captain Underpants for another
            epic showdown of Wedgie Power vs. Potty Power as our tighty-whitey-wearing superhero GOES TO ELEVEN!
            """)

    def readBook7(self):
        print("""
        The 39 Clues Book One: The Maze of Bones by Rick Riordan
            Minutes before she died Grace Cahill changed her will, leaving her decendants an impossible decision:
            "You have a choice - one million dollars or a clue."
            """)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.BookcaseTileSearch())
        if self.searchFlag == True:
            moves.extend([act.BookcaseTileRead1(), act.BookcaseTileRead2(), act.BookcaseTileRead3(), act.BookcaseTileRead4(), act.BookcaseTileRead5(), act.BookcaseTileRead6(), act.BookcaseTileRead7()])
        return moves

bookcaseTile = BookcaseTile("key")

class PaintingTile(MapTile):
    def __init__(self):
        super().__init__(name = "painting",
                         desc = "You see a classical painting of doge",
                         event = """
                         it's just a painting, did you expect something cool to happen?
                         """,
                         x = 0,
                         y = 1)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.PaintingTileSearch())
        return moves

paintingTile = PaintingTile()

class DeskTile(MapTile):
    def __init__(self):
        super().__init__(name = "desk",
                        desc = "You see a desk ",
                        event = """
                        The desk has papers all over it, must be an AP student
                        """,
                        x = 2,
                        y = 1)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.DeskTileSearch())
        return moves

deskTile = DeskTile()

class EmptyTile(MapTile):
    def __init__(self):
        super().__init__(name = "",
                         desc = "",
                         event = """
                         There is nothing to see here
                         """,
                         x = 3,
                         y = 1)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.EmptyTileSearch())
        return moves

emptyTile = EmptyTile()

class ShelveTile(MapTile):
    def __init__(self):
        super().__init__(name = "shelve",
                         desc = "You see a shelve floating on the wall",
                         event = """
                         Looks like a strong shelf
                         """,
                         x = 0,
                         y = 2)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.ShelveTileSearch())
        return moves

shelveTile = ShelveTile()

class TableTile(MapTile):
    def __init__(self):
        super().__init__(name = "table",
                        desc = "You see a table",
                        event = """
                        The table appears to have four legs
                        """,
                        x = 1,
                        y = 2)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.TableTileSearch())
        return moves

tableTile = TableTile()

class ChairTile(MapTile):
    def __init__(self, item):
        self.item = item
        self.sitFlag = False
        self.keyFlag = False
        super().__init__(name = "chair",
                         desc = "You see a chair sitting in the corner",
                         event = """
                         It seems very sturdy
                         """,
                         x = 2,
                         y= 2)

    def modifyPlayer(self, player):
        if self.sitFlag:
            if self.keyFlag:
                print("""
                The chair made squeeked a little when you sat on it
                """)
            else:
                player.inventory.append(self.item)
                print("""
                Upon sitting on the chair you notice that it wobbles a little
                and found a key for a chest underneath the legs
                """)
                self.keyFlag = True

    def sit(self):
        self.sitFlag = True

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.ChairTileSearch())
        if self.searchFlag:
            moves.append(act.ChairTileSit())
        return moves

chairTile = ChairTile("chest key")

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
