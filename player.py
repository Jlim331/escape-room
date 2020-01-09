# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Nested dictionaries for game properties
import numpy as np
import math as m
import tabulate as tab
import map as mp
import action as act


class Player:
    """Contains player name, inventory and position
    """
    def __init__(self, name, inventory):
        # initiates with name and inventory
        self.name = name
        self.inventory = inventory
        self.x = 1  # value for start tile
        self.y = 1  # value for start tile

    def viewInventory(self):
        """function for viewing the inventory of the player"""
        for i in self.inventory:
            print(f"\t{i}")  # prints list

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

    def adjacentMoves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if map.tileExists(self.x + 1, self.y):
            moves.append(actions.moveRight)
        if map.tileExists(self.x - 1, self.y):
            moves.append(actions.moveLeft)
        if map.tileExists(self.x, self.y - 1):
            moves.append(actions.moveUp)
        if map.tileExists(self.x, self.y + 1):
            moves.append(actions.moveDown)
        return moves

    def availableActions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacentMoves()
        moves.append(actions.viewInventory)
        return moves

    def doAction(self, action, **kwargs):
        actionMethod = getattr(self, action.method)
        if actionMethod:
            actionMethod(**kwargs)
