app.controller("HomeController", ['$scope', '$http', function($scope, $http) {
    console.log("Welcome to home.");

    $http.get('/gemeentes').then(function(response){
      $scope.results = response.data.results;
    });

}]);
