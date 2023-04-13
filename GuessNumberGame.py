# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:23:36 2023

@author:
"""

import random

print("Welcome to the guessing game!")
con = True
turns = 0
while con == True:
    num = random.randrange(1, 101)
    while con == True:
        userInp = int(input("Enter your number: "))
        if userInp == num:
            print("You have guessed correctly. Well Done!")
            turns += 1
            print("Your number of turns was: ", turns)
            break
        elif userInp < num:
            turns += 1
            print("Your number is less than the number generated.")
        elif userInp > num:
            turns += 1
            print("Your number is more than the number generated.")
    again = input("Play again?(y/n)")
    if again == "n":
        con = False