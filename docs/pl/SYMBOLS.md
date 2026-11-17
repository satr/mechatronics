# Symbole i notacja matematyczna

**Języki:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](SYMBOLS.md)

**Jednostki używane na tej stronie (wyjaśnione przed przykładami):** `s` — sekunda; `mm` — milimetr; `mm/s` — milimetr na sekundę; `kg·m²` — moment bezwładności; `N·m` — moment siły; `N·m·s/rad` — współczynnik momentu względem prędkości kątowej; `rpm` — obroty na minutę (poza SI); `rad/s` — prędkość kątowa w radianach na sekundę; `%` — procent. [Pełny słownik jednostek](UNITS.md).

[Spis treści](README.md) · [Ściąga ze wzorami](CHEATSHEET.md) · [Ruch](notes/01-motion-calculus.md) · [Dynamika](notes/02-first-order-dynamics.md)

## Spis treści

- [Sumowanie — wielka sigma](#summation)
- [Łatwo mylone symbole](#different-symbols)
- [Zapis matematyczny w Markdown](#math-delimiters)
- [Separator dziesiętny, SI i odstępy](#si-notation)

<a id="summation"></a>

## Σ / ∑ — sumowanie (summation)

Symbol $\sum$ (wielka grecka litera **sigma**) oznacza dodawanie kolejnych składników. W zapisie $\sum_{n=0}^{N-1}(2nh)h$ indeks $n$ przyjmuje wartości $0; 1; \ldots; N-1$, czyli mamy $N$ składników. Możesz wyobrazić sobie pętlę Pythona `for`, która dodaje do sumy następny wyraz. Przykład: $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Podobnie wyglądające symbole mają różne znaczenia

Mała litera $\varepsilon(t)$ (epsilon) oznacza błąd prędkości (speed error), a prosta litera $\mathrm{e}\approx2.71828$ — liczbę Eulera. $\tau$ (tau) jest stałą czasową, $\omega$ (omega) — prędkością kątową, $\alpha$ (alfa) — przyspieszeniem kątowym, a $\Delta$ (delta) oznacza zmianę. Mała $\sigma$ (sigma) może w innych zagadnieniach oznaczać odchylenie standardowe lub naprężenie. Zawsze odczytuj znaczenie z definicji w danym rozdziale.

<a id="math-delimiters"></a>

## Dlaczego widać znaki dolara?

W **źródłowym** Markdown fragment `$...$` oznacza wzór w linii tekstu, a `$$...$$` na osobnych liniach — blok matematyczny. Znaki dolara nie należą do wzoru i nie powinny być widoczne w wyrenderowanej stronie GitHub. Gdy się pojawiają, sprawdź, czy nie przeglądasz kodu źródłowego albo czy składnia wzoru nie została uszkodzona. Tekst odnośników nawigacyjnych pozostaje zwykłym tekstem.

[Dokumentacja matematyki GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Liczby dziesiętne, jednostki SI i odstępy

We wszystkich edycjach używamy **kropki** dziesiętnej: `0.5`, `3.8`, `63.2 %`. Między wartością a symbolem jednostki stosuj odstęp: `1 s`, `4 mm`, `10 mm/s`. Iloczyn jednostek zapisujemy kropką środkową `·`, np. `kg·m²` i `N·m·s/rad`, bez odstępów wokół ukośnika. Kropka środkowa oznacza mnożenie, nie część dziesiętną. `1 N·m` to jeden niutonometr. We wzorach stosuj `\mathrm{kg}\cdot\mathrm{m}^2` oraz różniczkę `\mathrm{d}t` zamiast mylącego zapisu z przecinkiem. Pojęcie `dt` w Pythonie oznacza *skończony krok czasowy*, natomiast `\mathrm{d}t` pod całką oznacza różniczkę matematyczną. Zobacz [broszurę BIPM o SI](https://www.bipm.org/en/publications/si-brochure).

### rpm i rad/s

`rpm` (revolutions per minute) to **obroty na minutę**, jednostka często spotykana, ale **spoza SI**. Prędkość kątowa w SI jest wyrażana w `rad/s` (radianach na sekundę): `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`, zatem `1000 rpm ≈ 104.72 rad/s`.
