godMode = ""
while godMode == "":
    godModeInput = raw_input("Would you like to manually choose biomes (y/n)? ")
    if godModeInput == "y":
        godMode = 1
    if godModeInput == "n":
        godMode = 0
    if godMode == "":
        print "Please enter y for yes or n for no."
print godMode
