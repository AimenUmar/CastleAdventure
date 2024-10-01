import random
class Castle:
    def __init__(self, map):
        self.map = map
        self.currentRoom = "Entrance Hall"
        self.directions = ["north", "south", "east", "west", "up", "down"]

    # Method for updating your Direction SP23-BAI-024
    def goDirection(self, direction, stepAndHealth):
        if direction in self.directions:
            if direction in self.map[self.getCurrentRoom()]:
                self.updateCurrentRoom(direction)
                self.showDescription()
                stepAndHealth.incrementSteps()
            else:
                print(f"You can't go towards {direction} \n")
        else:
            print("Invalid input. No such direction present \n")
    
    # method for updating current room SP23-BAI-008
    def updateCurrentRoom(self, direction):
        roomDetails = self.map[self.currentRoom]
        if direction in roomDetails.keys():
            self.currentRoom = roomDetails[direction]
            print("You are now in " , self.currentRoom, "\n")
        else:
            print("No room there. \n")

    # Method for Displaying Detailed Description of your room SP23-BAI-008
    def look(self, inventory):    
        roomDetails = self.map[self.currentRoom]
        print("You are now in " , self.currentRoom , "\n")

        for roomDirection in self.directions:
            if roomDirection in roomDetails:
                nextRoom = roomDetails[roomDirection]
                print(f"There is {nextRoom} to the {roomDirection}. \n")
        if roomDetails["items"]:

            items_to_display = [item for item in roomDetails["items"] if item not in inventory.UserItems and item in inventory.TotalItems]
            
            if items_to_display:
                print("The items that are present in this room:", ',\n'.join(items_to_display))
            else:
                print("There are no new items in this room.")

    # Method to show comprehensive description of room SP23-BAI-024
    def showDescription(self):
        print(self.map[self.currentRoom]["description"] , "\n")

    # SP23-BAI-024
    def getCurrentRoom(self):
        return self.currentRoom
    
class Inventory:
    def __init__(self, items):
        self.TotalItems = items
        self.UserItems = []

    # Add item to your inventory SP23-BAI-024
    def takeItem(self, item, castle):
        itemsList = list(self.TotalItems.keys())
        CurrentRoomItems = list(castle.map[castle.getCurrentRoom()]["items"].keys())
        if item in itemsList and item in CurrentRoomItems:
            if item not in self.UserItems:
                self.UserItems.append(item)
                self.TotalItems.pop(item)
                print(f"{item} picked successfully")
            else:
                print(f"{item} already present")
        else:
            print(f"Can't add {item}")

    # Drop item from your inventory SP23-BAI-024
    def dropItem(self, item):
        if item in self.UserItems:
            self.UserItems.remove(item)
            self.UserItems.append(item)
            print(f"{item} dropped successfully \n")
        else:
            raise("No such item present in your inventory \n")

    # To Show description of an item SP23-BAI-024
    def examine(self, item):
        if item in self.TotalItems:
            print(self.TotalItems[item])

    # To use an item SP23-BAI-024
    def use(self, item):
        if item in self.UserItems:
            self.UserItems.remove(item)
            return True
        else:
            print("No such item present in your inventory. Go find it in order to use it.\n")
            return False
        
    def showItems(self):
        print(self.UserItems)

