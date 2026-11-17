# 5. Pyöriminen, lineaarinen nopeus ja singulariteetit

**Kielet:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](../../pt/notes/05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `rad` — radiaani; `rad/s` — radiaani / sekunti — kulmanopeus; `mm/rad` — millimetri / radiaani — Jacobimatriisin kerroin (pituus kulmaa kohti); `°` — aste. [Yksikköluettelo](../UNITS.md).

[Sisällysluettelo](../README.md) · [Trigonometria](../TRIGONOMETRY.md#unit-circle-values) · [Koordinaatistot](04-coordinate-frames.md) · [Differentiaali- ja integraalilaskennan perusteet](00-calculus-foundations.md)

> Vain ideaalinen synteettinen malli. Älä käytä todellisten laitteiden ohjaamiseen.

Pyörivän varren pää kulkee ympyränkaarta. Sen hetkellinen nopeus osoittaa kaaren **tangentin suuntaan**, ei varren suuntaan. Tässä luvussa edetään geometriasta aikaderivaattoihin ja lopuksi valinnaiseen Jacobin matriisiin. Derivaattojen nivelkulmat ilmaistaan radiaaneina; esimerkeissä käytetään myös asteita havainnollisuuden vuoksi.

## Sisältö

1. [Pyörivästä varresta tangentiaaliseen nopeuteen](#section-1)
2. [Mistä derivaatat tulevat?](#section-2)
3. [Lasketut nopeus- ja etumerkkiesimerkit](#section-3)
4. [Kaksi pyörivää vartta: suhteelliset ja absoluuttiset kulmat](#section-4)
5. [Taitetun ja suoristetun asennon singulariteetit](#section-5)
6. [Kolme erilaista siirtymää taitoksen lähellä](#section-6)
7. [Valinnainen Jacobin matriisi ja ratkaistut tarkistukset](#section-7)

<a id="section-1"></a>
## 1. Pyörivästä varresta tangentiaaliseen nopeuteen

Olkoon jäykän varren pituus $L$ ja kiinteä kiertopiste $O$. Aikavälillä $\Delta t>0$ kulma muuttuu määrän $\Delta Q$ verran, ja kulma mitataan **radiaaneina**. Jos kiertosuunta ei vaihdu tämän välin aikana, kärki kulkee ympyränkaarta. Kuljetun **kaaren pituus** on täsmälleen $\Delta s=L|\Delta Q|$. **Etumerkillinen matka kaarta pitkin** on $L\Delta Q$; etumerkki ilmoittaa kiertosuunnan. Tätä ei pidä sekoittaa kärjen alku- ja loppupisteiden väliseen suoraviivaiseen siirtymään (jänteeseen).

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Kun jaamme kaaren pituuden kuluneella ajalla, saamme aikavälin **keskimääräisen vauhdin**:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

**Hetkellinen vauhti** saadaan ottamalla raja-arvo $\Delta t\to0$. Kulmanopeus on $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$ yksikössä rad/s, joten kärjen vauhti on $v=L|\omega|$. Nopeusvektorin **suunta on ympyrän tangentti**, siis kohtisuorassa vartta vastaan. Kun $Q=45^\circ$ ja kiertosuunta on vastapäivään ($\omega>0$), kärki liikkuu vasemmalle ja ylös: vaakasuuntainen nopeuskomponentti on negatiivinen ja pystysuuntainen positiivinen.

$$
v=L\lvert\dot Q\rvert
$$

![Jäykän varren kärjen tangentiaalinen nopeus, Q=45 astetta, vastapäiväinen kierto ja komponenttien merkit](../../../assets/figures/link_tangent_velocity.svg)

*Jäykkä varsi ja kärjen tangentiaalinen nopeus: Q=45°, vastapäiväinen kierto, nopeuskomponenttien etumerkit.*

<a id="section-2"></a>
## 2. Mistä derivaatat tulevat?

Kärjen koordinaatit riippuvat kulmasta, joka puolestaan riippuu ajasta. Kyseessä on **kaksi eri riippuvuutta**. Ketjusääntö kertoo koordinaatin muutoksen radiaania kohti käännettyjen radiaanien määrällä sekunnissa. Sinin ja kosinin derivaatat edellyttävät radiaaneja:

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

Kulmanopeus $\dot Q=\mathrm{d}Q/\mathrm{d}t$ mitataan rad/s, eikä se ole sama asia kuin kulma. Kun $L$ ilmoitetaan millimetreinä, $v_x$ ja $v_y$ ovat yksikössä mm/s. Trigonometristen funktioiden derivointi käyttää radiaaneja.

$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Lasketut nopeus- ja etumerkkiesimerkit

Kun $Q=45^\circ$, $L=150$ mm ja $\omega=+0.1$ rad/s, kärki liikkuu vasemmalle ja ylös yhtä suurilla nopeuskomponenteilla. Kiertosuunnan vaihto arvoon −0.1 rad/s vaihtaa kummankin komponentin etumerkin, mutta ei vauhdin suuruutta. Kun $Q=0^\circ$, vaakasuuntainen nopeus on nolla ja pystysuuntainen +15 mm/s. Piste symbolin $\dot Q$ päällä tarkoittaa aikaderivaattaa, ei kertomista kulmalla.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

<a id="section-4"></a>
## 4. Kaksi pyörivää vartta: suhteelliset ja absoluuttiset kulmat

Tasomaisen kaksivartisen robotin ensimmäisen varren maailmankulma on $Q_1$ ja toisen nivelen kulma $Q_2$ on **suhteellinen**. Siksi toisen varren absoluuttinen suunta maailmassa on $Q_1+Q_2$ ja sen kulmanopeus $\omega_1+\omega_2$. Suoran kinematiikan paikkakoordinaattien derivointi antaa kummankin nivelen vaikutuksen:

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

<a id="section-5"></a>
## 5. Taitetun ja suoristetun asennon singulariteetit

Ideaalisilla rajoittamattomilla varsilla $L_1=100$ mm ja $L_2=50$ mm etäisyys $r$ vaihtelee 50 mm:stä (täysin taitettu $Q_2=\pm180^\circ$) 150 mm:iin (täysin suora $Q_2=0^\circ$). Molemmissa samalla suoralla olevissa asennoissa nivelten tuottamat hetkelliset nopeudet ovat poikittaisia varsien linjaan nähden: **mielivaltaista säteensuuntaista nopeutta ei voi tuottaa täsmälleen tässä asennossa äärellisillä nivelnopeuksilla**. Nivelrajat ja törmäykset voivat pienentää todellista työaluetta. Paikan saavutettavuus ei takaa työkalun orientaatiota eikä esteettömyyttä.

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

Derivaatan kaava edellyttää, että $r>0$. Kun kaksi yhtä pitkää vartta taittuu täsmälleen jalustaan ($L_1=L_2$, $Q_2=180^\circ$), $r=0$ ja kaavassa jaetaan nollalla. Säteittäinen etäisyys ei ole tässä pisteessä derivoituva kyynärkulman etumerkillisen poikkeaman funktiona. Tämä ei vaikuta alla oleviin eripituisten varsien esimerkkeihin.

<a id="section-6"></a>
## 6. Kolme erilaista siirtymää taitoksen lähellä

Kiinnitetään ensimmäinen varsi vaakasuoraan ja oletetaan toisen varren osoittavan aluksi taaksepäin. Olkoon $\delta\ge0$ pieni poikkeama täysin taitetusta asennosta radiaaneina. Ensimmäisen varren **kiinteän akselin suuntainen siirtymä** ei ole sama asia kuin etäisyyden muutos jalustasta kärkeen. Tarkat yhtälöt ovat:

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

Neliö ja kerroin 1/2 seuraavat identiteetistä $1-\cos\delta=2\sin^2(\delta/2)$ ja pienen kulman approksimaatiosta $\sin(\delta/2)\approx\delta/2$. Erikokoisilla varsilla säteittäisen muutoksen kerroin on erilainen: $\Delta r\approx50\delta^2$ mm, mutta kiinteän akselin suuntainen muutos on noin $25\delta^2$ mm. Kulman $\delta$ puolittaminen pienentää kumpaakin neliöllistä muutosta neljäsosaan mutta poikittaista siirtymää vain puoleen. Approksimaatiot pätevät vain pienille kulmille.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Kolme siirtymää taitetun varren avautuessa, kulmat kuvassa asteina ja approksimaatiot radiaaneina](../../../assets/figures/folded_displacement_curves.svg)

*Kolme siirtymää taitetun varren avautuessa. Kuvaajan kulmat esitetään asteina, mutta approksimaatiot lasketaan radiaaneina.*

Jos vaaditaan vakioista, nollasta poikkeavaa ulospäin suuntautuvaa säteisnopeutta $v_r$ lähellä taitettua rajaa, kyynärnivelen kulmanopeuden täytyy kasvaa, kun $\delta$ lähestyy nollaa. Täsmälleen kohdassa $\delta=0$ ensimmäisen kertaluvun säteisnopeus on nolla kaikilla äärellisillä nivelnopeuksilla. Ideaalinen käänteisnopeusvaatimus kasvaa rajatta. Todellinen robotti voi avautua äärellisellä kulmanopeudella, jolloin säteisnopeus alkaa nollasta ja kasvaa vähitellen.

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

![Kyynärnivelen kulmanopeus, jolla säteisnopeus 1 mm/s säilyisi, ja singulariteettiraja](../../../assets/figures/folded_radial_speed.svg)

*Kyynärnivelen kulmanopeus, jota tarvittaisiin 1 mm/s säteisnopeuden ylläpitämiseen; singulariteettiraja näkyy kuvassa.*

<a id="section-7"></a>
## 7. Valinnainen Jacobin matriisi ja ratkaistut tarkistukset

Jacobin matriisi kokoaa työkalun koordinaattien osittaisderivaatat nivelkulmien suhteen. Se muuntaa **hetkelliset nivelnopeudet työkalun nopeudeksi**, ei nivelten paikkoja absoluuttisiksi koordinaateiksi. Tässä ideaalissa tasomallissa determinantti on nolla täsmälleen silloin, kun $\sin Q_2=0$: suorassa ja taitetussa asennossa. Näiden asentojen lähellä käänteinen nopeusmuunnos on huonosti ehdollistunut. Malli on tarkoitettu vain oppimiseen; oikeissa järjestelmissä on lisäksi nivelrajat, työkalusiirtymät, välys, jousto ja törmäysriskit.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Kerroin | Nopeusmuunnoksen geometria |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |

**Determinantin johtaminen.** Jokainen kerroin on työkalun X- tai Y-koordinaatan osittaisderivaatta nivelkulman Q1 tai Q2 suhteen radiaaneina. Kun pituus on mm, yksikkö on mm/rad; kertominen yksiköllä rad/s tuottaa mm/s.

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

Kun determinantin kaksi tuloa avataan, L2:n neliön sisältävät termit kumoavat toisensa. Sinien erotuskaava poistaa sen jälkeen Q1:n.

$$
\det J=L_1L_2\sin(Q_2)
$$

![Nivelten kaksi nopeusosuutta lasketaan yhteen vektoreina työkalun nopeudeksi.](../../../assets/figures/two_link_jacobian_velocity.svg)

*Nivelten kaksi nopeusosuutta lasketaan yhteen vektoreina työkalun nopeudeksi.*

### Täysin ratkaistut tarkistustehtävät

1. Yksi jäykkä 150 mm varsi osoittaa oikealle ($Q=0^\circ$). Kun $\omega=+0.1$ rad/s, $v_x=0$ ja $v_y=150\cdot0.1=+15$ mm/s. Nopeus osoittaa ylös.
2. Kun $Q=45^\circ$ ja $\omega=-0.1$ rad/s (myötäpäivään), $v_x=-150\sin45^\circ(-0.1)=+10.61$ mm/s ja $v_y=150\cos45^\circ(-0.1)=-10.61$ mm/s. Kärki liikkuu alas ja oikealle; vauhdin suuruus pysyy 15 mm/s.
3. Kun $L_1=100$ mm, $L_2=50$ mm, $Q_1=30^\circ$, $Q_2=60^\circ$, $\omega_1=0.1$ rad/s ja $\omega_2=0.2$ rad/s, toisen varren absoluuttinen kulmanopeus on 0.3 rad/s. Siksi $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-20$ mm/s ja $v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s.
4. Kun taitetusta asennosta poiketaan $\delta=0.02$ rad, kiinteän akselin suuntainen muutos on noin $25\cdot0.02^2=0.010$ mm, poikittainen siirtymä noin $50\cdot0.02=1.000$ mm ja jalustan ja kärjen välisen etäisyyden kasvu noin $50\cdot0.02^2=0.020$ mm. Älä sekoita neliöllisten termien eri kertoimia.

[Trigonometria](../TRIGONOMETRY.md) · [Koordinaatistot](04-coordinate-frames.md) · [Differentiaali- ja integraalilaskennan perusteet](00-calculus-foundations.md)
