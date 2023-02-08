# INTRODUCITON
print("Welcome to dungeon crawler.")
print("You are working as a treasure hunter for hire. You have been asked by your client to enter into an old underground mansion left by the dwarves of yore. The mansion was abandoned years ago, and is full of stange creatures and not structurally sound. You could encounter hostile creatures, and once you jump down in, you will have to find another different exit.")
print("")

name = input("What's your name?")
print("Hi " + name)
print("")
print("Your client hands you a backpack. It has some health potions in it. You can also put anything you find along the way in there. At any time you can type 'check backpack' and see what's inside.")

# set up backpack. key is the item, value is the amount
backpack = {"potions": 5}

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.maxhealth = 5
        self.positionx = 0
        self.positiony = 0
        self.alive = True
    def moveforward(self):
        if self.positiony <= 4:
            self.positiony += 1
        else:
            print("You can't move this way, there's a wall")
    def movebackward(self):
        if self.positiony >= 0:
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
        if self.health > self.maxhealth:
            self.health = self.maxhealth
    def losehealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            print("{} died.".format(self.name))

class Room:
    def __init__(self, positionx, positiony, content):
        self.positionx = positionx
        self.positiony = positiony
        self.content = content
    def __repr__(self):
        if self.content == "empty":
            return "This room is empty."
        elif self.content == "enemy1":
            return "There is a scary ghost here!"
        elif self.content == "enemy2":
            return "There is a mean looking goblin here!"
        elif self.content == "enemy3":
            return "There is a fearsome bear here!"
        elif self.content == "snake":
            return "There is a sleepy snake here."
        elif self.content == "mouse":
            return "There is a smiling mouse here."
        elif self.content == "key":
            return "There is a small key shining in the corner here."
        else:
            return "There is a heavy door here with a small keyhole."

room1 = Room(-1, 0, "empty")
room2 = Room(0,0, "empty")
room3 = Room (1, 0, "empty")
room4 = Room(-1, 1, "enemy1")
room5 = Room(0, 1, "enemy3")
room6 = Room(1, 1, "snake")
room7 = Room(-1, 2, "key")
room8 = Room(0, 2, "lake")
room9 = Room(1, 2, "empty")
room10 = Room(-1, 4, "mouse")
room11 = Room(0, 4, "enemy2")
room12 = Room(1, 4, "door")

class Enemy

def check_backpack():
    response = "Your backpack currently contains "
    for key in backpack.keys():
        if backpack[key] > 0:
            response += (str(backpack[key]) + " " + key)
    print(response)