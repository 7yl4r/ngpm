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
        raise ValueError('module name '+str(directory)+'" already taken')
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

    data = utils.get_package_json()
    data['browser'][hyphen_name] = directory + camel_name + '.coffee'
    utils.write_package_json(data)

    utils.add_coffee(hyphen_name)

    utils.add_less(camel_name)