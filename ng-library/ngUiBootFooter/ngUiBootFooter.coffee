require('angular')

app = angular.module('ng-ui-boot-footer', [])

app.directive("ngUIBootFooter", () ->
    return {
        restrict: 'E',
        templateUrl: "ng-modules/ngUIBootFooter/ngUIBootFooter.html"
    }
)

module.exports = angular.module('ng-ui-boot-footer').name