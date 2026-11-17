# Simboli e notazione

**Leggi questa pagina in:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Unità usate qui (spiegate prima degli esempi):** `s` — secondo; `mm` — millimetro = 0.001 m; `mm/s` — millimetro / secondo — velocità lineare; `kg·m²` — chilogrammo · metro² — momento d'inerzia; `N·m` — newton · metro — momento torcente; `N·m·s/rad` — newton · metro · secondo / radiante — guadagno per unità di velocità; `rpm` — giro al minuto; `rad/s` — radiante / secondo — velocità angolare; `%` — percento (un centesimo). [Glossario delle unità](UNITS.md).

[← README](README.md) · [Formulario](CHEATSHEET.md) · [Moto](notes/01-motion-calculus.md) · [Dinamica](notes/02-first-order-dynamics.md)

## Indice

- [Sommatoria: sigma maiuscola](#summation)
- [Simboli che si possono confondere](#different-symbols)
- [Formule in Markdown](#math-delimiters)
- [Punto decimale, unità SI e spaziatura](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Sommatoria

Il simbolo $\sum$ (sigma maiuscola greca, **sommatoria** / summation) indica la somma di più termini. In $\sum_{n=0}^{N-1}(2nh)h$, l’indice $n$ assume i valori $0; 1; \ldots; N-1$: in totale $N$ termini. È come un ciclo Python `for` che accumula ogni contributo. Per esempio, $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Simboli simili, significati diversi

La lettera $\varepsilon(t)$ (epsilon) indica l’errore di velocità; la costante $\mathrm{e}\approx2.71828$ è il numero di Eulero. $\tau$ (tau) è la costante di tempo, $\omega$ (omega) la velocità angolare, $\alpha$ (alfa) l’accelerazione angolare e $\Delta$ (delta) una variazione. La $\sigma$ minuscola (sigma) è un simbolo diverso, da definire secondo il contesto.

<a id="math-delimiters"></a>

## Perché appaiono i segni del dollaro?

Nel sorgente Markdown, `$...$` delimita formule in linea e `$$...$$` formule separate. I delimitatori non fanno parte della matematica e non dovrebbero apparire nella pagina GitHub visualizzata. Se compaiono, controllare la vista del sorgente, i titoli dei link e la sintassi Markdown.

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Punto decimale, unità SI e spaziatura

Usiamo sempre il punto decimale: `0.5`, `3.8`, `63.2 %`, anche nelle traduzioni italiane. La virgola può separare elementi di un elenco, non il numero dalla sua unità né l’integrando da `dt`. Inserire uno spazio tra numero e unità: `1 s`, `4 mm`, `10 mm/s`. Nei simboli composti `·` indica la moltiplicazione (`kg·m²`, `N·m·s/rad`); nessuno spazio accanto a `/` (`mm/s`). Nelle equazioni usare `\mathrm{kg}\cdot\mathrm{m}^2` e il differenziale `\mathrm{d}t`. Il punto è ammesso dalla [Brochure SI del BIPM](https://www.bipm.org/en/publications/si-brochure). Nel codice `dt` è un passo finito; in un integrale `\mathrm{d}t` è il differenziale.


### rpm and rad/s

`rpm` indica i **giri al minuto** (revolutions per minute) e **non** è un’unità SI. La velocità angolare nel SI si esprime in `rad/s` (radians per second): `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`; quindi `1000 rpm ≈ 104.72 rad/s`.