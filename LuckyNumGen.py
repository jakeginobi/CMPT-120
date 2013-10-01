#########Lucky Number Generator by Alex Land and Evan Chisholm############
############September 30 2013, worked on for 1.5 hours total ############

import math
import random


# Welcome Statement

print "Salutations! Welcome to the Lucky Number Generator!"
print "Enter the following data and we'll provide you with some lucky numbers!"

# Initial User Input

userName = raw_input("Enter your name (First then Last): ")
userAddress = raw_input("Enter your address: ")
userCode = raw_input("Enter your two digit character code: ")

# Calculations

addressPlace = userAddress.find(" ")                    # Finding the index of the address
addressNum = userAddress[0:(addressPlace + 1)]      # Slicing the number of the address

sqrtAddress = float(math.sqrt(float(addressNum)))       # Taking the root of the address
strSqrt = str(sqrtAddress)                             # Converting to a string             
decimalPos = strSqrt.find(".")                          # Indexing the answer of the root
d1 = int(strSqrt[(decimalPos + 1):(decimalPos + 2)])    # Saving the number after the decimal

nameValue = userName[0].upper()                     # Converting the name into CAPS

if (nameValue < "M"):           # This if statement determines whether
    d1_mod = d1 + -1         # the value d1 is changed by + or - 1
elif (nameValue >= "M"):
    d1_mod = d1 + 1

if (d1_mod == -1):                  # This if statement round the number to 0 or 9
    d1_round = 9
elif (d1_mod == 10):
    d1_round = 0

if 'd1_round' in globals():         # This if statement determines which value of d1
    d1_final = d1_round         # (either d1_mod or d1_round) is to be used for
else:                           # the final answer (If d1_round exists, it will be used)
    d1_final = d1_mod

streetLetter = userAddress[(len(userAddress) - 1):(len(userAddress))] # Slices the last letter of the street name
                                                                 
stars = "*" * d1_final              # Creates the appropriate number of stars for s2

nameLetters = userName[0:2].lower()     # Slices the first two letters of the users name for s2

if userCode.isalpha() == True:  #This if statement determines whether s2 should include one or both of the characters in the special character code
    s2 = streetLetter + stars + nameLetters + userCode
elif userCode.isalpha() == False:
    s2 = streetLetter + stars + nameLetters + userCode[0:1]

if len(s2) % 2 == 0:        # This if statement determines whether to add Even or Odd to s2
    s2_final = s2 + "Even"
elif len(s2) % 2 != 0:
    s2_final = s2 + "Odd"

randNum = random.randint(0,9)   # This statement produces a random integer

# Results and Tracing
# These commands should be pretty self explanatory
print " "
print "TRACING - Initial value of d1:", d1
print "TRACING - Value of d1 + or - 1:", d1_mod
print "TRACING - Value of d1 after rounding to 0 or 9:", d1_final
print "TRACING - Length of s2 before the final word:", len(s2)

print " "
print " "
print "These are your results: "
print " "
print "Your lucky digit (d1) is", d1_final
print "Your code is", s2_final
print "A random digit is", randNum




