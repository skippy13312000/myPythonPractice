#!/usr/bin/python3
# Another simple func() practice program
# Author: Brian Skipper
# Date: 6/26/2020

def math_stuff(x):
    """
    A simple Math fuction. With a simple docstring
    """
    number = x * x
    return number
    

print("Enter a number: ")

num1 = abs(int(input()))

print("Number returned is "+str(math_stuff(num1)))