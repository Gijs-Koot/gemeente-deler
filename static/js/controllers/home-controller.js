app.controller("HomeController", ['$scope', '$http', function($scope, $http) {
    console.log("Welcome to home.");



    $http.get('api/gemeentes').then(function(response){
      $scope.results = response.data.results;
        console.log('results', $scope.results);
          $scope.selected_gemeente = 0;
    });

    $scope.datasets = [];

    $http.get('api/datasets').then(function(response){
        $scope.datasets = response.data;
        console.log('datasets', $scope.datasets);
        //temp workaround select value

    });

    $scope.search_similar = function(){
        console.log('Zoeken');


        var categories = [];

        $scope.datasets.map(function(dataset){
            if(dataset.active){
                categories.push(dataset.id);
            }
        });

        if (categories.length == 0 ) {
            categories.push($scope.datasets[0].id);
            $scope.datasets[0].active = true;
        }

        $http.post('api/similar', {
            "gemeente_id": $scope.selected_gemeente,
            "categories": categories
        }).then(function(response){

          $scope.similarResults = response.data;
            console.log('similarResults', $scope.similarResults);




        });

    }

}]);
