app.controller("GeoJSONController", ['$scope', '$http', function($scope, $http) {
    angular.extend($scope, {
        japan: {
            lat: 52,
            lng: 4,
            zoom: 7
        },
        defaults: {
            scrollWheelZoom: false
        }
    });

    // Get the countries geojson data from a JSON
    $http.get("data/townships.geojson").success(function(data, status) {
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

app.filter('reverse', function() {
  return function(items) {
    return items.slice().reverse();
  };
});
