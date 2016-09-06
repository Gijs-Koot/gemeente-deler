console.log("Welcome!");

var app = angular.module('gd-app', ['ngRoute', 'ui.bootstrap']);

app.config(function($routeProvider) {
    $routeProvider.when('/about', {
            templateUrl : 'partials/about.html',
            controller  : function(){

            }
        }).otherwise({
                templateUrl : 'partials/home.html',
                controller  : function($scope){
                    console.log("Welcome to home.");
                    $scope.checkModel = {
                      wot: "wot"
                    };
                }
        })
});
