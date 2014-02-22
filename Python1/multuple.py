#!/usr/local/bin/python3

'''
This program provides examples of string formatting
in Python 3.

First Written by Justin Lynn Reid 9/8/2013
'''

data = ((1,1), (2, 2), (12, 13), (4, 4), (99, 98))

for num1, num2 in data:
    product = num1 * num2
    
    print("{0:>4d} = {1:>2d} x {2:>2d}".format(product, num1, num2))