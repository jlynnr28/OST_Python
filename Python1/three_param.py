#!/usr/local/bin/python3

'''
This program demonstrates the usage of functions.

- First Written by Justin Lynn Reid 9/28/2012
'''

def my_func(a, b='b was not entered', c='c was not entered'):
    print(a)
    print(b)
    print(c)
 
my_func('test')
my_func('test', 'test2')
my_func('test', 'test2', 'test3')

print(my_func)
 