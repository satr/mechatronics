# 2. Førsteordensdynamikk og rotasjon


**Les denne siden på:** [en](../../en/notes/02-first-order-dynamics.md) · [fr](../../fr/notes/02-first-order-dynamics.md) · [de](../../de/notes/02-first-order-dynamics.md) · [it](../../it/notes/02-first-order-dynamics.md) · [es](../../es/notes/02-first-order-dynamics.md) · [pt](../../pt/notes/02-first-order-dynamics.md) · [zh](../../zh/notes/02-first-order-dynamics.md) · [ja](../../ja/notes/02-first-order-dynamics.md) · [nb](02-first-order-dynamics.md) · [ru](../../ru/notes/02-first-order-dynamics.md) · [ko](../../ko/notes/02-first-order-dynamics.md) · [fi](../../fi/notes/02-first-order-dynamics.md) · [pl](../../pl/notes/02-first-order-dynamics.md)

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `mm/s` — millimeter / sekund — lineær hastighet; `kg` — kilogram; `m` — meter; `rad/s` — radian / sekund — vinkelhastighet; `N` — newton; `N·m` — newton · meter — dreiemoment; `J` — joule; `rpm` — omdreining per minutt; `kg·m²` — kilogram · meter² — treghetsmoment; `N·m·s/rad` — newton · meter · sekund / radian — forsterkning per hastighet; `%` — prosent (en hundredel); `rad` — radian. [Enhetsoversikt](../UNITS.md).

**Grunnlag:** [0. Grunnlag for derivasjon, differensialer og integraler](00-calculus-foundations.md) · [Integraltabell](../INTEGRAL_TABLE.md)

[README](../README.md) · [Kort formelsamling](../CHEATSHEET.md) · [Python-øvelser](../exercises/README.md) · [Bevegelse, derivasjon og integrasjon](01-motion-calculus.md)

> **Advarsel:** Dette KI-assisterte lærematerialet kan inneholde feil, unøyaktige oversettelser og ugyldige forutsetninger. Bruk skjer på eget ansvar. Kontroller alle beregninger uavhengig, og bruk aldri eksemplene til å styre virkelige motorer eller maskiner.

> **Forutsetninger i motormodellen:** Vi antar ideell proporsjonal momentregulering uten last, friksjon, forsinkelser, spenningsgrenser, metning eller dynamikk av høyere orden. Dette er ikke en universell beskrivelse av motorer.

## Kort oppsummering

Tidskonstanten $\tau$ beskriver hvor raskt et førsteordenssystem nærmer seg en ny likevekt. Simuleringens tidssteg $dt$ styrer numerisk oppløsning, ikke de fysiske egenskapene. I den idealiserte modellen er $\tau=\frac{J}{K}$, men samme tidskonstant betyr ikke samme energibehov.

**Engelske faguttrykk:**

- førsteordenssystem (first-order system)
- tidskonstant (time constant)
- tidssteg (time step)
- treghetsmoment (moment of inertia)
- dreiemoment (torque)
- regulatorforsterkning (controller gain)
- vinkelakselerasjon (angular acceleration)
- systemidentifikasjon (system identification)
- rotasjonsenergi (rotational kinetic energy)

## På denne siden

