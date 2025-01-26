# Angular 1

OBSOLETE: Používejte [Angular 2](angular2.md)

## Instalace

```
npm install -g @angular/cli
ng new <my-app>
cd <my-app>
ng serve --open
```

## Použití

Výrazy: `{{ var }}` nebo `{{ 3 + x }}`

Module je namespace. V modulu jsou controlery.

Directives: funkce přímo rozšřiřující HTML (tag, atribut).

**ng tagy**: `ng-show`, `ng-hide`, `ng-disabled`, `ng-model`, `ng-repeat="x in names"`, obsahuje `$index`, `$odd`, `$even`

**Module** 2. parametr jsou závislosti. Bez `[]` bychom daný modul získali, nikoliv tvořili.
```js
var app = angular.module('myApp', []);
```

**Controller** proměnné ze `$scope` jsou dostupné v dané template.

```js
app.controller('myCtrl', function($scope) {
    $scope.firstName= "John";
    $scope.lastName= "Doe";
});
```

**Services** `$scope` je jen jedna ze services. Další je např. `$location`, `$http`, `$timeout`, `$interval`. Lze je použít v modulech, controlerech, filtrech i direktivách.

**Filtry**

## Dir tree

<small>

```
├── node_modules
├── package.json
├── README.md
└── src
  ├── app
  |   ├── app.component.css
  |   ├── app.component.html
  |   ├── app.component.ts
  |   └── app.module.ts
  ├── assets
  ├── environments
  ├── favicon.ico
  ├── index.html
  ├── main.ts
  ├── polyfills.ts
  └── styles.css
```

</small>

https://angular.io
https://www.w3schools.com/angular/
