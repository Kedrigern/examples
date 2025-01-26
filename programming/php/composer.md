# Composer

Composer je nástroj pro správu závislostí u webových projektů.

## Základní práce

### Vytvoření projektu
Obecně: `composer create-project <project> <local-name>` např:
`composer create-project nette/sandbox mySandbox`

### Update a install
`composer update`

`composer install`

### Update composeru
`composer self-update`

## composer.json
Konfigurační soubor projektu, např.:

```json
{
  "name": "nette/sandbox",
  "description": "The sandbox is a pre-packaged Nette Framework project, basic configured structure for your application.",
  "homepage": "http://nette.org",
  "license": ["BSD-3-Clause", "GPL-2.0", "GPL-3.0"],
  "authors": [
    {
      "name": "David Grudl",
      "homepage": "http://davidgrudl.com"
    },
    {
      "name": "Nette Community",
      "homepage": "http://nette.org/contributors"
    }
  ],
  "config": {
    "vendor-dir": "libs"
  },
  "require": {
    "php": ">= 5.3.0",
    "nette/nette": ">= 2.0.7"
  },
    "require-dev": {
        "nette/tester": "@dev"
  }
}
```

`vendor-lib` je složka použita pro knihovny. Default je `vendor`.

`require-dev` jsou závislosti pro vývojáře, např. pro unit testing, syntax checking etc. Pokud chceme nainstalovat i `dev` věci, tak je potřeba přidat přepínač `--dev`.

##Repozitáře
* [packagist.org](https://packagist.org) obsahuje např:
    * "phpunit/phpunit": "3.7.*"
    * "phpunit/dbunit": ">=1.2"
    * "nette/nette": "2.0.*"
    * "nette/tester": "@dev"
    * "dg/texy": "v2.2.*"
    * "dg/dibi": "v2.0.*"


