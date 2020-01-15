# Josh Lim
# Comp Sci 30 P4
# 01/08/2020
# File containing all the actions property
from player import Player
import map

# Code adapted from
# Let's talk data: How to Write a Text Adventure in Python Part 3
#https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
#part-3-player-action/
class Action:
    def __init__(self, method, name, hotKey, **kwargs):
        self.method = method
        self.name = name
        self.hotKey = hotKey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey[0], self.name)


class MoveUp(Action):
    def __init__(self):
        super().__init__(method = Player.moveUp,
                        name = "move up",
                        hotKey = ["w", "up"])


class MoveDown(Action):
    def __init__(self):
        super().__init__(method = Player.moveDown,
                        name = "move down",
                        hotKey = ["s", "down"])

class MoveRight(Action):
    def __init__(self):
        super().__init__(method = Player.moveRight,
                        name = "move right",
                        hotKey = ["d", "right"])


class MoveLeft(Action):
    def __init__(self):
        super().__init__(method = Player.moveLeft,
                        name = "move left",
                        hotKey = ["a", "left"])


class ViewInv(Action):
    def __init__(self):
        super().__init__(method = Player.viewInventory,
                         name = "view inventory",
                         hotKey = ["i", "inv", "inventory"])

class Quit(Action):
    def __init__(self):
        super().__init__(method = Player.quit,
                         name = "quit",
                         hotKey = ["q", "quit", "stop"])


class WinTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.WinTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class WinTileOpenDoor(Action):
    def __init__(self):
        super().__init__(method = map.WinTile.openDoor,
                         name = "open door",
                         hotKey = ["o", "open"])


class StartTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.StartTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class EndTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.EndTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class EndTileOpenDoor(Action):
    def __init__(self):
        super().__init__(method = map.EndTile.openDoor,
                         name = "open",
                         hotKey = ["o", "open"])


class CabinetTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.CabinetTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class CabinetTileSearchClothes(Action):
    def __init__(self):
        super().__init__(method = map.CabinetTile.searchClothes,
                         name = "search clothes",
                         hotKey = ["z", "search clothes"])


class CabinetTileLookMirror(Action):
    def __init__(self):
        super().__init__(method = map.CabinetTile.lookMirror,
                         name = "look at mirror",
                         hotKey = ["x", "look mirror", "look into mirror"])


class CabinetTileOpenDrawer(Action):
    def __init__(self):
        super().__init__(method = map.CabinetTile.openDrawer,
                         name = "open drawer",
                         hotKey = ["c", "open drawer"])


class ChestTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.ChestTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class ChestTileOpenChest(Action):
    def __init__(self):
        super().__init__(method = map.ChestTile.openChest,
                         name = "open Chest",
                         hotKey = ["o", "open chest"])


class BookcaseTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class BookcaseTileRead1(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook1,
                         name = "Minecraft: Combat Handbook: Ultimate Collector's Edition by Erik Aronsen",
                         hotKey = ["1", "read one", "read 1"])


class BookcaseTileRead2(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook2,
                         name = "THE ESSENTIAL CALVIN AND HOBBES by Bill Watterson",
                         hotKey = ["2", "read two", "read 2"])


class BookcaseTileRead3(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook3,
                         name = "Diary of a Wimpy Kid Book 1 by Jeff Kinney",
                         hotKey = ["3", "read three", "read 3"])


class BookcaseTileRead4(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook4,
                         name = "Goosebumps: Welcome to Camp Nightmare by R L Stine",
                         hotKey = ["4", "read four", "read 4"])


class BookcaseTileRead5(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook5,
                         name = "Little Red Riding Hood by Gaby Goldsack",
                         hotKey = ["5", "read five", "read 5"])


class BookcaseTileRead6(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook6,
                         name = "Captain Underpants and the Tyrannical Retaliation of the Turbo Toilet 2000 by Dav Pilkey",
                         hotKey = ["6", "read six", "read 6"])


class BookcaseTileRead7(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.readBook7,
                         name = "The 39 Clues Book One: The Maze of Bones by Rick Riordan",
                         hotKey = ["7", "read seven", "read 7"])


class PaintingTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.PaintingTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class DeskTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.DeskTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class EmptyTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.EmptyTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class ShelveTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.ShelveTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class TableTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.TableTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class ChairTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.ChairTile.search,
                         name = "search",
                         hotKey = ["e", "search"])

class ChairTileSit(Action):
    def __init__(self):
        super().__init__(method = map.ChairTile.sit,
                         name = "sit",
                         hotKey = ["z", "sit"])
