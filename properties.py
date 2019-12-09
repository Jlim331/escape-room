# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Nested dictionaries for game properties
import numpy as np
import math as m
import tabulate as tab


class Player:
    """Contains player name, inventory and position"""
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.x = 0
        self.y = 0

    def description(self):
        print(f"Hello {self.name}")
        print(f"Inventory: \n{self.inventory}")

    def findPos(self):
        "Used to find position for debugging purpose"
        print(f"y: {self.y}")
        print(f"x: {self.x}")

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -=1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1


class Map:
    """Contains world map and event conditions"""
    def __init__(self, map, eventCond):
        self.map = maps
        self.eventCond = eventCond


class Room(Map):
    """Contains positional values, roomInv and events"""
    def __init__(self, roomInv, events):
        a


def printNDict(dictName):
    """Prints out content in a nested dictionary with up to 2 layers,
    takes dictName as the dictionary name.
    """
    for dictName, key in dictName.items():
        """loops through the keys in the nested dictionary, dictName, and then
        prints the nested dictionary names along with its values.
        """
        print(dictName.title() + ":")  # prints nested dictionary name
        for items in key:
            """loops through nested dictionary key values and and prints the
            key along with the value with a tab before.
            """
            print(f"\t{items.title()} - {key[items]}")
