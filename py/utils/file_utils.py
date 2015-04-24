import json
import os

from ..CONFIG import CONFIG
from name_utils import *


def get_package_json():
    with open(CONFIG.package_json, 'r') as json_file:
        return json.load(json_file)


def write_package_json(data):
    # overwrites package.json
    with open(CONFIG.package_json, 'w') as json_file:
        json.dump(data,json_file, indent=4, sort_keys=True)


def remove_line(filename, rm_line):
    """
    :param filename:
    :param rm_line:
    :return: number of lines removed from the given file
    """
    TEMP_FILE = ".temp.file.txt"
    count = 0
    with open(filename, 'r') as in_file:
        with open(TEMP_FILE, 'w') as out_file:
            for line in in_file:
                if line != rm_line:
                    out_file.write(line)
                else:
                    count += 1
    if count > 0:
        os.remove(filename)
        os.rename(TEMP_FILE, filename)
    else:
        os.remove(TEMP_FILE)
    return count


def remove_less(name):
    # removes line importing <name> module from app.less
    name = get_camel_name(name)
    if remove_line(CONFIG.app_less, '@import "' + CONFIG.module_dir + '/'+name+'/'+name + '";\n') < 1:
        return False
    else:
        return True


def remove_coffee(name):
    # removes line require()ing <name> module from app.coffee
    name = get_hyphen_name(name)
    if remove_line(CONFIG.app_coffee, "        require('" + name + "'),") < 1:
        return False
    else:
        return True