# Josh Lim
# Comp Sci 30 P4
# 01/08/2020
# File containing all the actions property
from player import Player
import map

# Code adapted from
# Let's talk data: How to Write a Text Adventure in Python Part 3
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
# part-3-player-action/


class Action:
    """Class for creating action objects"""
    def __init__(self, method, name, hotKey, **kwargs):
        self.method = method  # method to be executed for the action
        self.name = name  # action name
        self.hotKey = hotKey  # action hotkey
        self.kwargs = kwargs  # any other parameter action method needs


class MoveUp(Action):
    """Creates a move up action object"""
    def __init__(self):
        super().__init__(method=Player.moveUp,
                         name="move up",
                         hotKey=["w", "up"])


class MoveDown(Action):
    """Creates a move down action object"""
    def __init__(self):
        super().__init__(method=Player.moveDown,
                         name="move down",
                         hotKey=["s", "down"])


class MoveRight(Action):
    """Creates a move right action object"""
    def __init__(self):
        super().__init__(method=Player.moveRight,
                         name="move right",
                         hotKey=["d", "right"])


class MoveLeft(Action):
    """Creates a move left action object"""
    def __init__(self):
        super().__init__(method=Player.moveLeft,
                         name="move left",
                         hotKey=["a", "left"])


class ViewInv(Action):
    """Creates a view inventory action object"""
    def __init__(self):
        super().__init__(method=Player.viewInventory,
                         name="view inventory",
                         hotKey=["i", "inv", "inventory"])


class Quit(Action):
    """Creates a quit action object"""
    def __init__(self):
        super().__init__(method=Player.quit,
                         name="quit",
                         hotKey=["q", "quit", "stop"])


class WinTileSearch(Action):
    """Creates a win tile search action object"""
    def __init__(self):
        super().__init__(method=map.WinTile.search,
                         name="search",
                         hotKey=["e", "search"])


class WinTileOpenDoor(Action):
    """Creates a win tile open door action object"""
    def __init__(self):
        super().__init__(method=map.WinTile.openDoor,
                         name="open door",
                         hotKey=["o", "open"])


class StartTileSearch(Action):
    """Creates a start tile search action object"""
    def __init__(self):
        super().__init__(method=map.StartTile.search,
                         name="search",
                         hotKey=["e", "search"])


class EndTileSearch(Action):
    """Creates an end tile search action object"""
    def __init__(self):
        super().__init__(method=map.EndTile.search,
                         name="search",
                         hotKey=["e", "search"])


class EndTileOpenDoor(Action):
    """Creates an end tile open door action object"""
    def __init__(self):
        super().__init__(method=map.EndTile.openDoor,
                         name="open",
                         hotKey=["o", "open"])


class CabinetTileSearch(Action):
    """Creates a cabinet tile search action object"""
    def __init__(self):
        super().__init__(method=map.CabinetTile.search,
                         name="search",
                         hotKey=["e", "search"])


class CabinetTileSearchClothes(Action):
    """Creates a cabinet tile search clothes action object"""
    def __init__(self):
        super().__init__(method=map.CabinetTile.searchClothes,
                         name="search clothes",
                         hotKey=["z", "search clothes"])


class CabinetTileLookMirror(Action):
    """Creates a cabinet tile look mirror action object"""
    def __init__(self):
        super().__init__(method=map.CabinetTile.lookMirror,
                         name="look at mirror",
                         hotKey=["x", "look mirror", "look into mirror"])


class CabinetTileOpenDrawer(Action):
    """Creates a cabinet tile open drawer action object"""
    def __init__(self):
        super().__init__(method=map.CabinetTile.openDrawer,
                         name="open drawer",
                         hotKey=["c", "open drawer"])


class ChestTileSearch(Action):
    """Creates a chest tile search action object"""
    def __init__(self):
        super().__init__(method=map.ChestTile.search,
                         name="search",
                         hotKey=["e", "search"])


class ChestTileOpenChest(Action):
    """Creates a chest tile open chest action object"""
    def __init__(self):
        super().__init__(method=map.ChestTile.openChest,
                         name="open Chest",
                         hotKey=["o", "open chest"])


class BookcaseTileSearch(Action):
    """Creates a bookcase tile search action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.search,
                         name="search",
                         hotKey=["e", "search"])


class BookcaseTileRead1(Action):
    """Creates a bookcase tile read 1 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook1,
                         name="read book 1",
                         hotKey=["1", "read one", "read 1"])


class BookcaseTileRead2(Action):
    """Creates a bookcase tile read 2 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook2,
                         name="read book 2",
                         hotKey=["2", "read two", "read 2"])


class BookcaseTileRead3(Action):
    """Creates a bookcase tile read 3 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook3,
                         name="read book 3",
                         hotKey=["3", "read three", "read 3"])


class BookcaseTileRead4(Action):
    """Creates a bookcase tile read 4 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook4,
                         name="read book 4",
                         hotKey=["4", "read four", "read 4"])


class BookcaseTileRead5(Action):
    """Creates a bookcase tile read 5 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook5,
                         name="read book 5",
                         hotKey=["5", "read five", "read 5"])


class BookcaseTileRead6(Action):
    """Creates a bookcase tile read 6 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook6,
                         name="read book 6",
                         hotKey=["6", "read six", "read 6"])


class BookcaseTileRead7(Action):
    """Creates a bookcase tile read 7 action object"""
    def __init__(self):
        super().__init__(method=map.BookcaseTile.readBook7,
                         name="read book 7",
                         hotKey=["7", "read seven", "read 7"])


class PaintingTileSearch(Action):
    """Creates a painting tile search action object"""
    def __init__(self):
        super().__init__(method=map.PaintingTile.search,
                         name="search",
                         hotKey=["e", "search"])


class DeskTileSearch(Action):
    """Creates a desk tile search action object"""
    def __init__(self):
        super().__init__(method=map.DeskTile.search,
                         name="search",
                         hotKey=["e", "search"])


class EmptyTileSearch(Action):
    """Creates a empty tile search action object"""
    def __init__(self):
        super().__init__(method=map.EmptyTile.search,
                         name="search",
                         hotKey=["e", "search"])


class ShelveTileSearch(Action):
    """Creates a shelf tile search action object"""
    def __init__(self):
        super().__init__(method=map.ShelveTile.search,
                         name="search",
                         hotKey=["e", "search"])


class TableTileSearch(Action):
    """Creates a table tile search action object"""
    def __init__(self):
        super().__init__(method=map.TableTile.search,
                         name="search",
                         hotKey=["e", "search"])


class ChairTileSearch(Action):
    """Creates a chair tile search action object"""
    def __init__(self):
        super().__init__(method=map.ChairTile.search,
                         name="search",
                         hotKey=["e", "search"])


class ChairTileSit(Action):
    """Creates a chair tile sit action object"""
    def __init__(self):
        super().__init__(method=map.ChairTile.sit,
                         name="sit",
                         hotKey=["z", "sit"])
