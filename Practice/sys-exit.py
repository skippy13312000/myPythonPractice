#!/usr/bin/python3
# sys.exit()
# Author: Brian Skipper
# Date: 6/26/2020

import sys

while True:
    print("Type in your name: (or exit to exit)")
    response = input()
    if response == "exit":
        sys.exit()
    print("You types "+ response +".")