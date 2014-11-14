var pingwin = angular.module('pingwin', ["ngResource", "ngRoute", "ngSanitize"]);


pingwin.config([
    "$routeProvider", "$locationProvider", function($routeProvider, $locationProvider) {
      return $routeProvider.when("/", {
        templateUrl: "/media/index.html",
        controller: 'Home'
      });
    }
  ]);

pingwin.controller("Home", [
  "$scope", "$http", "$route", function($scope, $http, $route) {
    
    $scope.services = [];
    $scope.form = {url: "", name: ""};
    $scope.ready_services = [];
    $scope.loading = {is: false};

    $scope.get_services = function(){
      $http.post("/api/get_services").success(function(data) {
        $scope.services = data;
      });
    };

    $scope.get_pings = function(){
      $scope.loading.is = true;
      $scope.ready_services = [];
      for (i = 0; i < $scope.services.length; i++) { 
        service = $scope.services[i];
        $scope.get_ping(service);
      }
    };

    $scope.get_ping = function(service){
      params = {service: service.id, name: $scope.form.url};
      // params = {name: $scope.form.url};
      $http.get("/api/get_ping?name="+$scope.form.url+"&service="+service.id).success(function(data) {
        data.name = service.name;
        data.country = service.country;
        $scope.ready_services.push(data);
        if($scope.ready_services.length == $scope.services.length){
          $scope.loading.is = false;
        }
      });
    };

    $scope.get_services();

    $scope.check_code = function(code){
      r = "";
      if(code[0] == 2){
        r = "btn-success";
      }
      if(code[0] == 3){
        r = "btn-warning";
      }
      if(code[0] == 4 || code[0] == 5 ){
        r = "btn-danger";
      }

      return r;

    };


  }
]);
