#!/usr/local/bin/python3

'''
This program demonstrates the usage of Python object

- First Written by Justin Lynn Reid 10/19/2012
'''

class Dog:

    def __init__(self, name, breed):
    	self.name = name
    	self.breed = breed
    	
dogs = []

while True:
    name = input('Name: ')
    
    if not name:
        break
    
    breed = input('Breed: ')
   
    dog = Dog(name, breed)
    dogs.append(dog)

    print('DOGS')
    
    for i, dog in enumerate(dogs):
         print(i, '.', dog.name, ':', dog.breed) 
    
    print('*' * 30)
    

