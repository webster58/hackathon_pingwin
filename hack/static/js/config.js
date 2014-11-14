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
    
    $scope.name = "scope";
    $scope.url = ""

    $scope.get_services = function(){
      console.log("get");
    };

    $scope.get_ping = function(){
      console.log($scope.url);
    };


  }
]);
