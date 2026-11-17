# Tabell over deriverte

**Språk:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](DERIVATIVE_TABLE.md) · [ru](../ru/DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `mm/s²` — millimeter / sekund² — akselerasjon. [Enhetsoversikt](UNITS.md).

[Kursoversikt](README.md) · [Integraltabell](INTEGRAL_TABLE.md) · [Grunnleggende kalkulus](notes/00-calculus-foundations.md)

La $u$ og $v$ avhenge av $x$, og la $a$ være konstant. Apostrofene viser derivasjon med hensyn til $x$, og vinkler måles i radianer. Den deriverte er bare definert der den tilsvarende grenseverdien finnes. For sammensatte funksjoner brukes kjerneregelen (chain rule). Her er $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ og $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Regler

| Funksjon | Derivert | Betingelser |
| --- | --- | --- |
| $c$ | $0$ | $c$ konstant |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | reell $n$; der funksjonen er definert og deriverbar |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ konstant |
| $uv$ | $u'v+uv'$ | produktregelen |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | kjerneregelen |
| $\frac{1}{u}$ | $-\frac{u'}{u^2}$ | $u\ne0$ |
| $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ | $u>0$ |
| $\exp(u)$ | $\exp(u)u'$ | — |
| $a^u$ | $a^u\ln(a)u'$ | $a>0$ |
| $\ln(u)$ | $\frac{u'}{u}$ | $u>0$ |
| $\ln\lvert u\rvert$ | $\frac{u'}{u}$ | $u\ne0$ |
| $\sin(u)$ | $\cos(u)u'$ | — |
| $\cos(u)$ | $-\sin(u)u'$ | — |
| $\tan(u)$ | $\frac{u'}{\cos^2(u)}$ | $\cos(u)\ne0$ |
| $\arcsin(u)$ | $\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arccos(u)$ | $-\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arctan(u)$ | $\frac{u'}{1+u^2}$ | — |
| $\mathrm{arsinh}(u)$ | $\frac{u'}{\sqrt{1+u^2}}$ | — |

## Eksempler

**Kjerneregelen (chain rule):** For $y=(3x^2+1)^4$ setter vi $u=3x^2+1$. Da er $u'=6x$, og dermed

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Fart og akselerasjon:** For posisjonen $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$ gir derivasjon med hensyn til tid hastigheten, og neste derivasjon gir akselerasjonen:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

Ved $t=2\ \mathrm{s}$ er hastigheten $11\ \mathrm{mm/s}$. Dette er et matematisk eksempel, ikke en instruksjon for maskinstyring.

**Omvendt funksjon (inverse function):** Hvis $y=f^{-1}(x)$, $f$ er deriverbar i $y$ og $f'(y)\ne0$, er $(f^{-1})'(x)=1/f'(y)$ på en lokalt inverterbar gren.
