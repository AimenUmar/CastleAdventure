# CastleAdventure
SP23-BAI-008
SP23-BAI-024

# Mystery Castle Game - Documentation

# Overview

The Mystery Castle Game is an interactive, text-based game where players explore a mysterious castle, solve puzzles, find hidden items, and make their way through different rooms. Each action contributes to advancing the game by unlocking new paths, interacting with objects, and managing health and steps. The game has the following key features:

 - Moving through different rooms in the castle
- Solving puzzles and riddles
- Managing inventory
- Tracking player’s health and steps
- Saving and loading game progress

# Main Classes and Functionalities

# 1. Castle Class

This class defines the castle structure, rooms, and the player’s ability to move in different directions. It also includes functions for looking around rooms and updating the player's current location.

# Attributes:
- `map`: Defines the layout of the castle and the connections between rooms.
- `currentRoom`: Tracks the player’s current room in the castle.
- `directions`: A list of possible directions the player can move (e.g., north, south, east, west, up, down).

# Methods:
- `goDirection(direction, stepAndHealth)`: Moves the player in the specified direction if it is valid for the current room, updating steps.
- `updateCurrentRoom(direction)`: Updates the player's current room based on the direction chosen.
- `look(inventory)`: Displays available directions and items in the current room, filtering items already in the player's inventory.
- `showDescription()`: Shows a detailed description of the current room.
- `getCurrentRoom()`: Returns the current room the player is in.

# 2. Inventory Class

Manages the player’s items. Players can collect, drop, and examine items they find in different rooms. It also allows for the use of specific items for solving puzzles.

# Attributes:
- `TotalItems`: A dictionary of all possible items in the game.
- `UserItems`: A list of items currently held by the player.

# Methods:
- `takeItem(item, castle)`**: Adds an item from the current room to the player's inventory if it is not already in possession.
- `dropItem(item)`**: Removes an item from the inventory.
- `examine(item)`**: Provides a description of an item.
- `use(item)`**: Allows the player to use an item from their inventory.
- `showItems()`**: Displays the list of items in the player's inventory.

# 3. Puzzles Class

Contains different puzzles and riddles that the player must solve to progress through the game. The puzzles may give clues, unlock new paths, or award items.
Methods:
- `AlchemyBookPuzzle(castle, inventory)`: A puzzle involving chemical elements to create a key.
- `ArtGalleryRiddle()`: A riddle in the art gallery that opens a secret door upon completion.
- `WineCellarHammer(castle, inventory)`: Requires the player to use a hammer to open a secret box.
- `theSigilsOfTower(ScoreAndHealth)`: A riddle that rewards the player with bonus steps.
- `CatacombRiddle()`: Solves a riddle to open the catacomb exit.
- `rodPuzzle(ScoreAndHealth)`: A rod movement puzzle that awards bonus points if solved.
- `symbolLockPuzzle(castle, inventory)`: A code-cracking puzzle that grants a key when solved.
- `banquetHallChandelier(castle, inventory)`: A puzzle to move a chandelier by using a rope.

# 4. StepsAndHealth Class

This class tracks the player's steps and health. As players move through the castle, their health depletes. If health reaches zero, the player must recharge it at the cost of extra steps.

# Attributes:
- `steps`: Tracks the number of steps taken by the player.
- `health`: Tracks the player's current health, starting from 1000 and decreasing over time.
- `highestScore`: The highest score saved in the game.

# Methods:
- `getSteps()`: Returns the total steps taken.
- `incrementSteps()`: Increases the step count and decreases health.
- `saveScore()`: Saves the current score (steps) to a file.
- `getHighestScore()`: Retrieves the highest score from saved scores.
- `getHealth()`: Returns the current health.
- `decrementHealth()`: Decreases the player's health by 100 per step, with warnings at 500 and 200.
- `rechargeHealth()`: Recharges health to 2000 at the cost of 20 additional steps.

# 5. GameState Class

Handles saving, loading, and clearing the game state. It captures the player's current room, inventory, health, and puzzle progress, allowing the player to resume from where they left off.

# Methods:
- `saveGame(castle, inventory, stepsAndHealth, game)`: Saves the current game state to a file.
- `loadGame(castle, inventory, stepsAndHealth, game)`: Loads the saved game state from a file.
- `clearGame()`: Clears the saved game state, resetting the game.

# Additional Functionalities

# Saving and Loading
The game allows players to save their progress, including the current room, inventory, steps, and health. Players can load the game later to resume from where they left off.

# Health Management
The player's health decreases with each step taken. If health drops to zero, they can recharge at the cost of additional steps, adding a survival element to the gameplay.

# Inventory System
The inventory system is critical for solving puzzles and advancing through the castle. Items found in one room may need to be used in another to solve puzzles or unlock hidden paths.

