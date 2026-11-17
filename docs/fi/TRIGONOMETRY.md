# Trigonometria: kulmat, sini, kosini ja tangentti

**Languages:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](../it/TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `°` — aste; `rad` — radiaani; `kg` — kilogramma; `m` — metri; `m/s²` — metri / sekunti² — kiihtyvyys; `N·m` — newton · metri — vääntömomentti; `mm` — millimetri = 0.001 m; `N` — newton. [Yksikköluettelo](UNITS.md).

[README](README.md) · [Integraalit](INTEGRAL_TABLE.md) · [Symbolit](SYMBOLS.md)

<a id="unit-circle-values"></a>
## Yksikköympyrä: sini ja kosini

Yksikköympyrässä kulmaa $\theta$ vastaavan pisteen koordinaatit ovat $(\cos\theta,\sin\theta)$. Kulma mitataan positiiviselta X-akselilta vastapäivään. Taulukossa on tarkat arvot ja desimaalilikiarvot.

![Yksikköympyrän 16 kulmaa](../../assets/figures/unit_circle_reference.svg)

Kuvassa näkyvät kaikkien 16 kulman tarkat etumerkilliset koordinaattiparit. Taulukko sisältää myös desimaalilikiarvot, tangentin ja arkustangentin pääarvot. Desimaalit on pyöristetty neljään desimaaliin. Kulmassa 360° arvot toistavat kulman 0° arvot.

*Yksikköympyrä ja kaikkien 16 kulman koordinaattiparit (cos θ, sin θ).*

| θ | cos θ (tarkka arvo) | cos θ (desimaaliarvo) | sin θ (tarkka arvo) | sin θ (desimaaliarvo) | tan θ (tarkka arvo) | tan θ (desimaaliarvo) | arctan(tan θ), pääarvo |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **ei määritelty** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **ei määritelty** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

Kulmissa $90^\circ$ ja $270^\circ$ tangenttia ei ole määritelty, koska $\cos\theta=0$. Lauseke $\arctan(\tan\theta)$ antaa pääarvon väliltä $(-90^\circ,90^\circ)$, ei välttämättä alkuperäistä kulmaa.

Esimerkiksi $\arctan(\tan135^\circ)=-45^\circ$ ja $\arctan(\tan225^\circ)=45^\circ$. Arkustangenttia ei voida laskea niissä kahdessa kulmassa, joissa tangentti ei ole määritelty.

<a id="trigonometric-identities"></a>
## Keskeiset trigonometriset identiteetit

Kun kulmaa siirretään 90°, sini ja kosini vaihtavat paikkaa ja joissakin tapauksissa etumerkki muuttuu. Sulkeet ovat olennaisia: $\cos(\theta-90^\circ)$ tarkoittaa kosinin laskemista vasta kulman vähentämisen jälkeen.

$$
\cos(90^\circ-\theta)=\sin(\theta),\qquad
\sin(90^\circ-\theta)=\cos(\theta)
$$

$$
\cos(\theta-90^\circ)=\sin(\theta),\qquad
\sin(\theta+90^\circ)=\cos(\theta)
$$

$$
\cos(\theta+90^\circ)=-\sin(\theta),\qquad
\sin(\theta-90^\circ)=-\cos(\theta)
$$

$$
\sin(-\theta)=-\sin(\theta),\qquad
\cos(-\theta)=\cos(\theta)
$$

$$
\tan(-\theta)=-\tan(\theta),\qquad
\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}
$$

$$
\sin(\theta+360^\circ)=\sin(\theta),\qquad
\cos(\theta+360^\circ)=\cos(\theta)
$$

$$
\tan(\theta+180^\circ)=\tan(\theta),\qquad
\sin^2(\theta)+\cos^2(\theta)=1
$$

Etumerkit neljänneksittäin järjestyksessä (kosini, sini, tangentti): I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Negatiivinen kulma mitataan myötäpäivään. Käänteisen trigonometrisen funktion kulmaa arvioitaessa tarkista yksikköympyrän merkit ja funktion sopiva monotoninen väli.

<a id="inverse-cosine-reference"></a>
## Arkuskosini ja kulman arviointi

Välillä $0^\circ$–$180^\circ$ kosini pienenee arvosta 1 arvoon −1. $\arccos(0.19)\approx79.05^\circ$. Kosini on parillinen: $\cos(79.05^\circ)=\cos(-79.05^\circ)$.

Koska $\cos80^\circ\approx0.1736$, $\arccos(0.19)$ on hieman alle 80° eli noin 79.05°. Kosini on parillinen, mutta arkuskosinin pääarvo on välillä 0°–180°. Siksi kyynärnivelen suhteelliselle kulmalle voi olla kaksi ratkaisua ±79.05°.

![Arkuskosinin viitekäyrä](../../assets/figures/arccos_reference_curve.svg)

