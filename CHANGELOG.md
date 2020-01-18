# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Prerelease Version]

## [0.0.1] - 2019-11-07
### Added
 - Created CHANGELOG.md
 - Created README.me
 - Created task.todo
 - Created game.py
 - Created locations.py
 - Created menu.py
 - Created properties.py

## [0.0.2] - 2019-11-07
### Changed
- Added continuous play functionality to menu.py
- Updated Task to reflect changes
- Updated locations to reflect new game

## [0.0.3] - 2019-11-18
### Added
 - Added a description for how to quit the game
 - Added more options for the user to search
 - Created map.py to generate a map of the locations and elements

### Changed
 - Changed format of printing in menu.py to look more readable
 - Updated properties.py to reflect new game
 - Organized escapeRoom into a module
 - Renamed nestedDictPrint to printNDict in properties.py

## [0.0.4] - 2019-12-09
### Added
 - Added movement.py file for the movement in the game
 - Added a xy based movement system in game.py
 - Added classes to store map tile objects in

### Removed
 - Removed the old choose your own adventure like menu system

### Fixed
 - Fixed a bug where rand center would duplicate center tile

## [0.0.4] - 2020-01-08
### Added
 - Unique tile option to cabinet tile
 - Title screen with play, help and quit option
 - Class function for each tile
 - Class function for actions
 - Class function for items

### Changed
 - Changed the name to movement.py to action.py

### Removed
 - removed formatting for menu (color doesn't work on all computers)
 - removed empty files
 - removed old way of generating map

## [0.0.5] - 2020-01-12
### Added
 - Unique Tile option

### Changed
 - Changed the game to work with class based tile

## [0.0.6] - 2020-01-13
### Added
 - player doAction to work both with player methods and tile methods
 - Unique tile option in menu list
 - Print out for player x andy and tile x and y for debugging

### Changed
 - tileExist to be based of an array rather than a dictionary


### Fixed
 - Menu system to work with unique tile option
 - Movement system to display correct option to avoid crashed

## [0.0.7] - 2020-01-14
### Added
 - Unique tile options

### Changeds

### Fixed
 - Found an alternative to passing player class through kwargs
 - rename openDrawer to openDrawerFlag to fix openDrawer() not running

## [0.0.8] - 2020-01-15
### Changed
 - searchFlag for each tile resets every time an action requiring search flag is ran
 - The formatting of the text in the text interface
 - The interface to clear after every action input

## [0.0.9] - 2020-01-16
### Added
 - Added a map that highlights player location as it is updated

### Changed
 - Updated the format of the text interface to look nicer
