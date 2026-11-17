# 0. Differentiaali- ja integraalilaskennan perusteet: derivaatat, raja-arvot ja integraalit

**Kielet:** [en](../../en/notes/00-calculus-foundations.md) · [fr](../../fr/notes/00-calculus-foundations.md) · [de](../../de/notes/00-calculus-foundations.md) · [it](../../it/notes/00-calculus-foundations.md) · [es](../../es/notes/00-calculus-foundations.md) · [pt](../../pt/notes/00-calculus-foundations.md) · [zh](../../zh/notes/00-calculus-foundations.md) · [ja](../../ja/notes/00-calculus-foundations.md) · [nb](../../nb/notes/00-calculus-foundations.md) · [ru](../../ru/notes/00-calculus-foundations.md) · [ko](../../ko/notes/00-calculus-foundations.md) · [fi](00-calculus-foundations.md) · [pl](../../pl/notes/00-calculus-foundations.md)

**Luonnollinen eksponenttifunktio** on $\exp(x)=\mathrm{e}^{x}$, missä **Eulerin luku** on $\mathrm{e}\approx2.71828$. Se kuvaa jatkuvaa kasvua tai vaimenemista; $\exp(0)=1$ ja $\exp(-1)\approx0.3679$. Luonnollinen logaritmi $\ln$ on sen käänteisfunktio: $\ln(\exp(x))=x$. Katso [symboliluettelo](../SYMBOLS.md).

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `s` — sekunti; `mm` — millimetri = 0.001 m; `mm/s` — millimetri / sekunti — lineaarinen nopeus; `mm/s²` — millimetri / sekunti² — kiihtyvyys; `kg·m²` — kilogramma · metri² — hitausmomentti; `rad/s` — radiaani / sekunti — kulmanopeus; `rad/s²` — radiaani / sekunti² — kulmakiihtyvyys; `N·m` — newton · metri — vääntömomentti; `W` — watti; `rpm` — kierros minuutissa; `N/m` — newton / metri — jäykkyys; `mm³/s` — millimetri³ / sekunti — tilavuusvirta; `%` — prosentti (sadasosa); `m` — metri; `kg` — kilogramma; `N` — newton; `J` — joule; `rad` — radiaani. [Yksikköluettelo](../UNITS.md).

[Sisällysluettelo](../README.md) · [Integraalitaulukko](../INTEGRAL_TABLE.md) · [Trigonometria](../TRIGONOMETRY.md) · [Liike](01-motion-calculus.md) · [Dynamiikka](02-first-order-dynamics.md) · [Symbolit](../SYMBOLS.md)

> **Opetukseen tarkoitettu likimääräinen malli:** Tarkista mallit ja yksiköt itsenäisesti. Älä liitä esimerkkikoodia oikeisiin laitteisiin.

Derivaatta kertoo, kuinka nopeasti suure muuttuu **juuri nyt**. Toinen derivaatta kertoo muutosnopeuden muuttumisesta. Integraali kokoaa pienet muutokset yhteen, ja raja-arvo määrittää hetkellisen muutosnopeuden. Logaritmilla voidaan ratkaista, milloin eksponentiaalinen vaste saavuttaa halutun tason.

Samoja menetelmiä käytetään koneen akselissa, servokäytössä, robotin nivelessä, jousessa ja anturissa. Aloita teknisestä kysymyksestä, määritä muuttuva suure ja sen yksiköt ja valitse sopiva laskusääntö.

## Sisällysluettelo

