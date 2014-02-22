#!/usr/local/bin/python3

'''
 - guess.py

This program demonstrates the useage of while loops
in Python in the context of a simple guessing game.

- First Written by Justin Lynn Reid 8/24/2013
'''

#===========================================================

secret = 12 # Secret Number to be guessed
num_guesses = 0 # Guess counter
num_in = float(input("Guess a number: "))

while num_in != secret:
    
    if num_in > secret:
        print("Guess Lower")
    elif num_in < secret:
        print("Guess Higher")
    
    num_guesses += 1
    
    if num_guesses >= 5:
        print("You have exceeded the number of guesses")
        break
        
    num_in = float(input("Guess a number: "))
    
else:
    if num_guesses < 5:
    	print("Correct! Well done, the number was ", secret)    
    	
#===========================================================