class Puzzles:
    def __init__(self):
        self.artGalleryPlayed = False

    # A puzzle to get Golden Key Part 1 SP23-BAI-024
    def AlchemyBookPuzzle(self, castle, inventory):
        print("To open this box you have to solve a puzzle.")
        userInput = input("Enter yes to solve the puzzle:\n")
        if userInput == 'yes' or userInput == 'Yes':
            print("You have to make a salt. In order to do it you have to chose the right chemical composition.")
            userInput = input("Choose one of these metals: Na  Au  Pb  Fe\n")
            while userInput != 'Na':
                userInput = input("Incorrect metal. Retry: ")
            userInput = input("Now choose one of the these element: O  Te  Cl  Xe \n")
            while userInput != 'Cl':
                userInput = input("Incorrect element. Retry: ")
            print("Congratulation you got 1st part of golden key! \n")
            item = list(castle.map[castle.getCurrentRoom()]["items"].keys())
            inventory.takeItem(item[0], castle)
            return True
        else:
            return False

    # A Puzzle to open secret room towards Catacombs SP23-BAI-024
    def ArtGalleryRiddle(self):
        print("Here is a riddle for you:")
        print("The man who made it does not need it, the man who bought it does not want it, and the man who needs it does not know it. What is it? \n")
        userinput = input()
        while userinput != 'a coffin' and userinput != "coffin":
            userinput = input("Retry: ")
        print("You made a painting shift from its location!\n A secret door towards north is open now.\n")

    # A puzzle to Open the Mystery Box in Art Gallery SP23-BAI-024
    def WineCellarHammer(self, castle, inventory):
        if castle.getCurrentRoom() == "Art Gallery":
            user = input("A secret box is present. Do you want to open it? \n")
            if user == 'Yes' or user == 'yes':
                user = input("In order to open it you have to use a hammer.\n")
                if user == "use hammer":
                    item = user.split()
                    flag = inventory.use(item[1])
                    if flag == True and self.artGalleryPlayed == False:
                        self.ArtGalleryRiddle()
                        self.artGalleryPlayed = True 
                        return True
            else:
                return False
    
    # A Puzzle to Get some Bonus Points SP23-BAI-024
    def theSigilsOfTower(self, ScoreAndHealth):
        print("What keeps you moving up, though it itself is still?")
        user = input()
        while user != "Stairs" and user != "stairs":
                user = input("Incorrect answer. Retry: ")
        print("Yay! you got 2 bonus steps")
        ScoreAndHealth.steps = ScoreAndHealth.steps - 2
    
    # A puzzle to Open the Secret Tunnel towards Secret Exit SP23-BAI-008
    def CatacombRiddle(self):
        print("Here is a riddle for you:")
        playerInput = input ("I am always running, but never get tired or hot. What am I?\n ")
        while playerInput != "a river" and playerInput != "river":
            playerInput = input("Retry: ")
        print("You have opened the door for secret underground river exit. \n")

    # A Puzzle to get Bonus points in Servant Quarters SP23-BAI-008
    def rodPuzzle(self, ScoreAndHealth):
        print("Here is a Puzzle for you! You will get Bonus Points for this\n")
        playerInput = input("Do you want to Play? \n")

        if playerInput == 'yes' or playerInput == 'Yes':
            print("On the walls, You can see rods arranged in the shape of a Hexagon .\nIn Order to solve the puzzle, you need to move Exactly two sticks in Clockwise Direction to make a Triangle.")           
            puzzleAnswer = {"rod 1": "rod 4", "rod 4" : "rod 1"}       
            count = 0
            maxCount = 4
            while count < maxCount:
                move1 = input("Enter your First Move (e.g 'rod 1' , 'rod 2'): ")
                move2 = input("Enter your Second Move (e.g 'rod 1' , 'rod 2'): ")
                if move1 in puzzleAnswer and puzzleAnswer[move1] == move2:
                    print("Congratulations! You have moved the rods and created a Triangle.")
                    ScoreAndHealth.steps = ScoreAndHealth.steps - 2
                    return True
                else:
                    print("Wrong move. Retry")
                    count += 1            
            print("Sorry! You've used all your tries.")
            return False
        else:
            print("You choose to miss this Golden Opportunity")
            return False
 
    # A Puzzle to get Golden key Part 2 SP23-BAI-008
    def symbolLockPuzzle(self, castle, inventory):
        symbol_dict = {
            '!': '1', '@': '2', '#': '3','$': '4','%': '5', '^': '6', '&': '7', '*': '8', '(': '9',')': '0' }
        symbol = "!@#$%^&*()" 

        safeCode = ""
        safeAnswer = ""
        for i in range(5):
            safeCode += random.choice(symbol)
        for j in safeCode:
            safeAnswer += symbol_dict[j]
                        
        print("To open this Safe you need to crack a code.")
        playerInput = input("Enter yes to solve the puzzle: ")
        if playerInput == 'yes' or playerInput == 'Yes':
            playerInput = input("Guess the Correct number sequence to unlock this Safe " + safeCode + "\n")
            while playerInput != safeAnswer:
                playerInput = input("Incorrect code. Try Again: ")
            print("Congratulations you got the 2nd part of golden key! \n")
            item = list(castle.map[castle.getCurrentRoom()]["items"].keys())
            inventory.takeItem(item[0], castle)
            return True
        else:
            return False
        
    # A puzzle to Pull up the Chandelier that is Blocking our way SP23-BAI-008
    def banquetHallChandelier(self, castle, inventory):
        checkPoint = False
        if castle.getCurrentRoom() == "Banquet Hall":
            print("A chandelier has fallen down.")           
            playerInput = input(" In order to move it, you need to use a rope.\n")
            while playerInput != 'use rope':
                playerInput = input("Wrong Answer. Retry: ")                
            if inventory.use("rope") == True:
                print("You have successfullly pulled the chandelier up. You can now move further. \n")
                checkPoint = True
        return checkPoint
            
               
