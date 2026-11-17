# 1. Liike, derivaatat ja integraalit

**Muut kielet:** [en](../../en/notes/01-motion-calculus.md) · [fr](../../fr/notes/01-motion-calculus.md) · [de](../../de/notes/01-motion-calculus.md) · [it](../../it/notes/01-motion-calculus.md) · [es](../../es/notes/01-motion-calculus.md) · [pt](../../pt/notes/01-motion-calculus.md) · [zh](../../zh/notes/01-motion-calculus.md) · [ja](../../ja/notes/01-motion-calculus.md) · [nb](../../nb/notes/01-motion-calculus.md) · [ru](../../ru/notes/01-motion-calculus.md) · [ko](../../ko/notes/01-motion-calculus.md) · [fi](01-motion-calculus.md) · [pl](../../pl/notes/01-motion-calculus.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `s` — sekunti; `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `mm/s²` — millimetri / sekunti² — kiihtyvyys; `%` — prosentti (sadasosa). [Yksikköluettelo](../UNITS.md).

**Kertaus:** [0. Differentiaali- ja integraalilaskennan perusteet](00-calculus-foundations.md) · [Integraalitaulukko](../INTEGRAL_TABLE.md)

[Sisällysluettelo](../README.md) · [Kaavakooste](../CHEATSHEET.md) · [Harjoitukset](../exercises/README.md) · [Seuraava luku](02-first-order-dynamics.md)

> **Tarkkuushuomautus:** Seuraava malli on yksinkertaistettu ja yksiulotteinen. Tarkista yksiköt, koordinaattien suunnat ja numeerinen tarkkuus ennen soveltamista.

## Pikakertaus

- **Kuljettu matka** on reitin kokonaispituus, kun taas **siirtymä** on loppu- ja alkupaikan erotus.
- **Vauhti** on epänegatiivinen; **nopeus** sisältää suunnan ja voi olla valitun akselin suhteen negatiivinen.
- Paikan aikaderivaatta antaa hetkellisen nopeuden. Etumerkillisen nopeuden integraali antaa siirtymän.
- **Eksplisiittinen Euler-integrointi** arvioi muuttuvaa suuretta olettamalla sen derivaatan vakioksi lyhyen aika-askeleen ajaksi.

## Tämän sivun sisältö

- [1. Matka, siirtymä, vauhti ja nopeus](#section-1)
- [2. Derivaatta: hetkellinen nopeus](#section-2)
- [3. Integraali: siirtymä ja kuljettu matka](#section-3)
- [4. Numeerinen integrointi](#section-4)
- [5. Kokeile itse](#section-5)
- [6. Lisätiedot (valinnainen)](#section-6)
  - [Miksi funktion 2t^2 derivaatta on 4t](#power-rule-derivation)
  - [Siirtymätaulukon arvojen johtaminen](#motion-values-derivation)

[SI-merkinnät ja desimaalipiste](../SYMBOLS.md)

<a id="section-1"></a>
## 1. Matka, siirtymä, vauhti ja nopeus

Kaavojen johtaminen, yksiköt ja numeeriset rajoitukset käsitellään kohdassa [Lisätiedot](#section-6).

Ajatellaan virtuaalista akselia, joka liikkuu nopeudella $+3\ \mathrm{mm/s}$ kaksi sekuntia ja sen jälkeen nopeudella $-3\ \mathrm{mm/s}$ toiset kaksi sekuntia. Siirtymä on $+6-6=0\ \mathrm{mm}$, mutta kuljettu matka on $6+6=12\ \mathrm{mm}$. Kummassakin vaiheessa vauhti on $3\ \mathrm{mm/s}$; etumerkillisen nopeuden suunta vaihtuu.

Aikavälillä $[t_1,t_2]$:

$$
\text{keskinopeus}=\frac{x(t_2)-x(t_1)}{t_2-t_1},\qquad
\text{keskivauhti}=\frac{\text{kuljettu kokonaismatka}}{t_2-t_1}.
$$

Kahdessa tai kolmessa ulottuvuudessa nopeus on vektori. Tasaisella vauhdilla ympyrää kiertävän kappaleen nopeusvektori muuttuu, koska sen suunta muuttuu. Jos kappale palaa kierroksen jälkeen lähtöpisteeseen, koko kierroksen keskinopeusvektori on nolla.

**Koko neljän sekunnin aikavälillä** etumerkillinen keskinopeus ja keskivauhti antavat **eri tulokset**. Akseli palaa lähtöpisteeseen, vaikka kuljettu matka on 12 mm:

$$
\overline{v}_x=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}
$$

$$
\overline{\lvert v\rvert}=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}
$$

Keskivauhti **ei välttämättä ole keskinopeusvektorin itseisarvo**. Yhden kokonaisen ympyräkierroksen jälkeen keskinopeusvektori on myös nolla, mutta kuljettu matka ja keskivauhti ovat positiivisia.

<a id="section-2"></a>
## 2. Derivaatta: hetkellinen nopeus

Kun paikkafunktio $x(t)$ on derivoituva,

$$
v(t)=\frac{dx}{dt}.
$$

Jos $x(t)=2t^2\ \mathrm{mm}$ ja aika mitataan sekunteina, niin $v(t)=4t\ \mathrm{mm/s}$. **Miksi kerroin on 4?** Potenssifunktion derivointisääntö antaa $d(t^2)/dt=2t$. Siksi funktion $2t^2$ derivaatta on $2\cdot2t=4t$. [Kaavan johtaminen yksikköineen](#power-rule-derivation). Hetkellä $t=1\ \mathrm{s}$ hetkellinen nopeus on $4\ \mathrm{mm/s}$.

Eteenpäin laskettu erotusosamäärä antaa arvion

$$
v(t)\approx\frac{x(t+\Delta t)-x(t)}{\Delta t}.
$$

Hetkellä $t=1\ \mathrm{s}$ aika-askeleet $\Delta t=1;\ 0.1;\ 0.01\ \mathrm{s}$ antavat vastaavasti $6;\ 4.2;\ 4.02\ \mathrm{mm/s}$. Tässä esimerkissä pienemmät askeleet lähestyvät tarkkaa derivaattaa, mutta lopulta liukulukujen pyöristysvirhe rajoittaa tarkkuutta.

**Miksi liian pieni aika-askel antaa virheellisen tuloksen:** Hetkellä $t=1\ \mathrm{s}$ funktion $x(t)=2t^2$ tarkka derivaatta on $4\ \mathrm{mm/s}$. Jos $dt=1e-17\ \mathrm{s}$, Pythonin `float` pyöristää laskun `t + dt` takaisin arvoksi `t`. Lasketut sijainnit ovat samat ja erotus antaisi virheellisesti nopeudeksi nolla. Vielä pienemmillä lukuarvoilla molemmat sijainnit voivat alivuotaa nollaan, vaikka derivaatta ei olisi nolla. Harjoituksen [`forward_derivative`](../../../exercises/01_motion_and_integral.py) antaa näissä tilanteissa `ValueError`-virheen väärän nollatuloksen sijaan. Se laskee edelleen aidon äärellisen erotuksen; aika-askeleen on oltava numeerisesti erotettavissa, eikä sitä pidä pienentää rajatta.

<a id="section-3"></a>
## 3. Integraali: siirtymä ja kuljettu matka

Yksiulotteiselle etumerkilliselle nopeudelle $v(t)$ pätee

$$
x(t_2)-x(t_1)=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t,\qquad
s=\int_{t_1}^{t_2}|v(t)|\ \mathrm{d}t.
$$

Ensimmäinen integraali voi olla negatiivinen tai nolla; toinen ei voi olla negatiivinen. Ensimmäinen vastaa geometrisesti nopeus–aika-käyrän etumerkillistä pinta-alaa. **Tämä on eri esimerkki kuin luvussa 2:** aiemman paikan $x(t)=2t^2$ derivaatta on $v(t)=4t$, kun taas seuraavassa integrointiesimerkissä käytetään tarkoituksella nopeutta $v(t)=2t$. Sitä vastaava paikka on $x(t)=t^2+C$ (yksiköt huomioiden). Kun $v(t)=2t\ \mathrm{mm/s}$ välillä $0\le t\le2\ \mathrm{s}$, siirtymä on $4\ \mathrm{mm}$.

<a id="section-4"></a>
## 4. Numeerinen integrointi

Tarkan siirtymän ja vasemman päätepisteen Euler-arvion vertailu (synteettinen aineisto).

![Tarkka siirtymä ja vasemman päätepisteen Euler-arvio](../../../assets/figures/euler_vs_exact.svg)

Eksplisiittinen Eulerin menetelmä käyttää derivaattaa kunkin välin **alussa**:

$$
x_{n+1}=x_n+v(t_n)\ \Delta t.
$$

Kun $v(t)=2t\ \mathrm{mm/s}$ välillä $t=0$–$2\ \mathrm{s}$:

| Aika-askel $\Delta t$ | Eulerin siirtymä |
| ---: | ---: |
| $0.5\ \mathrm{s}$ | $3.000\ \mathrm{mm}$ |
| $0.1\ \mathrm{s}$ | $3.800\ \mathrm{mm}$ |
| $0.01\ \mathrm{s}$ | $3.980\ \mathrm{mm}$ |
| Tarkka integraali | $4.000\ \mathrm{mm}$ |

Eulerin menetelmä aliarvioi tässä esimerkissä siirtymän, koska nopeus kasvaa jokaisella aikavälillä. Puolisuunnikassääntö käyttää päätepisteiden keskiarvoa ja antaa tarkan integraalin lineaariselle nopeusfunktiolle, mutta ei välttämättä epälineaariselle funktiolle.

[Katso, miten arvot 3, 3.8 ja 3.98 lasketaan.](#motion-values-derivation)

<a id="section-5"></a>
## 5. Kokeile itse

Suorita [`01_motion_and_integral.py`](../../../exercises/01_motion_and_integral.py). Tutki, miten $\Delta t$:n pienentäminen vaikuttaa tulokseen. Selitä sitten, miksi edestakaisen matkan siirtymä voi olla nolla, vaikka kuljettu matka on positiivinen.

Esimerkit perustuvat synteettiseen aineistoon eivätkä ohjaa todellisia laitteita.

<a id="section-6"></a>
## 6. Lisätiedot (valinnainen)

### Yksiköt ja kertoimien merkitys

Jos $t$ mitataan sekunteina, merkintä $x(t)=2t^2$ millimetriä on lyhennys: kertoimen yksikkö on $2\ \mathrm{mm/s^2}$. Tällöin $v(t)=4t$ ilmaistaan yksikössä mm/s. Tarkista aina yksiköt ennen lukuarvojen sijoittamista kaavoihin.

### Erotusosamäärä ja numeerinen virhe

Erotusosamäärä arvioi derivaattaa äärellisellä aika-askeleella eikä ole täsmälleen sama kuin hetkellinen arvo. Sileille funktioille pienempi askel vähentää katkaisuvirhettä, mutta hyvin pieni askel voi lisätä liukulukujen kumoutumisvirhettä tai mittauskohinan vaikutusta. Euler-integrointi käyttää aika-askeleen alun arvoa ja aliarvioi kasvavan lineaarisen nopeuden integraalin.

### Useampi ulottuvuus

Paikkavektorille $\mathbf r(t)$ nopeusvektori on $\mathbf v(t)=d\mathbf r/dt$. Vauhti on vektorin normi $\|\mathbf v\|$, ja kuljettu matka on $s=\int\|\mathbf v(t)\|dt$.

<a id="power-rule-derivation"></a>
### Miksi funktion $2t^2$ derivaatta on $4t$

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
### Siirtymätaulukon arvojen johtaminen

$$
a=2\ \mathrm{mm/s^2},\qquad v(t)=at,\qquad 0\le t\le2\ \mathrm{s}.
$$

$$
\Delta x=\int_{0}^{2\ \mathrm{s}}at\ \mathrm{d}t
=\left[\frac{at^2}{2}\right]_{0}^{2\ \mathrm{s}}
=4\ \mathrm{mm}.
$$

Merkki $\sum$ on kreikkalainen iso **sigma**, ja se tarkoittaa termien **summaamista**. Lausekkeessa $\sum_{n=0}^{N-1}(2nh)h$ indeksi $n$ saa arvot $0;1;\ldots;N-1$, eli termejä on $N$. Ajattele Pythonin `for`-silmukkaa, joka lisää yhden termin kerrallaan. Esimerkiksi $\sum_{n=1}^{3}n=1+2+3=6$. [Symbolien selitykset](../SYMBOLS.md).

$$
h=\frac{dt}{1\ \mathrm{s}},\qquad N=\frac{2}{h}.
$$

$$
x_{\mathrm{Euler}}(2\ \mathrm{s})
=\left[\sum_{n=0}^{N-1}(2nh)h\right]\ \mathrm{mm}
=\left[h^2N(N-1)\right]\ \mathrm{mm}
=(4-2h)\ \mathrm{mm}.
$$

Tässä `h` on sekunteina mitatun aika-askeleen `dt` **lukuarvo**: esimerkiksi `dt = 0.5 s` tarkoittaa `h = 0.5`. `N` on askelten määrä. Tulos on **millimetreinä ilmoitettu matka**, ei dimensioton luku.

Aika-askeleilla `dt = 0.5`, `0.1` ja `0.01` sekuntia saadaan 3 mm, 3.8 mm ja 3.98 mm. Lasku olettaa, että dimensioton askelmäärä $N=(2\ \mathrm{s})/dt$ on kokonaisluku.


[SI-yksiköt ja merkintätavat](../SYMBOLS.md#si-notation) · [Summamerkki Σ](../SYMBOLS.md#summation)

Nopeus (velocity) on etumerkillinen paikan muutosnopeus; vauhti (speed) on sen itseisarvo.