- [1. Mitatusta muutoksesta matemaattiseen malliin](#section-1)
- [2. Raja-arvot ja ensimmäiset derivaatat](#section-2)
- [3. Liikkuvan akselin ensimmäinen ja toinen derivaatta](#section-3)
- [4. Ketjusääntö ja pyörimisenergia](#section-4)
- [5. Eksponenttifunktiot, logaritmit ja asettumisaika](#section-5)
- [6. Integraalit: siirtymä ja mekaaninen työ](#section-6)
- [7. Lisäesimerkki: laajeneva pallo](#section-7)
- [8. Yksiköt, tarkistukset ja seuraavat vaiheet](#section-8)

<a id="section-1"></a>
## 1. Mitatusta muutoksesta matemaattiseen malliin

| Fysikaalinen kysymys | Matemaattinen menetelmä |
| --- | --- |
| Kuinka nopeasti akseli liikkuu **nyt**? | Ensimmäinen derivaatta $dx/dt$ |
| Kuinka nopeasti nopeus muuttuu? | Toinen derivaatta $d^2x/dt^2$ |
| Milloin vaste saavuttaa 90 %? | Luonnollinen logaritmi $\ln$ |
| Kuinka suuri siirtymä tapahtui 2 sekunnissa? | Määrätty integraali $\int v\ \mathrm{d}t$ |
| Kuinka paljon työtä muuttuva voima tekee? | Integraali $\int F\ \mathrm{d}x$ |

<a id="section-2"></a>
## 2. Raja-arvot ja ensimmäiset derivaatat

Kahden mittauksen välinen erotusosamäärä on aikavälin **keskimääräinen muutosnopeus**. Derivaatta on tämän suhteen raja-arvo, kun aikaväli lähestyy nollaa.

$$
v(t)=\frac{dx}{dt}=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
$$

Kun paikka on $x(t)=at^2$ ja $a=2\ \mathrm{mm/s^2}$, avaa osoittajan lauseke ennen raja-arvon laskemista:

$$
\frac{x(t+h)-x(t)}h=\frac{a[(t+h)^2-t^2]}h=a(2t+h)\longrightarrow 2at.
$$

Tekijä $h$ supistetaan **ennen** kuin sen annetaan lähestyä nollaa. Hetkellä $t=1\ \mathrm{s}$ hetkellinen nopeus on $4\ \mathrm{mm/s}$. Raja-arvon laskeminen ei tarkoita määrittelemättömän suhteen $0/0$ laskemista suoraan.

**Tavallisia derivointisääntöjä** (kertoimet $c$ ja $n$ ovat vakioita; trigonometristen funktioiden argumentit radiaaneina):

| Sääntö | Kaava |
| --- | --- |
| Vakio | $\frac{d}{dt}c=0$ |
| Potenssi | $\frac{d}{dt}t^n=n t^{n-1}$ |
| Kerroin ja summa | $(cf+g)'=cf'+g'$ |
| Tulo | $(fg)'=f'g+fg'$ |
| Osamäärä ($g\ne0$) | $\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}$ |
| Ketjusääntö | $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ |
| Eksponenttifunktio | $\frac{d}{dt}\exp(t)=\exp(t)$ |
| Luonnollinen logaritmi ($t>0$) | $\frac{d}{dt}\ln t=\frac1t$ |
| Sini ja kosini | $\frac{d}{dt}\sin t=\cos t$, $\frac{d}{dt}\cos t=-\sin t$ |

![Paikkakäyrän kulmakerroin ja nopeuskäyrän alle jäävä pinta-ala](../../../assets/figures/calculus_slope_area.svg)

<a id="section-3"></a>
## 3. Liikkuvan akselin ensimmäinen ja toinen derivaatta

Kelkan alkupaikka on 2 mm, alkunopeus 3 mm/s ja vakiokiihtyvyys 4 mm/s². Sen paikka on

$$
x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2.
$$

**Ensimmäinen derivaatta (nopeus):** derivoi jokainen termi. Vakio 2 mm häviää, $t$-termi muuttuu arvoksi 3 mm/s ja $t^2$-termi muuttuu ajan suhteen lineaariseksi.

$$
v(t)=\frac{dx}{dt}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t.
$$

**Toinen derivaatta (kiihtyvyys):** derivoi nopeus vielä kerran. Kahden sekunnin kohdalla paikka on 16 mm, nopeus 11 mm/s ja kiihtyvyys edelleen 4 mm/s².

$$
a(t)=\frac{d^2x}{dt^2}=\frac{dv}{dt}=4\ \mathrm{mm/s^2}.
$$

Toisen derivaatan yksikkö on pituus jaettuna ajan neliöllä. Se **ei** ole ensimmäisen derivaatan neliö.

<a id="section-4"></a>
## 4. Ketjusääntö ja pyörimisenergia

Pyörivään vauhtipyörään varastoituu liike-energiaa. Kun kulmanopeus $\omega$ riippuu ajasta, energia $E$ muuttuu kulmanopeuden välityksellä. Tämä on **ketjusääntö**.

$$
E(\omega)=\frac12J\omega^2,\quad \omega=\omega(t),
$$

$$
\frac{dE}{dt}=\frac{dE}{d\omega}\frac{d\omega}{dt}=J\omega\alpha=M\omega=P.
$$

Kun $J=0.01\ \mathrm{kg\cdot m^2}$, $\omega=10\ \mathrm{rad/s}$ ja $\alpha=2\ \mathrm{rad/s^2}$, moottorin momentti on $J\alpha=0.02\ \mathrm{N\cdot m}$ ja hetkellinen mekaaninen teho $0.2\ \mathrm{W}$. Yhtälö $P=M\omega$ on ketjusäännön käytännön sovellus.

<a id="section-5"></a>
## 5. Eksponenttifunktiot, logaritmit ja asettumisaika

Yksinkertaisessa ensimmäisen kertaluvun käyttömallissa nopeus voi lähestyä loppuarvoaan eksponentiaalisesti. Aikavakio $\tau$ ilmaistaan sekunteina.

$$
\omega(t)=\omega_\infty\bigl(1-\exp(-t/\tau)\bigr),\quad t\ge0,\ \tau>0.
$$

Kaava olettaa, että **alkukulmanopeus on nolla**, $\omega(0)=0$, ja tavoite $\omega_\infty$ on vakio. Kun alkukulmanopeus on $\omega_0\ne0$, yleinen ensimmäisen kertaluvun vaste on

$$
\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau).
$$

**Esimerkki alkunopeudella, joka ei ole nolla:** Olkoon $\omega_0=200\ \mathrm{rpm}$, $\omega_\infty=1000\ \mathrm{rpm}$ ja $\tau=0.5\ \mathrm{s}$. Yhden aikavakion kuluttua ($t=0.5\ \mathrm{s}$):

$$
\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}.
$$

Vaste on saavuttanut **63.2 % nopeuden muutoksesta 800 rpm**, ei 63.2 % loppunopeudesta 1000 rpm. Kun $t=0$, kaava antaa 200 rpm; ajan kasvaessa se lähestyy 1000 rpm. Esimerkki on matemaattinen, ei moottorikomento.

Eksponenttifunktio kuvaa jäljellä olevan alkuvirheen osuutta. Kun halutaan tietää, **milloin** tietty osuus on jäljellä, käytetään eksponenttifunktion käänteisfunktiota, luonnollista logaritmia $\ln$. Logaritmin argumentti 0.1 on dimensioton.

$$
\exp(-t/\tau)=0.1
\quad\Longrightarrow\quad
-\frac{t}{\tau}=\ln(0.1)
\quad\Longrightarrow\quad
t=-\tau\ln(0.1)=\tau\ln(10)\approx2.303\tau.
$$

Kun 90 % kokonaismuutoksesta on saavutettu, alkuvirheestä on jäljellä 10 %. Aikavakiolla $\tau=0.5\ \mathrm{s}$ ideaalinen malli antaa ajaksi noin 1.151 s. Todellisissa käytöissä voi olla muita rajoituksia ja viiveitä.

Funktion $\ln z$ derivaatta on $1/z$, kun $z>0$. Jos $z=z(t)$, kerro ketjusäännön mukaisesti derivaatalla $dz/dt$. Dimensiollisesta suureesta ei oteta logaritmia suoraan, vaan ensin muodostetaan dimensioton suhde.

$$
\ln(1)=0,\quad \ln(\mathrm{e})=1,\quad \ln(\mathrm{e}^{z})=z,\quad \frac{d}{dz}\ln z=\frac1z\ (z>0).
$$

<a id="section-6"></a>
## 6. Integraalit: siirtymä ja mekaaninen työ

**Määräämätön integraali** antaa kaikki integraalifunktiot ja sisältää integroimisvakion $C$. **Määrätty integraali** antaa tarkasteltavalla välillä kertyneen nettomuutoksen.

$$
\int 4t\ \mathrm{d}t=2t^2+C,\qquad \int t^n\ \mathrm{d}t=\frac{t^{n+1}}{n+1}+C\ (n\ne-1).
$$

**Liike-esimerkki.** Kelkan alkupaikka on $x_0=2\ \mathrm{mm}$ ja nopeus kasvaa lineaarisesti kaavan $v(t)=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t$ mukaan. Laske siirtymä välillä 0–2 s:

$$
\Delta x=\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
$$

$$
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}=6\ \mathrm{mm}+8\ \mathrm{mm}=14\ \mathrm{mm}.
$$

Siirtymä on 14 mm. Lisää alkupaikka, niin saat $x(2)=16\ \mathrm{mm}$. Negatiivinen nopeus antaa negatiivisen osuuden etumerkilliseen siirtymään, mutta kuljettu matka ei ole negatiivinen.

**Jousen työ.** Venytä ideaalista lineaarista jousta välillä $x=0$–$x=0.01\ \mathrm{m}$, kun jousivakio on $k=200\ \mathrm{N/m}$. Voima kasvaa venymän mukana. Jokaiselle pienelle siirtymälle käytetään sen hetkistä voimaa ja tulot integroidaan:

$$
F(x)=kx,\qquad W=\int_0^{0.01\ \mathrm{m}}kx\ \mathrm{d}x
=\left[\frac{kx^2}{2}\right]_0^{0.01\ \mathrm{m}}
=\frac{200\ \mathrm{N/m}}2(0.01\ \mathrm{m})^2=0.01\ \mathrm{J}.
$$

Työ on 0.01 J. Jos käyttäisit loppuvoimaa $F=2\ \mathrm{N}$ koko matkalla, saisit virheellisen arvon 0.02 J, koska voima ei ollut vakio.

<a id="section-7"></a>
## 7. Lisäesimerkki: laajeneva pallo

**Valinnainen ketjusääntöesimerkki.** Pallon tilavuus riippuu säteestä, joka voi puolestaan muuttua ajan mukana. Riippuvuusrakenne on sama kuin vauhtipyörän energian riippuvuus kulmanopeudesta.

$$
V(r)=\frac43\pi r^3,\qquad \frac{dV}{dt}=\frac{dV}{dr}\frac{dr}{dt}=4\pi r^2\frac{dr}{dt}.
$$

Kun $r=10\ \mathrm{mm}$ ja $dr/dt=1\ \mathrm{mm/s}$, tilavuuden hetkellinen kasvunopeus on $400\pi\approx1256.64\ \mathrm{mm^3/s}$. Jos $r(t)=10\ \mathrm{mm}+(1\ \mathrm{mm/s^2})t^2$, hetkellä 2 s saadaan $r=14\ \mathrm{mm}$, $dr/dt=4\ \mathrm{mm/s}$ ja $3136\pi\approx9852.03\ \mathrm{mm^3/s}$.

<a id="section-8"></a>
## 8. Yksiköt, tarkistukset ja seuraavat vaiheet

**Tarkistukset:** paikan derivaatan yksikkö on m/s ja toisen derivaatan m/s². Voiman N integroiminen matkan m suhteen antaa N·m = J. Määräämätön integraali tarvitsee vakion $C$. Derivaatta kuvaa paikallista muutosta, määrätty integraali aikavälin kertymää. Differentiaali $dt$ ei ole sama asia kuin Eulerin ohjelmakoodin äärellinen näyteväli `dt`.

**Laske itse:** (1) Kun $x(t)=5\ \mathrm{mm}+(2\ \mathrm{mm/s})t+(1\ \mathrm{mm/s^2})t^2$, laske nopeus ja kiihtyvyys hetkellä 3 s. (2) Kuinka kauan ideaalinen ensimmäisen kertaluvun vaste tarvitsee saavuttaakseen 90 % muutoksesta, kun $\tau=1\ \mathrm{s}$? (3) Integroi vakionopeus $v=4\ \mathrm{mm/s}$ kahden sekunnin ajalta. **Vastaukset:** 8 mm/s ja 2 mm/s²; noin 2.303 s; 8 mm.

**Ratkaisut vaiheittain:**

1. $v(t)=\frac{dx}{dt}=2\ \mathrm{mm/s}+2(1\ \mathrm{mm/s^2})t$; $v(3\ \mathrm{s})=2+2\cdot3=8\ \mathrm{mm/s}$. $a(t)=\frac{dv}{dt}=2\ \mathrm{mm/s^2}$.
2. $f(t)=1-\exp(-t/\tau)=0.9$; $\exp(-t/\tau)=0.1$; $t=-\tau\ln(0.1)=\tau\ln(10)$. $\tau=1\ \mathrm{s}$; $t\approx2.303\ \mathrm{s}$.
3. $\Delta x=\int_0^{2\ \mathrm{s}}(4\ \mathrm{mm/s})\ \mathrm{d}t=(4\ \mathrm{mm/s})(2\ \mathrm{s})=8\ \mathrm{mm}$.


[Integraalitaulukko](../INTEGRAL_TABLE.md) · [Trigonometria](../TRIGONOMETRY.md) · [Seuraavaksi: liike](01-motion-calculus.md) · [Python-harjoitukset](../exercises/README.md)
