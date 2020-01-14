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
    def __init__(self, player):
        super().__init__(method = map.WinTile.openDoor,
                         name = "open door",
                         hotKey = ["o", "open"],
                         player = player)


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


class CabinetTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.CabinetTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class ChestTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.ChestTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


class BookcaseTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.BookcaseTile.search,
                         name = "search",
                         hotKey = ["e", "search"])


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
