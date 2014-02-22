#!/usr/local/bin/python3

'''
This code is used to demonstrate merciless refactoring.

- Justin Lynn Reid 11/10/2013
'''

small_words = ('into', 'a', 'of', 'at', 'in', 'for', 'on', 'into', 'the')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    
    title_str = ''
    title_words = title.split(' ')
    
    for i, word in enumerate(title_words): 
    	if word.lower() not in small_words or i == 0:
    	    if i < len(title_words) - 1:
    	        title_str += word.title() + ' '
    	    else:
    	        title_str += word.title()
    	else:
    	    if i < len(title_words) - 1:
    	        title_str += word.lower() + ' '
    	    else:
    	        title_str += word.lower()
    	    
    return title_str
    

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()