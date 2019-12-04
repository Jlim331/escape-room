# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Nested dictionaries for game properties
import numpy as np
import math as m
import tabulate as tab


class Player:
    """Contains player name, inventory and position"""
    def __init__(self, name, inventory, position):
        self.name = name
        self.inventory = inventory
        self.position = position

    def findPosition(self):
        a


class Map:
    """Contains world map and event conditions"""
    def __init__(self, array):
        a


class Room(Map):
    """Contains positional values, roomInv and events"""
    def __init__(self,):
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
