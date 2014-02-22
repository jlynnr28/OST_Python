#!/usr/local/bin/python3

'''
This program demonstrates the useage of module
imports via a simple guessing game.

- First Written by Justin Lynn Reid 10/5/2013

'''

import random

answer = random.randint(1, 99)

while True:
    guess = int(input("Guess a number: "))
    
    if guess > answer:
       print("Too high")
    elif guess < answer:
       print("Too low")
    elif guess == answer:
       print("Your answer is correct!")
       break