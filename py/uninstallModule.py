import shutil
import json

import CONFIG
import utils

def remove_module(name):
    print name
    # del the module
    #shutil.rmtree(CONFIG.module_dir+'/'+name)

    # remove from package.json
    data = utils.get_package_json()
    for module in data['browser']:
        print module, ',',

    # remove from app.less
    # remove from app.coffee
