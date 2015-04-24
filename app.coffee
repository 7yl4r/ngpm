# jquery must be loaded before this...
require('angular')

# "main" controller
app = angular.module('the-oregon-trajectory', [
        # WARN: do not change this comment line unless you update newModule.py as well!
        require('ship-customizer'),
        require('leaderboard'),
        require('asteroid-mining'),
        require('situation'),
        require('trader'),
        require('example-module'),
        require('debris-encounter'),
        require('audio-controls'),
        require('maneuver-screen'),
        require('game-over'),
        require('ui.bootstrap'),
        require('ngTouch'),
        require('header-navbar'),
        require('splash-header'),
        require('app-footer'),
        require('main-menu'),
        require('shop'),
        require('you-win'),
        require('travel-screen')
    ]
)

app.controller('MainCtrl', ['$scope', ($scope)->


])