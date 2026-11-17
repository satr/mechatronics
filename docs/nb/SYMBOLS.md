# Symboler og notasjon

**Les denne siden på:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `kg·m²` — kilogram · meter² — treghetsmoment; `N·m` — newton · meter — dreiemoment; `N·m·s/rad` — newton · meter · sekund / radian — forsterkning per hastighet; `rpm` — omdreining per minutt; `rad/s` — radian / sekund — vinkelhastighet; `%` — prosent (en hundredel). [Enhetsoversikt](UNITS.md).

[← README](README.md) · [Formelark](CHEATSHEET.md) · [Bevegelse](notes/01-motion-calculus.md) · [Dynamikk](notes/02-first-order-dynamics.md)

## Innhold

- [Summering: stor sigma](#summation)
- [Symboler som kan forveksles](#different-symbols)
- [Matematikk i Markdown](#math-delimiters)
- [Desimalpunkt, SI-enheter og avstand](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Summasjon

Symbolet $\sum$ (stor gresk sigma, **summasjon** / summation) betyr at ledd skal legges sammen. I $\sum_{n=0}^{N-1}(2nh)h$ går indeksen $n$ gjennom $0; 1; \ldots; N-1$: totalt $N$ ledd. Tenk på en Python-`for`-løkke som legger til hvert bidrag. For eksempel er $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Like symboler kan ha ulik betydning

Den lille $\varepsilon(t)$ (epsilon) betegner hastighetsfeilen; konstanten $\mathrm{e}\approx2.71828$ er Eulers tall. $\tau$ (tau) er tidskonstanten, $\omega$ (omega) vinkelhastigheten, $\alpha$ (alfa) vinkelakselerasjonen og $\Delta$ (delta) en endring. Liten $\sigma$ (sigma) er et annet symbol og må defineres for hver sammenheng.

<a id="math-delimiters"></a>

## Hvorfor vises dollartegn?

I Markdown-kilden markerer `$...$` matematikk i teksten og `$$...$$` en egen matematikklinje. De er ikke del av uttrykket og skal normalt ikke vises på GitHub. Hvis de vises, kontroller kildevisning, lenketekst med formler og feil i Markdown.

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Desimalpunkt, SI-enheter og avstand

Vi bruker desimalpunkt i alle språkversjoner: `0.5`, `3.8`, `63.2 %`, selv om komma er vanlig på norsk. Komma kan skille listeledd, men skal ikke stå mellom tall og enhet eller integrand og `dt`. Bruk mellomrom mellom tall og enhet: `1 s`, `4 mm`, `10 mm/s`. Midtstilt punkt `·` markerer multiplikasjon av enheter (`kg·m²`, `N·m·s/rad`); ingen mellomrom ved `/` (`mm/s`). I formler bruker vi `\mathrm{kg}\cdot\mathrm{m}^2` og differensialen `\mathrm{d}t`. Desimalpunktet er tillatt i [BIPMs SI-brosjyre](https://www.bipm.org/en/publications/si-brochure). `dt` i et program er et endelig tidssteg; `\mathrm{d}t` i et integral er en differensial.


### rpm and rad/s

`rpm` betyr **omdreininger per minutt** (revolutions per minute), en vanlig **ikke-SI-enhet**. SI-enheten for vinkelhastighet er `rad/s` (radians per second): `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`; altså `1000 rpm ≈ 104.72 rad/s`.