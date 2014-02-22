#!/usr/local/bin/python3

'''
This program demonstrates the useage of dicts and sets
via text input.

First Written by Justin Lynn Reid 9/3/2013
'''

words = {}
word_set = set({})

str_input = input("Enter Text: ")

while len(str_input) > 0:
    word_list = str_input.lower().strip().split()
    
    for word in word_list:
        start_len_set = len(word_set)
        word_set.add(word)
        if len(word_set) > start_len_set:
            words[word] = len(word_set)            
    
    for key in words.keys():
        print(key, " ", words[key])
        
    str_input = input("Enter Text:")   