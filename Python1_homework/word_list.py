#!/usr/local/bin/python3

'''
This program demonstrates the usage of Python sequences by
creating and printing lists of strings.

First written by Justin Lynn Reid 8/31/2013
'''

capital_words = []; lower_words = []

str_input = input("Input your words: ")

words = str_input.strip().split()

for word in words:
    for letter in word:
        if letter.isupper():
            capital_words.append(word)
            break
        else:
            lower_words.append(word)
            break

combined_words = capital_words + lower_words

for word in combined_words:
    print(word)
    