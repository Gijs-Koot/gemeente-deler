var app = angular.module('gd-app', ['ngRoute', 'ui.bootstrap', 'rzModule', 'leaflet-directive', 'ui.grid']);

app.config(function($routeProvider) {
    $routeProvider.when('/about', {
            templateUrl : 'partials/about.html',
            controller  : function(){

            }
        }).when('/ui-test', {
            templateUrl: 'partials/ui-test.html',
            controller: function($scope){
                $scope.verticalSlider = {
                  value: 4,
                  options: {
                    floor: 0,
                    ceil: 10,
                    vertical: true
                  }
                };
              }
        }).when('/map-test', {
            templateUrl: 'partials/map-test.html',
            controller: "GeoJSONController"
        }).otherwise({
                templateUrl : 'partials/home.html',
                controller  : 'HomeController'
        })
});
