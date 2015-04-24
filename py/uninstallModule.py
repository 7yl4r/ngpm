import shutil

import CONFIG


def remove_module(name):
    print name
    shutil.rmtree(CONFIG.module_dir+'/'+name)
