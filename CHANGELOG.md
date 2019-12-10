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
