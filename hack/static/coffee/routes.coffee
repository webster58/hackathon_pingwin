pingwin.config [ "$routeProvider", "$locationProvider", ($routeProvider, $locationProvider) ->
  
  $routeProvider.when "/",
    templateUrl: "index.html"
    controller: 'Main'

]