# Puzzles and Riddles
Puzzles add variety and challenge to the game, requiring players to use logical reasoning, memory, and their inventory to proceed.

# Example Gameplay Flow
1. The player starts in the **Entrance Hall** and can explore by typing directions (north, south, etc.).
2. Upon entering a new room, the player can "look" around to see possible exits and items.
3. Players can collect items into their inventory and use them later to solve puzzles.
4. Health and steps are continuously tracked as the player moves through the castle.
5. Solving puzzles unlocks new rooms or rewards the player with special items.
6. The player can save and load the game at any time to continue their progress later.


# SAMPLE OUTPUT 1 #
Welcome to the Mysterious Castle Adventure!
To go towards a specific you have to write 'go directionName'.
To pick, drop, examine and use items you have to write 'pick itemName', 'drop itemName', 'examine itemName' and 'use itemName'.
You have 2000 cells as your health. Every step will cost you 100 cells.
To exit the game enter 'quit'.

To start game enter start: start
A grand and open space with high ceilings and a chandelier. The air smells slightly of old wood.

go north
You are now in  Great Hall

A vast, open hall with a long table in the center. Portraits of old kings line the walls.

The ancient staircase rose, quiet and unmoving, as you ascended higher.
This might be a hint for any of your puzzle.
pick rope
rope picked successfully
go east
You are now in  Banquet Hall

A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.

A chandelier has fallen down.
 In order to move it, you need to use a rope.
use rope
You have successfullly pulled the chandelier up. You can now move further.

look
You are now in  Banquet Hall

There is Wine Cellar to the north.

There is Chapel to the east.

There is Great Hall to the west.

The items that are present in this room: screwdriver
go north
You are now in  Wine Cellar

Rows of dusty wine bottles line the walls. The air is cool, and the floor is cold stone.

pick hammer
hammer picked successfully
go east
You are now in  Library

A small, musty library filled with ancient books. There’s a strange draft coming from behind a bookshelf.

To open this box you have to solve a puzzle.
Enter yes to solve the puzzle:
yes
You have to make a salt. In order to do it you have to chose the right chemical composition.
Choose one of these metals: Na  Au  Pb  Fe
Na 
Now choose one of the these element: O  Te  Cl  Xe
Cl
Congratulation you got 1st part of golden key!

Golden key 1 picked successfully
go west
You are now in  Wine Cellar

Rows of dusty wine bottles line the walls. The air is cool, and the floor is cold stone.

Health has been Decremented to 500
go south
You are now in  Banquet Hall

A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.

look
You are now in  Banquet Hall

There is Wine Cellar to the north.

There is Chapel to the east.

There is Great Hall to the west.

The items that are present in this room: screwdriver
go west
You are now in  Great Hall

A vast, open hall with a long table in the center. Portraits of old kings line the walls.

The ancient staircase rose, quiet and unmoving, as you ascended higher.
This might be a hint for any of your puzzle.
go west
You are now in  Tower Staircase

A spiraling stone staircase, dimly lit by torches, leading up to the tower.

WARNING! Health has been Decremented to 200
A bonus puzzle for you. Enter yes to play or no to skip: yes
What keeps you moving up, though it itself is still?
stairs
Yay! you got 2 bonus steps
go up
You are now in  Art Gallery

A narrow room filled with paintings of unknown origin. Dust-covered statues stand in the corners.

A secret box is present. Do you want to open it?
yes
In order to open it you have to use a hammer.
use hammer
Here is a riddle for you:
The man who made it does not need it, the man who bought it does not want it, and the man who needs it does not know it. What is it?

a coffin
You made a painting shift from its location!
 A secret door towards north is open now.

go north
You are now in  Catacombs

A dark, musty tunnel filled with bones and ancient burial sites. The air is damp and suffocating.

Note: Your health is at 0. You need to Recharge in order to Continue the Game.
 Recharging your Health will cost 20 additional Steps to your end score.

Do you want to Recharge you health: yes
Your Health has been Recharged. Total Steps now:  28

Here is a riddle for you:
I am always running, but never get tired or hot. What am I?
 a river
You have opened the door for secret underground river exit.

go north
You are now in  Underground River Exit

A small cave opening that leads to an underground river. The sound of water echoes around.

Congratulations you got out using the secret way!!
Save file has been cleared.



# SAMPLE OUTPUT 2 #
Welcome to the Mysterious Castle Adventure!
To go towards a specific you have to write 'go directionName'.
To pick, drop, examine and use items you have to write 'pick itemName', 'drop itemName', 'examine itemName' and 'use itemName'.
You have 2000 cells as your health. Every step will cost you 100 cells.
To exit the game enter 'quit'.

