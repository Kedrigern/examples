# JavaScript

* Dynamic typing: proměnné nemají daný typ
* Objekty jsou vlastně asociativní pole: `obj.x == obj['x']`
* First-class functions: funkce jsou objekt, mají atributy, lze je předávat etc.

## Prototypování

```js
function Auto(znacka, spz) {
        this.znacka = znacka;
        this.spz = spz;
        this.toString = function() {
                return 'Auto značky ' + this.znacka + ' s SPZ ' + this.spz;
        };
};

var auto1 = new Auto('Mercedes', 'A1blb');
var auto2 = new Auto('Audi', 'A2blb');
```

## this
`this` je v JS řízena kontextově (dle scope/uzávěru). Čili v `this` je ten, kdo danou funkci vyvolal:

```
------------ window --------------------------------------
|                                          / \           |
|                                           |            |
|                                          this          |
|   ----------------                        |            |
|   | HTML element | <-- this         -----------------  |
|   ----------------      |           | doSomething() |  |
|               |         |           -----------------  |
|          --------------------                          |
|          | onclick property |                          |
|          --------------------                          |
|                                                        |
----------------------------------------------------------
```
To je zcela pochopitelné pro funkce pracující s DOMem.
Již poněkud méně pro soustavu funkcí, které jsou podobné OOP.
 * [podrobnější vysvětlení](http://www.quirksmode.org/js/this.html)

Pokud chceme udržet `this` na očekávané hodnotě nadřazeného objektu, tak použijeme trik s definici: `var self = this`, anebo mnohem systémověji (v novějích verzích) `bind`.

Bind je funkce, která naší funkci obalí. Čili máme funkci:
```js
var pi = 3; // wrong value

function A() {
        this.pi = 3.14;
        this.circumference = function(radius) {
                return this.pi * radius * 2;
        };
};

var a = new A();
var c1 = a.circumference(1);
var c2 = a.circumference(1).bind(a);
```

* [bind na MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)


## Výjimky
Vyhodit lze jakýkoliv typ.

```js
try {
        throw "siome string";
        throw {
                name: "Some error",
                code: 1,
                message: "..."
        }
} catch(ex if condition) {

} catch(ex) {

} finaly {

}
```

## Std. objekty

* Math: konstanty, `min`, `max`
* Date: vytvoření, formátování data
* Number: `MAX_VALUE`, `MIN_VALUE`, ...
* String: `length`, `replace`, `toLowerCase`, `trim`, ...

## Debuging
Jednou z možností je použít doplněk pro Firefox Firebug. Zde na panelu `konzole > chyby` vidíme chyby, které nahlasí javascript.

Užitečný je též příkaz `console.log()`, který do konzole ve Firebugu vypíše argument(y). Popřípadě `console.table()`.

## Frameworks

* [Underscore](http://underscorejs.org/): base library of most important function for functional programming.
* [Knockout](knockout.md): event driven MVVM library
* [JQuery](http://jquery.com/)`
* [Angular](https://angularjs.org/)
* [Require](http://requirejs.org/): dependency managment in js
