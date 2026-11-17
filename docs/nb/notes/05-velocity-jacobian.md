# 5. Rotasjon, lineær hastighet og singulariteter

**Languages:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Enheter på denne siden (forklart før eksemplene):** `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `rad` — radian; `rad/s` — radian / sekund — vinkelhastighet; `mm/rad` — millimeter / radian — Jacobi-koeffisient (lengde per vinkel); `°` — grad. [Enhetsoversikt](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> Kun en idealisert læringsmodell; ikke for styring av ekte maskiner.

Endepunktet til et roterende ledd følger en sirkelbue. Den momentane hastigheten er tangentielt rettet, altså vinkelrett på leddet. Først gjennomgås geometrien, deretter tidsderivater og til slutt en valgfri Jacobi-matrise (Jacobian matrix).

## Innhold

1. [Fra rotasjon til tangentiell hastighet](#section-1)
2. [Hvor kommer de deriverte fra?](#section-2)
3. [Eksempler på hastighet og fortegn](#section-3)
4. [To ledd: relative og absolutte vinkler](#section-4)
5. [Singulariteter i foldet og utstrakt stilling](#section-5)
6. [Tre forskyvninger nær sammenfolding](#section-6)
7. [Videre: Jacobi-matrisen og løste oppgaver](#section-7)

<a id="section-1"></a>
## 1. Fra rotasjon til tangentiell hastighet

La et stivt ledd med lengde $L$ rotere om et fast punkt $O$. I tidsintervallet $\Delta t>0$ er vinkelendringen $\Delta Q$, målt **i radianer**. Når rotasjonsretningen ikke endrer seg i intervallet, går spissen langs en sirkelbue. **Buelengden** er nøyaktig $\Delta s=L|\Delta Q|$. Den **fortegnsbestemte strekningen langs buen** er $L\Delta Q$, der fortegnet angir rotasjonsretningen. Dette må ikke forveksles med den rettlinjede forskyvningen (korden) mellom spissens to posisjoner.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Del buelengden på tiden som har gått for å få **gjennomsnittsfarten**:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

For **øyeblikkelig fart** lar vi $\Delta t\to0$. Vinkelhastigheten er $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$ i rad/s, og derfor blir farten $v=L|\omega|$. Hastighetsvektoren er **tangent til sirkelen** og står vinkelrett på leddet. Ved $Q=45^\circ$ og rotasjon mot urviseren ($\omega>0$) beveger spissen seg mot venstre og oppover: horisontalkomponenten er negativ og vertikalkomponenten positiv.

$$
v=L\lvert\dot Q\rvert
$$

![Tangentiell hastighet og fortegn ved Q=45°.](../../../assets/figures/link_tangent_velocity.svg)

*Tangentiell hastighet og fortegn ved Q=45°.*

<a id="section-2"></a>
## 2. Hvor kommer de deriverte fra?

Koordinatene avhenger av Q, og Q avhenger igjen av tiden. Kjerneregelen (chain rule) multipliserer posisjonsendring per radian med radianer per sekund.

$$
x(t)=L\cdot\cos\bigl(Q(t)\bigr),\qquad y(t)=L\cdot\sin\bigl(Q(t)\bigr)
$$

$$
v_x=\frac{\mathrm{d}x}{\mathrm{d}t}
=\frac{\mathrm{d}x}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=-L\cdot\sin(Q)\cdot\dot{Q}
$$

$$
v_y=\frac{\mathrm{d}y}{\mathrm{d}t}
=\frac{\mathrm{d}y}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=L\cdot\cos(Q)\cdot\dot{Q}
$$

Vinkelhastigheten $\dot Q=\mathrm{d}Q/\mathrm{d}t$ måles i rad/s og er ikke selve vinkelen. Med L i mm er vx og vy i mm/s. Trigonometriske derivater krever radianer.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Eksempler på hastighet og fortegn

Med L=150 mm, Q=45° og ω=+0.1 rad/s har komponentene lik størrelse og peker mot venstre og oppover. Når ω skifter fortegn, gjør begge komponentene det samme. Ved Q=0° er vy=15 mm/s og vx=0.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

Prikken over $Q$ betyr **tidsderivert** $\dot Q$, ikke multiplikasjon med vinkelen. Når $\omega$ erstattes med $-\omega$, skifter begge hastighetskomponentene fortegn, men farten $L|\omega|$ endres ikke.

<a id="section-4"></a>
## 4. To ledd: relative og absolutte vinkler

Q1 er absolutt vinkel fra +X, Q2 er relativ albuevinkel. Andre ledds absolutte orientering er Q1+Q2, og vinkelhastigheten er ω₁+ω₂.

$$
X=L_1\cdot\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)
$$

$$
Y=L_1\cdot\sin(Q_1)+L_2\cdot\sin(Q_1+Q_2)
$$

$$
v_x=-L_1\cdot\sin(Q_1)\cdot\dot{Q}_1
-L_2\cdot\sin(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

$$
v_y=L_1\cdot\cos(Q_1)\cdot\dot{Q}_1
+L_2\cdot\cos(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

Begge leddene bidrar til spissens hastighet: første ledd bruker $\dot Q_1$, mens andre ledd bruker $\dot Q_1+\dot Q_2$. Å bruke bare $\dot Q_2$ for det andre leddet ville være feil fordi albuevinkelen er relativ til det første leddet.

<a id="section-5"></a>
## 5. Singulariteter i foldet og utstrakt stilling

Med L1=100 mm og L2=50 mm ligger ideell rekkevidde mellom 50 og 150 mm. Helt sammenfoldet (Q2=180°) og helt utstrakt (Q2=0°) er singulariteter: endelige leddhastigheter gir ingen momentan radial hastighet akkurat der.

$$
r^2=L_1^2+L_2^2+2L_1L_2\cos(Q_2)
$$

$$
\lvert L_1-L_2\rvert\le r\le L_1+L_2
$$

$$
\frac{\mathrm{d}r}{\mathrm{d}Q_2}
=-\frac{L_1L_2\sin(Q_2)}{r}
$$

Denne deriverte formelen forutsetter $r>0$. Hvis leddene har lik lengde ($L_1=L_2$), får vi $r=0$ når de er helt foldet tilbake til basen ($Q_2=180^\circ$), og formelen ville dele på null. Akkurat der er radialavstanden ikke deriverbar som funksjon av et **fortegnsbestemt** avvik i albuevinkelen. Unntaket gjelder ikke de ulike lengdene $L_1=100$ mm og $L_2=50$ mm i eksemplet.

Leddgrenser og kollisjoner kan innskrenke det faktiske arbeidsområdet ytterligere. At et punkt kan nås, betyr ikke at verktøyet får riktig orientering eller har tilstrekkelig klaring til hindringer.

<a id="section-6"></a>
## 6. Tre forskyvninger nær sammenfolding

Hold første ledd fast; δ er et lite vinkelavvik i radianer fra full sammenfolding. Langsforskyvning langs første ledds faste akse er forskjellig fra endringen i avstand til basen.

$$
\Delta x_{\mathrm{axis}}=L_2\bigl(1-\cos(\delta)\bigr)
\approx\frac{L_2\delta^2}{2}
$$

$$
\Delta y_{\mathrm{perp}}=L_2\cdot\sin(\delta)\approx L_2\delta
$$

$$
\Delta r=\sqrt{(L_1-L_2)^2+2L_1L_2\bigl(1-\cos(\delta)\bigr)}-(L_1-L_2)
$$

$$
L_1>L_2>0:\qquad
\Delta r\approx\frac{L_1L_2}{2(L_1-L_2)}\delta^2
$$

Identiteten 1−cosδ=2sin²(δ/2) og sin(δ/2)≈δ/2 forklarer kvadratet og faktoren 1/2. Her er radial endring ≈50δ² mm, mens aksial forskyvning ≈25δ² mm.

Tilnærmingene gjelder bare for små $\delta$ målt i radianer. Hvis $\delta$ halveres, blir både aksial og radial endring (som er kvadratiske) omtrent **en firedel**, mens tverrforskyvningen blir **halvparten**. Hvis vi krever en konstant radial hastighet ulik null mens $\delta\to0$, krever den ideelle inverse hastighetsmodellen en ubegrenset leddvinkelhastighet. En virkelig arm kan begynne å folde seg ut med endelig vinkelhastighet og radial hastighet lik null i første øyeblikk.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Aksial, tverrgående og radial forskyvning nær sammenfolding.](../../../assets/figures/folded_displacement_curves.svg)

*Aksial, tverrgående og radial forskyvning nær sammenfolding.*

For konstant, positiv radial hastighet nær foldet stilling må vinkelhastigheten øke kraftig når δ→0. I nøyaktig foldet stilling kan endelige leddhastigheter ikke gi øyeblikkelig radial hastighet.

$$
\left.\frac{\mathrm{d}r}{\mathrm{d}\delta}\right|_{L_1=100,L_2=50}
=\frac{5000\sin(\delta)}{r}
\approx100\delta\ \mathrm{mm/rad}
$$

$$
v_r\approx(100\delta)\dot\delta\ \mathrm{mm/s},
\qquad
\dot\delta\approx\frac{1\ \mathrm{mm/s}}{100\ \mathrm{mm/rad}\cdot\delta}
$$

![Nødvendig albuevinkelhastighet nær singulariteten.](../../../assets/figures/folded_radial_speed.svg)

*Nødvendig albuevinkelhastighet nær singulariteten.*

<a id="section-7"></a>
## 7. Videre: Jacobi-matrisen og løste oppgaver

Jacobi-matrisen (Jacobian matrix) kobler leddhastigheter til verktøyets hastighet. Determinanten L1L2 sin Q2 er null når leddene er kollineære. Virkelige leddgrenser og kollisjoner er ikke inkludert.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Koeffisient | Geometrien i hastighetstransformasjonen |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Utledning av determinanten.** Hver koeffisient er en partiell derivert av verktøykoordinaten X eller Y med hensyn til leddvinkelen Q1 eller Q2 i radianer. Med lengder i mm blir enheten mm/rad; multiplisert med rad/s får vi mm/s.

$$
J_{11}=\frac{\partial X}{\partial Q_1},\qquad
J_{12}=\frac{\partial X}{\partial Q_2}
$$

$$
J_{21}=\frac{\partial Y}{\partial Q_1},\qquad
J_{22}=\frac{\partial Y}{\partial Q_2}
$$

$$
\det J=J_{11}J_{22}-J_{12}J_{21}
$$

$$
\det J=L_1L_2\bigl[\sin(Q_1+Q_2)\cos(Q_1)
-\sin(Q_1)\cos(Q_1+Q_2)\bigr]
$$

$$
\det J=L_1L_2\sin\bigl((Q_1+Q_2)-Q_1\bigr)
$$

Når de to produktene i determinanten utvides, kanselleres leddene med L2 i andre potens. Sinusformelen for differansen fjerner deretter Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![De to leddbidragene summeres som vektorer til verktøyhastigheten.](../../../assets/figures/two_link_jacobian_velocity.svg)

*De to leddbidragene summeres som vektorer til verktøyhastigheten.*

### Fullstendig løste eksempler

1. Et ledd med $L=150$ mm peker mot høyre ved $Q=0^\circ$. Når $\omega=+0.1$ rad/s, har vi $\sin0^\circ=0$ og $\cos0^\circ=1$. Dermed blir $v_x=-150\cdot0\cdot0.1=0$ og $v_y=150\cdot1\cdot0.1=+15$ mm/s; spissen går oppover.
2. Ved $Q=45^\circ$ og $\omega=-0.1$ rad/s snur rotasjonen: $v_x=-150\sin45^\circ\cdot(-0.1)\approx+10.61$ mm/s og $v_y=150\cos45^\circ\cdot(-0.1)\approx-10.61$ mm/s. Spissen går nedover og til høyre, mens farten fortsatt er $L|\omega|=15$ mm/s.
3. For $L_1=100$ mm, $L_2=50$ mm, $Q_1=30^\circ$, $Q_2=60^\circ$, $\omega_1=0.1$ rad/s og $\omega_2=0.2$ rad/s blir andre ledds absolutte orientering $Q_1+Q_2=90^\circ$ og vinkelhastigheten $\omega_1+\omega_2=0.3$ rad/s. Da er $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-5-15=-20$ mm/s og $v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s.
4. Nær sammenfolding med $\delta=0.02$ rad er aksial endring langs første ledds **faste** akse omtrent $25\delta^2=25\cdot0.02^2=0.010$ mm, tverrforskyvningen $50\delta=1.000$ mm og radial økning $50\delta^2=0.020$ mm. De to kvadratiske endringene har forskjellige koeffisienter.

[Trigonometry](../TRIGONOMETRY.md) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)
