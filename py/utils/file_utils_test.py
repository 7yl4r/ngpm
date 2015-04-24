import unittest

from ..CONFIG import CONFIG
import file_utils


class TestPackageLookup(unittest.TestCase):
    def test_lookup_existing_library_pkg_returns_true(self):
        TEST_PACK = "ngUIBootFooter"
        self.assertTrue(file_utils.package_exists(TEST_PACK, CONFIG.library))


class TestAddCoffee(unittest.TestCase):
    def setUp(self):
        self.TEST_NAME = "temp2"  # fake module name to use for testing (should be lowerCamelCase)
        file_utils.add_coffee(self.TEST_NAME)
        return

    def tearDown(self):
        file_utils.remove_coffee(self.TEST_NAME)
        return

    def test_that_require_is_added(self):
        self.assertTrue(file_utils.module_required_in_app(self.TEST_NAME))
        return
    
if __name__ == '__main__':
    unittest.main()