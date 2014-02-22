#!/usr/local/bin/python3

'''
This file demonstrates file writing and reading.

First Written by Justin Lynn Reid 9/15/2013
'''
#Create File if it doesn't exist
f = open('input_txt.txt', 'a+')
f.close()

#Print Contents of the file at the start of 
#the program.
f = open('input_txt.txt', 'r+')

prev_lines = ''

for line in f.readlines():
    prev_lines += line
print(prev_lines.replace('\n', ''))
    
f.close()

while True:

    in_words = input('Enter text: ').strip('\n')
    
    #Open files for placing input in and
    #reading output out for each enter
    f = open('input_txt.txt', 'a+')

    if len(in_words) != 0:
        f.write('{0}\n'.format(in_words))
        f.close()
        
        r = open('input_txt.txt', 'r')
        lines = ''
        
        for line in r.readlines():\
            lines += line 	
            
        print(lines.replace('\n', ''))
        r.close()

    else:
        break

#Close all files