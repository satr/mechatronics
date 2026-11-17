# Symbole und Schreibweise

**Diese Seite lesen auf:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `s` — Sekunde; `mm` — Millimeter = 0.001 m; `mm/s` — Millimeter / Sekunde — lineare Geschwindigkeit; `kg·m²` — Kilogramm · Meter² — Trägheitsmoment; `N·m` — Newton · Meter — Drehmoment; `N·m·s/rad` — Newton · Meter · Sekunde / Radiant — Verstärkung pro Geschwindigkeit; `rpm` — Umdrehung pro Minute; `rad/s` — Radiant / Sekunde — Winkelgeschwindigkeit; `%` — Prozent (ein Hundertstel). [Einheitenverzeichnis](UNITS.md).

[← README](README.md) · [Formelübersicht](CHEATSHEET.md) · [Bewegung](notes/01-motion-calculus.md) · [Dynamik](notes/02-first-order-dynamics.md)

## Inhalt

- [Summenzeichen: großes Sigma](#summation)
- [Verwechslungsgefahr bei Symbolen](#different-symbols)
- [Mathematik in Markdown](#math-delimiters)
- [Dezimalpunkt, SI-Einheiten und mathematische Abstände](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Summe

Das Zeichen $\sum$ (großes griechisches Sigma, **Summenzeichen** / summation) bedeutet: Terme addieren. In $\sum_{n=0}^{N-1}(2nh)h$ durchläuft der Index $n$ die Werte $0; 1; \ldots; N-1$: insgesamt $N$ Terme. Das entspricht einer Python-`for`-Schleife, die die Beiträge aufsummiert. Beispielsweise gilt $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Ähnliche Zeichen, unterschiedliche Bedeutungen

Das kleine $\varepsilon(t)$ (Epsilon) steht für den Geschwindigkeitsfehler; die Konstante $\mathrm{e}\approx2.71828$ ist die Euler-Zahl. $\tau$ (Tau) ist die Zeitkonstante, $\omega$ (Omega) die Winkelgeschwindigkeit, $\alpha$ (Alpha) die Winkelbeschleunigung; $\Delta$ (Delta) bezeichnet eine Änderung. Das kleine $\sigma$ (Sigma) ist ein anderes Symbol und muss je nach Kontext definiert werden.

<a id="math-delimiters"></a>

## Warum werden Dollarzeichen angezeigt?

Im Markdown-Quelltext markiert `$...$` eine Formel im Satz und `$$...$$` eine abgesetzte Formel. Die Zeichen gehören nicht zur Mathematik und sollten in der gerenderten GitHub-Ansicht verschwinden. Sichtbare Zeichen können auf Quelltextansicht, mathematische Ausdrücke in Links oder fehlerhafte Markdown-Syntax hinweisen.

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Dezimalpunkt, SI-Einheiten und mathematische Abstände

In allen Sprachfassungen steht ein Dezimalpunkt: `0.5`, `3.8`, `63.2 %`, auch wenn im Deutschen sonst das Komma üblich ist. Ein Komma trennt Listeneinträge, aber nie Wert und Einheit oder den Integranden und `dt`. Zwischen Zahl und Einheit steht ein Leerzeichen (`1 s`, `4 mm`, `10 mm/s`). Bei zusammengesetzten Einheitensymbolen bezeichnet `·` die Multiplikation (`kg·m²`, `N·m·s/rad`); neben `/` steht kein Leerzeichen (`mm/s`). In Gleichungen schreiben wir `\mathrm{kg}\cdot\mathrm{m}^2` und das Differential `\mathrm{d}t`. Dies entspricht der erlaubten Punkt-Schreibweise der [BIPM-SI-Broschüre](https://www.bipm.org/en/publications/si-brochure). Das `dt` im Programm ist ein endlicher Zeitschritt, `\mathrm{d}t` im Integral ein Differential.


### rpm and rad/s

`rpm` bedeutet **Umdrehungen pro Minute** (revolutions per minute). Das ist **keine** SI-Einheit. Die SI-Einheit der Winkelgeschwindigkeit ist `rad/s` (radians per second): `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`, also `1000 rpm ≈ 104.72 rad/s`.