'''
This module contains a function that calculates the counts of unique
extensions in a given directory.

- First Written by Justin Lynn Reid 1/19/2013
'''

import os
import glob


def count_exts():
    '''
    This function finds all extensions in the current working directory
    and returns a dictionary of counts for each unique extension name.
    '''
    
    #Get file extension info from the current working directory and
    #create empty dictionary for final output
    ext_counts = {}
    ext_files = glob.glob("*.*")
    all_exts = [os.path.splitext(fil)[1] for fil in ext_files]
    uniq_exts = tuple(set(all_exts))
    
    #Iterate through the unique extensions and find every key value
    #pair for each of those extensions
    for ext in uniq_exts:
        count = 0
        for raw_ext in all_exts:
            if raw_ext == ext:
                count += 1
        ext_counts.update({ext: count})
        
    return ext_counts