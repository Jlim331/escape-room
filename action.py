# Josh Lim
# Comp Sci 30 P4
# 01/08/2020
# File containing all the actions property
import player
import map as mp


player = player.Player("joe")

# Code adapted from
# Let's talk data: How to Write a Text Adventure in Python Part 3
#https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
#part-3-player-action/
class Action():
    def __init__(self, method, name, hotKey, **kwargs):
        self.method = method
        self.hotKey = hotKey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey[0], self.name)


moveUp = Action(method = player.moveUp,
                name = "move up",
                hotKey = ["w", "up"],)

moveDown = Action(method = player.moveDown,
                name = "move down",
                hotKey = ["s", "down"],)

moveRight = Action(method = player.moveRight,
                name = "move right",
                hotKey = ["d", "right"],)

moveLeft = Action(method = player.moveLeft,
                name = "move left",
                hotKey = ["a", "left"],)

viewInv = Action(method = player.viewInventory,
                 name = "view inventory",
                 hotKey = ["i", "inv", "inventory"],)
