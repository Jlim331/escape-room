# Josh Lim
# Comp Sci 30 P4
# 11/18/2019
# File containing all tiles and map property
import numpy as np
import tabulate as tab
import action as act
import format as form
global map  # globalize map to be used in other files


class MapTile:
    """Map Class to create tiles for the game"""
    def __init__(self, name, desc, event, x, y):
        """Method to initiate value for the class"""
        self.searchFlag = False  # flag to check wether tile has been searched
        self.name = name  # name of tile
        self.desc = desc  # description of tile
        self.event = event  # event of tile
        self.x = x  # tiles x value
        self.y = y  # tiles y value

    def __str__(self):
        """Initiates values to be returned as a string"""
        return self.name  # returns name as a string

    # Code adapted from
    # Let's talk data: How to Write a Text Adventure in Python Part 3
    # https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
    # part-3-player-action/
    def modifyPlayer(self, player):
        """Method to modify the player"""
        pass

    # Code adapted from
    # Let's talk data: How to Write a Text Adventure in Python Part 3
    # https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
    # part-3-player-action/
    def adjacentMoves(self, maxX, maxY):
        """Method for searching for adjacent moves in a map with maxX and maxY
        being the perimeter of the map"""
        moves = []  # list for storing action
        if self.y - 1 >= 0:  # player is inside map from up side
            moves.append(act.MoveUp())  # append move up object
        if self.y + 1 <= maxY:  # player is inside map from down side
            moves.append(act.MoveDown())  # append move move down
        if self.x + 1 <= maxX:  # player is inside map from right side
            moves.append(act.MoveRight())  # append move right
        if self.x - 1 >= 0:  # player is inside map from left side
            moves.append(act.MoveLeft())  # append move left
        return moves  # return moves list

    def defaultActions(self, maxX, maxY):
        """Method to store default actions in the game, with maxX and maxY
        used for adjacentMoves method"""
        moves = self.adjacentMoves(maxX, maxY)  # find adjacent moves
        moves.append(act.ViewInv())  # appends view invetory to moves
        moves.append(act.Quit())  # appends quit to moves
        return moves  # return move list

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        # creates a list with default actions
        moves = self.defaultActions(maxX, maxY)
        return moves  # returns move list

    def search(self):
        """Method to search a tile"""
        self.searchFlag = True  # tell program it has been searched
        print(form.border(self.event))  # prins the search event of tile


class WinTile(MapTile):
    """Class to create the win tile"""
    def __init__(self):
        """Method to initiate values for the class"""
        self.searchFlag = False  # tells game it hasn't been searched
        self.open = False  # tells game the door hasn't been opened
        # initiates values for class
        super().__init__(name="locked door",
                         desc="You see a locked door with some light "
                              "surface rust.\nYou try and open the "
                              "door but all you hear is a rattle",
                         event="\nUpon further examination it looks "
                               "like each lock needs a key to open the "
                               "door.\n\n Do you wish to attempt to open "
                               "the door?\nPress o to search.\n",
                         x=3,
                         y=2)

    def modifyPlayer(self, player):
        """Function to modify player"""
        if self.open:  # if door has been opened
            # player must have three keys
            if player.inventory.count("key") == 3:
                player.win = True  # player wins the game
                print(f"Turn {player.turnCounter}")  # prints turn counter
                print(form.border("""
                Congratulation on finding three keys
                You win!
                """))
            else:  # if the player doesn't have 3 keys
                print(form.border("""
                You need to collect 3 keys to unlock this door
                """))
                self.open = False  # resets open flag

    def openDoor(self):
        """Method for opening the door"""
        self.open = True  # let the game know it has been opened
        self.searchFlag = False  # resets search flag

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # creates a move list
        moves.append(act.WinTileSearch())  # appends available actions
        if self.searchFlag is True:  # if it has been search
            moves.append(act.WinTileOpenDoor())  # appends a open door option
        return moves  # returns list

winTile = WinTile()  # intiates win tile class


class StartTile(MapTile):
    """Class to create the starting tile"""
    def __init__(self):
        """Method to intiates all the value for the class"""
        # initiates value for the class
        super().__init__(name="start",
                         desc="Welcome to the escape room!!!\nThe "
                              "objective of the game is to find all three "
                              "keys in the scattered in the room."
                              "\nGood Luck!",
                         event="\nNothing to see here :)\n",
                         x=1,
                         y=1)

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.StartTileSearch())  # appends search option to list
        return moves  # return move list


startTile = StartTile()  # initites start tile class


