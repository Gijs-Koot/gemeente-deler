console.log("Welcome!");

var app = angular.module('gd-app', ['ngRoute', 'ui.bootstrap', 'rzModule', 'leaflet-directive']);

app.config(function($routeProvider) {
    $routeProvider.when('/about', {
            templateUrl : 'partials/about.html',
            controller  : function(){

            }
        }).when('/ui-test', {
            templateUrl: 'partials/ui-test.html',
            controller: function($scope){
                console.log("Welcome to home.");
                $scope.checkModel = {
                  wot: "wot"
                };
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
                controller  : function($scope){

                }
        })
});

app.controller("GeoJSONController", ['$scope', '$http', function($scope, $http) {
    angular.extend($scope, {
        japan: {
            lat: 37.26,
            lng: 138.86,
            zoom: 4
        },
        defaults: {
            scrollWheelZoom: false
        }
    });

    // Get the countries geojson data from a JSON
    $http.get("data/JPN.geo.json").success(function(data, status) {
        angular.extend($scope, {
            geojson: {
                data: data,
                style: {
                    fillColor: "green",
                    weight: 2,
                    opacity: 1,
                    color: 'white',
                    dashArray: '3',
                    fillOpacity: 0.7
                }
            }
        });
    });
}]);
