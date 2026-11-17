# 4. Robotin koordinaatistot ja tasokinematiikka

**Kielet:** [en](../../en/notes/04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `mm` — millimetri = 0.001 m; `°` — aste. [Yksikköluettelo](../UNITS.md).

[Sisällysluettelo](../README.md) · [Trigonometria](../TRIGONOMETRY.md) · [Matemaattiset symbolit](../SYMBOLS.md) · [Takaisinkytkentäsäätö](03-feedback-control.md)

> **Opetusmalli:** Älä käytä tätä yksinkertaistettua geometriaa oikeiden koneiden ohjaamiseen.

## Sisältö
1. [Miksi koordinaatistot ovat tärkeitä](#section-1)
2. [Pisteen kierto ja siirto](#section-2)
3. [Koordinaatistojen ketjuttaminen](#section-3)
4. [Kaksivartisen mekanismin suora kinematiikka](#section-4)
5. [Kaksi kyynärpään ratkaisua ja ulottuvuusalue](#section-5)
6. [Lasketut esimerkit täydellisine ratkaisuineen](#section-6)
7. [Mallin rajoitukset ja matriisimerkintä](#section-7)

<a id="section-1"></a>
## 1. Miksi koordinaatistot ovat tärkeitä

Koordinaatisto (coordinate frame) koostuu origosta ja suunnatuista akseleista. **Maailmakoordinaatisto** W voi pysyä kiinteänä robotin jalustaan nähden, kun taas **työkalukoordinaatisto** T liikkuu työkalun mukana. Saman pisteen koordinaatit riippuvat valitusta koordinaatistosta. **Sijainti** kertoo pisteen paikan ja **orientaatio** akseleiden suunnat. Pelkkä koordinaattien muuntaminen ei liikuta robottia.

Kaikki pituudet ilmaistaan samalla yksiköllä (tässä mm). Positiiviset kulmat mitataan vastapäivään maailman +X-akselista. Alaindeksit w ja l tarkoittavat maailman- ja paikalliskoordinaatistoa. Käytämme jäykän kappaleen kaksiulotteista likimääräistä mallia.

<a id="section-2"></a>
## 2. Pisteen kierto ja siirto

![Maailman akselit ja 90 astetta kierretyt työkalun akselit sekä paikalliset pisteet P ja Q](../../../assets/figures/world_local_frames.svg)

*Maailman ja työkalun akselit, työkalun kierto +90°, paikalliset pisteet P ja Q.*

Kuvassa työkalun origo T on maailman koordinaateissa (100 mm, 50 mm) ja sen akselit ovat kääntyneet +90°. Paikallinen +x osoittaa maailman +Y-suuntaan ja paikallinen +y maailman −X-suuntaan. Siten T:n piste P=(0 mm, 10 mm) on maailman koordinaateissa (90 mm, 50 mm), ja Q=(20 mm, 0 mm) on (100 mm, 70 mm).

Olkoon $(t_x,t_y)$ paikallisen origon sijainti maailmassa, $\theta$ sen orientaatiokulma ja $(x_l,y_l)$ pisteen paikalliset koordinaatit. **Kierrä ensin, siirrä sitten:**

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

Sinin ja kosinin etumerkit riippuvat kulman suunnasta. Kun $\theta=0^\circ$, yhtälöt lisäävät vain origon siirtymän. Ne muuttavat pisteen **koordinaatteja**, eivät muodosta moottorikomentoja.

<a id="section-3"></a>
## 3. Koordinaatistojen ketjuttaminen

Koordinaatistot voivat muodostaa ketjun **W → T → S** (maailma → työkalu → anturi). Käytetään edellistä T:tä. Jos S:n origo on T:ssä (20 mm, 0 mm) ja S:n akselit ovat T:n suuntaiset, S:n origo on maailmassa (100 mm, 70 mm). S:ssä mitattu piste (0 mm, 10 mm) on maailmassa (90 mm, 70 mm). Muunna koordinaatit lapsikoordinaatistosta emokoordinaatistoon oikeassa järjestyksessä.

Sarakevektoreilla $T_{WS}=T_{WT}T_{TS}$, missä $T_{AB}$ muuntaa koordinaatit **B:stä A:han**. Matriisikertolasku ei yleensä ole vaihdannainen.

**Koko matriisilasku (sarakevektorit):** Työkalukoordinaatisto T on kääntynyt +90° suhteessa W:hen ja sen maailman koordinaattien origo on (100 mm, 50 mm). Anturikoordinaatistolla S ei ole lisäkiertoa T:hen nähden ja sen origo on T:ssä (20 mm, 0 mm), samassa paikassa kuin edellisen kuvan Q. Kiertomatriisin alkiot ovat dimensiottomia ja siirtymät annetaan millimetreinä:

$$
T_{WT}=
\begin{bmatrix}
0 & -1 & 100\\
1 & 0 & 50\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{TS}=
\begin{bmatrix}
1 & 0 & 20\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{WS}=T_{WT}T_{TS}=
\begin{bmatrix}
0 & -1 & 100\\
1 & 0 & 70\\
0 & 0 & 1
\end{bmatrix}
$$

$$
T_{WS}\begin{bmatrix}0\\10\\1\end{bmatrix}
=\begin{bmatrix}90\\70\\1\end{bmatrix}
$$

Matriisitulo kiertää ensin anturin paikallisen siirtymän (20 mm, 0 mm) maailman siirtymäksi (0 mm, 20 mm), joka lisätään pisteeseen (100 mm, 50 mm). Näin S:n piste (0 mm, 10 mm) sijaitsee W:ssä (90 mm, 70 mm). Olisi väärin lisätä 20 mm suoraan maailman X-koordinaattiin, sillä siirtymä on ilmoitettu **T:ssä**. Homogeenisen vektorin viimeinen komponentti 1 on dimensioton, ei pituus. Kyse on koordinaattimatematiikasta; [ROS 2:n tf2](06-ros2-foundations.md#section-7) julkaisee ja hakee aikaleimattuja muunnoksia, muttei ratkaise käänteistä kinematiikkaa.

<a id="section-4"></a>
## 4. Kaksivartisen mekanismin suora kinematiikka

![Ensimmäinen nivel 30 astetta ja toinen suhteellinen nivel 60 astetta; toinen varsi pystysuora](../../../assets/figures/two_link_fk.svg)

*Ensimmäinen nivel 30°, toinen suhteellinen nivel 60°; toinen varsi osoittaa suoraan ylös.*

Tasomaisen robotin varsien pituudet ovat $L_1,L_2$. Ensimmäisen nivelen kulma $\theta_1$ mitataan maailman +X-akselista, mutta toisen nivelen kulma $\theta_2$ mitataan **suhteessa ensimmäiseen varteen**. Toisen varren absoluuttinen kulma maailmassa on siis $\theta_1+\theta_2$. Kärjen paikka on varsivektorien summa:

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

Kun $L_1=100$ mm, $L_2=50$ mm, $\theta_1=30^\circ$ ja $\theta_2=60^\circ$, kyynärnivel on pisteessä (86.60 mm, 50 mm). Toinen varsi osoittaa ylös absoluuttisessa kulmassa 90°, joten kärki on pisteessä (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. Kaksi kyynärpään ratkaisua ja ulottuvuusalue

![Kaksi erilaista nivelkulmaparia saavuttaa saman tavoitepisteen](../../../assets/figures/two_link_elbow_solutions.svg)

*Kaksi eri nivelkulmien yhdistelmää saavuttaa saman tavoitteen.*

Käänteiskinematiikka etsii tavoitepaikkaan sopivat nivelkulmat. Kun kumpikin varsi on 100 mm, sekä $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ että $(+90^\circ,-90^\circ)$ saavuttavat pisteen (100 mm, 100 mm). Nämä ovat nivelkulmia: $\theta_2$ on suhteellinen, ei absoluuttinen kulma.

![Ideaalinen saavutettava rengasalue säteiden 50 mm ja 150 mm välissä](../../../assets/figures/two_link_workspace.svg)

*Ideaalinen saavutettava rengasalue säteiden 50 mm ja 150 mm välissä.*

Kun 2D-nivelet saavat pyöriä vapaasti eikä törmäyksiä ole, etäisyyden $r$ on täytettävä $|L_1-L_2|\le r\le L_1+L_2$. Varrenpituuksilla 100 mm ja 50 mm ideaalinen ulottuvuusalue on rengas säteiden 50–150 mm välissä. Nivelrajat ja esteet voivat pienentää todellista ulottuvuutta.

<a id="section-6"></a>
## 6. Lasketut esimerkit täydellisine ratkaisuineen

Seuraavat **kuusi itsenäistä esimerkkiä sisältävät kaikki tehtävän, ratkaisun ja selityksen**. Ne eivät ole kenellekään lukijalle henkilökohtaisesti osoitettuja kysymyksiä.

<a id="worked-1"></a>
### 6.1. Paikallinen piste P kierretyssä koordinaatistossa

**Tehtävä.** T on maailman pisteessä (100 mm, 50 mm) ja kierretty +90°. Selvitä paikallisen pisteen P=(0 mm, 10 mm) maailman koordinaatit.

**Ratkaisu.** Paikallinen +y osoittaa maailman −X-suuntaan, joten vähennetään X-koordinaatista 10 mm.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Vastaus:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Paikallinen piste Q työkalun x-akselilla

**Tehtävä.** Etsi samassa työkalukoordinaatistossa pisteen Q=(20 mm, 0 mm) maailman koordinaatit.

**Ratkaisu.** Paikallinen +x osoittaa maailman +Y-suuntaan, joten Y-koordinaattiin lisätään 20 mm.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Vastaus:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Kaksivartisen mekanismin suora kinematiikka

**Tehtävä.** $L_1=100$ mm, $L_2=50$ mm, $\theta_1=30^\circ$ ja suhteellinen $\theta_2=60^\circ$. Etsi kärjen sijainti.

**Ratkaisu.** Toisen varren kulma maailmassa on 30°+60°=90°, ei 60°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Vastaus:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. Kaksi asentoa samaan tavoitteeseen

**Tehtävä.** Kaksi 100 mm vartta saavuttaa pisteen (100 mm, 100 mm). Etsi kaksi nivelkulmaparia.

**Ratkaisu.** Ensimmäinen asento ulottuu ensin oikealle ja sitten ylös; toinen ensin ylös ja sitten oikealle.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Saavutettavuus ilman kulmien ratkaisemista

**Tehtävä.** $L_1=100$ mm ja $L_2=50$ mm. Voidaanko saavuttaa pisteet (0 mm, 120 mm) ja (0 mm, 0 mm)?

**Ratkaisu.** Vertaa kummankin pisteen etäisyyttä varsien pituuksien erotukseen ja summaan.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

Piste (0 mm, 120 mm) on **saavutettavissa**, koska 50 ≤ 120 ≤ 150. Origo (0 mm, 0 mm) **ei ole saavutettavissa**, koska sen säde on nolla.

<a id="worked-6"></a>
### 6.6. Kosinilause kyynärkulmalle

**Tehtävä.** $L_1=100$ mm, $L_2=50$ mm ja $r=120$ mm. Laske $\cos\theta_2$.

**Ratkaisu.** Kosini määrää taivutuskulman suuruuden. Kahdessa peilikuvamaisessa kyynärasennossa suhteellisten kulmien etumerkit ovat vastakkaiset.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

Kolmion sisäkulma on $\varphi=180^\circ-|\theta_2|$. Pelkkä säde ei määritä kulmaa $\theta_1$. Katso [Trigonometrian](../TRIGONOMETRY.md) kuva.

<a id="section-7"></a>
## 7. Mallin rajoitukset ja matriisimerkintä

Tämä ideaalinen jäykkä tasomalli ei sisällä nivelrajoja, törmäyksiä, välystä, joustoa, enkooderin nollavirheitä, kameran kalibrointia eikä 3D-liikettä. Nivelanturit mittaavat nivelkulmia, eivät suoraan maailman koordinaatteja. Muunna anturihavainnot kalibroitujen koordinaatistojen kautta. Mikään näistä laskelmista ei ole käsky liikuttaa laitteita.

Valinnainen homogeeninen matriisiesitys: sarakevektoreilla 3×3-muunnos siirtää paikallisen pisteen $[x_l,y_l,1]^T$ maailman koordinaatistoon. Vapaan siirtymävektorin kolmas komponentti on 0, joten translaatio ei vaikuta siihen.

$$
T_{WL}=
\begin{bmatrix}
\cos\theta & -\sin\theta & t_x \\
\sin\theta & \cos\theta & t_y \\
0 & 0 & 1
\end{bmatrix},
\qquad
\begin{bmatrix}x_w\\y_w\\1\end{bmatrix}
=T_{WL}\begin{bmatrix}x_l\\y_l\\1\end{bmatrix}
$$

[Trigonometria](../TRIGONOMETRY.md) · [Matemaattiset symbolit](../SYMBOLS.md) · [Takaisinkytkentäsäätö](03-feedback-control.md)

[Seuraavaksi: pyöriminen, nopeus ja singulariteetit](05-velocity-jacobian.md)
