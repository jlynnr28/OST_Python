#!/usr/local/bin/python3

'''
This program demonstrates the use of built in
Python functions via the use of a cipher.

- First Written by Justin Lynn Reid 9/21/2013
'''

#User Input
input = input("Message: ")

#List that will hold the changed char values
char_vals_lst = []

#Encoded Message
en_msg = ''

for char in input:
    char_num = ord(char)
    char_trans = char_num + 1 
    char_vals_lst.append(char_trans)

for valid_num in reversed(char_vals_lst):
    en_msg += chr(valid_num)

print(en_msg)
    
    