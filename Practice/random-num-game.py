#!/usr/bin/python3
# number guessing game
# Author: Brian Skipper
# Date: 6/26/2020

import sys, random

print("Enter the first number for the guessing game: ")
num1 = int(input())
print("Enter a number higher then the first number for the 2nd number in the guessing game: ")
num2 = int(input())

x = random.randint(num1, num2)

while True:
    print("Enter an INTEGER for your guess: ")
    y = int(input())
    if y == x:
        print("Correct guess! The number was "+str(x)+"!")
        sys.exit()
    elif y < x:
        print("Too low")
    elif y > x:
        print("Too high")