class EndTile(MapTile):
    """Class to create the "giving up" tile"""
    def __init__(self):
        """Method for initiating the value for the class"""
        self.searchFlag = False  # tile hasn't been searched
        self.open = False  # tile hasn't been opened
        # initiates class values
        super().__init__(name="exit",
                         desc="You see a bright exit sign on top of a door",
                         event="\nYou see a door with an exit sign on top, "
                               "do you wish to open the door?\nWARNING - "
                               "THIS WILL BE TREATED AS YOU GIVING UP ON "
                               "THE GAME - WARNING\n",
                         x=3,
                         y=0)

    def modifyPlayer(self, player):
        """Method to modify the player"""
        if self.open:  # if the door has been opened
            player.giveUp = True  # let the game know player gave up
            print(f"Turn {player.turnCounter}")  # print turns
            print(form.border("""
            You lose
            """))
            self.open = False  # resets open flag

    def openDoor(self):
        """Method for opening the door"""
        self.open = True  # door has been opened
        self.searchFlag = False  # reset search flag

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.EndTileSearch())  # appends search option
        if self.searchFlag is True:  # if the tile has been search
            moves.append(act.EndTileOpenDoor())  # append open door
        return moves  # return list


endTile = EndTile()  # initiates end tile class


class CabinetTile(MapTile):
    """Class to create cabinet tile class"""
    def __init__(self, item):
        """Method to intiate the class with item being the item that is going
        to be collected"""
        self.item = item  # item that is going to be given to player
        self.openDrawerFlag = False  # set drawer to be closed
        self.searchFlag = False  # set tile to has not been search
        self.keyFlag = False  # let game know key hasn't been collected
        # initiates value for class
        super().__init__(name="cabinet",
                         desc="You see a brown cabinet with two doors "
                              "open",
                         event="\nYou see a generic cabinet with some "
                               "clothes hanged, a mirror and a drawer.\n",
                         x=0,
                         y=0)

    def modifyPlayer(self, player):
        """Method to modify the player"""
        if self.openDrawerFlag:  # if the drawer is open
            if self.keyFlag:  # if the key has been collected
                print(form.border("""
                you opened the drawer and see nothing
                """))
                self.openDrawerFlag = False  # resets open drawer
            else:  # if the key hasn't been collected
                print(form.border("""
                You opened the drawer and found a key!

                You picked up the key.
                """))
                player.inventory.append("key")  # add key to player inv
                self.keyFlag = True  # key has been collected
                self.openDrawerFlag = False  # resets open drawer flag

    def searchClothes(self):
        """Method for searching the clothes"""
        print(form.border("""
        You searched through the clothes and noticed some Balenciaga,
        Supreme, Gucci, Louis Voutton, but didn't find any keys at all.
        """))

    def lookMirror(self):
        """Method for looking at the mirror"""
        print(form.border("""
        You look in the mirror and notice a reflection that resembles yourself
        """))

    def openDrawer(self):
        """Method for opening the drawer"""
        self.searchFlag = False  # resets search flag
        self.openDrawerFlag = True  # drawer is open

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.CabinetTileSearch())  # appends search option to list
        if self.searchFlag is True:  # if the tile has been search
            # append search clothes, look mirror, open drawer
            moves.extend([act.CabinetTileSearchClothes(),
                         act.CabinetTileLookMirror(),
                         act.CabinetTileOpenDrawer()])
        return moves  # return moves


# intiates cabinet tile with key being the item that is going to be collected
cabinetTile = CabinetTile("key")


class ChestTile(MapTile):
    """Class to create the chest tile"""
    def __init__(self, item):
        """Initiates the class with item being the item that is going to be
        collected"""
        self.item = item  # item that is going to be collected
        self.openChestFlag = False  # chest is closed
        self.openFlag = False  # chest hans't been opened yet
        # initates the values for the class
        super().__init__(name="chest",
                         desc="You see a chest in the corner,"
                              "covered with dust",
                         event="\nYou see a chest\n",
                         x=1,
                         y=0)

    def modifyPlayer(self, player):
        """Method to modify player"""
        if self.openChestFlag:  # if the chest is being opened
            if self.openFlag:  # if the key hasn't been taken
                print(form.border("""
                You opened the chest and see nothing
                """))
                self.openFlag = False  # reset open flag
            else:  # if the chest hasn't been opened
                # if the playaer has a chest key
                if "chest key" in player.inventory:
                    print(form.border("""
                    You opened the chest and found a key!

                    You picked up the key.
                    """))
                    # appends a key to player inventory
                    player.inventory.append("key")
                    # removes chest key from player inventory
                    player.inventory.remove("chest key")
                    self.openChestFlag = False  # reset open chest flag
                    self.openFlag = True  # the key has been taken
                else:
                    print(form.border("""
                    You need to find the chest key to open this chest
                    """))
                    self.openChestFlag = False  # resets open chest flag

    def openChest(self):
        """Method for opening the chest"""
        self.searchFlag = False  # resets search flag
        self.openChestFlag = True  # the chest is being opened

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.ChestTileSearch())  # appends search to list
        if self.searchFlag is True:  # if the tile is being searched
            moves.append(act.ChestTileOpenChest())  # append open chest action
        return moves  # return list


