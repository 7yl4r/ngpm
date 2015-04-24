import json
import re
import os

import CONFIG


def get_package_json():
    with open(CONFIG.package_json, 'r') as json_file:
        return json.load(json_file)


def write_package_json(data):
    # overwrites package.json
    with open(CONFIG.package_json, 'w') as json_file:
        json.dump(data,json_file, indent=4, sort_keys=True)


def remove_line(filename, rm_line):
    TEMP_FILE = ".temp.file.txt"
    with open(filename, 'r') as in_file:
        with open(TEMP_FILE, 'w') as out_file:
            for line in in_file:
                if line != rm_line:
                    out_file.write(line)
    os.remove(filename)
    os.rename(TEMP_FILE, filename)


def remove_less(name):
    # removes line importing <name> module from app.less
    name = get_camel_name(name)
    remove_line(CONFIG.app_less, '@import "' + CONFIG.module_dir + '/'+name+'/'+name + '";\n')


def remove_coffee(name):
    # removes line require()ing <name> module from app.coffee
    name = get_hyphen_name(name)
    remove_line(CONFIG.app_coffee, "        require('" + name + "'),")


def get_space_name(string):
    # convert CamelCase or hyphen-delimited to "space name"
    # camel-case to spaces
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower()
    # hyphens to spaces
    return s2.replace('-', ' ')


def get_hyphen_name(name):
    name = get_space_name(name)
    name.replace(" ", "-")
    return name


def get_camel_name(name):
    name = get_space_name(name)
    words = name.split(' ')
    if len(words) == 1:
        return words[0]
    elif len(words) > 1:
        c_name = words[0]
        for word in words[1:]:
            c_name += word.title()
        return c_name
    else:
        raise ValueError('wordlist ' + str(words) + 'len < 1')