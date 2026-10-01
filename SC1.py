#Name: Jacob Alexander
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
mobStats = \
    {"zombie": {
        "health": 20,
        "damage": 4,
        "combat style": "close melee"},
    "skeleton":
        {"health": 20,
         "damage": 5,
         "combat style": "ranged"},
    "creeper":
        {"health": 20,
         "damage": 30,
         "combat style": "spontaneous combustion" },
    "enderman":
        {"health": 40,
         "damage": 10,
         "combat style": "teleportation"},
    "witch":
        {"health": 20,
         "damage": 8,
         "combat style": "debuff potions"}}
print(mobStats)
mobStats[input("which mob's damage would you like to change?")].update({"damage": int(input("change damage to?"))})
print(mobStats)