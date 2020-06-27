#!/usr/bin/python3
# LISTS
# Author: Brian Skipper
# Date: 6/26/2020
import random

#create a list. Lists use [x,x,...,x]
spam = ["cat", "dog", "fish", "gerbil", "elephant"]

#print out items from the list
print("First: "+str(spam[2:5])+" and "+spam[1]+"\n1\n2")

#return the length of the list
print("Length of Spam: "+str(len(spam)))

#print the list out with a 'for loop'
for x in spam:
    print(x)

#print out the indexes and the corresponding item in the list
for index, item in enumerate(spam):
    print("Index "+str(index)+" in spam list "+item)

#print out a random item from the list
print("Random thing from list spam: "+random.choice(spam))

