app.controller("HomeController", ['$scope', '$http', function($scope, $http) {
    console.log("Welcome to home.");

    $http.get('api/gemeentes').then(function(response){
      $scope.results = response.data.results;
        console.log("data", response.data);
        console.log("results", response.data.results);
    });

    $scope.datasets = [];

    $http.get('api/datasets').then(function(response){
        $scope.datasets = response.data;
    });

    $scope.search_similar = function(){
        console.log('Zoeken');
        console.log($scope.selected_gemeente);

        var categories = [];

        $scope.datasets.map(function(dataset){
            if(dataset.active){
                categories.push(dataset.id);
                console.log('categories', categories);
            }
        });

        $http.post('api/similar', {
            "gemeente_id": $scope.selected_gemeente,
            "categories": categories
        }).then(function(response){

          $scope.header = response.data.header;

          $scope.rows = response.data.rows;


        });

    }

}]);
