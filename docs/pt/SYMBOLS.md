# Símbolos e notação

**Ler esta página em:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `kg·m²` — quilograma · metro² — momento de inércia; `N·m` — newton · metro — binário (torque); `N·m·s/rad` — newton · metro · segundo / radiano — ganho por velocidade; `rpm` — rotação por minuto; `rad/s` — radiano / segundo — velocidade angular; `%` — percentagem (uma centésima parte). [Glossário de unidades](UNITS.md).

[← README](README.md) · [Resumo de fórmulas](CHEATSHEET.md) · [Movimento](notes/01-motion-calculus.md) · [Dinâmica](notes/02-first-order-dynamics.md)

## Índice

- [Somatório: sigma maiúsculo](#summation)
- [Símbolos que podem confundir](#different-symbols)
- [Notação matemática em Markdown](#math-delimiters)
- [Ponto decimal, unidades SI e espaçamento](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Somatório

O símbolo $\sum$ (sigma maiúsculo grego, **somatório** / summation) indica a adição dos termos. Em $\sum_{n=0}^{N-1}(2nh)h$, o índice $n$ percorre $0; 1; \ldots; N-1$: são $N$ parcelas. É semelhante a um ciclo Python `for` que acumula contribuições. Por exemplo, $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Símbolos semelhantes com significados diferentes

O $\varepsilon(t)$ (épsilon) representa o erro de velocidade; a constante $\mathrm{e}\approx2.71828$ é o número de Euler. $\tau$ (tau) é a constante de tempo, $\omega$ (ómega) a velocidade angular, $\alpha$ (alfa) a aceleração angular e $\Delta$ (delta) uma variação. O $\sigma$ minúsculo (sigma) é outro símbolo e deve ser definido em cada contexto.

<a id="math-delimiters"></a>

## Porque aparecem cifrões?

No código Markdown, `$...$` marca uma fórmula em linha e `$$...$$` um bloco matemático. Os delimitadores não fazem parte da fórmula e não devem aparecer na página renderizada do GitHub. Se aparecerem, verificar se a página mostra o código-fonte ou se há fórmulas em links ou erros de formatação.

[GitHub — Markdown / MathJax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Ponto decimal, unidades SI e espaçamento

Usamos sempre o ponto decimal: `0.5`, `3.8`, `63.2 %`, também em português. A vírgula separa itens de uma lista, não o número da unidade nem o integrando de `dt`. Escrever espaço entre valor e unidade: `1 s`, `4 mm`, `10 mm/s`. O ponto médio `·` indica multiplicação de unidades (`kg·m²`, `N·m·s/rad`); não pôr espaços junto de `/` (`mm/s`). Nas fórmulas usar `\mathrm{kg}\cdot\mathrm{m}^2` e a diferencial `\mathrm{d}t`. O ponto decimal é permitido pelo [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure). No código, `dt` é o passo finito; numa integral, `\mathrm{d}t` é a diferencial.


### rpm and rad/s

`rpm` significa **rotações por minuto** (revolutions per minute), unidade **não SI**. A velocidade angular em SI é dada em `rad/s` (radians per second): `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`; portanto `1000 rpm ≈ 104.72 rad/s`.