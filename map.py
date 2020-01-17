# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# File containing all tiles and map property
import numpy as np
import math as m
import tabulate as tab
import action as act
import format as form
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
        print(form.border(self.event))

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
                         desc = "You see a locked door with some light " \
                                "surface rust.\nYou try and open the " \
                                "door but all you hear is a rattle",
                         event = "\nUpon further examination it looks " \
                                 "like each lock needs a key to open the " \
                                 "door.\n\n Do you wish to attempt to open " \
                                 "the door?\nPress o to search.\n",
                         x = 3,
                         y = 2)

    def modifyPlayer(self, player):
        if self.open:
            if player.inventory.count("key") == 3:
                player.win = True
                print(f"Turn {player.turnCounter}")
                print(form.border("""
                Congratulation on finding three keys
                You win!
                """))
            else:
                print(form.border("""
                You need to collect 3 keys to unlock this door
                """))
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
                         desc = "Welcome to the escape room!!!\nThe " \
                                "objective of the game is to find all three " \
                                "keys in the scattered in the room." \
                                "\nGood Luck!",
                         event = "\nNothing to see here :)\n",
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
                         event = "You see a door with an exit sign on top, " \
                                 "do you wish to open the door?\nWARNING - " \
                                 "THIS WILL BE TREATED AS YOU GIVING UP ON " \
                                 "THE GAME - WARNING",
                         x = 3,
                         y = 0)

    def modifyPlayer(self, player):
        if self.open:
            player.giveUp = True
            print(f"Turn {player.turnCounter}")
            print(form.border("""
            You lose
            """))
            self.open = False

    def openDoor(self):
        self.open = True
        self.searchFlag = False

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
                         event = "You see a generic cabinet with some " \
                                 "clothes hanged, a mirror and a drawer.",
                         x = 0,
                         y = 0)

    def modifyPlayer(self, player):
        if self.openDrawerFlag:
            if self.keyFlag:
                print(form.border("""
                you opened the drawer and see nothing
                """))
                self.openDrawerFlag = False
            else:
                print(form.border("""
                You opened the drawer and found a key!

                You picked up the key.
                """))
                player.inventory.append("key")
                self.keyFlag = True
                self.openDrawerFlag = False

    def searchClothes(self):
        self.searchFlag = False
        print(form.border("""
        You searched through the clothes and noticed some Balenciaga,
        Supreme, Gucci, Louis Voutton, but didn't find any keys at all.
        """))

    def lookMirror(self):
        self.searchFlag = False
        print(form.border("""
        You look in the mirror and notice a reflection that resembles yourself
        """))

    def openDrawer(self):
        self.searchFlag = False
        self.openDrawerFlag = True

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.CabinetTileSearch())
        if self.searchFlag == True:
            moves.extend([act.CabinetTileSearchClothes(),
            act.CabinetTileLookMirror(), act.CabinetTileOpenDrawer()])
        return moves


cabinetTile = CabinetTile("key")