class StepsAndHealth:
    def __init__(self):
        self.steps = 0
        self.health = 1000
        self.highestScore = 10000

    def getSteps(self):
        return self.steps
    
    # A Method to count your steps SP23-BAI-024
    def incrementSteps(self):
        self.steps = self.steps + 1
        self.decrementHealth()


    # A Method to put your score in File SP23-BAI-024
    def saveScore(self):
        try:
            f = open('Score.txt' , 'w')
            print(self.steps, file= f)
            f.close()
        except Exception as e:
            print(f"Error: {e}")


    # A Method to get Highest Score at the end of the Game SP23-BAI-024
    def getHighestScore(self):
        try:
            scores = [int(score.strip()) for score in open('Score.txt').read()]
            if not hasattr(self, 'highestScore'):
                self.highestScore = -10
            for score in scores:
                if score > self.highestScore:
                    self.highestScore = score
        except Exception as e:
            print(f"Error: {e}")
        
        
        return self.highestScore       

    
    def getHealth(self):
         return self.health


    # A Method to decrease your health with each step SP23-BAI-008
    def decrementHealth(self):
        if self.health > 0:
            self.health -= 100   
            if self.health == 500:
                print("Health has been Decremented to 500")
            if self.health == 200:
                print("WARNING! Health has been Decremented to 200")
            if self.health <= 0:
                self.rechargeHealth()
        else:
            return
            
    # A method to recharge your health SP23-BAI-008
    def rechargeHealth(self):
        print("Note: Your health is at 0. You need to Recharge in order to Continue the Game.\n Recharging your Health will cost 20 additional Steps to your end score.\n")    
        playerInput = input("Do you want to Recharge you health: ")
        if playerInput == 'yes' or playerInput == 'Yes':
            self.health = 2000
            self.steps += 20
            print("Your Health has been Recharged. Total Steps now: ", self.steps ,"\n")
        else:
            return
        
