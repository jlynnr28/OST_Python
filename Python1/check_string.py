#!/usr/local/bin/python3

"""
check_string.py A program that tests Python's string checking capabilities.

--Justin Lynn Reid 8/18/2013
"""

str_input = input("Please enter an upper case string ending with a period:")

if str_input.endswith(".") and str_input.isupper():
    print("Input meets both requirements")
else:
    if not str_input.endswith("."):
        print("String does not end with a period")
    if not str_input.isupper():
        print("String is not all uppercase")
    