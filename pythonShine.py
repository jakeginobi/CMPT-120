# PYTHON LOL (Name a Work in Progess)
# Created by Evan Chisholm and Alex Land

import random
import turtle as t

# VARIABLES

godMode = ""
biomePosition = ""
fillColor = "tan"
catastropheNumber = 0

# FUNCTIONS

def gameStart():
    global godMode
    godMode = ""
    while godMode == "":
        godModeInput = raw_input("Would you like to manually choose biomes (y/n)? ")
        if godModeInput == "y":
            godMode = 1
        elif godModeInput == "n":
            godMode = 0
        else:
            print "Please enter y for yes or n for no."
    return godMode

def biomeGenerator(godMode):
    global biomePosition
    biomePosition = ""
    if godMode == 1:
        biomePosition = input("Which biome would you like to start at (Pick a number between 1 and 8)? ")
    if godMode == 0:
        biomePosition = random.randint(1,8)
    return biomePosition

def biomeDraw(fillColor):
        t.fillcolor(fillColor)
        t.begin_fill()
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.end_fill()
        t.forward(70)
        
def drawBoard(catastropheNumber):
    biomeDraw() * (8 - catastropheNumber)
    
    
    

gameStart()

biomeGenerator(godMode)
print godMode
print biomePosition
