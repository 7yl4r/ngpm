import unittest

import shutil
import os.path

import CONFIG
import utils
import newModule

TEST_NAME = "temp2"  # fake module name to use for testing (should be lowerCamelCase)


class TestNewModule(unittest.TestCase):

    def setUp(self):
        newModule.create_module(TEST_NAME)

    def tearDown(self):
        shutil.rmtree(CONFIG.module_dir+'/'+TEST_NAME)

    def test_that_requested_files_exists(self):
        """tests that directory is created"""
        self.assertTrue(os.path.isfile(CONFIG.module_dir+'/'+TEST_NAME+'/'+TEST_NAME+'.html'))
        self.assertTrue(os.path.isfile(CONFIG.module_dir+'/'+TEST_NAME+'/'+TEST_NAME+'.less'))

    def test_that_dep_added_to_package_json(self):
        data = utils.get_package_json()
        self.assertIsNotNone(data['browser'][utils.get_hyphen_name(TEST_NAME)])
    
if __name__ == '__main__':
    unittest.main()