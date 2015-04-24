import shutil

from CONFIG import CONFIG
import utils


def install(name):
    # installs module from library
    if not utils.package_exists(name, CONFIG.library):
        raise LookupError('module "' + name + '" not found in library ('+CONFIG.library+').')
    else:
        name = utils.get_camel_name(name)
        utils.add_coffee(name)
        utils.add_less(name)
        utils.add_to_json(name)
        src = CONFIG.library + '/' + name
        dest = CONFIG.module_dir + '/' + name
        shutil.copytree(src, dest)