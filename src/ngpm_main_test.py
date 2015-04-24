import unittest

import os

from CONFIG import CONFIG
import utils
from ..ngpm import main


class TestMain(unittest.TestCase):

    def test_create_new(self):
        """tests create new module"""
        fake_module = 'temp123abc'
        try:
            main(['new', fake_module])
            self.assertTrue(utils.module_is_installed(fake_module))
        finally:
            main(['rm', fake_module])

    def test_add_n_remove(self):
        """tests install new, then rm module should return to initial state"""
        module = 'ngUiBootFooter'  # NOTE: must be real module in library
        main(['add', module])
        self.assertTrue(utils.module_is_installed(module))

        main(['rm', module])
        self.assertFalse(utils.module_is_installed(module))

    
if __name__ == '__main__':
    unittest.main()