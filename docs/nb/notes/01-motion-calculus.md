# 1. Bevegelse, derivasjon og integrasjon


**Les denne siden på:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](../../fi/notes/01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `mm/s²` — millimeter / sekund² — akselerasjon; `%` — prosent (en hundredel). [Enhetsoversikt](../UNITS.md).

**Grunnlag:** [0. Grunnlag for derivasjon, differensialer og integraler](00-calculus-foundations.md) · [Integraltabell](../INTEGRAL_TABLE.md)

[README](../README.md) · [Kort formelsamling](../CHEATSHEET.md) · [Python-øvelser](../exercises/README.md) · [Førsteordensdynamikk og rotasjon](02-first-order-dynamics.md)

> **Advarsel:** Dette KI-assisterte lærematerialet kan inneholde feil, unøyaktige oversettelser og ugyldige forutsetninger. Bruk skjer på eget ansvar. Kontroller alle beregninger uavhengig, og bruk aldri eksemplene til å styre virkelige motorer eller maskiner.

## Kort oppsummering

Tilbakelagt strekning er den totale veilengden; forflytning er sluttposisjon minus startposisjon. Fart (speed) er ikke-negativ, mens hastighet (velocity) er en vektor som også angir retning. Den deriverte av posisjon gir momentan hastighet; integralet av hastighet med fortegn gir forflytning.

**Engelske faguttrykk:**

- tilbakelagt strekning (distance traveled)
- forflytning (displacement)
- fart (speed)
- hastighetsvektor (velocity)
- derivasjon (derivative)
- integral (integral)
- numerisk integrasjon (numerical integration)
- eksplisitt Euler-metode (explicit Euler method)

## På denne siden

- [1. Bevegelseseksempel](#section-1)
- [2. Derivasjon og momentan hastighet](#section-2)
- [3. Integrasjon og forflytning](#section-3)
- [4. Numerisk integrasjon](#section-4)
- [5. Prøv selv](#section-5)
- [6. Fordypning (valgfritt)](#section-6)
  - [Hvorfor den deriverte av 2t² er 4t](#power-rule-derivation)
  - [Beregning av forflytningene i tabellen](#motion-values-derivation)

[SI-enheter og desimalpunkt](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Bevegelseseksempel

Se [Fordypning](#section-6) for enheter, utledninger og numeriske begrensninger.

En virtuell akse beveger seg med $+3\ \mathrm{mm/s}$ i to sekunder og deretter med $-3\ \mathrm{mm/s}$ i to sekunder. Forflytningen er $+6-6=0\ \mathrm{mm}$, men tilbakelagt strekning er $12\ \mathrm{mm}$. Ved sirkelbevegelse endres hastighetsvektorens retning selv om farten er konstant.

$$
\overline{v}=\frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

$$
\text{gjennomsnittsfart}=\frac{\text{hele den tilbakelagte strekningen}}{t_2-t_1}.
$$

Over **hele tidsrommet på fire sekunder** gir gjennomsnittlig hastighet med fortegn og gjennomsnittsfart **ulike svar**. Aksen er tilbake ved startpunktet, men har tilbakelagt 12 mm:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Gjennomsnittsfart er altså **ikke nødvendigvis absoluttverdien av gjennomsnittlig hastighet**. Etter én hel runde i en sirkel er gjennomsnittlig hastighetsvektor også null, selv om veilengde og gjennomsnittsfart er positive.

<a id="section-2"></a>

## 2. Derivasjon og momentan hastighet

For $x(t)=2t^2\ \mathrm{mm}$, der $t$ måles i sekunder, er $v(t)=4t\ \mathrm{mm/s}$. **Hvorfor 4?** Potensregelen gir $d(t^2)/dt=2t$, så derivasjon av $2t^2$ gir $2\cdot2t=4t$. [Se utregning og enheter](#power-rule-derivation). Ved $t=1\ \mathrm{s}$ er den momentane hastigheten $4\ \mathrm{mm/s}$. Foroverdifferansen gir $6$, $4.2$ og $4.02\ \mathrm{mm/s}$ med $dt=1$, $0.1$ og $0.01\ \mathrm{s}$.

$$
v(t)=\frac{dx}{dt},\qquad v(t)\approx\frac{x(t+dt)-x(t)}{dt}.
$$

**Hvorfor et altfor lite tidssteg kan gi feil:** Ved $t=1\ \mathrm{s}$ er den eksakte deriverte av $x(t)=2t^2$ lik $4\ \mathrm{mm/s}$. Med $dt=1e-17\ \mathrm{s}$ avrunder Python `float` verdien `t + dt` tilbake til `t`. Begge beregnede posisjoner blir like, og differansen ville feilaktig gitt hastighet null. Ved enda mindre skalaer kan begge posisjoner avrundes til null selv om den deriverte ikke er null. Eksempelet [`forward_derivative`](../../../exercises/01_motion_and_integral.py) gir nå `ValueError` i slike tilfeller i stedet for en falsk nullverdi. Den endelige differansen blir fortsatt beregnet; velg et tidssteg som kan representeres, ikke stadig mindre steg uten grense.

<a id="section-3"></a>

## 3. Integrasjon og forflytning

Integralet av hastighet med fortegn kan være negativt eller null; integralet av absoluttverdien gir en ikke-negativ strekning. For $v(t)=2t\ \mathrm{mm/s}$ fra $0$ til $2\ \mathrm{s}$ er den eksakte forflytningen $4\ \mathrm{mm}$.

$$
\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Geometrisk tilsvarer integralet av hastigheten med fortegn det fortegnede arealet under hastighet–tid-kurven. **Dette er et annet eksempel enn i del 2.** Der var posisjonen $x(t)=2t^2$, med derivert $v(t)=4t$. For å vise integrasjon velges her med hensikt en annen hastighet: $v(t)=2t$. Den tilhørende posisjonen er $x(t)=t^2+C$ (med konsistente enheter). De to bevegelsesmodellene må ikke blandes sammen.

<a id="section-4"></a>

## 4. Numerisk integrasjon

Eksakt forflytning og Euler-tilnærming med verdien ved stegets start (syntetiske data).

![Eksakt forflytning og Euler-tilnærming med verdien ved stegets start (syntetiske data)](../../../assets/figures/euler_vs_exact.svg)

Eksplisitt Euler-metode bruker hastigheten **ved starten** av hvert intervall, ikke den faktiske gjennomsnittshastigheten. For den økende hastigheten i eksemplet undervurderer metoden forflytningen: med $dt=0.5$, $0.1$ og $0.01\ \mathrm{s}$ får vi $3$, $3.8$ og $3.98\ \mathrm{mm}$ (eksakt $4\ \mathrm{mm}$). Trapesmetoden er eksakt her fordi hastigheten er lineær i tid.

$$
x_{n+1}=x_n+v(t_n)\ dt.
$$

| `dt` (s) | Euler (mm) |
| ---: | ---: |
| 0.5 | 3.000 |
| 0.1 | 3.800 |
| 0.01 | 3.980 |
| Eksakt | 4.000 |


[Se hvordan 3, 3.8 og 3.98 beregnes.](#motion-values-derivation)

<a id="section-5"></a>

## 5. Prøv selv

Kjør bevegelsesprogrammet og reduser $dt$. Hvorfor kan en tur frem og tilbake gi null forflytning, men positiv tilbakelagt strekning?

[01_motion_and_integral.py](../../../exercises/01_motion_and_integral.py)

<a id="section-6"></a>

## 6. Fordypning (valgfritt)

### Enheter og koeffisienter

Når $t$ måles i sekunder, er $x(t)=2t^2$ mm en forkortelse: koeffisienten har enheten $2\ \mathrm{mm/s^2}$. Da har $v(t)=4t$ enheten mm/s. Kontroller enhetene i alle formler.

### Begrensninger ved tilnærmingen

En endelig differanse (finite difference) anslår den deriverte over et intervall som ikke er null. Mindre steg reduserer ofte diskretiseringsfeil, men svært små steg kan forsterke avrundingsfeil eller målestøy. Euler bruker verdien i starten av steget.

### Bevegelse i flere dimensjoner

For posisjonsvektoren $\mathbf r(t)$ er hastigheten $\mathbf v=d\mathbf r/dt$, farten er $\|\mathbf v\|$, og veilengden $s=\int\|\mathbf v(t)\|dt$.


<a id="power-rule-derivation"></a>

### Hvorfor den deriverte av $2t^2$ er $4t$



$$
x(t)=at^2,\qquad
\frac{dx}{dt}=\lim_{h\to0}\frac{a(t+h)^2-at^2}{h}
=\lim_{h\to0}a(2t+h)=2at.
$$

$$
 a=2\ \mathrm{mm/s^2},\qquad
 v(t)=2at=(4\ \mathrm{mm/s^2})t.
$$

<a id="motion-values-derivation"></a>

### Beregning av forflytningene i tabellen

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$



Symbolet $\sum$ (stor gresk sigma, **summasjon** / summation) betyr at ledd skal legges sammen. I $\sum_{n=0}^{N-1}(2nh)h$ går indeksen $n$ gjennom $0; 1; \ldots; N-1$: totalt $N$ ledd. Tenk på en Python-`for`-løkke som legger til hvert bidrag. For eksempel er $\sum_{n=1}^{3}n=1+2+3=6$. [← Symbolforklaringer](../SYMBOLS.md#summation).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Her er `h` tallverdien til tidssteget `dt` målt i sekunder (`dt = 0.5 s` betyr `h = 0.5`), og `N` er antall steg. Resultatet er en **strekning i millimeter**.



Når $dt=0.5$, $0.1$ og $0.01$ sekunder, får vi $3$, $3.8$ og $3.98$ millimeter. Her er $2/dt$ et heltall.
