'''
This module tests whether a given function properly returns a count
of the given unique file extensions in a given directory.

- First Written by Justin Lynn Reid 1/19/2013
'''

import unittest
import os
import glob
import shutil
import extensions


class TestExt(unittest.TestCase):
    
    def setUp(self):
        
        self.file_exts = ('ex.txt', 'ex.doc', 'ex.log', 'ex2.txt')
        
        self.dirname = "test_dir_{0}".format(os.getpid())
        os.mkdir(self.dirname)
        os.chdir(self.dirname)
        
        for fn in self.file_exts:
            fil = open(fn, 'w')
            fil.close()
        
    def test_dir(self):
        '''
        This function tests the directory ext function for a given file directory.
        '''
        counts = extensions.count_exts()
        expected_counts = {'.txt':2, '.doc':1, '.log':1}
        
        self.assertEqual(counts, expected_counts)
  
        
    def tearDown(self):
        pardir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        os.chdir(pardir)
        shutil.rmtree(self.dirname)
        
if __name__ == '__main__':
    unittest.main()