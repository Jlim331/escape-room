# Josh Lim
# Comp Sci 30 P4
# 11/07/2019
# Nested dictionaries for game properties


def nestedDictPrinter(dictName):
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
# Nested dictionary containing information for inventory
inventory = {
    "stick": {
        "ATTACK": 3,
        "DURABILITY": 5,
        },
    "iron sword": {
        "ATTACK": 15,
        "DURABILITY": 20,
        "SHARPNESS": 10,
        }
    }
# Nested dictionary containing information for mobs
mobs = {
    "spider": {
        "ATTACK": 3,
        "HIT POINTS": 10,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
    }
# Nested dictionary containing information for character
character = {
    "stats": {
        "ATTACK": 10,
        "HIT POINTS": 100,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
}
# Nested dictionary containing information for locations
locations = {
    "path 1": {
        "description": "You have encountered a level 1 mob!",
        },
    "path 2": {
        "description": "You are greeted with 2 paths, which will you choose?",
        },
    "path 3": {
        "description": "You find yourself in a forest, what will you do?",
    }
}
print("\nInventory")
# Prints out the content of the weapons nested dictionary
nestedDictPrinter(inventory)
print("\nMobs")
# Prints out the content of the mobs nested dictionary
nestedDictPrinter(mobs)
print("\nCharacter")
# Prints out the content of the character nested dictionary
nestedDictPrinter(character)
print("\nLocations")
# Prints out the content of the locations nested dictionary
nestedDictPrinter(locations)
