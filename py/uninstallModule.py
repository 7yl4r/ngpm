import shutil

import utils
import CONFIG


def remove_module(name):
    camel_name = utils.get_camel_name(name)
    hyphen_name = utils.get_hyphen_name(name)

    # del the module
    shutil.rmtree(CONFIG.module_dir+'/'+camel_name)

    # remove from package.json
    data = utils.get_package_json()
    del data['browser'][hyphen_name]
    # overwrite package.json
    utils.write_package_json(data)

    # remove from app.less
    utils.remove_less(name)

    # remove from app.coffee
    utils.remove_coffee(name)