## Suorakulmaisen kolmion sivut

![Right-triangle ratios](../../assets/figures/trig_ratios.svg)

Suorakulmaisessa kolmiossa $a$ on vastainen kateetti, $b$ viereinen kateetti ja $c$ hypotenuusa. Terävälle kulmalle $\theta$ pätee:

$$
\sin\theta=\frac{a}{c},\qquad \cos\theta=\frac{b}{c},\qquad \tan\theta=\frac{a}{b}\quad(b\ne0).
$$

Sivujen pituudet eivät ole negatiivisia. Suorakulmaisen kolmion kuva ei yksin kerro sinin ja kosinin etumerkkejä negatiivisilla kulmilla tai muissa neljänneksissä. Positiiviselta x-akselilta mitatulle suunnatulle kulmalle $\sin(+60^\circ)=+\sqrt3/2$ mutta $\sin(-60^\circ)=-\sqrt3/2$.

## Mekaniikan esimerkki: painovoiman momentti vivussa

Kun massa $m$ sijaitsee etäisyydellä $L$ nivelestä ja vipu muodostaa vaakatasoon kulman $\theta$, painovoiman momentin itseisarvo ideaalissa pistemassamallissa on:

$$
|M_g|=mgL|\cos\theta|.
$$

Kun $m=0.5\ \mathrm{kg}$, $L=0.2\ \mathrm{m}$ ja $g=9.81\ \mathrm{m/s^2}$, momentin itseisarvo kulmassa $\theta=60^\circ$ on $0.4905\ \mathrm{N\cdot m}$. Momentin merkki riippuu sovitusta kiertosuunnasta. Samassa mallissa momentin itseisarvo on 0.981 N·m kulmassa 0° ja nolla kulmassa 90°.

## Kulman ratkaiseminen geometriasta

Jos vaakasuora etenemä on $0.1\ \mathrm{m}$ ja korkeuden muutos $0.05\ \mathrm{m}$, kulmakerroin on $0.5$.

$$
\theta=\arctan\left(\frac{0.05}{0.1}\right)\approx26.565^\circ,\qquad
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

Tarkista aina, käyttävätkö ohjelmointikirjastot radiaaneja vai asteita. Esimerkit ovat opiskelua varten.

Sama kulma radiaaneina on:

$$
\arctan(0.5)\approx26.565^\circ,\qquad \arctan(0.5)\approx0.46365\ \mathrm{rad}.
$$


### Vektorin suunta: miksi `atan2` tarvitaan

Origosta pisteeseen $(x,y)$ kulkevan vektorin tavallinen arkustangentti käyttää vain suhdetta $y/x$. Vektoreilla $(1, -1)$ ja $(-1, 1)$ on sama suhde, mutta ne osoittavat **eri neljänneksiin**. Kun $x=-1\ \mathrm{mm}$ ja $y=+1\ \mathrm{mm}$, pelkän suhteen käyttäminen antaa väärän suunnan maailman koordinaatistossa:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` ottaa huomioon **molempien komponenttien etumerkit** ja palauttaa nollasta poikkeavan 2D-vektorin suunnan. Argumenttien on käytettävä samaa pituusyksikköä. Kun $x=0$, suhdetta $y/x$ ei ole määritelty, mutta `atan2` antaa akselin suunnan, jos $y\ne0$. Pisteessä $(0, 0)$ suunta on määrittelemätön; $+180^\circ$ ja $-180^\circ$ kuvaavat samaa suuntaa. Tämä on olennaista [koordinaatistokulmia](notes/04-coordinate-frames.md) laskettaessa.

## Kosinilause: kaksivartisen mekanismin geometria

![Kaksivartinen kolmio OAB ja kosinilause](../../assets/figures/two_link_cosine_law.svg)

Jalusta O, kyynärnivel A ja työkalu B muodostavat kolmion. OA=$L_1$, AB=$L_2$ ja OB=$r$ on suora etäisyys jalustasta työkaluun. Kuvassa $L_1=100$ mm, $L_2=50$ mm ja $r=120$ mm. Kolmion sisäkulma $\varphi$ eroaa kyynärnivelen suhteellisesta kulmasta $\theta_2$: $\varphi=180^\circ-|\theta_2|$. Kuvassa $\theta_2$ on negatiivinen; peilikuva-asennossa se on positiivinen.

$$
r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi
=L_1^2+L_2^2+2L_1L_2\cos\theta_2
$$

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=0.19
$$

Siksi $|\theta_2|\approx79.05^\circ$. Määrättyyn pisteeseen $(X,Y)$ pääsemiseksi on ratkaistava myös ensimmäisen nivelen kulma $\theta_1$.

[Differentiaali- ja integraalilaskenta](notes/00-calculus-foundations.md) · [Takaisinkytketty säätö](notes/03-feedback-control.md)
