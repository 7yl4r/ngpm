import unittest

import os.path

import CONFIG
import utils
import installModule
from ..ngpm import main

TEST_NAME = "temp2"  # fake module name to use for testing (should be lowerCamelCase)


class TestInstallModule(unittest.TestCase):

    def setUp(self):
        #installModule.install(TEST_NAME)
        return

    def tearDown(self):
        #main(['rm', TEST_NAME])
        return

    def test_that_requested_files_exists(self):
        """tests that directory is created"""
        return

    def test_that_dep_added_to_package_json(self):
        data = utils.get_package_json()
        #self.assertIsNotNone(data['browser'][utils.get_hyphen_name(TEST_NAME)])
    
if __name__ == '__main__':
    unittest.main()