- [1. Førsteordensrespons](#section-1)
- [2. Dreiemoment og treghet](#section-2)
- [3. Numerisk tidssteg og tidskonstant](#section-3)
- [4. Estimere tidskonstanten fra målinger](#section-4)
- [5. Rotasjonsenergi](#section-5)
- [6. Prøv selv](#section-6)
- [7. Fordypning (valgfritt)](#section-7)
  - [Hvor kommer 63.2 %, 86.5 % og 95.0 % fra?](#time-constant-derivation)
  - [Utregning av Euler-verdiene](#euler-values-derivation)

[SI-enheter og desimalpunkt](../SYMBOLS.md#si-notation)

<a id="section-1"></a>

## 1. Førsteordensrespons

Se [Fordypning](#section-7) for enheter, utledninger og numeriske begrensninger.

Med konstant målhastighet $u$, faktisk hastighet $v$ og $\tau>0$ er omtrent $63.2\ \%$ av endringen gjennomført etter $\tau$, $86.5\ \%$ etter $2\tau$ og $95.0\ \%$ etter $3\tau$. Dette betyr **ikke** at målet nås nøyaktig etter ett tidskonstantintervall.

**Notasjon:** $\varepsilon(t)=u-v(t)$ er hastighetsfeilen (speed error; gresk epsilon). Den naturlige eksponentialfunksjonen (exponential function) skrives $\exp(z)=\mathrm{e}^{z}$, der $\mathrm{e}\approx2.71828$ er Eulers tall (Euler’s number), **ikke** feilen. [Se utledningen og beregningen av 63.2 %](#time-constant-derivation).

$$
\frac{dv}{dt}=\frac{u-v}{\tau}.
$$

$$
v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right).
$$

| Tid | Andel av endringen |
| --- | ---: |
| $\tau$ | 63.2 % |
| $2\tau$ | 86.5 % |
| $3\tau$ | 95.0 % |

[Hvorfor akkurat disse prosentene? Se utregningen.](#time-constant-derivation)

![Normalisert førsteordensrespons: hver tidskonstant fjerner omtrent 63.2 % av den gjenværende feilen.](../../../assets/figures/first_order_response.svg)

<a id="section-2"></a>

## 2. Dreiemoment og treghet

Regulatoren beregner et elektrisk styresignal; det er motoren som fysisk skaper dreiemomentet $M$. I modellen er $J$ treghetsmomentet, $\omega$ vinkelhastigheten og $K$ koeffisienten mellom dreiemoment og hastighetsfeil. Dobling av $J$ med konstant $K$ dobler $\tau$. Dobling av begge beholder $\tau$, men krever dobbelt dreiemoment ved samme hastighetsfeil. Friksjon, belastning, forsinkelse og strømgrenser er ikke inkludert.

$$
J\frac{d\omega}{dt}=M,\qquad M=K(u-\omega).
$$

$$
\frac{d\omega}{dt}=\frac{K}{J}(u-\omega),\qquad \tau=\frac{J}{K}.
$$

**Enheter:** $J$: $\mathrm{kg}\cdot\mathrm{m}^2$; $\omega,u$: $\mathrm{rad/s}$; $M$: $\mathrm{N}\cdot\mathrm{m}$; $K$: $\mathrm{N}\cdot\mathrm{m}\cdot\mathrm{s}/\mathrm{rad}$; $\tau$: s.

Symbolsk tilbakekoblingssløyfe for idealmodellen. Regulatoren sender kommandoen; motoren lager det fysiske dreiemomentet.

![Symbolsk tilbakekoblingssløyfe for idealmodellen. Regulatoren sender kommandoen; motoren lager det fysiske dreiemomentet](../../../assets/figures/control_loop.svg)

<a id="section-3"></a>

## 3. Numerisk tidssteg og tidskonstant

Euler-metoden oppdaterer tilstanden med tidssteg $dt$. Kortere $dt$ gjør ikke modellmotoren raskere; bare den numeriske tilnærmingen endres. For $u=10\ \mathrm{mm/s}$, $\tau=1\ \mathrm{s}$ og én sekunds kjøretid får Euler $6.513$ med $dt=0.1$ eller $6.340\ \mathrm{mm/s}$ med $dt=0.01$; eksakt verdi er $6.321\ \mathrm{mm/s}$.

$$
v_{n+1}=v_n+\frac{u-v_n}{\tau}\ dt.
$$

| Metode | $v(1\ \mathrm{s})$ (mm/s) |
| --- | ---: |
| Euler $dt=0.1\ \mathrm{s}$ | 6.513 |
| Euler $dt=0.01\ \mathrm{s}$ | 6.340 |
| Eksakt | 6.321 |

[Se beregningen av disse tallene.](#euler-values-derivation)

<a id="section-4"></a>

## 4. Estimere tidskonstanten fra målinger

Ved et sprang fra 0 til 1000 rpm (omdreininger per minutt) finner vi når målt hastighet når omtrent 632 rpm. Hvis det skjer etter 2 sekunder, antyder førsteordensmodellen $\tau\approx2\ \mathrm{s}$. Med en annen startverdi bruker vi 63.2 % av **hele endringen**, ikke av absolutt målverdi. Målefeil, forsinkelse og oversving gjør denne enkle systemidentifikasjonen (system identification) mindre sikker.

**Hva koden faktisk returnerer:** Funksjonen [`estimate_tau`](../../../exercises/02_first_order_response.py) krever målinger med **strengt stigende tidsstempler**, regnet fra starten av spranget. Den returnerer tidspunktet for **første observerte måling** som når terskelen 63.2 % av endringen, med en toleranse på halvparten av kjent måleoppløsning. Hvis terskelen først observeres etter 2 s og forrige måling var etter 1 s, kan den reelle passeringen ha skjedd **mellom målingene**. Derfor er 2 s et samplingsbegrenset estimat, ikke en eksakt kurvetilpasning. Ugyldige målinger og gjentatte eller usorterte tidsstempler blir avvist, også etter terskelpasseringen; uten passering returneres `None`.

**Måleoppløsningen har betydning:** Parameteren `resolution` i `estimate_tau` må være **mindre enn størrelsen på hele hastighetsendringen**. Hvis hastigheten går fra 0 til 10 rpm, men displayet bare endrer seg i trinn på 10 rpm, kan tidspunktet for 63.2 %-terskelen ikke anslås pålitelig. Funksjonen avviser da dataene i stedet for å melde en kunstig terskelpassering ved første måling. Selv med god oppløsning er anslaget begrenset av samplingsfrekvensen.

<a id="section-5"></a>

## 5. Rotasjonsenergi

Resulterende dreiemoment oppfyller $M=J\alpha$. Med $J=2\ \mathrm{kg}\cdot\mathrm{m}^2$ og $\omega=10\ \mathrm{rad/s}$ er rotasjonsenergien $100\ \mathrm{J}$; dobling av $J$ gir $200\ \mathrm{J}$. Dobling av $\omega$ gir fire ganger så mye energi. Mekanisk energi er ikke det samme som totalt elektrisk energiforbruk.

$$
M=J\alpha,\qquad \alpha=\frac{d\omega}{dt}.
$$

$$
E=\frac{1}{2}J\omega^2.
$$

<a id="section-6"></a>

## 6. Prøv selv

I en ideell sprangrespons fra 0 til 1000 omdreininger/minutt tyder omtrent 632 omdreininger/minutt etter to sekunder på $\tau\approx2\ \mathrm{s}$. Støy og begrenset målefrekvens kan kreve mer robust systemidentifikasjon. Sammenlign Euler og eksakt løsning i programmet.

[02_first_order_response.py](../../../exercises/02_first_order_response.py) · [03_rotation_energy.py](../../../exercises/03_rotation_energy.py) · [plot_models.py](../../../exercises/plot_models.py)


<a id="section-7"></a>

## 7. Fordypning (valgfritt)


### Stabilitet i Euler-metoden

For hvert steg ganges **den gjenværende hastighetsfeilen** med $1-\frac{dt}{\tau}$. Konvergens for denne modellen krever $0<dt<2\tau$; når $\tau<dt<2\tau$, vil tallverdien svinge rundt målverdien. Det innebærer ikke fysisk svingning i motoren.

### Modellbegrensninger

Mer generelt er $J\ \frac{d\omega}{dt}=M_{\text{motor}}-M_{\text{last}}-M_{\text{friksjon}}$. $\tau=\frac{J}{K}$ gjelder bare under den spesielle antakelsen $M_{\text{netto}}=K(u-\omega)$. Last, friksjon, forsinkelse og strømgrenser kan endre responsen.

### Energi og effekt

Når $J$ er konstant, er $\Delta E=\frac{1}{2} J(\omega_2^2-\omega_1^2)$ og den øyeblikkelige mekaniske effekten (mechanical power) er $P=M\omega$. Dette sier ikke direkte hvor mye elektrisk energi som brukes.


<a id="time-constant-derivation"></a>

### Hvor kommer 63.2 %, 86.5 % og 95.0 % fra?

Prosentene og eksponentialfunksjonen kommer fra **samme ligning**. Hastighetsfeilen defineres som $\varepsilon(t)=u-v(t)$ (ikke Eulers tall). Ved konstant målverdi $u$ er $\frac{d\varepsilon}{dt}=-\frac{dv}{dt}$:

$$
\varepsilon(t)=u-v(t),\qquad \frac{d\varepsilon}{dt}=-\frac{\varepsilon}{\tau}.
$$

$$
\frac{d\varepsilon}{\varepsilon}=-\frac{dt}{\tau}
\quad\Longrightarrow\quad
\ln\left\lvert\frac{\varepsilon(t)}{\varepsilon(0)}\right\rvert=-\frac{t}{\tau}
\quad\Longrightarrow\quad
\varepsilon(t)=\varepsilon(0)\exp\!\left(-\frac{t}{\tau}\right).
$$

Når variablene separeres, dividerer vi med $\varepsilon$. Dette trinnet forutsetter derfor at startfeilen ikke er null. Hvis $u=v_0$, er feilen null hele tiden, og den opprinnelige differensialligningen gir den konstante løsningen $v(t)=u$ direkte.

$$
f(t)=\frac{v(t)-v_0}{u-v_0}=1-\exp\!\left(-\frac{t}{\tau}\right),\qquad (u\ne v_0).
$$

| $t$ | $f(t)$ |
| ---: | ---: |
| $\tau$ | $1-\exp(-1)=0.63212056\ldots\approx63.2\ \%$ |
| $2\tau$ | $1-\exp(-2)=0.86466472\ldots\approx86.5\ \%$ |
| $3\tau$ | $1-\exp(-3)=0.95021293\ldots\approx95.0\ \%$ |

Ved et sprang fra 0 til 1000 omdreininger/minutt får vi omtrent 632, 865 og 950 rpm etter én, to og tre tidskonstanter. Den ideelle modellen nærmer seg målet asymptotisk.

<a id="euler-values-derivation"></a>

### Utregning av Euler-verdiene

$$
v_N=u+(v_0-u)\left(1-\frac{dt}{\tau}\right)^N,\qquad N=\frac{t}{dt}.
$$

$$
\begin{aligned}
u&=10,\quad v_0=0,\quad t=\tau=1;\\
v_{dt=0.1}&=10(1-0.9^{10})\approx6.5132;\\
v_{dt=0.01}&=10(1-0.99^{100})\approx6.3397;\\
v_{\mathrm{exact}}&=10(1-\exp(-1))\approx6.3212.
\end{aligned}
$$
