import unittest

from CONFIG import CONFIG
import utils
import installModule
from ..ngpm import main

TEST_NAME = "temp2"  # fake module name to use for testing (should be lowerCamelCase)


class TestInstallModule(unittest.TestCase):

    def setUp(self):
        # installModule.install(TEST_NAME)
        return

    def tearDown(self):
        # main(['rm', TEST_NAME])
        return

    def test_that_module_installed(self):
        """tests that module is created"""
        # self.assertTrue(utils.module_is_installed(TEST_NAME))
        return
    
if __name__ == '__main__':
    unittest.main()