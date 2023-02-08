# INTRODUCITON
print("Welcome to dungeon crawler.")
print("You are working as a treasure hunter for hire. You have been asked by your client to enter into an old underground mansion left by the dwarves of yore. The mansion was abandoned years ago, and is full of stange creatures and not structurally sound. You could encounter hostile creatures, and once you jump down in, you will have to find another different exit.")
print("")

name = input("What's your name?")
print("Hi " + name)
print("")
print("Your client hands you a backpack.")

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.maxhealth = 5
        self.positionx = 0
        self.positiony = 0
        self.alive = True
    def moveforward(self):
        if self.positiony <= 2:
            self.positiony += 1
        else:
            print("You can't move this way, there's a wall")
    def movebackward(self):
        if self.positiony >= 1:
            self.positiony -= 1
        else:
            print("You can't move this way, there's a wall")
    def moveleft(self):
        if self.positionx >= 0:
            self.positionx -= 1
        else:
            print("You can't move this way, there's a wall")
    def moveright(self):
        if self.positionx <= 0:
            self.positionx += 1
        else:
            print("You can't move this way, there's a wall")
    def gainhealth(self, amount):
        self.health += amount
        print("Your health is now at {}.".format(self.health))
        if self.health > self.maxhealth:
            self.health = self.maxhealth
    def losehealth(self, amount):
        self.health -= amount
        print("Your health is now at {}.".format(self.health))
        if self.health <= 0:
            self.alive = False
            print("{} died.".format(self.name))

class Enemy:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.health = 2*self.strength
        self.alive = True
    def losehealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            print("{} died.".format(self.name))

#build and initiate new player
player = Player(name)

#build enemies
enemy1 = Enemy("Ghost", 1)
enemy2 = Enemy("Goblin", 2)
enemy3 = Enemy("Bear", 3)

# build rooms
rooms = {}
rooms[1] = [-1, 0, "empty", True]
rooms[2] = [0,0, "empty", True]
rooms[3] = [1, 0, "empty", True]
rooms[4] = [-1, 1, "enemy1", True]
rooms[5] = [0, 1, "lake", True]
rooms[6] = [1, 1, "enemy2", True]
rooms[7] = [-1, 2, "key", True]
rooms[8] = [0, 2, "snake", True]
rooms[9] = [1, 2, "empty", True]
rooms[10] = [-1, 3, "mouse", True]
rooms[11] = [0, 3, "enemy3", True]
rooms[12] = [1, 3, "door", True]

# set up backpack. key is the item, value is the amount
backpack = {"potions": 5}
doorState = "locked"

def check_backpack():
    response = "Your backpack currently contains"
    for key in backpack.keys():
        if backpack[key] > 0:
            response += " " + (str(backpack[key]) + " " + key + ",")
    print (response)

winState = False

def endturn():
    print("This turn has ended.")
    print("")
    if player.alive == True:
        newturn()
    else:
        print("Game Over.")

def enemy1encounter():
    print("The ghost is startled by your presense but doesn't move. It seems to think you can't see it.")
    print("")
    while enemy1.alive == True and player.alive == True:
        action = input("Would you like to move on or attack?")
        if action == "move on":
            print("You pretend not to see the ghost.")
            endturn()
        elif action == "attack":
         print("You lunge at the ghost. You do 2 damage. It screams and does {} damage to your eardrums.".format(enemy1.strength))
         player.losehealth(enemy1.strength)
         enemy1.losehealth(2)
    endturn()

def enemy2encounter():
    print("The goblin hisses and moves to protect something.")
    print("")
    while enemy2.alive == True and player.alive == True:
        action = input("Would you like to move on or attack?")
        if action == "move on":
            print("You slowly back away from the goblin.")
            endturn()
        elif action == "attack":
         print("You swing your fists at the goblin. You do 2 damage. It growls and does {} damage it scratches at you.".format(enemy2.strength))
         player.losehealth(enemy2.strength)
         enemy2.losehealth(2)
    if enemy2.alive == False:
        print("You look behind the goblin's body and see he was guarding a shiny ruby. You take it.")
        backpack["ruby"] = 1
    endturn()

