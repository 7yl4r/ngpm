#!/usr/bin/env python
__author__ = '7yl4r'

import sys
from setup import VERSION

from ngpm.newModule import create_module
from ngpm.uninstallModule import remove_module
from ngpm.lsModules import ls
from ngpm.installModule import install

SHORT_FLAGS = {
    '-v': '--version',
    '-h': '--help'
}


def show_usage():
    print """
Angular Package Manager (ngpm) usage:
    FLAGS:
    -v | --version [pkg]      show version of ngpm or pkg
    -h | --help | --man       shows this help

    COMMANDS:
    new [moduleName]                      creates boilerplate for a new module
    rm  | uninstall | remove [moduleName] uninstalls module
    add | install [moduleName]            installs module
    ls [search_string]                    list installed modules

    """


def handle_flag(flag, args):
    """
    :param flag: long flag to handle
    :param args: full list of args (in case flag uses them)
    :return: number of args consumed
    """
    if flag == '--version':
        if len(args) < 2:
            print 'ngpm v' + VERSION
            return 1
        else:
            raise NotImplementedError('show version of module' + args[1])
            return 2
    elif flag == '--help' or '--man':
        show_usage()
        return 1
    else:
        print('ERR: unknown flag: ', flag)
        show_usage()
        return 1


def main(args):
    if len(args) < 1:
        show_usage()
    else:
        for i in range(len(args)):
            if args[i][0] == '-':
                # flag
                if args[i][1] == '-':
                    # long flag
                    i += handle_flag(args[i], args[i:])
                else:
                    # short flag
                    i += handle_flag(SHORT_FLAGS[args[i]], args[i:])

            elif args[i] == 'new':
                try:
                    create_module(args[i+1])
                except IndexError:
                    create_module()
                return

            elif args[i] in ['rm', 'remove', 'uninstall']:
                try:
                    remove_module(args[i+1])
                except IndexError:
                    print "\n\nERR: must give module name to be removed\n\n"
                    show_usage()
                return

            elif args[i] in ['list', 'ls']:
                try:
                    ls(args[i+1])
                except IndexError:
                    ls()
                return

            elif args[i] in ['add', 'install']:
                try:
                    install(args[i+1])
                except IndexError:
                    print "\n\nERR: must give module name to install from library\n\n"
                    show_usage()
                return

            # TODO: elif args[i] in ['mv', 'rename']:

            else:
                show_usage()
    return

if __name__ == "__main__":
    main(sys.argv[1:])
