import unittest

import os.path

from CONFIG import CONFIG
import utils
import newModule
from ..ngpm import main

TEST_NAME = "temp2"  # fake module name to use for testing (should be lowerCamelCase)


class TestNewModule(unittest.TestCase):

    def setUp(self):
        newModule.create_module(TEST_NAME)

    def tearDown(self):
        main(['rm', TEST_NAME])

    def test_that_new_module_is_created(self):
        self.assertTrue(utils.module_is_installed(TEST_NAME))
    
if __name__ == '__main__':
    unittest.main()