class GameState:
    def __init__(self):
        self
    
    # A method to save an incomplete game SP23-BAI-008
    def saveGame(self, castle, inventory, stepsAndHealth, game):

        f = open('gameState.txt', 'w')

        print(castle.getCurrentRoom(), file=f)
        print(','.join(inventory.UserItems), file=f)
        print(stepsAndHealth.getHealth(), file=f)
        print(game.AlchemyPlayed, file=f)
        print(game.HammerPlayed, file=f)
        print(game.SymbolPlayed, file=f)
        print(game.CatacombsPlayed, file=f)
        print(game.chandlierPlayed, file=f)
        print(game.rodPuzzlePlayed, file=f)
        print(game.SigilsOfTowerPlayed, file=f)

        f.close()

    # A method to load yourr previous game SP23-BAI-008
    def loadGame(self, castle, inventory, stepsAndHealth, game):
        try:
            load = [line.strip() for line in open('gameState.txt').readlines()]

            castle.currentRoom = load[0] 
            print("Current Room: " , castle.currentRoom) 
            if load[1]:
                inventory.UserItems = load[1].split(',')
                print("Inventory: " , ','.join(inventory.UserItems))
            else:
                inventory.UserItems = []
                print("No Items Present")

            stepsAndHealth.health = int(load[2])
            print("Health: " , stepsAndHealth.health)

            game.AlchemyPlayed = load[3]
            print("Alchemy Puzzle: ", game.AlchemyPlayed)
            game.HammerPlayed = load[4]
            print("Hammer Puzzle: ", game.HammerPlayed)
            game.SymbolPlayed = load[5]
            print("Symbol Puzzle: ", game.SymbolPlayed)
            game.CatacombsPlayed = load[6]
            print("Catacombs Puzzle: ", game.CatacombsPlayed)
            game.chandlierPlayed = load[7]
            print("Chandlier Puzzle: ", game.chandlierPlayed)
            game.rodPuzzlePlayed = load[8]
            print("Rod Puzzle: ", game.rodPuzzlePlayed)
            game.SigilsOfTowerPlayed = load[9]
            print("Sigils Of Tower: ", game.SigilsOfTowerPlayed)

            print("Game has been loaded successfully\n")           
        except Exception as e:
            print(f"Exception: {e}")

    # A method to clear game after successfully completing SP23-BAI-008
    def clearGame(self):
        try:
            open('gameState.txt', 'w').close()
            print("Save file has been cleared.\n")
        except Exception as e:
            print(f"Error: {e}")



