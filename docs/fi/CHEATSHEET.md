# Kaavakooste — liike ja ensimmäisen kertaluvun järjestelmät

**Kielet:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](../nb/CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `s` — sekunti; `m` — metri; `m/s` — metri / sekunti — lineaarinen nopeus; `rad/s` — radiaani / sekunti — kulmanopeus; `kg·m²` — kilogramma · metri² — hitausmomentti; `N·m` — newton · metri — vääntömomentti; `N·m·s/rad` — newton · metri · sekunti / radiaani — nopeuteen suhteutettu vahvistus; `J` — joule; `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `%` — prosentti (sadasosa). [Yksikköluettelo](UNITS.md).

[Sisällysluettelo](README.md) · [Liike](notes/01-motion-calculus.md) · [Dynamiikka](notes/02-first-order-dynamics.md) · [Harjoitukset](exercises/README.md)

> **Ei ole tekninen suunnitteluspesifikaatio.** Tarkista yksiköt ja idealisoivat oletukset ennen käyttöä.

| Käsite | Määritelmä tai kaava |
| --- | --- |
| Siirtymä | $\Delta x=x_2-x_1$ (etumerkillinen) |
| Kuljettu matka | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ (epänegatiivinen) |
| Keskimääräinen nopeus (etumerkillinen) | $\bar v=\frac{\Delta x}{\Delta t}$ (1D, etumerkillinen) |
| Keskimääräinen vauhti | $\frac{s}{\Delta t}$ (epänegatiivinen) |
| Hetkellinen nopeus | $v(t)=\frac{dx}{dt}$  |
| Siirtymä nopeudesta | $\Delta x=\int_{t_1}^{t_2}v(t)\ \mathrm{d}t$  |
| Eksplisiittinen Euler-integrointi | $x_{n+1}=x_n+v_n\ dt$  |
| Ensimmäisen kertaluvun dynamiikka | $\frac{dv}{dt}=\frac{u-v}{\tau}$  |
| Nopeusvirhe | $\varepsilon(t)=u-v(t)$  |
| Tarkka askelvaste | $v(t)=u+(v_0-u)\exp\!\left(-\frac{t}{\tau}\right)$ (kun $u$ on vakio) |
| Aikavakio | Kun $t=\tau$, noin 63.2 % kokonaismuutoksesta on tapahtunut |
| Yksinkertaistettu momenttimalli | $M=K(u-\omega)$  |
| Pyörimiskiihtyvyys | $M=J\alpha,\quad\alpha=\frac{d\omega}{dt}$  |
| Mallin aikavakio | $\tau=\frac{J}{K}$ (vain momenttimallin oletuksilla) |
| Pyörimisenergia | $E=\frac{1}{2}J\omega^2$  |

**Merkinnät:** $\varepsilon$ on nopeusvirhe ja $\mathrm{e}\approx2.71828$ Eulerin luku. $\exp(z)=\mathrm{e}^{z}$ on luonnollinen eksponenttifunktio. Symbolit eivät tarkoita samaa asiaa.

**SI-yksiköt:**

| Suure | Nimi | Yksikkö |
| --- | --- | --- |
| `t, dt, τ` | Aika | s (sekunti) |
| `x` | Paikka | m (metri) |
| `v` | Vauhti | m/s (metriä sekunnissa) |
| `ω` | Kulmanopeus | rad/s (radiaania sekunnissa) |
| `J` | Hitausmomentti | kg·m² |
| `M` | Momentti | N·m |
| `K` | Momenttivahvistus | N·m·s/rad |
| `E` | Energia | J (joule) |

Keskipiste `·` tarkoittaa kertolaskua, ei luettelon erotinta. Lineaarisessa mallissa $u$ on lineaarinen nopeus ja pyörimismallissa kulmanopeus.

**Tavallisia virheitä:** Vauhti ei ole sama kuin etumerkillinen nopeus. Kuljettu matka ei ole sama kuin siirtymä. Aika-askel $dt$ ei ole aikavakio $\tau$. Yhden aikavakion jälkeen tavoitetta ei ole vielä täysin saavutettu. $J/K$ ei ole yleinen laki kaikille moottoreille. Mekaaninen energia ei ole sama kuin sähköinen energiankulutus.

[Lisätietoja derivoinnista ja integroinnista](notes/01-motion-calculus.md#section-6) · [Mallin oletukset ja Eulerin vakaus](notes/02-first-order-dynamics.md#section-7)

[Aikavakion prosenttilukujen johtaminen](notes/02-first-order-dynamics.md#time-constant-derivation)

[Arvojen 3, 3.8 ja 3.98 laskeminen](notes/01-motion-calculus.md#motion-values-derivation)

## Symbolit ja merkintätavat

**Σ / ∑ (summa)** tarkoittaa termien yhteenlaskua. Esimerkki: $\sum_{n=1}^{3}n=1+2+3=6$. Ylä- ja alarajat kertovat summattavat termit. [Lisää symboleista](SYMBOLS.md).

## Integraalitaulukko

[Differentiaali- ja integraalilaskennan perusteet](notes/00-calculus-foundations.md) · [Integraalitaulukko](INTEGRAL_TABLE.md)

## Takaisinkytkentäsäätö: PID ja pitomomentti

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[PID ja pitomomentti](notes/03-feedback-control.md) · [Trigonometriataulukko ja mekaniikan esimerkit](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Pyöriminen, nopeus ja Jacobin matriisi

Nivelten kulmanopeudet ilmoitetaan rad/s; pituuksien ollessa millimetreinä lineaarinen nopeus on mm/s.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Pyöriminen, nopeus ja Jacobin matriisi](notes/05-velocity-jacobian.md)
