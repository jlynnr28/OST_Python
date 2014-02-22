#!/usr/local/bin/python3

'''
This program tests more advanced function features

- First Written by Justin Lynn Reid
'''

#=========================================================

import sys

#=====================Functions===========================

def capitalize(in_string):
    cap_str = in_string.capitalize()
    
    return cap_str
    
    
def title(in_string):
    title_str = in_string.title()
    
    return title_str
 
    
def upper(in_string):
    upper_str = in_string.upper()
    
    return upper_str
 
    
def lower(in_string):
    lower_str = in_string.lower()
    
    return lower_str


def exit(in_str):
    sys.exit(1)

#=========================================================

functions = {
    'capitalize': capitalize,
    'title': title,
    'upper': upper,
    'lower': lower,
    'exit': exit,
}
    
while True:
    func_name = input("Enter a function name (capitalize, title, upper, lower or exit): ")
    in_string = input("Enter a string: ")
        
    result = functions[func_name.lower()](in_string)
        
    print(result)
        