class Game:
    def __init__(self):
        self.map = {
        "Entrance Hall": {
            "north": "Great Hall",
            "description": "A grand and open space with high ceilings and a chandelier. The air smells slightly of old wood.",
            "items": {}
        },
        "Great Hall": {
            "south": "Entrance Hall",
            "west": "Tower Staircase",
            "east": "Banquet Hall",
            "north": "Chapel",
            "description": "A vast, open hall with a long table in the center. Portraits of old kings line the walls.",
            "items": {
                "rope": "A frayed rope, slightly damp and with a faint scent of the sea. It seems to have been used recently.",
                "knife": "An old, tarnished blade with strange runes etched into its handle. It hums faintly when held."
            },
        },
        "Tower Staircase": {
            "east": "Great Hall",
            "up": "Art Gallery",
            "description": "A spiraling stone staircase, dimly lit by torches, leading up to the tower.",
            "items": {}
        },
        "Banquet Hall": {
            "west": "Great Hall",
            "north": "Wine Cellar",
            "east": "Chapel",
            "description": "A lavish room filled with long tables adorned with decayed feast remnants. The smell of wine lingers.",
            "items": {
                "screwdriver": "A rusted screwdriver, its handle worn smooth as if passed between many hands. There's a faint glow at its tip."}
        },
        "Chapel": {
        "west": "Banquet Hall",
        "south": "Great Hall",
        "east": "Royal Vault",
        "north": "Inner Chambers",
        "description": "An ancient chapel with dusty pews and stained-glass windows. The room is eerily silent.",
        "items": {"Golden key 2": "2nd part of golden key"},
        "mysterious_item": "Safe"
        },
        "Inner Chambers": {
        "south": "Chapel",
        "north": "Servant Quarters",
        "description": "A dimly lit, narrow room with stone walls. A single table sits in the center, covered in dust. It feels like it once held something valuable.",
        "items": {
            "mirror": "A cracked hand mirror, its frame tarnished with age. The reflection is distorted and unsettling."}
        },
        "Servant Quarters": {
        "south": "Inner Chambers",
        "description": "A small, cramped space filled with old, worn-out beds and broken furniture. The air smells musty and stale.",
        "items": {}
        },
        "Art Gallery": {
            "down": "Tower Staircase",
            "north": "Catacombs",
            "description": "A narrow room filled with paintings of unknown origin. Dust-covered statues stand in the corners.",
            "items": {},
            "mysterious_item": "Box"
        },
        "Wine Cellar": {
            "south": "Banquet Hall",
            "east": "Library",
            "description": "Rows of dusty wine bottles line the walls. The air is cool, and the floor is cold stone.",
            "items": {
                "hammer": "A heavy hammer with an unusual weight. It leaves a chill in your hands long after you put it down."
            },
        },
        "Library": {
            "west": "Wine Cellar",
            "description": "A small, musty library filled with ancient books. There’s a strange draft coming from behind a bookshelf.",
            "items": {"Golden key 1": "1st part of golden key"},
            "mysterious_item": "Experiment Box"
        },
        "Royal Vault": {
            "west": "Chapel",
            "north": "Main Exit",
            "description": "A heavily fortified room with a large vault door. The air is dense with secrets.",
            "items": {}
        },
        "Catacombs": {
            "south": "Art Gallery",
            "north": "Underground River Exit",
            "description": "A dark, musty tunnel filled with bones and ancient burial sites. The air is damp and suffocating.",
            "items": [],
            "mysterious_item": "Casket"
        },
        "Main Exit": {
            "south": "Royal Vault",
            "description": "A narrow, hidden exit from the castle, leading into the dense forest.",
            "items": {}
        },
        "Underground River Exit": {
            "south": "Catacombs",
            "description": "A small cave opening that leads to an underground river. The sound of water echoes around.",
            "items": {},
        }
    }
        self.Items = {}
        for self.room, self.details in self.map.items():
            if "items" in self.details and self.details["items"]:
                self.Items.update(self.details["items"])
        self.GrandCastle = Castle(self.map)
        self.CastleInventory = Inventory(self.Items)
        self.puzzles = Puzzles()
        self.ScoreAndHealth = StepsAndHealth()
        self.gameState = GameState()
        self.AlchemyPlayed = False
        self.HammerPlayed = False
        self.SymbolPlayed = False
        self.CatacombsPlayed = False
        self.chandlierPlayed = False
        self.rodPuzzlePlayed = False
        self.SigilsOfTowerPlayed = False
        self.previousRoom = self.GrandCastle.getCurrentRoom()

    # A method to resume your previous game SP23-BAI-008
    def resumePreviousGame(self):
        try:
            loadFile = open('gameState.txt', 'r')
            readFile = loadFile.read(1)

            if readFile:
                userInput = input("A Game already Exists. Do you want to continue that? (yes/no) ")
                if userInput == 'yes' or userInput == 'Yes':
                    self.gameState.loadGame(self.GrandCastle, self.CastleInventory, self.ScoreAndHealth, game)
                    self.startGame()
                    return 
            loadFile.close()
        except Exception as e:
            print(e)

    # A method to start game (SP23-BAI-008,SP23-BAI-024)
    def startGame(self):
            print("Welcome to the Mysterious Castle Adventure!")
            print("To go towards a specific you have to write 'go directionName'.")
            print("To pick, drop, examine and use items you have to write 'pick itemName', 'drop itemName', 'examine itemName' and 'use itemName'.")
            print("You have 2000 cells as your health. Every step will cost you 100 cells.")
            print("To exit the game enter 'quit'.\n")


            userInput = input("To start game enter start: ")
            if userInput == "start":
                self.GrandCastle.showDescription()
                while True:
                    userInput = input()
                    if userInput == "quit":
                        print("Quitting Game")
                        break
                    splitInput = userInput.split()
                    if splitInput[0] == "go":
                        self.previousRoom = self.GrandCastle.getCurrentRoom()
                        if self.previousRoom == "Art Gallery" and self.HammerPlayed == False and splitInput[1] == "north":
                            print("The door is closed. To open it you have to open the box in art gallery")
                            continue
                        elif self.previousRoom == "Banquet Hall" and self.chandlierPlayed == False and splitInput[1] in ["north", "east"]:
                            print(f"You cannot go towards the {splitInput[1]} as the chandelier is blocking the way. You need a rope to remove it.")
                            continue
                        elif self.previousRoom == "Catacombs" and self.CatacombsPlayed == False and splitInput[1] == "north":
                            print("The Tunnel is closed. To open it you have answer the riddle correctly")
                            continue
                        else:
                            self.GrandCastle.goDirection(splitInput[1], self.ScoreAndHealth)
                        if self.GrandCastle.getCurrentRoom() == "Library" and self.AlchemyPlayed == False:
                            check = self.puzzles.AlchemyBookPuzzle(self.GrandCastle, self.CastleInventory)
                            if check == True:
                                self.AlchemyPlayed = True
                        elif self.previousRoom == "Library" and userInput in ["go north", "go east", "go south", "go up", "go down"]:
                            print("You are at a dead end. You can only go backward toward the Wine Cellar.")
                        elif self.GrandCastle.getCurrentRoom() == "Art Gallery" and self.HammerPlayed == False:
                            check = self.puzzles.WineCellarHammer(self.GrandCastle, self.CastleInventory)
                            if check == True:
                                self.HammerPlayed = True
                        elif self.GrandCastle.getCurrentRoom() == "Tower Staircase" and self.SigilsOfTowerPlayed == False:
                            user = input("A bonus puzzle for you. Enter yes to play or no to skip: ")
                            if user == 'Yes' or user == 'yes':
                                self.puzzles.theSigilsOfTower(self.ScoreAndHealth)
                                self.SigilsOfTowerPlayed = True
                            else:
                                continue
                        elif self.GrandCastle.getCurrentRoom() == "Banquet Hall" and self.chandlierPlayed == False:
                            checkPoint = self.puzzles.banquetHallChandelier(self.GrandCastle, self.CastleInventory)
                            if checkPoint == True:
                                self.chandlierPlayed = True
                        elif self.GrandCastle.getCurrentRoom() == "Chapel" and self.SymbolPlayed == False:
                            check = self.puzzles.symbolLockPuzzle(self.GrandCastle, self.CastleInventory)
                            if check == True:
                                self.SymbolPlayed = True
                        elif self.GrandCastle.getCurrentRoom() == "Catacombs" and self.CatacombsPlayed == False:
                            self.puzzles.CatacombRiddle()
                            self.CatacombsPlayed = True
                        elif self.previousRoom == "Royal Vault" and splitInput[1] == "north":
                            if "Golden key 1" in self.CastleInventory.UserItems and "Golden key 2" in self.CastleInventory.UserItems:
                                keyInput = input("Use golden key part 1 and golden key part 2 to open the main exit\n in order to use them simultaneously you have to write 'Use Golden key 1 and Golden key 2'\n")
                                if keyInput == "Use Golden key 1 and Golden key 2":
                                    print("You made it through main exit.")
                                    self.CastleInventory.use("Golden key 1")
                                    self.CastleInventory.use("Golden key 2")
                                    break
                            else:
                                print("You must have both parts of golden key in order to open main exit")
                        elif self.previousRoom == "Catacombs" and splitInput[1] == "north":
                            print("Congratulations you got out using the secret way!!")
                            break
                        elif self.GrandCastle.getCurrentRoom() == "Servant Quarters" and self.rodPuzzlePlayed== False:
                            self.puzzles.rodPuzzle(self.ScoreAndHealth)
                            self.rodPuzzlePlayed = True
                        elif self.previousRoom == "Catacombs" and splitInput[1] == "north":
                            print("Congratulations you got out using the secret way!!")
                            break
                        elif self.previousRoom == "Servant Quarters" and userInput in ["go north", "go east", "go west", "go up", "go down"]:
                            print("You are at a dead end. You can only go backward toward the Inner Chamber.")
                    elif splitInput[0] == "pick":
                        self.CastleInventory.takeItem(splitInput[1], self.GrandCastle)
                    elif splitInput[0] == "drop":
                        self.CastleInventory.dropItem(splitInput[1])
                    elif splitInput[0] == "use":
                        self.CastleInventory.use(splitInput[1])
                    elif splitInput[0] == "examine":
                        self.CastleInventory.examine(splitInput[1])
                    elif splitInput[0] == "show":
                        self.CastleInventory.showItems()
                    elif splitInput[0] == "look":
                        self.GrandCastle.look(self.CastleInventory)
                    else:
                        print("Invalid Command.")
                if userInput == "quit":
                    self.gameState.saveGame(self.GrandCastle, self.CastleInventory, self.ScoreAndHealth, game)
                else:
                    self.gameState.clearGame()
                
if __name__ == "__main__":
    game = Game()
    game.resumePreviousGame()
    game.startGame()