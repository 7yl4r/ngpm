__author__ = 'tylar'

from ..CONFIG import CONFIG
import file_utils


def add_dependency_link(name, depender):
    # use to indicate that named module depends on depender
    file = CONFIG.module_dir + '/' + name + '/package.json'
    data = file_utils.get_package_json(file)
    try:
        data['abl-dependers'].append(depender)
    except KeyError:
        data['abl-dependers'] = [depender]
    file_utils.write_package_json(data, file)
