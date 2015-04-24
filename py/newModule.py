#!/usr/bin/env python
import os
import fileinput

import utils

CONTROLLER_TEMPLATE = """require('angular');
Howl = require('howler');    // for sounds (if you need them)
Nodule = require('nodule');  // for nodule helpers

var app = angular.module('{0}', []);

app.directive("{1}", function() {{
    return {{
        restrict: 'E',
        templateUrl: "ng-modules/{1}/{1}.html"
    }};
}});

app.controller("{1}Controller", ['data', '$scope', '$rootScope', function(data, $scope, $rootScope) {{
    var vm = this;
    vm.nodule = new Nodule($rootScope, '{0}');

    // your controller code here
    vm.clickedTheButton = function(){{
        alert('you clicked {0} button')
    }}
}}]);

module.exports = angular.module('{0}').name;"""


def create_module(module_name=None):
    if module_name is None:
        module_name = raw_input("enter module name (spaces, lowercase). example: my module\n").strip()

    module_name = utils.get_space_name(module_name)

    camel_name = utils.get_camel_name(module_name)
    hyphen_name = utils.get_hyphen_name(module_name)

    directory = './ng-modules/'+camel_name+'/'
    print 'creating', directory
    if os.path.exists(directory):
        raise ValueError("module name already taken")
    else:
        os.makedirs(directory)

    print 'making html template (view) ', camel_name + '.html'
    with open(directory + camel_name + '.html', 'w') as w_file:
        w_file.write('<div ng-controller="' + camel_name + 'Controller as ' + camel_name + 'Ctrl">\n\t' +
                     'put ' + module_name + " view content here...\n" +
                     '\t<button ng-click="' + camel_name + 'Ctrl.clickedTheButton()"></button>\n</div>')

    print 'making angular module ', camel_name + '.js'
    with open(directory + camel_name + '.js', 'w') as w_file:
        w_file.write(CONTROLLER_TEMPLATE.format(hyphen_name, camel_name))

    print 'making less style file', camel_name + '.less'
    with open(directory + camel_name + '.less', 'w') as w_file:
        w_file.write("/* styles for " + module_name + " module */")

    try:
        print 'adding module to package.json'
        inserted = False
        for line in fileinput.input('package.json', inplace=1):
            if line.strip() == '"browser":{':
                inserted = True
            else:
                if inserted:
                    print '        "' + hyphen_name + '":"' + directory + camel_name + '.js",'
                inserted = False
            print line,
    except OSError as err:
        print '\n\nERR: Could not write to package.json\n\n'
        raise err

    try:
        print 'adding module to app.coffee main module'
        inserted = False
        for line in fileinput.input('app.coffee', inplace=1):
            if line.strip() == "        # WARN: do not change this comment line unless you update newModule.py as well!":
                inserted = True
            else:
                if inserted:
                    print "        require('" + hyphen_name + "'),"
                inserted = False
            print line,
    except OSError as err:
        print '\n\nERR: could not write to app.coffee\n\n'
        raise err

    try:
        print 'adding styles to app.less'
        with open("app.less", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('@import "' + directory[2:] + camel_name + '";\n' + content)
    except OSError as err:
        print '\n\nERR: could not write to app.less\n\n'
        raise err