# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Nested dictionaries for game properties
import numpy as np
import math as m
import tabulate as tab


class Player:
    """Contains player name, inventory and position
    """
    def __init__(self, name, inventory):
        # initiates with name and inventory
        self.name = name
        self.inventory = inventory
        self.x = 1  # value for start tile
        self.y = 1  # value for start tile

    def invGen(self):
        """function for generating the inventory of player"""
        invList = []
        for i in self.inventory:
            print(f"\t{i}")  # prints list out
            invList.append(i)  # adds each item to invList

    def description(self):
        """function for generating a description"""
        print(f"Hello {self.name}")  # greets player

    def findPos(self):
        """function for finding the position of the player, used for debug"""
        print(f"y: {self.y}")  # prints y value
        print(f"x: {self.x}")  # prints x value

    def moveUp(self):
        """functino for moving the player up"""
        self.y -= 1  # moves player up

    def moveDown(self):
        """functino for moving the player down"""
        self.y += 1  # moves player down

    def moveRight(self):
        """functino for moving the player right"""
        self.x += 1  # moves player to the right

    def moveLeft(self):
        """functino for moving the player left"""
        self.x -= 1  # moves player to the left
