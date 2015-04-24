import unittest

import os
import shutil

import CONFIG
from ..ngpm import main


class TestMain(unittest.TestCase):

    def test_create_new(self):
        """tests that directory is created"""
        try:
            main(['new', 'temp'])
            self.assertTrue(os.path.isfile(CONFIG.module_dir+'/temp/temp.html'))
            self.assertTrue(os.path.isfile(CONFIG.module_dir+'/temp/temp.less'))
        finally:
            shutil.rmtree(CONFIG.module_dir+'/temp')
    
if __name__ == '__main__':
    unittest.main()