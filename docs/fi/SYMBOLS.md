# Symbolit ja merkintätavat

**Kielet:** [en](../en/SYMBOLS.md) · [fr](../fr/SYMBOLS.md) · [de](../de/SYMBOLS.md) · [it](../it/SYMBOLS.md) · [es](../es/SYMBOLS.md) · [pt](../pt/SYMBOLS.md) · [zh](../zh/SYMBOLS.md) · [ja](../ja/SYMBOLS.md) · [nb](../nb/SYMBOLS.md) · [ru](../ru/SYMBOLS.md) · [ko](../ko/SYMBOLS.md) · [fi](SYMBOLS.md) · [pl](../pl/SYMBOLS.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `s` — sekunti; `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `kg·m²` — kilogramma · metri² — hitausmomentti; `N·m` — newton · metri — vääntömomentti; `N·m·s/rad` — newton · metri · sekunti / radiaani — nopeuteen suhteutettu vahvistus; `rpm` — kierros minuutissa; `rad/s` — radiaani / sekunti — kulmanopeus; `%` — prosentti (sadasosa). [Yksikköluettelo](UNITS.md).

[Sisällysluettelo](README.md) · [Kaavakooste](CHEATSHEET.md) · [Liike](notes/01-motion-calculus.md) · [Dynamiikka](notes/02-first-order-dynamics.md)

## Sisältö

- [Σ: iso sigma ja summa](#summation)
- [Samannäköiset mutta eri symbolit](#different-symbols)
- [Markdownin matematiikkarajaimet](#math-delimiters)
- [Desimaalipiste, SI-yksiköt ja matemaattiset välit](#si-notation)

<a id="summation"></a>
## Σ / ∑ — Summa

$\sum$ on kreikkalainen iso **sigma** ja tarkoittaa **summaamista**. Lausekkeessa $\sum_{n=0}^{N-1}(2nh)h$ indeksi $n$ saa arvot $0, 1,\ldots,N-1$, joten yhteenlaskettavia termejä on $N$. Ajattele Pythonin `for`-silmukkaa, jossa joka kierroksella lisätään yksi termi. Esimerkiksi $\sum_{n=1}^{3}n=1+2+3=6$. Ala- ja ylärajat kertovat, mitkä termit summataan.

<a id="different-symbols"></a>
## Samannäköiset mutta eri symbolit

Pieni $\varepsilon(t)$ (epsilon) tarkoittaa nopeusvirhettä, kun taas pystyssä kirjoitettu vakio $\mathrm{e}\approx2.71828$ on Eulerin luku eli luonnollisen logaritmin kantaluku. $\tau$ (tau) on aikavakio, $\omega$ (omega) kulmanopeus, $\alpha$ (alfa) kulmakiihtyvyys ja $\Delta$ (delta) muutos. Pieni $\sigma$ (sigma) on eri symboli, jota käytetään esimerkiksi keskihajonnasta tai jännityksestä. Tarkista aina symbolin määritelmä asiayhteydestä.

<a id="math-delimiters"></a>
## Miksi Markdown-lähteessä näkyy dollarimerkkejä?

Markdownin **lähdetekstissä** `$...$` merkitsee tekstinsisäistä kaavaa ja `$$...$$` erillistä kaavalohkoa. Ne ovat muotoilurajaimia, eivät osa kaavaa. GitHubin renderöidyssä näkymässä niiden ei pitäisi näkyä dollarimerkkeinä. Jos näkyvät, tarkista katsotko lähdetekstiä, onko kaava linkin otsikossa tai onko Markdown-merkintä virheellinen. Tämän sivun navigointilinkit käyttävät tavallista tekstiä eivätkä matematiikkamerkintää.

[GitHubin matematiikkaohje](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).

<a id="si-notation"></a>
## Desimaalipiste, SI-yksiköt ja matemaattiset välit

Myös käännöksissä desimaalit kirjoitetaan **pisteellä**: `0.5`, `3.8`, `63.2 %`. Pilkku erottaa luettelon alkioita, ei lukua sen yksiköstä eikä differentiaalia. Numeron ja yksikkötunnuksen väliin tulee välilyönti: `1 s`, `4 mm`, `10 mm/s`. Yhdistetyissä yksiköissä kertolasku merkitään keskipisteellä (`kg·m²`, `N·m·s/rad`), ja jakomerkin ympärillä ei ole välilyöntejä (`mm/s`, ei `mm / s`). Keskipiste tarkoittaa kertolaskua, ei desimaalierotinta. `1 N·m` tarkoittaa yhtä newtonmetriä.

Kaavoissa käytetään esimerkiksi merkintää `\mathrm{kg}\cdot\mathrm{m}^2`, ja differentiaali kirjoitetaan `\mathrm{d}t`, ei pilkkuna ja sen jälkeisenä `dt`:nä. Merkintätavat perustuvat [BIPM:n SI-oppaaseen](https://www.bipm.org/en/publications/si-brochure). Tässä repositoriossa käytetään johdonmukaisesti sallittua desimaalipistettä. Pythonin `dt` tarkoittaa **äärellistä aika-askelta**, mutta integraalin $\mathrm{d}t$ on **differentiaali**.

### rpm ja rad/s

`rpm` tarkoittaa **kierrosta minuutissa** (revolutions per minute) ja on yleinen **SI-järjestelmän ulkopuolinen** pyörimisnopeuden yksikkö. Kulmanopeuden SI-merkintä on `rad/s` (radiaania sekunnissa). Muunnos: `1 rpm = 2π/60 rad/s ≈ 0.10472 rad/s`, joten `1000 rpm ≈ 104.72 rad/s`.
