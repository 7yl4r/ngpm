import unittest

import os
import shutil

from ..ngpm import main


class TestMain(unittest.TestCase):

    def test_create_new(self):
        """tests that directory is created"""
        try:
            main(['ngpm.py', 'new', 'temp'])
            self.assertTrue(os.path.isfile('ng-modules/temp/temp.html'))
            self.assertTrue(os.path.isfile('ng-modules/temp/temp.less'))
        finally:
            shutil.rmtree('ng-modules/temp')
    
if __name__ == '__main__':
    unittest.main()