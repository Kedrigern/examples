#Testing aplikací v PHP

##Tahák
V správně připraveném Nette projektu s Dibi: `./libs/bin/phpunit --colors --no-globals-backup tests/*`

##Terminologie

* unit test - test jednotky: typicky testujeme jednu třídu. Tyto testy jsou nenáročné, krásně izolované, ale upozorňují především na regresní chyby (omylem překopeme API).
* integrační test: test, který zkoumá součinost částí kódu (např. modelu) s externími zdroji (DB, filesystem, ale i rozsáhlejší programová API). 

Velmi dobře vše shrnuje [seriál](http://www.zdrojak.cz/serialy/testovani-a-tvorba-testovatelneho-kodu-v-php) na [zdrojak.cz](http://www.zdrojak.cz). Který krom teorie podrobně rozebírá phpunit.

##Nette a PHPunit

###Instalace a úprava Nette
Přes composer dodáme do `require-dev`:
```json
    "require-dev": {
        "phpunit/phpunit": "3.7.*",
        "phpunit/dbunit": ">=1.2"
    }
```

Dále potřebujeme zajisti, aby se nám Nette nespustilo, ale pouze načetlo. Čili ```$container->application->run();```
nahradíme za:

```php
if (! \Nette\Environment::isConsole()) {        // condition for integration tests
	$container->application->run();
}
```

(pokud je Nette spuštěno z konzole, tak nespustíme `run()`.

Dále se musíme postarat o to, aby nám robotloader nenačítal phpunit a spol, neb to nechceme (a bude to dělat bordel). To zajistíme přidáním soubory `netterobots.txt` do adresáře `libs`:

```
Disallow: /phpunit
Disallow: /symfony
```

###Základní použití
Díky composeru jsme phpunit nainstalovali lokálně, čili bude ve `vendor/bin` resp. v Nette v `lib/bin`. Testy tedy normálně spustíme z cmd (jsme v rootu projektu):

```bash
phpunit ./lib/bin/phpunit tests/*
```

Dobré je přidat parametr `--colors` pro obarvený výstup. Pokud pracujeme s Dibi, tak je třeba přidat i `--no-globals-backup`, neb Dibi se brání serializaci, kterou jinak phpunit dělá.

###Integrační testy
Na ty využijeme rozšíření DB unit. Bohužel neexistuje předpřipravené rozšíření pro naše typické DB wrappery (Dibi a Nette\Database). Proto budeme muset trochu improvizovat. Zde použijeme PDO pro kontrolu a naše normální Dibi spojení pro testing.

```php
// Loading of Nette (be carefoul not run it!)
require_once __DIR__ . "/../../www/index.php"; 

/**
 * Base class for integral testing of database
 */
abstract class BaseDb extends PHPUnit_Extensions_Database_TestCase
{
    /**
     * @var array
     */
    protected $postgres_option = array(
        'driver' => 'postgre',
        'host' => 'localhost',
        'user' => '',
        'password' => '',
        'dbname' => '',
        'charset' => 'UTF-8'
    );

    /**
     * @return PDO
     */
    protected function getPdo()
    {
        return new PDO("pgsql:host=;dbname=", "", "");
    }

    /**
     * @return PHPUnit_Extensions_Database_DB_DefaultDatabaseConnection|PHPUnit_Extensions_Database_DB_IDatabaseConnection
     */
    protected function getConnection()
    {
        return $this->createDefaultDBConnection( $this->getPdo() );
    }

    /**
     * @return PHPUnit_Extensions_Database_DataSet_DataSetFilter|PHPUnit_Extensions_Database_DataSet_IDataSet
     */
    protected function getDataSet()
    {
        throw new \Nette\NotImplementedException("getDataSet() must be implement");
    }
}

```

Samotná testovací třída bude vypadat takto:

```php
require_once __DIR__ . "/BaseDb.php";

/**
 * Integration test of log repository with is wrapper for cezar_log table in our DB
 */
class LogRepositoryTest extends BaseDb
{
    /**
     * @return PHPUnit_Extensions_Database_DataSet_DataSetFilter|PHPUnit_Extensions_Database_DataSet_IDataSet
     */
    protected function getDataSet()
    {
        $ds = $this->createXmlDataSet(__DIR__ . "/logDataSet.xml");

        $filterDataSet = new PHPUnit_Extensions_Database_DataSet_DataSetFilter($ds);
        $filterDataSet->addIncludeTables(array('cezar_log'));

        return $filterDataSet;
    }

    public function testInitialDataCount()
    {
        $con = new \DibiConnection ( $this->postgres_option );
        $repository = new \Carty\Pairing\LogRepository($con);

        $this->assertSame(2, $repository->count('all') );
        //$this->assertSame(1, $repository->Count('success') );
        //$this->assertSame(1, $repository->Count('error') );
        $this->assertSame(1, $repository->getCritical() );
    }

    public function testInitialDataId()
    {
        $con = new \DibiConnection ( $this->postgres_option );
        $repository = new \Carty\Pairing\LogRepository($con);

        $item = $repository->Get(1);

        $this->assertEquals( 1, $item->id, '');
        $this->assertEquals( 'success', $item->type, '' );
        $this->assertEquals( 'test', $item->modul, '' );
    }

    public function testDeleteDate()
    {
        $con = new \DibiConnection ( $this->postgres_option );
        $repository = new \Carty\Pairing\LogRepository($con);

        $this->assertSame(2, $repository->count('all') );

        $repository->Delete(1);

        $this->assertSame(1, $repository->count('all') );
    }
}

```

Ještě jsme použili soubor s cvičnými daty:
```xml
<?xml version="1.0" ?>
<dataset>
    <table name="cezar_log">
        <column>id</column>
        <column>type</column>
        <column>text</column>
        <column>modul</column>
        <column>produkty_id</column>
        <column>cezar_id</column>
        <column>user_id</column>
        <row>
            <value>1</value>
            <value>success</value>
            <value>Success 1 from testing</value>
            <value>test</value>
            <null />
            <null />
            <null />
        </row>
        <row>
            <value>2</value>
            <value>error</value>
            <value>Error 1 from testing</value>
            <value>test</value>
            <null />
            <null />
            <null />
        </row>
    </table>
</dataset>
```

###Testování presenteru

##Nette a Nette/tester

V samostatném adresáři.
