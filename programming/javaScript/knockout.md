# Knockout.js

* Globální objekt `ko`
* Model je funkce (co jiného), kterou zaregistrujeme pomocí: `ko.applyBindings(new AppViewModel);`
* Šablony tvoříme přímo v html pomocí atributu `data-bind`, v něm řetězíme jednotlivé bindy. Např.: `data="text: someVar, enable: someBool"`

## Links
* http://knockoutjs.com
* http://www.knockmeout.net
* [ko.utils functions (3.1)](https://gist.github.com/hyle/9363349)

## Observable

## Binding

### visible
Jako argument bere boolean proměnnou. Pokud je true element se zobrazí.

### text
Zobrazí v elementu text dané proměnné. Html je ošetřeno.

### html
Jako text, ale interpretuje i html.

### css
Vkládá css třídy.

### attr
Vkládá atributy

## Cykly

### Foreach
Mějme proměnnou `items`, která je pole. Položky mají vlastnost `name`. Ve forcyklu máme dvě speciální proměnné `$index` a `$data` (aktuální objekt) . Např.:

```
<ul data-bind="foreach: items">
        <li data-bind="text: name"></li>
</ul>
```

```
<ul data-bind="foreach: { data: items, as: 'item' }">
        <li data-bind="text: item.name"></li>
</ul>
```

Lze iterovat i bez elementu:
```
<!-- ko foreach: myItems -->
        <li>Item <span data-bind="text: $data"></span></li>
<!-- /ko -->
```

