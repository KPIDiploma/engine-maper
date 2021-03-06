/**
 * Created by Kryvonis on 3/23/17.
 */
angular.module('indexApp', ['ngRoute'])
    .config(
        ['$interpolateProvider', '$httpProvider', function ($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('[[');
            $interpolateProvider.endSymbol(']]');
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }]
    )


    .controller('indexController', function ($scope, $location, $http, $window) {

        $scope.login = function () {
            $http
                .post('api/v1/auth/login', $scope.user)
                .success(function (data, status, headers, config) {
                    $window.location = '/profile';
                }).error(function (data, status, header, config) {
                    $scope.result = 'email or password not correct';
            });
        };



    });