def enemy3encounter():
    print("The bear runs at you!")
    print("")
    while enemy3.alive == True and player.alive == True:
        action = input("Would you like to move on or attack?")
        if action == "move on":
            print("You can't outrun a bear.It swipes it massive paw at you and does {} damage.".format(enemy3.strength))
            player.losehealth(enemy3.strength)
            print("")
        elif action == "attack":
         print("You grab a rock and smash it into the bear. You do 3 damage. It swipes it massive paw at you and does {} damage.".format(enemy3.strength))
         player.losehealth(enemy3.strength)
         enemy2.losehealth(3)
    if enemy2.alive == False:
        print("You successfully survived a bear attack. Well done.")
    endturn()

def snakeencounter():
    if rooms[12][3] == True:
        action = input("Would you like to wake the snake? y/n")
        if action == "y":
            print("You poke the snake and he slowly opens an eye.")
            print("He hisses: Silly human, looking for treasure I presume? Good luck.")
        if action == "n":
            print("The snake smirks knowingly.")
            print("He mutters: beware a bear in the next room forward.")
        rooms[12][3] == False
    else:
        print("The snake is sleeping peacefully.")
    endturn()

def mouseencounter(): 
    if rooms[10][3] == True:
        action = input("Would you like to try to talk to the mouse? y/n")
        if action == "y":
            print("SQUEE!")
            print("The exit is top right ok? Don't interrupt my art!")
            rooms[10][3] == False
    else:
        print("The mouse is doing a little jig. She seems immersed.")
    endturn()  

def newLocation():
    currentroomkey = 0
    playerposition = [player.positionx, player.positiony]
    for key, value in rooms.items():
        if value[0] == playerposition[0] and value[1] == playerposition[1]:
            currentroomkey = key
    current_room_content = rooms[currentroomkey][2]
    if current_room_content == "empty":
        print("This room is empty.")
        endturn()
    elif current_room_content == "enemy1":
        if enemy1.alive == True:
            print("There is a scary ghost here!")
            enemy1encounter()
        else:
            print("This room is empty.")
            endturn()
    elif current_room_content == "enemy2":
        if enemy2.alive == True:
            print("There is a mean looking goblin here!")
            enemy2encounter()
        else:
            print("This room is empty.")
            endturn()
    elif current_room_content == "enemy3":
        if enemy3.alive == True:
            print("There is a fearsome bear here!")
            enemy3encounter()
        else:
            print("This room is empty.")
            endturn()
    elif current_room_content == "snake":
        print("There is a sleepy snake here.")
        snakeencounter()
    elif current_room_content == "mouse":
        print("There is a little mouse humming to herself and drawing on the walls.")
        mouseencounter()
    elif current_room_content == "key":
        if "key" not in backpack.keys():
            print("There is a small key shining in the corner here.")
            print("You walk over and pick it up. You put it in your backpack.")
            backpack["key"] = 1
        else:
            print("This room is empty.")
        endturn()
    elif current_room_content == "door":
        print("There is a heavy door here with a small keyhole.")
        if "key" in backpack.keys():
            print("You take out the key you found and try it in the door. It swings open!")
            print("Well done! You've escaped.")
            print("YOU WIN")
        else:
            print("You try the door but the lock is solid. You'll need some sort of key to get out.")
            endturn()
    elif current_room_content == "lake":
        print("There's a small lake in here. It looks cold. Best go around it.")
        endturn()
    else:
        endturn()
        

def newturn():
    if winState == True:
        print ("Congratulations, {}, you beat the game.".format(player.name))
    else:
        action = input("What would you like to do? move or heal or check backpack?")
        if action == "heal":
            if player.health >= player.maxhealth:
                print("You're already at max health, don't waste!")
                endturn()
            if backpack["potions"] >= 1:
                player.gainhealth(3)
                backpack["potions"] -=1
                print("You drank a potion.")
                endturn()
            else: 
                print("You don't have any potions left.")
                endturn()
        elif action == "move":
            print("You've chosen to move.")
            movement_direction = input("Which way would you like to move? forward/right/backward/left")
            if movement_direction == "forward":
                player.moveforward()
                newLocation()
            elif movement_direction == "right":
                player.moveright()
                newLocation()
            elif movement_direction == "backward":
                player.movebackward()
                newLocation()
            elif movement_direction == "left":
                player.moveleft()
                newLocation()
        elif action == "check backpack":
            check_backpack()
            endturn()
        else:
            print("Try that again.")
            endturn()

print("Good luck, {}! Your client slaps you on the back and you fall into the first room.".format(player.name))
newLocation()

