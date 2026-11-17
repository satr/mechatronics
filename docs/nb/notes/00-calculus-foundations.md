# 0. Grunnleggende kalkulus: derivasjon, grenser og integraler fra mekanikk

**Språk:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](../../fi/notes/00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

Den **naturlige eksponentialfunksjonen** er $\exp(x)=\mathrm{e}^{x}$, der **Eulers tall** er $\mathrm{e}\approx2.71828$. Den beskriver kontinuerlig vekst eller avtagning; $\exp(0)=1$ og $\exp(-1)\approx0.3679$. Den naturlige logaritmen $\ln$ er inversfunksjonen: $\ln(\exp(x))=x$. Se [symboloversikten](../SYMBOLS.md).

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `mm/s²` — millimeter / sekund² — akselerasjon; `kg·m²` — kilogram · meter² — treghetsmoment; `rad/s` — radian / sekund — vinkelhastighet; `rad/s²` — radian / sekund² — vinkelakselerasjon; `N·m` — newton · meter — dreiemoment; `W` — watt; `rpm` — omdreining per minutt; `N/m` — newton / meter — stivhet; `mm³/s` — millimeter³ / sekund — volumstrøm; `%` — prosent (en hundredel); `m` — meter; `kg` — kilogram; `N` — newton; `J` — joule; `rad` — radian. [Enhetsoversikt](../UNITS.md).

[README](../README.md) · [Integral table](../INTEGRAL_TABLE.md) · [Trigonometry table](../TRIGONOMETRY.md) · [Motion](01-motion-calculus.md) · [Dynamics](02-first-order-dynamics.md) · [Symbols](../SYMBOLS.md)

> **Læringsmodell:** Kontroller modeller og enheter; ikke bruk demo-kode på virkelig utstyr.

En **derivert (derivative)** viser hvor raskt en størrelse endrer seg akkurat nå. Den **andrederiverte (second derivative)** viser hvordan endringshastigheten endres. Et **integral (integral)** summerer små endringer. En **grenseverdi (limit)** definerer øyeblikkelig endring; en **logaritme (logarithm)** finner tid i en eksponentiell respons.

Disse verktøyene brukes på maskinakser, servodrifter, robotledd, fjærer og sensorer. Start med det fysiske spørsmålet og finn deretter regneregel og enhet.

## Innhold

- [1. Fra målt endring til matematisk modell](#section-1)
- [2. Grenser og første derivert](#section-2)
- [3. Første og andre derivert: en akse i bevegelse](#section-3)
- [4. Kjerneregelen: rotasjonsenergi](#section-4)
- [5. Eksponentialfunksjon og logaritme: responstid](#section-5)
- [6. Integraler: forflytning og mekanisk arbeid](#section-6)
- [7. Tilleggseksempel: kule som utvider seg](#section-7)
- [8. Enheter, kontroll og oppgaver](#section-8)

<a id="section-1"></a>
## 1. Fra målt endring til matematisk modell

| Fysisk spørsmål | Matematisk verktøy |
| --- | --- |
| Hvor raskt beveger aksen seg **nå**? | Første derivert $dx/dt$ |
| Hvordan endres hastigheten? | Andre derivert $d^2x/dt^2$ |
| Når nås 90 % av responsen? | Logaritme $\ln$ |
| Hva er forflytningen på 2 s? | Bestemt integral $\int v\ \mathrm{d}t$ |
| Hva er arbeidet fra en variabel kraft? | Integral $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Grenser og første derivert

En **endelig differanse (finite difference)** mellom to målinger gir gjennomsnittlig endringshastighet over intervallet. Den deriverte er grenseverdien når intervallet går mot null.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

For posisjonen $x(t)=a t^2$, med $a=2\ \mathrm{mm/s^2}$, utvider vi telleren før vi tar grensen:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

Faktoren $h$ forkortes **før** $h$ settes mot null. Ved $t=1\ \mathrm{s}$ er øyeblikkelig hastighet $4\ \mathrm{mm/s}$. Vi setter ikke inn ubestemt $0/0$ direkte.

**Viktige derivasjonsregler (differentiation rules)**: $c$ og $n$ er konstanter; trigonometriske argumenter er i radianer.

| Regel | Formel |
| --- | --- |
| Konstant | $\frac{d}{dt}c=0$ |
| Potens | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Koeffisient og sum | $(cf+g)'=cf'+g'$ |
| Produkt | $(fg)'=f' g+fg'$ |
| Kvotient, $g\ne0$ | $\left(\frac{f}{g}\right)'=\frac{f' g-fg'}{g^2}$ |
| Sammensatt funksjon | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Eksponential | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Naturlig logaritme, $t>0$ | $\frac{d}{dt}\ln t=\frac1t$ |
| Sinus / cosinus | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Tangenthelning og areal under hastighetskurven](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Første og andre derivert: en akse i bevegelse

En sleide starter ved 2 mm med starthastighet 3 mm/s og konstant akselerasjon 4 mm/s². Posisjonen er:

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Første derivert** gir hastighet. Konstantleddet forsvinner, det lineære leddet gir 3 mm/s, og andregradsleddet blir lineært i $t$.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Andre derivert** gir akselerasjon. Vi deriverer hastigheten en gang til. Etter 2 s: posisjon 16 mm, hastighet 11 mm/s, akselerasjon 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

Andre derivert har enheten lengde/tid². Det er **ikke** kvadratet av første derivert.

<a id="section-4"></a>
## 4. Kjerneregelen: rotasjonsenergi

Et roterende svinghjul lagrer kinetisk energi. Når vinkelhastigheten $\omega$ varierer med tid, endres energien $E$ gjennom $\omega$. Dette er **kjerneregelen (chain rule)**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$
$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

For $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$ og $\alpha=2\ \mathrm{rad/s^2}$ er momentet $J\alpha=0.02\ \mathrm{N\cdot m}$ og den mekaniske effekten $0.2\ \mathrm{W}$. Vi får $P=M\omega$.

<a id="section-5"></a>
## 5. Eksponentialfunksjon og logaritme: responstid

I en enkel førsteordensmodell nærmer hastigheten seg sluttverdien eksponentielt. $\tau$ er **tidskonstanten (time constant)**, målt i sekunder.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Denne formen forutsetter **null vinkelhastighet ved start**, $\omega(0)=0$, og en konstant sluttverdi $\omega_\infty$. Når starthastigheten er $\omega_0\ne0$, er den generelle førsteordensresponsen:

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Eksempel med starthastighet ulik null:** La $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ og $\tau=0.5\ \mathrm{s}$. Etter én tidskonstant ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

Dette er **63.2 % av endringen på 800 rpm**, ikke 63.2 % av sluttverdien på 1000 rpm. Ved $t=0$ gir formelen 200 rpm; etter lang tid nærmer svaret seg 1000 rpm. Det er et matematisk eksempel, ikke en motorkommando.

Eksponentialfunksjonen viser hvor stor del av feilen som gjenstår. For å finne **tiden** bruker vi **naturlig logaritme (natural logarithm)** $\ln$, inversen av $\exp$. Argumentet $0.1$ er dimensjonsløst.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Når 90 % av endringen er fullført, gjenstår 10 % av startfeilen. Med $\tau=0.5\ \mathrm{s}$ gir modellen omtrent 1.151 s. Virkelige drivsystemer kan ha grenser og forsinkelser.

Den deriverte av $\ln z$ er $1/z$ for $z>0$; hvis $z=z(t)$, multipliser også med $dz/dt$. Logaritmen til en fysisk størrelse krever et dimensjonsløst forhold.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integraler: forflytning og mekanisk arbeid

Et **ubestemt integral (indefinite integral)** gir antideriverte funksjoner (antiderivatives) pluss konstanten $C$. Et **bestemt integral (definite integral)** gir akkumulert endring over et intervall.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Forflytning.** Sleiden starter ved $x_0=2\ \mathrm{mm}$, hastigheten er $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$. Finn forflytningen mellom 0 og 2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$
$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Forflytningen blir 14 mm; legg til startposisjonen og få $x(2)=16\ \mathrm{mm}$. Negativ hastighet gir negativ fortegnet forflytning, ikke negativ tilbakelagt avstand.

**Fjærarbeid.** En ideell lineær fjær med $k=200\ \mathrm{N/m}$ strekkes fra $x=0$ til $x=0.01\ \mathrm{m}$. Kraften øker med strekkingen, derfor integrerer vi alle små arbeid:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

Arbeidet er 0.01 J. Å multiplisere sluttkraften $F=2\ \mathrm{N}$ med hele forflytningen ville gitt feil 0.02 J, fordi kraften ikke er konstant.

<a id="section-7"></a>
## 7. Tilleggseksempel: kule som utvider seg

**Valgfritt eksempel på kjerneregelen.** Kulens volum avhenger av radiusen, som kan avhenge av tiden. Samme matematikk som for energien i svinghjulet og vinkelhastigheten.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Ved $r=10\ \mathrm{mm}$ og $dr/dt=1\ \mathrm{mm/s}$ får vi $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Hvis $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, får vi ved 2 s: $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$ og $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Enheter, kontroll og oppgaver

**Sjekk:** den deriverte av posisjon har enhet m/s, den andrederiverte m/s²; integral av kraft over avstand gir N·m = J; husk $C$ for ubestemt integral; derivert beskriver et øyeblikk, integral en akkumulering; differensial $\mathrm{d}t$ er ikke det samme som endelig tidstrinn `dt` i kode.

**Oppgaver:** (1) For $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, finn hastighet og akselerasjon ved 3 s. (2) For $\tau=1\ \mathrm{s}$, tid til 90 % endring? (3) Forflytning ved 4 mm/s i 2 s? **Svar:** 8 mm/s og 2 mm/s²; omtrent 2.303 s; 8 mm.

**Utregnede løsninger:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integral reference](../INTEGRAL_TABLE.md) · [Trigonometry](../TRIGONOMETRY.md) · [Next: motion](01-motion-calculus.md) · [Python exercises](../exercises/README.md)
