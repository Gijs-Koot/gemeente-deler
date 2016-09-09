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
            "categories": ["aantal_verdachten"]
        }).then(function(response){

          $scope.header = response.data.header;

          $scope.rows = response.data.rows;


        });

    }

}]);
