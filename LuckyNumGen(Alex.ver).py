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

#addressPlace = userAddress.find(" ")
addressNum = userAddress[0:(userAddress.find(" ") + 1)]

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

print d1

s2 = str(userAddress[len(userAddress)]

print s2
