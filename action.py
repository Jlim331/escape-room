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
    def __init__(self, method, name, hotKey):
        self.method = method
        self.name = name
        self.hotKey = hotKey

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

class StartTileSearch(Action):
    def __init__(self):
        super().__init__(method = map.StartTile.search,
                         name = "search",
                         hotKey = ["e", "search"])