# initiates the chest tile with key being the item that is going to be picked
# up
chestTile = ChestTile("key")


class BookcaseTile(MapTile):
    """Class for creating the bookcase class"""
    def __init__(self, item):
        """Initiates the class with item being the item that is going to be
        collected"""
        self.item = item  # item that is going to be picked up
        self.openBookFlag = False  # flag to check if book has been open
        self.keyFlag = False  # flag to check if key hasn't been taken
        # initiate value for class
        super().__init__(name="bookcase",
                         desc="You see a bookcase standing tall and strong",
                         event="\nYou see a bookcase filled with a "
                         "variety of books with the most common color "
                         "being red\n",
                         x=2,
                         y=0)

    def modifyPlayer(self, player):
        """Method to modify player"""
        if self.openBookFlag:  # if the book is being read
            if self.keyFlag:  # if the key has been taken
                self.openBookFlag = False  # resets open book flag
            else:  # if the key has not been taken
                print(form.border("""
                As you opened the book a key fell out!
                """))
                player.inventory.append("key")  # add key to player inventory
                self.openBookFlag = False  # reset open book flag
                self.keyFlag = True  # key has been taken

    def readBook1(self):
        """Method for reading book 1"""
        # summary from https://www.chapters.indigo.ca/en-ca/books/minecraft-
        # combat-handbook-ultimate-collectors/9781537037868-item.html
        print(form.border("""
Minecraft: Combat Handbook: Ultimate Collector's Edition by Erik Aronsen
    The Masterpiece from Amazon #1 Bestselling Minecraft Authors Creative
    Community.This time we're delighted to present A Stunning Master Work
    Minecraft Combat Handbook: Collector's Edition Our goal is to show you
    the most Incredible Possibilities and unlockyour Creative Abilities to
    Master Minecraft World together with us!
            """))

    def readBook2(self):
        """Method for reading book 2"""
        # summary from https://www.amazon.ca/Essential-Calvin-Hobbes-Bill-
        # Watterson/dp/0836218051/ref=sr_1_1?crid=1YAN87VEA3JWD&keywords=the+
        # essential+calvin+and+hobbes&qid=1579321108&sprefix=the+essential+cal
        # %2Caps%2C181&sr=8-1
        print(form.border("""
THE ESSENTIAL CALVIN AND HOBBES by Bill Watterson
    Beginning with the day Hobbes sprang into Calvin's tuna fish trap, the
    first two Calvin and Hobbes collections, Calvin and Hobbes and Something
    Under The Bed Is Drooling, are brought together in this treasury.
    Including black-and-white dailies and color Sundays, The Essential Calvin
    and Hobbes also features an original full-color 16-page story.
            """))

    def readBook3(self):
        """Method for reading book 3"""
        # summary from https://www.amazon.ca/DIARY-WIMPY-Kinney-Author-
        # Hardcover/dp/B0051XV5Y6/ref=sr_1_13?crid=2YHZ0XW6OKNET&keywords=
        # diary+of+a+wimpy&qid=1579321142&sprefix=dairy+of+a+wimpy%2Caps
        # %2C184&sr=8-13
        print(form.border("""
Diary of a Wimpy Kid Book 1 by Jeff Kinney
    It’s a new school year, and Greg Heffley finds himself thrust into middle
    school, where undersized weaklings share the hallways with kids who are
    taller, meaner, and already shaving. The hazards of growing up before
    you’re ready are uniquely revealed through words and drawings as Greg
    records them in his diary.
            """))

    def readBook4(self):
        """Method for reading book 4"""
        # summary from https://www.amazon.ca/Goosebumps-Welcome-Camp-Nightmare
        # -Stine/dp/0545158893/ref=sr_1_7?keywords=goosebumps&qid=1579321183&
        # sr=8-7
        print(form.border("""
Goosebumps: Welcome to Camp Nightmare by R L Stine
    The food isn't great. The counselors are strange. And the camp director
    seems demented. Okay, so Billy can handle all that. But then his fellow
    campers start to disappear. What's going on? Why won't his parents answer
    his letters? What's lurking out there after dark? Camp Nightmoon is
    turning into Camp Nightmare! And Billy might be next...
                """))

    def readBook5(self):
        """Method for reading book 5"""
        # summary from https://www.amazon.ca/Little-Riding-Hood-Gaby-Goldsack
        # /dp/1680524488/ref=sr_1_1?keywords=little+red+riding+hood+book&qid=
        # 1579321224&sr=8-1
        self.openBookFlag = True  # book 5 is being read
        print(form.border("""
Little Red Riding Hood by Gaby Goldsack
    he classic tale of Little Red Riding Hood comes to life in this vibrant
    retelling perfect for beginning readers.  Designed to encourage vocabulary
    development and help children read aloud, this story uses larger font
    types and vivid, contemporary illustrations to help early learning skills.
    It's a perfect addition to any children's library
            """))

    def readBook6(self):
        """Method for reading book 6"""
        # summary from https://www.amazon.ca/Captain-Underpants-Tyrannical-
        # Retaliation-Toilet/dp/0545504902/ref=sr_1_2?crid=28U0PXHDGQBN7&
        # keywords=captain+underpants+and+the+terrifying+return+of+tippy+
        # tinkletrousers&qid=1579321256&sprefix=captain+underpants+and+the+
        # %2Caps%2C180&sr=8-2
        print(form.border("""
Captain Underpants and the Tyrannical Retaliation of the Turbo Toilet 2000
by Dav Pilkey
    Just when you thought it was safe to flush . . .

    The Turbo Toilet 2000 strikes back! The carnivorous commode known for
    devouring everything in its path has built up a real appetite . . . for
    REVENGE! Join Captain Underpants for another epic showdown of Wedgie Power
    vs. Potty Power as our tighty-whitey-wearing superhero GOES TO ELEVEN!
            """))

    def readBook7(self):
        """Method for reading book 7"""
        # summary from https://www.amazon.ca/39-Clues-Book-One-Bones/dp/
        # 0545060397/ref=sr_1_7?keywords=the+39+clues&qid=1579321295&sr=8-7
        print(form.border("""
The 39 Clues Book One: The Maze of Bones by Rick Riordan
    Minutes before she died Grace Cahill changed her will, leaving her
    decendants an impossible decision:

    "You have a choice - one million dollars or a clue."
            """))

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.BookcaseTileSearch())  # apends search option
        if self.searchFlag is True:  # if the tile has been searched
            # append read book 1-7 to list
            moves.extend([act.BookcaseTileRead1(), act.BookcaseTileRead2(),
                         act.BookcaseTileRead3(), act.BookcaseTileRead4(),
                         act.BookcaseTileRead5(), act.BookcaseTileRead6(),
                         act.BookcaseTileRead7()])
        return moves  # return list


