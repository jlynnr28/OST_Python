#!/usr/local/bin/python3

'''
This program processes the Declaration of Independence and finds 
the unique counts of all the words in it.

- Justin Lynn Reid
'''

import sys

def count_words():
    '''
    Get all word counts from the declaration of independence
    by ignoring punctation and using lists. Returns a dictionary
    of all unique counts and their individual frequencies.
    '''
    
    dec_file = open('declaration.txt')
    file_txt = dec_file.readlines()
    puncs = (',', ';', '\'', '"', '.','?', ':', '\n', '-', '&')
    word_counts_raw = []
    
    #Iterate through the file lines, get all the 
    #word counts from those lines denoted by spaces
    #and then append those counts to a list.
    for line in file_txt:
        words = line.split() # Get words denoted by spaces
        for word in words:
            char_count = 0 # Count the characters in the word
            for char in word:
                if char not in puncs: # Ignore all defined punctuation chars
                    char_count += 1
                else:
                    
                    continue
            if char_count != 0:
            	word_counts_raw.append(char_count)
            
    dec_file.close() # Close the file
    
    #Get unique count numbers by changing the 
    #raw count list into a set and then back into
    #a sorted list.
    unique_counts = sorted(list(set(word_counts_raw)))
    
    #Create a dictionary that will hold all the unique
    #counts as keys and the amount of those counts as values
    length_count = {}
    
    for val in unique_counts:
        val_freq = 0
        for raw_val in word_counts_raw:
            if raw_val == val:
                val_freq += 1
        length_count.update({val: val_freq})
        
    return length_count
    
            
def print_length_tab(lengths):
    '''
    Prints out the count dictionary in a legible and
    sane fashion.
    '''    
    for key in sorted(lengths.keys()):
         print('{0} {1}'.format(key, lengths[key]))     
    
    print('\n')


def print_histogram(hist_data):
    '''
    Print a histogram from the data read in from the file.
    '''
    
    #Set bar range
    counts = range(400, 0, -20)
    
    #Print out all histogram bars
    for ct in counts:
        bar_str = ''
        if ct % 100 == 0:
            bar_str += '{0} -| {1}'.format(ct, ' ' * 2)
        else:
            bar_str += '{0}| {1}'.format(' ' * 5, ' ' * 2)
            
        
        for key in hist_data.keys():
            if ct == hist_data[key] or hist_data[key] > ct: 
               bar_str += '***'
        
        print(bar_str)
        
    #Initialize x axis string and labels
    axis_str = '{0}0 -+-+--'.format(' ' * 2)
    label_str = '{0} | 1'.format(' ' * 4)
    label_nums = list(hist_data.keys())
    label_nums.append(16)
    
    #Create axis and label strings to be printed via 
    #concatenation
    for lbl in label_nums:
        if lbl > 1:  
            if lbl == 16:
                axis_str += '+-'
            else:
                axis_str += '+--'
            
            if lbl < 10:
                label_str += '{0}{1}'.format(' ' * 2, lbl)
            else:
                label_str += ' {0}'.format(lbl)
                
         
            
    print(axis_str)
    print(label_str)


def main():

    length_count = count_words()
    print_length_tab(length_count)
    print_histogram(length_count)

if __name__ == '__main__':
    main()
