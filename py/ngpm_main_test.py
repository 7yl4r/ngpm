import unittest

import os

import CONFIG
import utils
from ..ngpm import main


class TestMain(unittest.TestCase):

    def test_create_new(self):
        """tests that directory is created"""
        try:
            main(['new', 'temp'])
            self.assertTrue(os.path.isfile(CONFIG.module_dir+'/temp/temp.html'))
            self.assertTrue(os.path.isfile(CONFIG.module_dir+'/temp/temp.less'))
        finally:
            main(['rm', 'temp'])

    def test_add_n_remove(self):
        """tests create new, then rm module should return to initial state"""
        main(['new', 'temp'])
        main(['rm', 'temp'])
        self.assertNotIn('temp', utils.get_package_json()['browser'])

    
if __name__ == '__main__':
    unittest.main()