import unittest

import name_utils


class TestHyphenNamer(unittest.TestCase):
    def test_hyphen_name_from_complex_camel_name(self):
        TEST_NAME = "ngUiBootFooter"
        self.assertEqual(name_utils.get_hyphen_name(TEST_NAME), 'ng-ui-boot-footer')


class TestCamelNamer(unittest.TestCase):
    def test_camel_name_acronym(self):
        # take note of how acronyms are camel-case-ified
        TEST_NAME = "myLittleTestGUIModule"
        self.assertEqual(name_utils.get_camel_name(TEST_NAME), 'myLittleTestGuiModule')


if __name__ == '__main__':
    unittest.main()