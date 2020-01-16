# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# File containing all player property
import numpy as np
import math as m
import tabulate as tab
import map as mp
import action as act


class Player():
    """Contains player name, inventory and position
    """
    def __init__(self, name):
        # initiates with name and inventory
        self.name = name
        self.inventory = []
        self.x = 1  # value for start tile
        self.y = 1  # value for start tile
        self.win = False
        self.giveUp = False

    def viewInventory(self):
        """function for viewing the inventory of the player"""
        for i in self.inventory:
            print("Your inventory: ")
            print(f"\t{i}")  # prints list

    def description(self):
        """function for generating a description"""
        print(f"Hello {self.name}")  # greets player

    def findPos(self):
        """function for finding the position of the player, used for debug"""
        print(f"y: {self.y}")  # prints y value
        print(f"x: {self.x}")  # prints x value

    def quit(self):
        self.giveUp = True
        print("Thank you for playing!")

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

    def doAction(self, action, tile, **kwargs):
        try:
            actionMethod = getattr(self, action.method.__name__)
            if actionMethod:
                actionMethod(**kwargs)
        except:
            actionMethod1 = getattr(tile, action.method.__name__)
            if actionMethod1:
                actionMethod1(**kwargs)
