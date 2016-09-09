app.controller("HomeController", ['$scope', '$http', function($scope, $http) {
    console.log("Welcome to home.");

    $http.get('/gemeentes').then(function(response){
      $scope.results = response.data.results;
    });


    $scope.search_similar = function(){
        console.log('Zoeken');
        console.log($scope.selected_gemeente);

        $http.post('/similar', {
            "gemeente_id": $scope.selected_gemeente,
            "categories": ["count_2015", "count_2014"]
        }).then(function(response){

          $scope.similar = response.data;

          var data = response.data;
          $scope.indices = data[0];

          console.log(indices);

        });

    }

}]);
