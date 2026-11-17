# Integraltabell

**Les på:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `mm/s²` — millimeter / sekund² — akselerasjon; `N` — newton; `m` — meter; `N/m` — newton / meter — stivhet; `J` — joule. [Enhetsoversikt](UNITS.md).

[README](README.md) · [0. Grunnlag for derivasjon, differensialer og integraler](notes/00-calculus-foundations.md) · [Symboler](SYMBOLS.md)

Alle ubestemte integraler har +C som integrasjonskonstant. a er konstant, og uttrykkene gjelder på intervaller der integranden er definert. Vinkler måles i radianer.

Begynn med polynomer; trigonometriske integraler og rotuttrykk kan komme senere.

## Innhold

- [Potenser og logaritmer](#section-1)
- [Eksponentialfunksjoner](#section-2)
- [Trigonometriske funksjoner](#section-3)
- [Rasjonale uttrykk og inverse trigonometriske funksjoner](#section-4)
- [Videre oppslag: røtter og resiproke funksjoner](#section-5)
- [Velge formel og kontrollere svaret](#section-6)

<a id="section-1"></a>
## 1. Potenser og logaritmer

| Formel | Vilkår / forklaring |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | alle reelle $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; følg det reelle definisjonsområdet for potenser |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Eksponentialfunksjoner

| Formel | Vilkår / forklaring |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | alle reelle $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Trigonometriske funksjoner

| Formel | Vilkår / forklaring |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ i radianer |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ i radianer |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Rasjonale uttrykk og inverse trigonometriske funksjoner

| Formel | Vilkår / forklaring |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | alle reelle $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Videre oppslag: røtter og resiproke funksjoner

| Formel | Vilkår / forklaring |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; intervaller uten poler |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; intervaller uten poler |

## Kontroller en formel

Deriver høyresiden for å kontrollere formelen. For potenser bruker du potensregelen baklengs.

Logaritmer krever dimensjonsløse argumenter; her antas x å være dimensjonsløs hvis ikke annet er oppgitt. Respekter valg av fortegn og definisjonsområde.

<a id="section-6"></a>
## 6. Velge formel og kontrollere svaret

Finn først variabelen etter differensialet (dx, dt eller dθ). En koeffisient er konstant bare hvis den ikke avhenger av denne variabelen. For ubestemt integral: legg til C. For bestemt integral: regn F(b) − F(a). Kontroller ved å derivere.

### Eksempel A — forflytning fra hastighet

For v(t) = 3 mm/s + (4 mm/s²)t mellom 0 og 2 s integreres hvert ledd:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

Resultatet er 14 mm, ikke 14 mm/s: å integrere hastighet over tid gir forflytning.

### Eksempel B — arbeid fra variabel kraft

En fjær F(x) = kx med k = 200 N/m strekkes fra 0 til 0.01 m:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

Arbeidet er 0.01 J. Sluttkraften kan ikke multipliseres med hele strekningen.

### Eksempel C — logaritme fra enkel funksjon

En antiderivert av 1/x er ln|x|. For dimensjonsløst x fra 1 til 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Svaret blir ln 2 ≈ 0.693. x er et forholdstall, ikke en lengde.
