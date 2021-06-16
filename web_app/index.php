<!DOCTYPE html>
<html lang="en" class="no-js" ng-app="GoARApp">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>GoAR</title>

    <!-- AngularJS -->
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular-route.js"></script>

    <!-- Firebase -->
    <script src="https://www.gstatic.com/firebasejs/3.6.6/firebase.js"></script>

    <!-- AngularFire -->
    <script src="https://cdn.firebase.com/libs/angularfire/2.3.0/angularfire.min.js"></script>

    <link rel="stylesheet" href="./ui/icofont/icofont.min.css">

    <script src="./config/config.js"></script>

    <script src="./scripts/init.js"></script>

    <script src="./ui/js/main.min.js"></script>

    <script src="./scripts/controllers.js"></script>

    <script src="./scripts/router.js"></script>

    <link rel="stylesheet" href="./ui/css/style.css">
</head>

<body class="has-animations">


<div class="body-wrap">


    <div ng-view></div>


<?php include "includes/footer.html" ?>

</div>



</body>
</html>