# initiates the bookcase tile with key being the item that is going to be
# picked up
bookcaseTile = BookcaseTile("key")


class PaintingTile(MapTile):
    """Class to create the painting tile class"""
    def __init__(self):
        """Initiates value for class"""
        # initites value for class
        super().__init__(name="painting",
                         desc="You see a classical painting of doge",
                         event="\nIt's just a painting, did you expect "
                         "something cool to happen?\n",
                         x=0,
                         y=1)

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.PaintingTileSearch())  # appends search option
        return moves  # return moves


paintingTile = PaintingTile()  # initates painting tile


class DeskTile(MapTile):
    """Class to create the desk tile class"""
    def __init__(self):
        """Initiates value for class"""
        # initites value for class
        super().__init__(name="desk",
                         desc="You see a desk ",
                         event="\nThe desk has papers all over it, must "
                         "be an AP student\n",
                         x=2,
                         y=1)

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.DeskTileSearch())  # appends search option
        return moves  # return moves


deskTile = DeskTile()  # initiates desk tile


class EmptyTile(MapTile):
    """Class to create the empty tile class"""
    def __init__(self):
        """Initiates value for class"""
        # initites value for class
        super().__init__(name="",
                         desc="Looks like an empty tile",
                         event="\nThere is nothing to see here -_-\n",
                         x=3,
                         y=1)

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.EmptyTileSearch())  # appends search option
        return moves  # return moves


emptyTile = EmptyTile()  # initites empty tile class


