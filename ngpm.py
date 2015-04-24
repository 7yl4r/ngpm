#!/usr/bin/env python
__author__ = '7yl4r'

import sys

VERSION = '0.0.1'
SHORT_FLAGS = {
    '-v': '--version',
    '-h': '--help'
}


def show_usage():
    print """Angular Package Manager (ngpm) usage:
    -v, --version       show version of ngpm
    -h, --help, --man   shows this help
    """
    exit()


def handle_flag(flag, args=None):
    """
    :param flag: long flag to handle
    :param args: full list of args (in case flag uses them)
    :return: number of args consumed
    """
    if flag == '--version':
        print 'ngpm v' + VERSION
    elif flag == '--help' or '--man':
        show_usage()
    else:
        print('ERR: unknown flag: ', flag)
        show_usage()


def main(args):
    if len(args) < 1:
        show_usage()
    else:
        for arg in args:
            print arg
            if arg[0] == '-':
                # flag
                if arg[1] == '-':
                    # long flag
                    handle_flag(arg)
                else:
                    # short flag
                    handle_flag(SHORT_FLAGS[arg])
            elif arg == 'new':
                print 'TODO: create new module'

            elif arg == 'list':
                print 'TODO: list installed modules'

            elif arg == 'install':
                print 'TODO: read package.json ng-dep, install packages to ng-modules, add to app.css, app.js'

            else:
                show_usage()


if __name__ == "__main__":
    main(sys.argv[1:])
