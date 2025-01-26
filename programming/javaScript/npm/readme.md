# npm

Je systém pro správu závislostí v `js` světě. Řeší backend závislosti. Resp. celý ekosystém server-side javascriptu.

Ve složce projektu zadáme: `npm init` a aplikace nás provede důležitými nastaveními(jméno projektu, licence etc.). To vše zapíše do souboru `package.json`.

Mnoho věcí můžeme nastavit globálně:
```
npm set init.author.email "wombat@npmjs.com"
npm set init.author.name "ag_dubs"
npm set init.license "MIT"
```

Npm samozřejmě umí vyhledávat `npm search <package>`. Moduly (balíčky) instaluje lokálně do složky `node_modules` (nezapomenout přidat do `.gitignore`).

# Bower

Řeší závislosti frontend (jquery etc).

```
npm install -g bower
```

Instaluje do složky `bower_components`.


# Gulp

Rychlý systém pro buildování (správu zavislostí řeší `npm`). Je alternativou např. ke `grunt`u.

Využívá noje.js streams a díky tomu nevytváří lokální soubory.

## Instalace

```
npm install gulp -g
```

[gulp quickstart][]

[gulp quickstart]: https://markgoodyear.com/2014/01/getting-started-with-gulp/

