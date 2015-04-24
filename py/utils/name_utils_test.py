import unittest

import name_utils


class TestHyphenNamer(unittest.TestCase):
    def test_hyphen_name_from_complex_camel_name(self):
        TEST_NAME = "ngUIBootFooter"
        self.assertEqual(name_utils.get_hyphen_name(TEST_NAME), 'ng-ui-boot-footer')


if __name__ == '__main__':
    unittest.main()