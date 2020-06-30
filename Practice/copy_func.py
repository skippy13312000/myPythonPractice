#!/usr/bin/python3
# this is function practice to show the id() output and how it does and doesn't change
# Author: Brian Skipper
# Date: 6/26/2020

import copy
spam = ['a','b','c','d']

print("ID:       "+str(id(spam)))
print(spam)

cheese=copy.copy(spam)
print("Cheese:   "+str(id(cheese)))
cheese[1] = 42
print(cheese)


