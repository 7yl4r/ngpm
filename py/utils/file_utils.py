import json
import os
import fileinput

from ..CONFIG import CONFIG
from name_utils import *


def module_is_installed(name):
    # returns true if module is installed properly
    return package_exists(name) and module_required_in_app(name) and module_imported_in_app(name)


def module_imported_in_app(name):
    # returns true if module "@import"ed is in app.less
    name = get_camel_name(name)
    count = 0

    count += count_substrings_in(CONFIG.app_less, '@import "'+CONFIG.module_dir+'/'+name+'/'+name)
    count += count_substrings_in(CONFIG.app_less, "@import '"+CONFIG.module_dir+'/'+name+'/'+name)

    if count > 1:
        print "\tWARN: module", name, '"@import"ed multiple times in', CONFIG.app_less
        return True
    elif count == 1:
        return True
    else:
        return False


def module_required_in_app(name):
    # returns true if module require() is in app.coffee
    name = get_hyphen_name(name)
    count = 0
    count += count_substrings_in(CONFIG.app_coffee, 'require("'+name)
    count += count_substrings_in(CONFIG.app_coffee, "require('"+name)
    count += count_substrings_in(CONFIG.app_coffee, 'require(" '+name)
    count += count_substrings_in(CONFIG.app_coffee, "require(' "+name)
    if count > 1:
        print "\tWARN: module", name, "require()d multiple times in", CONFIG.app_coffee
        return True
    elif count == 1:
        return True
    else:
        return False


def package_is_complete(camel_name, dir=CONFIG.module_dir):
    # returns true if all is good, returns false if malformed package
    return (os.path.isfile(dir+'/'+camel_name+'/'+camel_name+'.html') and
            os.path.isfile(dir+'/'+camel_name+'/'+camel_name+'.less') and
            (
                os.path.isfile(dir+'/'+camel_name+'/'+camel_name+'.coffee') or
                os.path.isfile(dir+'/'+camel_name+'/'+camel_name+'.js')
            )
    )


def package_exists(package_name, dir=CONFIG.module_dir):
    name = get_camel_name(package_name)
    return os.path.isdir(dir+"/"+name) and package_is_complete(name, dir)


def get_package_json():
    with open(CONFIG.package_json, 'r') as json_file:
        return json.load(json_file)


def write_package_json(data):
    # overwrites package.json
    with open(CONFIG.package_json, 'w') as json_file:
        json.dump(data,json_file, indent=4, sort_keys=True)


def count_substrings_in(filename, substring):
    # returns number of lines which contain substring in filename
    count = 0
    with open(filename, 'r') as in_file:
        for line in in_file:
            if substring in line:
                count += 1
    return count


def remove_line(filename, substring):
    """
    removes lines with substring in them
    :param filename:
    :param rm_line:
    :return: number of lines removed from the given file
    """
    TEMP_FILE = ".temp.file.txt"
    count = 0
    with open(filename, 'r') as in_file:
        with open(TEMP_FILE, 'w') as out_file:
            for line in in_file:
                if not substring in line:
                    out_file.write(line)
                else:
                    count += 1
    if count > 0:
        os.remove(filename)
        os.rename(TEMP_FILE, filename)
    else:
        os.remove(TEMP_FILE)
    return count


def add_less(name):
    name = get_camel_name(name)
    try:
        print 'adding styles to', CONFIG.app_less
        with open(CONFIG.app_less, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('@import "' + CONFIG.module_dir + '/' + name + '/' + name + '";\n' + content)
    except OSError as err:
        print '\n\nERR: could not write to', CONFIG.app_less, '\n\n'
        raise err


def remove_less(name):
    # removes line importing <name> module from app.less
    name = get_camel_name(name)
    count = 0
    count += remove_line(CONFIG.app_less, '@import "' + CONFIG.module_dir + '/'+name+'/'+name)
    count += remove_line(CONFIG.app_less, "@import '" + CONFIG.module_dir + '/'+name+'/'+name)

    if count < 1:
        return False
    else:
        return True


def add_coffee(name):
    # adds line require()ing name module to app.coffee
    name = get_hyphen_name(name)
    try:
        print 'adding module to app.coffee main module'
        inserted = False
        flag = False
        flag2 = False
        lines = []
        for line in fileinput.input('app.coffee', inplace=1):
            if "# WARN: This comment required for ngpm; do not alter!" in line:
                inserted = True
                flag = True
            else:
                if inserted:
                    print "        require('" + name + "'),"
                    lines.append("       require('"+name+"'),\n")
                    flag2 = True
                    inserted = False
            print line,
            lines.append(line)

        print "flag:", flag
        print "flag2:", flag2
        my_str = "# WARN: This comment required for ngpm; do not alter!"
        for i, line in enumerate(lines):
            if i < 4 or i > 7:
                continue
            print line, '==', '     '+my_str, '=', my_str in line
    except OSError as err:
        print '\n\nERR: could not write to app.coffee\n\n'
        raise err


def remove_coffee(name):
    # removes line require()ing <name> module from app.coffee
    name = get_hyphen_name(name)
    count = 0
    count += remove_line(CONFIG.app_coffee, 'require("' + name)
    count += remove_line(CONFIG.app_coffee, "require('" + name)
    count += remove_line(CONFIG.app_coffee, 'require( "' + name)
    count += remove_line(CONFIG.app_coffee, "require( '" + name)
    if count > 1:
        print "\tWARN: multiple require()s removed from", CONFIG.app_coffee
        return True
    elif count == 1:
        return True
    else:
        return False