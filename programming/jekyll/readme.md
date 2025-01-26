# Jekyll

Je aplikace napsaná v ruby, která z předdefinovaných šablon vygeneruje statickou
stránku. Tím pádem dovoluje tvořit i trochu složitější weby (např. blogy,
firemní prezentace) bez nutnosti jakýhkoliv nároků na hosting. Navíc je nativně
podporován Github pages, čili vše můžete hostovat na Githubu.

## Github pages

## Struktura

```
├── about.md                -- statická stránka
├── _config.yml             -- konfigurační soubor
├── css                         
│   └── main.scss
├── feed.xml                -- atom feed             
├── _includes               -- snippety stránky
│   ├── footer.html         -- patička stránky
│   ├── header.html         -- hlavička stránky
│   └── head.html           -- meta hlavička stránky
├── index.html              
├── _layouts                -- různé druhy layoutů
│   ├── default.html
│   ├── page.html
│   └── post.html
├── _posts                  -- příspěvky v markdown s metadaty
│   ├── people-ondrej-profant.md
│   ├── 2016-02-12-another-post.md
│   └── 2016-02-13-welcome-to-jekyll.md
├── _sass
│   ├── _base.scss
│   ├── _layout.scss
│   └── _syntax-highlighting.scss
└── _site                   -- zkompilovaná stránka
```

[Dokumentace](http://jekyllrb.com/docs/structure/)

## Liquid

Dva typy závorek:

`{{ x }}` - vyhodnotí se na text (output)

`{% if %}` - syntax (tagy)

Příklad outputu:

```
Hello {{name}}
Hello {{user.name}}
Hello {{ 'tobi' }}
Hello {{ 'tobi' | upcase }}
Hello tobi has {{ 'tobi' | size }} letters!
Hello {{ '*tobi*' | textilize | upcase }}
Hello {{ 'now' | date: "%Y %h" }}
```
Tagy:

- `assign` - Assigns some value to a variable:
    ```
    assign item = site.tags["featured"].first
    ```
- `capture` - Block tag that captures text into a variable
- `case` - Block tag, its the standard case...when block
- `comment` - Block tag, comments out the text in the block
- `cycle` - Cycle is usually used within a loop to alternate between values, like colors or DOM classes.
- `for` - For loop
- `break` - Exits a for loop
- `continue` Skips the remaining code in the current for loop and continues with the next loop
- `if` - Standard if/else block
- `include` - Includes another template; useful for partials
- `raw` - temporarily disable tag processing to avoid syntax conflicts.
- `unless` - Mirror of if statement

[Více](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)

### Cykly

- [Rozdělení cyklu na dvojice](http://stackoverflow.com/questions/20924471/for-loop-wrap-every-two-posts-in-a-div)
- [Sudé/liché položky](http://stackoverflow.com/questions/8980192/liquid-templates-even-odd-items-in-for-loop)

## Vlastní kolekce

Pozor: Jedná se o nestabilní API.

Jedná se o vlsatní

[Dokumentace](http://jekyllrb.com/docs/collections/)

## Tipy

### Vypsání jen určitých kategorii

```html
<ul class="posts">
{% for post in site.posts %}
    {% if post.categories contains 'demography' %}
        <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
```