To start game enter start: start
A grand and open space with high ceilings and a chandelier. The air smells slightly of old wood.

go north
You are now in  Great Hall

A vast, open hall with a long table in the center. Portraits of old kings line the walls.

The ancient staircase rose, quiet and unmoving, as you ascended higher.
This might be a hint for any of your puzzle.
go east
You are now in  Banquet Hall

A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.

A chandelier has fallen down.
 In order to move it, you need to use a rope.
use rope
No such item present in your inventory. Go find it in order to use it.

look
You are now in  Banquet Hall

There is Wine Cellar to the north.

There is Chapel to the east.

There is Great Hall to the west.

The items that are present in this room: screwdriver
go east
You cannot go towards the east as the chandelier is blocking the way. You need a rope to remove it.
go west
You are now in  Great Hall

A vast, open hall with a long table in the center. Portraits of old kings line the walls.

The ancient staircase rose, quiet and unmoving, as you ascended higher.
This might be a hint for any of your puzzle.
pick rope
rope picked successfully
go east
You are now in  Banquet Hall

A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.

A chandelier has fallen down.
 In order to move it, you need to use a rope.
use rope
You have successfullly pulled the chandelier up. You can now move further.

go east
You are now in  Chapel

An ancient chapel with dusty pews and stained-glass windows. The room is eerily silent.

Health has been Decremented to 500
To open this Safe you need to crack a code.
Enter yes to solve the puzzle: yes
Guess the Correct number sequence to unlock this Safe &^#))
76300
Congratulations you got the 2nd part of golden key!

Golden key 2 picked successfully
look
You are now in  Chapel

There is Inner Chambers to the north.

There is Great Hall to the south.

There is Royal Vault to the east.

There is Banquet Hall to the west.

There are no new items in this room.
go west 
You are now in  Banquet Hall

A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.

go north
You are now in  Wine Cellar

Rows of dusty wine bottles line the walls. The air is cool, and the floor is cold stone.

go east
You are now in  Library

A small, musty library filled with ancient books. There’s a strange draft coming from behind a bookshelf.

WARNING! Health has been Decremented to 200
To open this box you have to solve a puzzle.
Enter yes to solve the puzzle:
yes
You have to make a salt. In order to do it you have to chose the right chemical composition.
Choose one of these metals: Na  Au  Pb  Fe
Na
Now choose one of the these element: O  Te  Cl  Xe
Cl
Congratulation you got 1st part of golden key!

Golden key 1 picked successfully
look
You are now in  Library

There is Wine Cellar to the west.

There are no new items in this room.
go north
You can't go towards north

You are at a dead end. You can only go backward toward the Wine Cellar.
go west
You are now in  Wine Cellar

Rows of dusty wine bottles line the walls. The air is cool, and the floor is cold stone.

look
You are now in  Wine Cellar

There is Banquet Hall to the south.

There is Library to the east.

The items that are present in this room: hammer
go south
You are now in  Banquet Hall

A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.

Note: Your health is at 0. You need to Recharge in order to Continue the Game.
 Recharging your Health will cost 20 additional Steps to your end score.

Do you want to Recharge you health: yes
Your Health has been Recharged. Total Steps now:  30

go east
You are now in  Chapel

An ancient chapel with dusty pews and stained-glass windows. The room is eerily silent.

go north
You are now in  Inner Chambers

A dimly lit, narrow room with stone walls. A single table sits in the center, covered in dust. It feels like it once held something valuable.

go north
You are now in  Servant Quarters

A small, cramped space filled with old, worn-out beds and broken furniture. The air smells musty and stale.

Here is a Puzzle for you! You will get Bonus Points for this

Do you want to Play?
yes
On the walls, You can see rods arranged in the shape of a Hexagon .
In Order to solve the puzzle, you need to move Exactly two sticks in Clockwise Direction to make a Triangle.
Enter your First Move (e.g 'rod 1' , 'rod 2'): rod 1
Enter your Second Move (e.g 'rod 1' , 'rod 2'): rod 4
Congratulations! You have moved the rods and created a Triangle.
go south
You are now in  Inner Chambers

A dimly lit, narrow room with stone walls. A single table sits in the center, covered in dust. It feels like it once held something valuable.

go south
You are now in  Chapel

An ancient chapel with dusty pews and stained-glass windows. The room is eerily silent.

go east
You are now in  Royal Vault

A heavily fortified room with a large vault door. The air is dense with secrets.

go north
You are now in  Main Exit

A narrow, hidden exit from the castle, leading into the dense forest.

Use golden key part 1 and golden key part 2 to open the main exit
 in order to use them simultaneously you have to write 'Use Golden key 1 and Golden key 2'
Use Golden key 1 and Golden key 2
You made it through main exit.
Save file has been cleared.