class ShelveTile(MapTile):
    """Class to create the shelve tile class"""
    def __init__(self):
        """Initiates value for class"""
        # initites value for class
        super().__init__(name="shelve",
                         desc="You see a shelve floating on the wall",
                         event="\nLooks like a strong shelf\n",
                         x=0,
                         y=2)

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.ShelveTileSearch())  # appends search option
        return moves  # return moves


shelveTile = ShelveTile()  # initiates shelve tile class


class TableTile(MapTile):
    """Class to create the table tile class"""
    def __init__(self):
        """Initiates value for class"""
        # initites value for class
        super().__init__(name="table",
                         desc="You see a table",
                         event="\nThe table appears to have four legs\n",
                         x=1,
                         y=2)

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.TableTileSearch())  # appends search option
        return moves  # return moves


tableTile = TableTile()  # initates table tile class


class ChairTile(MapTile):
    """Class to create the chair tile class"""
    def __init__(self, item):
        """Initiates the class with item being the item that is going to be
        collected"""
        self.item = item  # item that is going to be picked up
        self.sitFlag = False  # flag for sitting on chair
        self.keyFlag = False  # flag for if key has been taken
        # initites value for class
        super().__init__(name="chair",
                         desc="You see a chair sitting in the corner",
                         event="\nIt seems very sturdy\n",
                         x=2,
                         y=2)

    def modifyPlayer(self, player):
        """Class to modify player"""
        if self.sitFlag:  # if the player is sitting
            if self.keyFlag:  # if the key has been taken
                print(form.border("""
                The chair made squeeked a little when you sat on it
                """))
                self.sitFlag = False  # resets sit flag
            else:  # if the tkey has not been taken
                player.inventory.append(self.item)  # append key to player inv
                print(form.border("""
                Upon sitting on the chair you notice that it wobbles a little
                and found a key for a chest underneath the legs
                """))
                self.keyFlag = True  # key has been taken
                self.sitFlag = False  # reset sit flag

    def sit(self):
        """Method for sitting"""
        self.sitFlag = True  # the player is sitting on the chair

    def availableActions(self, maxX, maxY):
        """Method to return available actions on a tile, with maxX and maxY
        for default actions"""
        moves = self.defaultActions(maxX, maxY)  # gets default action list
        moves.append(act.ChairTileSearch())  # appends search option
        if self.searchFlag:  # if the tile is being searched
            moves.append(act.ChairTileSit())  # append sit option
        return moves  # return list


# initiates the bookcase tile with key being the item that is going to be
# picked up
chairTile = ChairTile("chest key")


map = [
    [cabinetTile, chestTile, bookcaseTile, endTile],
    [paintingTile, startTile, deskTile, emptyTile],
    [shelveTile, tableTile, chairTile, winTile]
]


# Code adapted from
# Let's talk data: How to Write a Text Adventure in Python Part 3
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
# part-3-player-action/
def tileAt(y, x):
    """Function for finding where the player is"""
    if x < 0 and y < 0:  # if the values are out of map
        return None  # return none
    try:  # if the values are in map
        return map[y][x]  # return map
    except:  # if an error occurs
        return None  # return no values


# Code adapted from
# Let's talk data: How to Write a Text Adventure in Python Part 3
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
# part-3-player-action/
def tileExist(x, y, maxX, maxY):
    """Functino for finding if a tile exist"""
    # if the x and y values are in the map
    if x >= 0 and y >= 0:
        if x <= maxX and y <= maxY:
            return True
    else:
        return False


def objArrayConv(array):
    """Converts an object array, array. to a string array"""
    list = []  # list to store object string value
    maxY = len(array)  # counts the rows
    for y in array:
        maxX = len(y)  # counts the col
        for x in y:
            list.append(x.name)  # appends eacht array object name
    # creates a numpy array with maxX being colunms and maxY being rows and
    # the string being the objects name
    array = np.array(list).reshape(maxY, maxX)
    return array  # return


def highlightPos(y, x, array):
    """Function that takes an x and y cord of an array and highlights that
    item"""
    strArray = objArrayConv(array)  # converts the array to a string array
    tileAt = "~ {} ~".format(strArray[y][x])  # highlight tile
    # replaces old tile with higlighted tile
    highlighted = np.where(strArray == strArray[y][x], tileAt, strArray)
    # creates a formated where the old tile is replaced with highlited one
    table = tab.tabulate(highlighted, tablefmt="grid")
    print(table)


def findMax(array):
    """finds the max num of row in an array"""
    max = len(array) - 1  # finds max value minus 1
    max = int(max)  # integerize old max value
    return max  # returns max value
