# INTRODUCITON
print("Welcome to dungeon crawler.")
print("You are working as a treasure hunter for hire. You have been asked by your client to enter into an old underground mansion left by the dwarves of yore. The mansion was abandoned years ago, and is full of stange creatures and not structurally sound. You could encounter hostile creatures, and once you jump down in, you will have to find another different exit.")
print("")

name = input("What's your name?")
print("Hi " + name)
print("")
print("Your client hands you a backpack. It has some health potions in it. You can also put anything you find along the way in there. At any time you can type 'check_backpack()' and see what's inside.")

# set up backpack. key is the item, value is the amount
backpack = {"potions": 5}
def check_backpack():
    response = "Your backpack currently contains "
    for key in backpack.keys():
        if backpack[key] > 0:
            response += (backpack[key] + " " + key)
    print(response)
        

