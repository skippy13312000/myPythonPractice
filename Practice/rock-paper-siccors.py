#!/usr/bin/python3
# Rock Paper Siccors game
# Author: Brian Skipper
# Date: 6/26/2020

import random, sys

wins = 0
losses = 0
ties = 0


r = 1
p = 2
s = 3
i = 0

while True:
    compnum = random.randint(1, 3)
    #print("COMPNUM: "+str(compnum)+" "+str(type(compnum)))
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    print("Enter your move: (r)ock (p)aper (s)iccors (q)uit:")
    playerMove = input()
    if playerMove == 'q':
        print("You have exited the game.")
        sys.exit() #quit program
    elif playerMove == 'r' and compnum == 3:
        print("Rock VS. Siccors!")
        print("Rock WIN!!!")
        wins = wins + 1
    elif playerMove == 'p' and compnum == 1:
        print("Paper VS. Rock!")
        print("Paper WIN!!!")
        wins = wins + 1
    elif playerMove == 's' and compnum == 2:
        print("Siccors VS. Paper!")
        print("Siccors WIN!!!")
        wins = wins + 1
    elif (playerMove == 'r' and compnum == 1) or (playerMove == 'p' and compnum == 2) or (playerMove == 's' and compnum == 3):
        print("It's TIE!")
        ties = ties + 1
    else:
        print("You LOST!")
        losses = losses + 1