# Símbolos y notación

**Leer esta página en:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidad lineal; `kg·m²` — kilogramo · metro² — momento de inercia; `N·m` — newton · metro — par de torsión; `N·m·s/rad` — newton · metro · segundo / radián — ganancia por velocidad; `rpm` — revolución por minuto; `rad/s` — radián / segundo — velocidad angular; `%` — por ciento (una centésima parte). [Glosario de unidades](UNITS.md).

[← README](README.md) · [Resumen de fórmulas](CHEATSHEET.md) · [Movimiento](notes/01-motion-calculus.md) · [Dinámica](notes/02-first-order-dynamics.md)

## Índice

- [Sumatorio: sigma mayúscula](#summation)
- [Símbolos que pueden confundirse](#different-symbols)
- [Notación matemática en Markdown](#math-delimiters)
- [Punto decimal, unidades SI y espacios](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Sumatorio

El símbolo $\sum$ (sigma mayúscula griega, **sumatorio** / summation) indica que se suman varios términos. En $\sum_{n=0}^{N-1}(2nh)h$, el índice $n$ recorre $0; 1; \ldots; N-1$: hay $N$ sumandos. Es equivalente a un bucle `for` de Python que acumula valores. Por ejemplo, $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Símbolos parecidos con significados distintos

La letra $\varepsilon(t)$ (épsilon) representa el error de velocidad; la constante $\mathrm{e}\approx2.71828$ es el número de Euler. $\tau$ (tau) es la constante de tiempo, $\omega$ (omega) la velocidad angular, $\alpha$ (alfa) la aceleración angular y $\Delta$ (delta) un cambio. La letra $\sigma$ minúscula (sigma) es otro símbolo cuyo significado depende del contexto.

<a id="math-delimiters"></a>

## ¿Por qué aparecen signos de dólar?

En el código fuente Markdown, `$...$` delimita fórmulas dentro de una línea y `$$...$$` fórmulas independientes. No forman parte de la matemática y deberían desaparecer en la vista renderizada de GitHub. Si aparecen, comprueba la vista del archivo, las etiquetas de los enlaces y la sintaxis Markdown.

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Punto decimal, unidades SI y espacios

Escribimos todos los decimales con punto: `0.5`, `3.8`, `63.2 %`, también en español. Una coma puede separar elementos de una lista, pero no una cantidad de su unidad ni el integrando de `dt`. Dejar un espacio entre número y símbolo: `1 s`, `4 mm`, `10 mm/s`. El punto centrado `·` multiplica unidades (`kg·m²`, `N·m·s/rad`); no dejar espacios alrededor de `/` (`mm/s`). En ecuaciones escribir `\mathrm{kg}\cdot\mathrm{m}^2` y el diferencial `\mathrm{d}t`. El punto decimal está permitido por el [folleto del SI del BIPM](https://www.bipm.org/en/publications/si-brochure). `dt` en el programa es un intervalo finito, pero `\mathrm{d}t` en una integral es un diferencial.


### rpm and rad/s

`rpm` significa **revoluciones por minuto** (revolutions per minute), una unidad **no SI**. La velocidad angular en el SI se expresa en `rad/s` (radians per second): `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`; por tanto `1000 rpm ≈ 104.72 rad/s`.