# Symbols and notation

**Read this page in:** [en](SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](../fi/SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Units used here (defined before the examples):** `s` — second; `mm` — millimetre = 0.001 m; `mm/s` — millimetre / second — linear speed; `kg·m²` — kilogram · metre² — moment of inertia; `N·m` — newton · metre — torque; `N·m·s/rad` — newton · metre · second / radian — gain per unit speed; `rpm` — revolution per minute; `rad/s` — radian / second — angular speed; `%` — percent (one part in a hundred). [Full unit reference](UNITS.md).

[← README](README.md) · [Cheat sheet](CHEATSHEET.md) · [Motion](notes/01-motion-calculus.md) · [Dynamics](notes/02-first-order-dynamics.md)

## Contents

- [Summation: capital sigma](#summation)
- [Symbols that can be confused](#different-symbols)
- [Markdown math notation](#math-delimiters)
- [Decimal points, SI units, and mathematical spacing](#si-notation)

<a id="summation"></a>

## Σ / ∑ — Summation

The symbol $\sum$ (capital Greek **sigma**, **summation**) means *add up the terms*. In $\sum_{n=0}^{N-1}(2nh)h$, the index $n$ takes the values $0; 1; \ldots; N-1$: there are $N$ contributions. Think of a Python `for` loop adding one contribution at a time. For example, $\sum_{n=1}^{3}n=1+2+3=6$.

<a id="different-symbols"></a>

## Some symbols look similar but mean different things

The lowercase $\varepsilon(t)$ (epsilon) is speed error; the upright constant $\mathrm{e}\approx2.71828$ is Euler’s number. $\tau$ (tau) is a time constant; $\omega$ (omega) is angular velocity; $\alpha$ (alpha) is angular acceleration; $\Delta$ (delta) means a change. Lowercase $\sigma$ (sigma) is a *different* symbol, often used for standard deviation or stress in other contexts. Its meaning always depends on the definition in the lesson.

<a id="math-delimiters"></a>

## Why do raw dollar signs appear?

In Markdown **source**, `$...$` marks inline math and `$$...$$` marks a separate math block. These are formatting delimiters, not part of the equation. In GitHub’s rendered Markdown they should not appear as dollar signs. If they do, check whether you are viewing source/plain text or whether the formula is inside a link label or malformed Markdown. This reference uses plain text, not math markup, inside navigation links.

[GitHub math documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>

## Decimal points, SI units, and mathematical spacing

Write decimals with a point everywhere: `0.5`, `3.8`, `63.2 %`, even in translations. A comma separates entries in a list; it never separates a number from its unit or a differential. Write a space between a numeric value and a unit symbol: `1 s`, `4 mm`, `10 mm/s`. Compound unit symbols use a middle dot for multiplication (`kg·m²`, `N·m·s/rad`) and no spaces around `/` (`mm/s`, not `mm / s`). The dot is multiplication, not a decimal marker. For example, `1 N·m` is one newton metre. In displayed equations, use `\mathrm{kg}\cdot\mathrm{m}^2`, and write the differential as `\mathrm{d}t`, not a comma followed by `dt`. Scientific facts and notation follow the [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure); this repository consistently chooses the permitted decimal point. The time step `dt` in Python represents a *finite* interval, while the `\mathrm{d}t` in an integral is a differential.


### rpm and rad/s

`rpm` means **revolutions per minute**, a commonly used **non-SI** rotation-rate unit. The SI angular-velocity symbol is `rad/s` (radians per second). Convert with `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`; therefore `1000 rpm ≈ 104.72 rad/s`.