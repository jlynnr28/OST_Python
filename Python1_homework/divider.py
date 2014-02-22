#!/usr/local/bin/python3

'''
This program demonstrates the useage of 
exception handling.

- Justin Lynn Reid 10/27/2013

'''

def get_integer():

    input_int = input("Provide an Integer: ")

    while True:
    
        if input_int == '':
            break
            
        try:
            print(10.0/int(input_int))
        except ValueError:
            print('Your input value must be an integer.')
        except ZeroDivisionError:
            print('Your input value cannot be zero.')
       
        input_int = input('Provide an Integer: ')
        
        
if __name__ == '__main__':
    get_integer()



   