# Symboles et notation

**Lire cette page en:** [en](../en/SYMBOLS.md) · [fr](SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Unités utilisées ici (définies avant les exemples):** `s` — seconde; `mm` — millimètre = 0.001 m; `mm/s` — millimètre / seconde — vitesse linéaire; `kg·m²` — kilogramme · mètre² — moment d'inertie; `N·m` — newton · mètre — moment de force; `N·m·s/rad` — newton · mètre · seconde / radian — gain par unité de vitesse; `rpm` — tour par minute; `rad/s` — radian / seconde — vitesse angulaire; `%` — pour cent (un centième). [Glossaire des unités](UNITS.md).

[← README](README.md) · [Aide-mémoire](CHEATSHEET.md) · [Mouvement](notes/01-motion-calculus.md) · [Dynamique](notes/02-first-order-dynamics.md)

## Sommaire

- [Sommation : sigma majuscule](#summation)
- [Symboles faciles à confondre](#different-symbols)
- [Notation mathématique Markdown](#math-delimiters)
- [Point décimal, unités SI et espacement mathématique](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Somme

Le symbole $\sum$ (sigma majuscule grec, **sommation** / summation) signifie « additionner les termes ». Dans $\sum_{n=0}^{N-1}(2nh)h$, l’indice $n$ prend les valeurs $0; 1; \ldots; N-1$ : il y a $N$ termes. C’est comme une boucle Python `for` qui ajoute chaque contribution. Par exemple, $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Des symboles proches mais de sens différents

Le $\varepsilon(t)$ minuscule (epsilon) désigne l’erreur de vitesse ; la constante $\mathrm{e}\approx2.71828$ est le nombre d’Euler. $\tau$ (tau) est la constante de temps ; $\omega$ (oméga) est la vitesse angulaire ; $\alpha$ (alpha) est l’accélération angulaire ; $\Delta$ (delta) signifie une variation. Le $\sigma$ minuscule est encore un autre symbole ; sa signification dépend du contexte.

<a id="math-delimiters"></a>

## Pourquoi voit-on des signes dollar ?

Dans la source Markdown, `$...$` délimite une formule dans le texte et `$$...$$` une formule en bloc. Ces signes ne font pas partie des maths et ne devraient pas apparaître dans l’affichage GitHub. Leur apparition peut signaler le mode source, un lien contenant une formule, ou une erreur Markdown.

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Point décimal, unités SI et espacement mathématique

Dans tous les documents, écrire les décimales avec un point : `0.5`, `3.8`, `63.2 %`, même si la virgule est courante en français. La virgule sépare les éléments d’une liste, jamais un nombre de son unité ou de `dt`. Insérer un espace entre la valeur et le symbole : `1 s`, `4 mm`, `10 mm/s`. Multiplier les unités par un point médian (`kg·m²`, `N·m·s/rad`) et ne jamais ajouter d’espace autour de `/` (`mm/s`). Dans les équations, écrire `\mathrm{kg}\cdot\mathrm{m}^2` et la différentielle `\mathrm{d}t`. Le point décimal est autorisé par la [Brochure du SI du BIPM](https://www.bipm.org/en/publications/si-brochure). Le pas `dt` du programme est fini ; `\mathrm{d}t` représente la différentielle dans l’intégrale.


### rpm and rad/s

`rpm` signifie **tours par minute** (revolutions per minute). Ce n’est **pas** une unité SI. La vitesse angulaire en SI se mesure en `rad/s` (radians per second) : `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`, donc `1000 rpm ≈ 104.72 rad/s`.