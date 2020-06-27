#!/usr/bin/python3
# LISTS
# Author: Brian Skipper
# Date: 6/26/2020

spam = ["cat", "dog", "fish", "gerbil", "elephant"]

print("First: "+str(spam[2:5])+" and "+spam[1]+"\n1\n2")

print("Length of Spam: "+str(len(spam)))

for x in spam:
    print(x)

for index, item in enumerate(spam):
    print("Index "+str(index)+" in spam list "+item)