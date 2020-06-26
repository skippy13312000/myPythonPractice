#!/usr/bin/python3
# number guessing game
# Author: Brian Skipper
# Date: 6/26/2020

import sys
import random

x = random.randint(1, 10)
print(x)

while True:
    print(x)
    print("Enter an INTEGER for your guess: ")
    y = int(input())
    if y == x:
        print("Correct guess! The number was "+str(x)+"!")
        sys.exit()
    elif y < x:
        print("Too low")
    elif y > x:
        print("Too high")