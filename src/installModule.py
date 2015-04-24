import shutil

from CONFIG import CONFIG
import utils


def install(name, depender='__app__'):
    """
    installs module from library
    :param name:
    :param depender:
    :return: True if installed, False if not installed (already exists)
    """

    name = utils.get_camel_name(name)

    if utils.module_is_installed(name):
        print "\tWARN: module already installed"
        utils.add_dependency_link(name, depender)
        return False
    elif not utils.package_exists(name, CONFIG.library):
        raise LookupError('module "' + name + '" not found in library ('+CONFIG.library+').')
    else:
        print 'installing', name, '...'
        try:  # install dependencies
            package_data =  utils.get_package_json(CONFIG.library + '/' + name + '/package.json')
            for dep in package_data['abl-dependencies']:
                install(dep, depender=name+package_data['version'])
        except KeyError:
            pass  # no dependencies

        utils.add_coffee(name)
        utils.add_less(name)
        utils.add_to_json(name)
        src = CONFIG.library + '/' + name
        dest = CONFIG.module_dir + '/' + name
        shutil.copytree(src, dest)

        utils.add_dependency_link(name, depender)
        return True