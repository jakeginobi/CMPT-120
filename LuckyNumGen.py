#############Lucky Number Generator by Alex Land and Evan Chisholm##############
#################September 27 2013, worked on for 0.5 seconds ##################

import math
import random


# Welcome Statement

print "Salutations! Welcome to the Lucky Number Generator!"

# Variables

userName = raw_input("Enter your name (First then Last): ")
userAddress = raw_input("Enter your address: ")
userCode = raw_input("Enter your two digit character code: ")

addressPlace = userAddress.find(" ")
addressNum = userAddress[0:(addressPlace + 1)]

# Calculations

sqrtAddress = float(math.sqrt(float(addressNum)))
strSqrt = str(sqrtAddress)
decimalPos = strSqrt.find(".")
d1 = int(strSqrt[(decimalPos + 1):(decimalPos + 2)])

nameValue = userName[0].upper()

if (nameValue < "M"):
    d1 += -1
elif (nameValue >= "M"):
    d1 += 1

if (d1 == -1):
    d1 = 9
elif (d1 == 10):
    d1 = 0
'''
streetName = userAddress[(addressPlace + 1):50]
streetPlace = streetName.find(" ")
streetLetter = streetName[(streetPlace - 1):streetPlace]
'''
streetLetter = userAddress[(len(userAddress) - 1):(len(userAddress))]

stars = "*" * d1

nameLetters = userName[0:2]

if userCode.isalpha() == True:
    s2 = streetLetter + stars + nameLetters + userCode
elif userCode.isalpha() == False:
    s2 = streetLetter + stars + nameLetters + userCode[0:1]

if len(s2) % 2 == 0:
    s2 += "Even"
elif len(s2) % 2 != 0:
    s2 += "Odd"

randNum = random.randint(0,9)

# Results
print "These are your results: "
print " "
print "Your lucky digit (d1) is", d1
print "Your code is", s2
print "A random digit is", randNum




