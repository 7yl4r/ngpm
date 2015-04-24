import unittest

import shutil
import os.path

import CONFIG
import newModule


class TestNewModule(unittest.TestCase):

    def setUp(self):
        newModule.create_module("temp")

    def tearDown(self):
        shutil.rmtree(CONFIG.module_dir+'/temp')

    def test_that_requested_files_exists(self):
        """tests that directory is created"""
        self.assertTrue(os.path.isfile(CONFIG.module_dir+'/temp/temp.html'))
        self.assertTrue(os.path.isfile(CONFIG.module_dir+'/temp/temp.less'))

    
if __name__ == '__main__':
    unittest.main()