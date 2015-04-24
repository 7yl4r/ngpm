import unittest

from CONFIG import CONFIG
import file_utils

TEST_NAME = "temp2"  # fake module name to use for testing (should be lowerCamelCase)


class TestAddCoffee(unittest.TestCase):

    def setUp(self):
        file_utils.add_coffee(TEST_NAME)
        return

    def tearDown(self):
        file_utils.remove_coffee(TEST_NAME)
        return

    def test_that_require_is_added(self):
        self.assertTrue(file_utils.module_required_in_app(TEST_NAME))
        return
    
if __name__ == '__main__':
    unittest.main()