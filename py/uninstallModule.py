import shutil

import utils
from CONFIG import CONFIG


def remove_module(name):
    camel_name = utils.get_camel_name(name)
    hyphen_name = utils.get_hyphen_name(name)

    # del the module
    try:
        shutil.rmtree(CONFIG.module_dir+'/'+camel_name)
    except OSError as err:
        if err.errno == 2:
            print "\tWARN: could not find installed module at", CONFIG.module_dir+'/'+camel_name+'/'
        else:
            raise err

    # remove from package.json
    data = utils.get_package_json()
    try:
        del data['browser'][hyphen_name]
    except KeyError:
        print "\tWARN: could not find", name, "in", CONFIG.package_json
    else:
        # overwrite package.json
        utils.write_package_json(data)

    # remove from app.less
    if not utils.remove_less(name):
        print '\tWARN: could not find @import of', name, 'in', CONFIG.app_less

    # remove from app.coffee
    if not utils.remove_coffee(name):
        print '\tWARN: could not find require("', name, '" in', CONFIG.app_coffee
