app.controller("mainCtrl", function($scope, $firebaseObject) {

});


app.controller("dashnCtrl", function($scope, $firebaseObject) {

});



app.controller("authCtrl", function($scope, $window, $firebaseAuth, $firebaseObject) {
    var auth = $firebaseAuth();

    $scope.user_name = '';
    $scope.user_email = '';
    $scope.user_password = '';

    $scope.alertMessage = '';
    $scope.loggedUserID = null;

    auth.$onAuthStateChanged(function(firebaseUser) {
        if (firebaseUser) {
            console.log("Signed in as:", firebaseUser.uid);
            // $window.location.href = '/dash.php';
            $scope.loggedUserID = firebaseUser.uid;
        } else {
            console.log("Signed out");
        }
    });


    $scope.loginWithFacebook = function() {
        auth.$signInWithPopup("facebook").then(function(firebaseUser) {
            createUserProfile(firebaseUser.user.displayName, firebaseUser.user.uid);
        }).catch(function(error) {
            $scope.alertMessage = error.message;
        });
    }


    $scope.loginWithGoogle = function() {
        auth.$signInWithPopup("google").then(function(firebaseUser) {
            createUserProfile(firebaseUser.user.displayName, firebaseUser.user.uid);
        }).catch(function(error) {
            $scope.alertMessage = error.message;
        });
    }


    $scope.createUser = function(name, email, password) {
        auth.$createUserWithEmailAndPassword(email, password).then(function(user) {
            createUserProfile(name, user.uid);
        }).catch(function(error) {
            $scope.alertMessage = error.message;
        });
    }


    var createUserProfile = function(name, uid) {
        var ref = firebase.database().ref('users/' + uid);
        var obj = $firebaseObject(ref);

        obj.$loaded().then(function() {
            obj.name = name;
            obj.$save().then(function(ref) {

            }, function(error) {
                $scope.alertMessage = error.message;
            });
        });
    }


    $scope.resetPassword = function(email) {
        auth.$sendPasswordResetEmail(email).then(function() {
            $scope.alertMessage = "Password reset email sent successfully!";
        }).catch(function(error) {
            $scope.alertMessage = error.message;
        });
    }


    $scope.loginUser = function(email, password) {
        auth.$signInWithEmailAndPassword(email, password).then(function(user) {
            console.log(user);
        }).catch(function(error) {
            $scope.alertMessage = error.message;
        });
    }


    $scope.resetPasswordCheck = false;
    $scope.resetTrigger = function() {
        if ($scope.resetPasswordCheck == false) {
            $scope.resetPasswordCheck = true;
        } else {
            $scope.resetPasswordCheck = false;
        }
    }


    $scope.signUserOut = function() {
        auth.$signOut();
    }



});