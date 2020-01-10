# Josh Lim
# Comp Sci 30 P4
# 01/09/2020
# File to test code
import map
import player as play
import action

player = play.Player("Joe")

print(map.cabinetTile.search())
print(map.cabinetTile.searchClothes())
print(map.cabinetTile.lookMirror())
print(map.cabinetTile.openDrawer(player))

print(player.inventory)

player.inventory.append("chest key")

print(map.chestTile.search())
print(map.chestTile.openChest(player))

print(player.inventory)

print(map.bookcaseTile.search())
print(map.bookcaseTile.readBook1())
print(map.bookcaseTile.readBook2())
print(map.bookcaseTile.readBook3())
print(map.bookcaseTile.readBook4())
print(map.bookcaseTile.readBook5(player))
print(map.bookcaseTile.readBook6())
print(map.bookcaseTile.readBook7(player))

print(player.inventory)

# startTile = mp.startTile("start", "fill in desc", 1, 1)
# exitTile = mp.endTile("exit door", "fill in desc", 3, 0)
# winTile = mp.winTile("locked door", "fill in desc", 3, 2)
# cabinetTile = mp.MapTile("cabinet", "fill in desc", 0, 0)
# chestTile = mp.MapTile("chest", "fill in desc", 1, 0)
# bookcaseTile = mp.MapTile("bookcase", "fill in desc", 2, 0)
# paintingTile = mp.MapTile("painting", "fill in desc", 0, 1)
# deskTile = mp.MapTile("desk", "fill in desc", 2, 1)
# emptyTile = mp.MapTile(" ", "fill in desc", 3, 1)
# shelveTile = mp.MapTile("shelve", "fill in desc", 0, 2)
# tableTile = mp.MapTile("table", "fill in desc", 1, 2)
# chairTile = mp.MapTile("chair", "fill in desc", 2, 2)

# Creates array for the game
# map =[
#     [cabinetTile, chestTile, bookcaseTile, exitTile],
#     [paintingTile, startTile, deskTile, emptyTile],
#     [shelveTile, tableTile, chairTile, winTile]
# ]

# class MapTile:
#     """Map Class to create tiles for the game"""
#     def __init__(self, name, desc, event, x, y):
#         self.name = name
#         self.desc = desc
#         self.event = event
#         self.x = x
#         self.y = y
