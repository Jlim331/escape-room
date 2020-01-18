# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# File containing all player property


class Player():
    """Class to create a player for the game"""
    def __init__(self, name):
        """intiates the class with an inputed name, name"""
        self.name = name
        self.inventory = []
        self.x = 1  # used to find which tileX player is on, 1 is start
        self.y = 1  # used to find which tileY player is on, 1 is start
        self.win = False  # boolean to check if player won
        self.giveUp = False  # boolean to check if player gave up
        self.turnCounter = 0  # turn counter to count turns

    def viewInventory(self):
        """Method for viewing the players inventory"""
        print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Your inventory:""".strip("\n"))  # strips the string of new lines
        if self.inventory:  # checks if there is anything in player's inv
            for i in self.inventory:
                print(f"\t{i}".title())  # prints each item in player inv
        else:
            print("Nothing")  # prints nothing if there is nothing in inv
        print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """.strip())  # strips the string of new lines

    def findPos(self):
        """Method for finding the position of the player, used for debug"""
        print(f"y: {self.y}")  # prints y value
        print(f"x: {self.x}")  # prints x value

    def quit(self):
        """Method for quitting the game"""
        self.giveUp = True  # sets give up to true
        print(f"Turn {self.turnCounter}")  # prints turn counter
        print("Thank you for playing!")

    def moveUp(self):
        """Method for moving the player up"""
        self.y -= 1  # moves player up

    def moveDown(self):
        """Method for moving the player down"""
        self.y += 1  # moves player down

    def moveRight(self):
        """Method for moving the player right"""
        self.x += 1  # moves player to the right

    def moveLeft(self):
        """Method for moving the player left"""
        self.x -= 1  # moves player to the left

    # Code adapted from
    # Let's talk data: How to Write a Text Adventure in Python Part 3
    # https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-
    # part-3-player-action/
    def doAction(self, action, tile, **kwargs):
        """Method used to execute a function, action, in a tile class, tile
        or player class, self, and any aditional paramets, **kwargs, that the
        action function needs"""
        # Tries to execute action in player class
        try:
            #  Looks for action method in player class
            actionMethod = getattr(self, action.method.__name__)
            if actionMethod:  # if found action method in player
                actionMethod(**kwargs)  # executes method
        # If it can't find action in player class then it'll execute it in
        # tile calss
        except:
            #  Looks for action method in the tile class
            actionMethod1 = getattr(tile, action.method.__name__)
            if actionMethod1:  # if found action method in tile
                actionMethod1(**kwargs)  # executes method