class ChestTile(MapTile):
    def __init__(self, item):
        self.item = item
        self.openChestFlag = False
        self.openFlag = False
        super().__init__(name = "chest",
                         desc = "You see a chest in the corner," \
                                "covered with dust",
                         event = """
 You see a chest
                         """,
                         x = 1,
                         y = 0)

    def modifyPlayer(self, player):
        if self.openChestFlag:
            if self.openFlag:
                print("""
You opened the chest and see nothing
                """)
                self.openFlag = False
            else:
                if "chest key" in player.inventory:
                    print("""
You opened the chest and found a key!

You picked up the key.
                    """)
                    player.inventory.append("key")
                    player.inventory.remove("chest key")
                    self.openChestFlag = False
                    self.openFlag = True
                else:
                    print("""
You need to find the chest key to open this chest
                    """)
                    self.openChestFlag = False

    def openChest(self):
        self.searchFlag = False
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
                self.openBookFlag = False
            else:
                print("""
As you opened the book a key fell out!
                """)
                player.inventory.append("key")
                self.openBookFlag = False
                self.keyFlag = True

    def readBook1(self):
        self.searchFlag = False
        print("""
Minecraft: Combat Handbook: Ultimate Collector's Edition by Erik Aronsen
    The Masterpiece from Amazon #1 Bestselling Minecraft Authors Creative
    Community.This time we're delighted to present A Stunning Master Work
    - Minecraft Combat Handbook:Collector's Edition Our goal is to show you
    the most Incredible Possibilities and unlockyour Creative Abilities to
    Master Minecraft World together with us!
            """)

    def readBook2(self):
        self.searchFlag = False
        print("""
THE ESSENTIAL CALVIN AND HOBBES by Bill Watterson
    Beginning with the day Hobbes sprang into Calvin's tuna fish trap, the
    first two Calvin and Hobbes collections, Calvin and Hobbes and Something
    Under The Bed Is Drooling, are brought together in this treasury.
    Including black-and-white dailies and color Sundays, The Essential Calvin
    and Hobbes also features an original full-color 16-page story.
            """)

    def readBook3(self):
        self.searchFlag = False
        print("""
Diary of a Wimpy Kid Book 1 by Jeff Kinney
    It’s a new school year, and Greg Heffley finds himself thrust into middle
    school, where undersized weaklings share the hallways with kids who are
    taller, meaner, and already shaving. The hazards of growing up before
    you’re ready are uniquely revealed through words and drawings as Greg
    records them in his diary.
            """)

    def readBook4(self):
        self.searchFlag = False
        print("""
Goosebumps: Welcome to Camp Nightmare by R L Stine
    The food isn't great. The counselors are strange. And the camp director
    seems demented. Okay, so Billy can handle all that. But then his fellow
    campers start to disappear. What's going on? Why won't his parents answer
    his letters? What's lurking out there after dark? Camp Nightmoon is
    turning into Camp Nightmare! And Billy might be next...
                """)

    def readBook5(self):
        self.searchFlag = False
        self.openBookFlag = True
        print("""
Little Red Riding Hood by Gaby Goldsack
    he classic tale of Little Red Riding Hood comes to life in this vibrant
    retelling perfect for beginning readers.  Designed to encourage vocabulary
    development and help children read aloud, this story uses larger font
    types and vivid, contemporary illustrations to help early learning skills.
    It's a perfect addition to any children's library
            """)


    def readBook6(self):
        self.searchFlag = False
        print("""
Captain Underpants and the Tyrannical Retaliation of the Turbo Toilet 2000
by Dav Pilkey
    Just when you thought it was safe to flush . . .

    The Turbo Toilet 2000 strikes back! The carnivorous commode known for
    devouring everything in its path has built up a real appetite . . . for
    REVENGE! Join Captain Underpants for another epic showdown of Wedgie Power
    vs. Potty Power as our tighty-whitey-wearing superhero GOES TO ELEVEN!
            """)

    def readBook7(self):
        self.searchFlag = False
        print("""
The 39 Clues Book One: The Maze of Bones by Rick Riordan
    Minutes before she died Grace Cahill changed her will, leaving her
    decendants an impossible decision:

    "You have a choice - one million dollars or a clue."
            """)

    def availableActions(self, maxX, maxY):
        moves = self.defaultActions(maxX, maxY)
        moves.append(act.BookcaseTileSearch())
        if self.searchFlag == True:
            moves.extend([act.BookcaseTileRead1(), act.BookcaseTileRead2(),
            act.BookcaseTileRead3(), act.BookcaseTileRead4(),
            act.BookcaseTileRead5(), act.BookcaseTileRead6(),
            act.BookcaseTileRead7()])
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
There is nothing to see here -_-
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
                self.sitFlag = False
            else:
                player.inventory.append(self.item)
                print("""
Upon sitting on the chair you notice that it wobbles a little
and found a key for a chest underneath the legs
                """)
                self.keyFlag = True
                self.sitFlag = False

    def sit(self):
        self.sitFlag = True
        self.searchFlag = False

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


def objArrayConv(array):
    """Creates an array from a list and determines the number of row and col"""
    list = []
    maxY = len(array)
    for y in array:
        maxX = len(y)
        for x in y:
            list.append(x.name)
    # creates a numpy array with the list and sqrtElem being the row and col
    array = np.array(list).reshape(maxY, maxX)
    return array


def highlightPos(y, x, array):
    """Function that takes an x and y cord of an array and highlights that
    item"""
    strArray = objArrayConv(array)
    tileAt = "~ {} ~".format(strArray[y][x])
    # replaces old tile with new tiles
    highlighted = np.where(strArray == strArray[y][x], tileAt, strArray)
    # prints out the table but with the highlighted tile higlighted
    table = tab.tabulate(highlighted, tablefmt="grid")
    print(table)


def findMax(array):
    """finds the max num of row in an array"""
    max = len(array) - 1
    max = int(max)
    return max
