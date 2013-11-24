# PYTHON LOL (Name a Work in Progess)
# Created by Evan Chisholm and Alex Land

import random

# VARIABLES

godMode = ""
biomePosition = ""

# FUNCTIONS

def gameStart(godMode):
    while godMode == "":
        godModeInput = raw_input("Would you like to manually choose biomes (y/n)? ")
        if godModeInput == "y":
            godMode = 1
        if godModeInput == "n":
            godMode = 0
        if godMode == "":
            print "Please enter y for yes or n for no."
    return godMode

def biomeGenerator(godMode, biomePosition):
    if godMode == 1:
        biomePosition = input("Which biome would you like to start at (Pick a number between 1 and 8)? ")
    if godMode == 0:
        biomePosition = random.randint(1,8)
    return biomePosition

gameStart(godMode)

biomeGenerator(godMode, biomePosition)
print godMode
print biomePosition
