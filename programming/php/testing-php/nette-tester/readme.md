#Testing aplikací v nette/tester 

Tento postup je použit pro testování projektu samotného. Více informací v [repositářích](https://github.com/nette/tester). 
Potřebné soubory jsou v DB struktuře.

  1. v Ubuntu 12.10 jsem potřeboval doinstalovat balík: `php5-cgi`
  1. `composer create-project nette/sandbox ntest`
  1. `sudo chown -R <user>:www-data ntest/ && chmod -R 775 ntest/ # nastavení přístupových práv`
  1. `cd ntest # přesuneme se do adresáře projektu`
  1. `composer update --dev # nainstalujeme vývojářské závislosti`
  1. vytvoříme lehce testovatelný model `prime.php` (kód dále)
  1. vytvoříme unit test `PrimeTest.phpt` (kód dále)
  1. připravíme `bootstrap.php` pro unit testy (kód dále)
  1. testy spustíme v rootu projektu: `php libs/nette/tester/Tester/tester.php tests/`

Když nám toto funguje, tak doplníme ještě `PrimeTest2.phpt`, kde je zápis testů podobnější PHPunit (a obecně unit testing frameworkům).

Objevila se nějaká chyba s PDO, stačilo v configu zakomentovat vše, co se týká DB.

##Testování presenterů

##Integrační testy


##Odkazy
* [Nette tester a PHPstorm](http://filip-prochazka.com/blog/nette-tester-a-phpstorm)
* [TDD v Nette](http://blog.satera.cz/2012/test-driven-development-v-nette/)
* [Testování presenterů](http://phpfashion.com/velestrucne-testovani-presenteru-v-nette) [(forum)](http://forum.nette.org/cs/14270-testovani-presenteru-v-nette-tester)
* [Slidy](http://www.slideshare.net/mediocz/testovn-presenter-v-nette)
* [Praktická ukázka](https://github.com/nette/nette/tree/master/tests/Nette/Database)
* [Zprovoznění přípony phpt v Apache](http://bytes.com/topic/apache/answers/614224-how-add-new-file-extension-phpt-apache)
