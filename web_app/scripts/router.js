app.config(function($routeProvider) {
    $routeProvider
        .when("#/!", {
            templateUrl: "index.php"
        })
        .when("/main", {
            templateUrl: "./pages/front/main.html",
            controller: 'authCtrl',
            cache: false,
        })
        .when("/login", {
            templateUrl: "./pages/auth/login.html",
            controller: 'authCtrl',
        })
        .when("/signup", {
            templateUrl: "./pages/auth/signup.html",
            controller: 'authCtrl',
        })
        .when("/dash", {
            templateUrl: "./pages/dash/main.html",
            controller: 'authCtrl',
        })

    ;
});