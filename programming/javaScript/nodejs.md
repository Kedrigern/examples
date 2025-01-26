#Node

Vysoce asynchroní dialekt javascriptu.

##Moduly

```javascript
var http = require('http');
var myModule = require('./myModule.js');
```

Ukázka modulu:
```javascript
var somethink = ""; // internal variable

exports.getSomethink = function() {	// public function
};
```

##Scope

Zůstává stejný jako v js, akorát moduly mají vlastní. Čili je třeba definovat proměnné s var, aby zůstaly lokální.

##npm

##Odkazy

* [Krátké shrnutí](http://code.tutsplus.com/tutorials/nodejs-for-beginners--net-26314)
* [Api 0.10.30](http://nodejs.org/docs/v0.10.30/api/)
