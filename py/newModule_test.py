import unittest

import shutil
import os.path

import newModule


class TestNewModule(unittest.TestCase):

    def setUp(self):
        newModule.create_module("temp")

    def test_that_requested_files_exists(self):
        """tests that directory is created"""
        try:
            self.assertTrue(os.path.isfile('ng-modules/temp/temp.html'))
            self.assertTrue(os.path.isfile('ng-modules/temp/temp.less'))
        finally:
            shutil.rmtree('ng-modules/temp')

    
if __name__ == '__main__':
    unittest.main()