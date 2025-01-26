# Angular 2

Angular 2 je rozdílný oproti Angularu 1. Je psán v typescriptu, čili je silně typovaný a vychází z ES6. Organizačně rozlišuje pouze:

- komponenty (bývalé controllery): mají styl, šablonu a kód
- service (model): obvykle komunikují se světem (http, localfiles, složité transformace)
- samostatné třídy a intefaces (model): třídy a intefaces našeho modelu (User apod)

Struktura je relativně složitá a míra provázanosti souborů velká a proto se používá angular-cli, což je cmd utilita, která nám pomáhá:

- vytvořit nový projekt `ng new [--minimal] [--skip-tests] [--skip-git] [--routing] <name>`
- běh aplikace `ng serve [-o]`
- kompilaci aplikace pro produkci `ng build`
- přidat komponentu: `ng generate component [--inline-template] [--inline-style] <name> `
- přidat service `ng generate service <name>`
- nápověda `ng help <cmd>`
- apod

Velmi dobrý [tutorial][] a [cheat sheet][]. Podrobnější vysvětlení [http][http example]. Jsony pro vývoj je možné umístit do složky `assets` a následně jsou po `ng serve` přístupné.[^1]

## Základy

Instalace: `npm install -g @angular/cli`, projekt vygenerujeme: `ng new --minimal --skip-test <name>`
```
[keddie@localhost min]$ tree --filelimit 10
.
├── node_modules [622 entries exceeds filelimit, not opening dir]
├── package.json
├── src
│   ├── app
│   │   ├── app.component.ts
│   │   └── app.module.ts
│   ├── assets
│   ├── environments
│   │   ├── environment.prod.ts
│   │   └── environment.ts
│   ├── index.html
│   ├── main.ts
│   ├── polyfills.ts
│   ├── styles.css
│   ├── tsconfig.app.json
│   └── typings.d.ts
└── tsconfig.json
```

`Index.html`: Vstupní bod aplikace. Uvedeme v něm speciální element `<app-root></app-root>`, ale ani v něm nelinkujeme styly a js. To vše za nás udělá ng. Při vývoji si aplikaci spustíme skrze `ng serve`, pro produkci ji vybuildíme skrze `ng build`.

`styles.css`: Globální styly, též můžeme vygnerovat SASS apod.

`app/app.module.ts`:

```ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [ AppComponent ], // where you declare the components and directives that belong to the current module.
  imports: [ BrowserModule ], // where you declare your module dependencies, for instance, browser, forms, routing or http.
  providers: [],
  bootstrap: [ AppComponent ] // that identifies the root component that Angular 2 should use to bootstrap your application.
})
export class AppModule { }
```

`app/app.component.ts`, `app/app.component.html`, `app/app.component.css`: Logika a šablony komponenty. Šablony mohou být i inline.

```ts
import { Component } from '@angular/core';

@Component({                            // decorátor s metadaty pro třídu AppComponent
  selector: 'app-root',                 // speciální element pro použití v šablonách
  templateUrl: './app.component.html',  // pomocí `` můžeme definovat i inline
  styleUrls: ['./app.component.scss']   // pomocí `` můžeme definovat i inline
})
export class AppComponent implements OnInit {
  title = 'app works!';                 // proměnná použitelná v šabloně pomocí {{title}}

  constructor() {}
  ngOnInit() {}
}
```

## Předávání proměnných mezi komponentami

V nadřazené komponntě: `<app-person-details [person]="selectedPerson"></app-person-details>`

V odkazované komponentě:

```ts
import { Component, Input } from '@angular/core'; // přidáme

export class PersonDetailsComponent {
  // decorator
  @Input() person : Person;
}
```

## Získávání dat

Můžeme použít 2 patterny - observable nebo promise.

`http.get()` nám vždy vrátí `Observable<Response>`


[^1]: Pokud chcete větší izolaci (např. nechcete, aby se vám data motala v aplikaci), ale tak doporučuji lokální [json server][], který nám data (primárně jsony) dodá.

[tutorial]: https://www.barbarianmeetscoding.com/blog/2016/03/25/getting-started-with-angular-2-step-by-step-1-your-first-component/
[cheat sheet]: https://www.cheatography.com/gregfinzer/cheat-sheets/angular-2/
[http example]: http://www.concretepage.com/angular-2/angular-2-http-get-example
[combine streams]: http://www.syntaxsuccess.com/viewarticle/combining-multiple-rxjs-streams-in-angular-2.0
[json server]: https://github.com/typicode/json-server
