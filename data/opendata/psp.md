
## NKOD

Zákon [106/1999](https://www.zakonyprolidi.cz/cs/1999-106) nařizuje otevřená data zveřejňovat v Národním katalogu otevřených dat (**NKOD**). Viz https://opendata.gov.cz/nastroj:narodni-katalog-otevrenych-dat

V případě potíží je nejjednodušší se obrátit na Michala Kubáně z MVČR, který je národním koordinátorem opendat.

## Formát

Kódování textu v **UTF-8**, starší kódování (CP1250) jsou zbytečné komplikace navíc. JSON to dokonce přímo vyžaduje.

Nejlepším formátem je **JSON**, jelikož je opravdu jednoduchý a v moderních webových aplikacích se s ním pracuje rovnou. XML má velký overhead (strašně moc znaků) a díky tomu je méně přehledné. Samozřejmě i **XML** je lepší něž nic.

Dobrou praxí je také do url uvést číslo verze API. Důvodem je, abychom mohli měnit obsah / strukturu dat, ale nerozbili jsme zpětnou kompatibilitu (čili např. 2 verze API fungují současně). Např.: `http://www.psp.cz/sqw/detail.sqw?id=6526&o=8&l=cz&format=json&version=0.1`

## Co zveřejnit (seznam)

- sněmovní tisky
  - výpis s odkazy na dokumenty
  - existuje již [RSS](http://www.psp.cz/rss/tisky.rss)
  - RSS ne vždy má celou historii, lze udělat i RSS se stránkováním
  - ale spíš bych udělal vedle XML výpis ve stejném formátu
- hlasování
  - obdobně jako na webu
  - [standard popolo](http://www.popoloproject.com/specs/motion.html)
  - [příklad JSON dle popolo](./motion_example.json)
- výpis poslanců: prostý výpis s odkazy
  - profil poslance:
    - [standard popolo](http://www.popoloproject.com/specs/person.html)
    - [příklad JSON dle popolo](./person_example.json)
    - rozcestník ala: http://www.psp.cz/sqw/detail.sqw?id=6526
    - funkce: členství ve výborech, podvýborech, komisích a delegacích
    - předkladatel tisků / zákonů
    - zpravodajované tisky / zákony
    - písemné pozměňovací návrhy
    - ústní interpelace
    - řeč ve sněmovně

## Příklady

### Sněmovní tisky

tisky.xml, vychází z RSS:

```XML
<?xml version="1.0" encoding="utf-8"?>
<title>Sněmovní tisky</title>
<description>Vypisuje sněmovní tisky.</description>
<language>cs</language>
<copyright>Copyright 2006 ČR - Kancelář Poslanecké sněmovny</copyright>
<webMaster>wwwadm@psp.cz (wwwadm@psp.cz)</webMaster>
<tisky>
  <item>
    <title>112/7 Záznam VEZ k tisku 112/0</title>
    <description>Záznam výboru pro evropské záležitosti č. 107 ze dne 20. června 2018 k návrhu poslanců Vojtěcha Filipa, Pavla Kováčika, Miloslavy Vostré, Stanislava Grospiče a Květy Matušovské na vydání zákona o zrušení zákona č. 99/2000 Sb., o zákazu dodávek pro jadernou elektrárnu Búšehr</description>
    <link>http://www.psp.cz/sqw/historie.sqw?o=8&amp;t=112&amp;rss-cz=7</link>
    <guid>http://www.psp.cz/sqw/historie.sqw?o=8&amp;t=112&amp;rss-cz=7</guid>
    <pubDate>Fri, 22 Jun 2018 12:02:00 GMT</pubDate>
  </item>
  <item>
    <title>212/0 Novela z. - zákoník práce</title>
    <description>Návrh poslance Aleše Juchelky a dalších na vydání zákona, kterým se mění zákon č. 262/2006 Sb., zákoník práce, ve znění pozdějších předpisů, a další související zákony</description>
    <link>http://www.psp.cz/sqw/historie.sqw?o=8&amp;t=212&amp;rss-cz=0</link>
    <guid>http://www.psp.cz/sqw/historie.sqw?o=8&amp;t=212&amp;rss-cz=0</guid>
    <pubDate>Fri, 22 Jun 2018 10:56:00 GMT</pubDate>
  </item>
</tisky>
```

### Poslanci

poslanci.xml:

```XML
<?xml version="1.0" encoding="utf-8"?>
<poslanci>
  <poslanec name="Ondřej" surname="Profant" club="Piráti">
    <vybory>
      <clen type="vybor">VVSRR</clen>
      <clen type="podvybor">Esbírka</clen>
    </vybory>
    <link name="předkladatel ST" url="">
    <link name="zpravodaj ST" url="">
    <link name="písemně poddané PN" url="">
    <link name="projevy" url="">
  </poslanec>
</poslanci>
```
