#!/usr/bin/python3

# Simple python: While loops
# Author: Brian Skipper
# Date: 6/26/2020

x = 0

print("What number would you like to count up to?")

y = int(input())

print()
print()
print("This prints out a list of EVEN numbers.")
while x <= y:
    if not x % 2 and x > 0:
        print("X is now equal to "+ str(x))
    elif x == 75:
        print("X IS NOW EQUAL TO " + str(x) + " <--- CAPITALIZED!!")    
    x = x+1