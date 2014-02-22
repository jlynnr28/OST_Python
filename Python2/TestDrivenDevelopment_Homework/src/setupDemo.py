"""
Demonstration of setUp and tearDown.
The tests do not actuall test anything this is a demo.
"""

import unittest
import tempfile
import shutil
import glob 
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible."
        fnames = ("this.txt", "that.txt", "the_other.txt")
        test_names = set(fnames)
        
        for filename in fnames:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        
        self.assertEqual(set(os.listdir(self.dirname)), test_names, "Files in directory aren't the same as those created.")
        
            
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Create a file a million bytes in size."
        os.chdir(self.dirname)
        
        f = open('ex_binary', 'wb')
        
        raw_bytes = [1 for i in range(0, int(1e6), 1)]
        byte_arr = bytes(raw_bytes)
        f.write(byte_arr)
        f.close()
        
        filesize = os.stat('ex_binary').st_size
        
        self.assertEqual(filesize, int(1e6), "The File size isn't equal to 1 million.")  
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
       
        
if __name__ == "__main__":
    unittest.main()