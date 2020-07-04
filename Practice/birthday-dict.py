#!/usr/bin/python3
# dict and list practice
# Author: Brian Skipper
# Date: 7/4/2020

birthdays = {'Brian':'Nov 26','Holly':'Apr 27','Dina':'Mar 6'}

while True:
    print("Enter a name: (blank to quit)")
    name=input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name]+" is the birthday of "+ name)
    else:
        print("i do not have a birthday for "+name)
        print("What is the bithday?") 
        bday=input()
        birthdays[name] = bday
        print("Birthdays updated")
       
