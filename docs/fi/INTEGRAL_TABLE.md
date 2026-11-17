# Integraalien kaavataulukko

**Kielet:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](../pt/INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `s` — sekunti; `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `mm/s²` — millimetri / sekunti² — kiihtyvyys; `N` — newton; `m` — metri; `N/m` — newton / metri — jäykkyys; `J` — joule. [Yksikköluettelo](UNITS.md).

[README](README.md) · [Derivaattojen taulukko](DERIVATIVE_TABLE.md) · [Differentiaali- ja integraalilaskennan perusteet](notes/00-calculus-foundations.md) · [Symbolit](SYMBOLS.md) · [Trigonometria](TRIGONOMETRY.md)

Määräämättömään integraaliin lisätään integroimisvakio $C$. Parametri $a$ on vakio, ja trigonometriset kulmat ovat radiaaneina. Kaavoja käytetään vain niiden määrittelyalueilla.

## Sisältö

- [Potenssit ja logaritmit](#section-1)
- [Eksponenttifunktiot](#section-2)
- [Trigonometriset funktiot](#section-3)
- [Rationaaliset ja käänteiset trigonometriset muodot](#section-4)
- [Juuret ja käänteisluvut](#section-5)
- [Kaavan valinta ja tarkistus](#section-6)

Aloita polynomien integraaleista ennen valinnaisia trigonometrisia ja juurifunktioiden kaavoja. Lisää jokaiseen määräämättömään integraaliin integroimisvakio $C$. Logaritmin argumentin on oltava dimensioton; ilman erillistä vertailuasteikkoa taulukon $x$ on dimensioton. Käytä kaavoja vain niiden määrittelyalueilla.

<a id="section-1"></a>
## 1. Potenssit ja logaritmit

| Kaava | Ehdot |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | kaikki reaaliluvut $x$ |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; huomioi reaalipotenssin määrittelyalue |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Eksponenttifunktiot

| Kaava | Ehdot |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | kaikki reaaliluvut $x$ |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Trigonometriset funktiot

| Kaava | Ehdot |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ radiaaneina |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ radiaaneina |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Rationaaliset ja käänteiset trigonometriset muodot

| Kaava | Ehdot |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | kaikki reaaliluvut $x$ |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Juuret ja käänteisluvut

| Kaava | Ehdot |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; väleillä, jotka eivät ylitä epäjatkuvuuskohtia |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; väleillä, jotka eivät ylitä epäjatkuvuuskohtia |

## Integraalin tarkistaminen

Derivoi määräämättömän integraalin oikea puoli: tuloksen pitää olla alkuperäinen integroitava funktio. Tarkista esimerkiksi potenssisäännön eksponentti ja kerroin derivoimalla. Määrätyssä integraalissa etsi integraalifunktio $F$ ja laske $F(b)-F(a)$.

<a id="section-6"></a>
## 6. Kaavan valinta ja tarkistus

Tunnista ensin differentiaalin jälkeinen integrointimuuttuja ($\mathrm{d}x$, $\mathrm{d}t$ tai $\mathrm{d}\theta$). Käsittele kertoimia vakioina vain, jos ne todella ovat vakioita. Lisää määräämättömään integraaliin $C$; määrätty integraali lasketaan kaavalla $F(b)-F(a)$. Tarkista vastaus derivoimalla.

### Ratkaistu esimerkki A — siirtymä mitatusta nopeudesta

Yksinkertaisessa akselimallissa $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$ aikavälillä 0–2 s. Integroidaan termit erikseen:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

Tulos on 14 mm, ei 14 mm/s. Nopeuden integrointi ajan suhteen antaa siirtymän.

### Ratkaistu esimerkki B — lineaarisesti kasvavan voiman työ

Jousen voima on $F(x)=kx$, jäykkyys $k=200\ \mathrm{N/m}$ ja venymä kasvaa nollasta arvoon 0.01 m:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

Tulos on 0.01 J. Voiman integrointi siirtymän suhteen antaa mekaanisen työn. Loppuvoiman kertominen koko matkalla antaisi liian suuren arvon.

### Ratkaistu esimerkki C — logaritmi yksinkertaisesta muutoslaista

Funktion $1/x$ integraalifunktio on $\ln|x|$. Kun dimensioton suhde $x$ kasvaa arvosta 1 arvoon 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Tulos on $\ln2\approx0.693$. Kyse ei ole metreissä mitatun pituuden logaritmista, sillä $x$ on dimensioton.
