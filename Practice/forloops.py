#!/usr/bin/python3
# For Loops and range command and modulus. Played around with the '%' modulus operator also.
# Author: Brian Skipper
# Date: 6/26/2020

print("Please neter your name: ")
name = input()
print("Please tell how many time to print your name: ")
num_name = input()

for prt in range(int(num_name)+1):
    if prt > 0 and (prt % 2 == 0):
        print("We have printed "+ name +" "+str(prt) +" times.")
# Some more of the options in the range() function
for i in range(0, 10, 3):
    print(i)

#test change 
