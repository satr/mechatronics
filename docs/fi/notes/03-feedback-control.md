# 3. Takaisinkytkentäsäätö: PID, näytteenotto, kyllästyminen ja pitomomentti

**Kielet:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Tämän sivun yksiköt (selitetty ennen esimerkkejä):** `rpm` — kierros minuutissa; `A` — ampeeri; `s` — sekunti; `rpm/s` — kierros minuutissa / sekunti — kulmakiihtyvyys; `A/rpm` — ampeeri / (kierros minuutissa) — nopeuteen suhteutettu vahvistus; `A/(rpm·s)` — ampeeri / (kierros minuutissa · sekunti) — integraalivahvistus; `A·s/rpm` — ampeeri · sekunti / (kierros minuutissa) — derivointivahvistus; `N·m` — newton · metri — vääntömomentti; `kg` — kilogramma; `m` — metri; `N` — newton. [Yksikköluettelo](../UNITS.md).

[Sisällysluettelo](../README.md) · [Matematiikan perusteet](00-calculus-foundations.md) · [Ensimmäisen kertaluvun dynamiikka](02-first-order-dynamics.md) · [Trigonometria](../TRIGONOMETRY.md)

> **Opetusmalli:** Älä kytke näitä yksinkertaistettuja algoritmeja oikeisiin moottoreihin tai koneisiin.

## Sisältö

- [1. Suljetun piirin nopeussäätö](#section-1)
- [2. P: suhteellinen vaste](#section-2)
- [3. I: kertynyt virhe ja virran asetusarvo](#section-3)
- [4. D: muuttuva virhe ja anturikohina](#section-4)
- [5. Näytteenotto, kyllästyminen ja anti-windup](#section-5)
- [6. Robotin nivelen pitäminen paikallaan painovoimaa vastaan](#section-6)
- [7. Tarkistukset ja rajoitukset](#section-7)

<a id="section-1"></a>
## 1. Suljetun piirin nopeussäätö

Takaisinkytketty säädin vertaa haluttua asetusarvoa anturin mittaukseen. Jos moottorin tavoitenopeus on 1000 rpm ja mitattu nopeus 950 rpm, nopeusvirhe on +50 rpm. PI/PID-säädin muuttaa tämän virheen ohjauskomennoksi. Tässä esimerkissä komento on **momenttia tuottavan virran asetusarvo** ampeereina, ei ohje lisätä sama ampeerimäärä edelliseen mitattuun virtaan.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

Käyttölaitteessa voi olla erillinen virransäätöpiiri, joka säätää jännitettä tai PWM-signaalia virran asetusarvon saavuttamiseksi. Muissa rakenteissa ulostulo voi olla jännite, momentti, PWM tai muu suure. Älä oleta, että kaikki todelliset käytöt hyväksyvät virran asetusarvon.

<a id="section-2"></a>
## 2. P: suhteellinen vaste

P-termi reagoi **tämänhetkiseen** virheeseen. Yksinkertaisessa mallissa ilman ennakko-ohjausta tai ohjauksen vakiosiirtoa vakioinen kuorma vaatii nollasta poikkeavan moottorimomentin ja siis virran. Jos nopeusvirhe olisi täsmälleen nolla, myös P-termi olisi nolla. Siksi pelkkä P-säätö voi asettua tilanteeseen, jossa nopeudessa on pysyvä säätöpoikkeama.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: kertynyt virhe ja virran asetusarvo

I-termi integroi virheen ajan suhteen. Se säilyttää **yhden kertyvän tilamuuttujan**, ei luetteloa kaikista aiemmista virheistä. Positiivisen virheen jatkuessa integraali kasvaa; virheen ollessa nolla se säilyttää arvonsa; negatiivinen virhe pienentää sitä. Näin integraalitermi voi pitää momenttikomennon nollasta poikkeavana myös nopeuden saavutettua asetusarvon.

$$
z(t)=\int_0^t\varepsilon(s)\ \mathrm{d}s,\quad u_I=K_i z(t),\quad [K_i]=\mathrm{A/(rpm\cdot s)}.
$$

```python
integral = 0.0  # saved between controller iterations
for speed in [950, 950, 950, 1000, 1020, 1020]:
    error = 1000 - speed       # rpm
    integral += error * 1.0   # rpm*s; dt = 1 s
    p_command = 0.02 * error # amperes
    i_command = 0.002 * integral # amperes
    current_setpoint = p_command + i_command
    print(round(integral), round(i_command, 2), round(current_setpoint, 2))
```

Havainnollistavassa säätimessä `dt = 1 s`, `Kp = 0.02 A/rpm` ja `Ki = 0.002 A/(rpm·s)`. Kolme peräkkäistä näytettä, joiden virhe on +50 rpm, tuottavat integraalit 50, 100 ja 150 rpm·s sekä I-termit 0.10, 0.20 ja 0.30 A. Nollavirheellä I-termi pysyy arvossa 0.30 A. Yksi sekunti virheellä −20 rpm muuttaa arvon 0.26 A:iin ja seuraava sekunti 0.22 A:iin. −0.04 A on **yhden askeleen muutos**, ei uusi absoluuttinen virran asetusarvo.

Ohjelma tulostaa vain kertyneen integraalin, I-termin ja koko virran asetusarvon. Taulukossa näkyvät lisäksi virhe ja P-termi, jotta jokainen laskuvaihe voidaan tarkistaa. Näytteiden väli on 1 s ja integraalin alkuarvo on nolla.

| k | Mitattu kierrosluku (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

Kun mitattu nopeus on 1020 rpm, virhe on −20 rpm: P-termi on −0.40 A, mutta I-termi on yhä +0.26 A. Summaksi saadaan **etumerkillinen virran asetusarvo −0.14 A**, ja seuraavalla näytteellä −0.18 A. I-termin muutos (−0.04 A näytettä kohti) ei ole kokonaiskomento. Luvut kuvaavat vain opetusmallia eivätkä oikean käytön asetuksia.

<a id="section-4"></a>
## 4. D: muuttuva virhe ja anturikohina

D-termi reagoi **virheen muutosnopeuteen**. Kun nopeuden asetusarvo pysyy vakiona ja mitattu nopeus kiihtyy, virhe pienenee ja derivaatan vaikutus on negatiivinen; tämä voi vähentää ylitystä. D-termi ei ole sama asia kuin moottorin nopeus. Jos anturin lukema hyppää 8 rpm ajassa 0.01 s, laskennallinen muutosnopeus on 800 rpm/s, vaikka todellinen nopeus pysyisi lähes vakiona.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

Virheen derivaatan yksikkö on rpm/s. Koska D-termi antaa virran asetusarvon yksikössä A, kertoimen `K_d` on kumottava rpm/s: sen yksikkö on A·s/rpm, jolloin tulon yksikkö on A.

Derivaatan suodatus voi vähentää suurtaajuista kohinaa, mutta liian voimakas suodatus viivästyttää myös hyödyllistä vastetta. Yleinen toteutus derivoi mittausta asetusarvon sijaan, jotta asetusarvon muutos ei aiheuta derivaatan äkillistä piikkiä. Vahvistukset ja etumerkit on sovitettava valittuun rakenteeseen.

<a id="section-5"></a>
## 5. Näytteenotto, kyllästyminen ja anti-windup

Digitaalinen säädin päivittää laskennan äärellisin aikavälein. Jos virhe on vakio 20 rpm yhden sekunnin ajan, 100 näytettä aika-askeleella `dt = 0.01 s` ja 10 näytettä aika-askeleella `dt = 0.1 s` integroivat molemmat arvon 20 rpm·s. Jos `dt` jätetään kertomatta, nopeammin päivittyvä säädin kerryttää virhettä kymmenkertaisesti. Käytännön viritys riippuu silti näytteenotosta, viiveistä, kohinasta ja käytön dynamiikasta.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Toimilaitteen rajat voivat estää pyydetyn virran toteuttamisen. Jos integraali jatkaa kasvuaan kyllästymisen aikana (**integral windup**), kuorman vähentyessä voi syntyä suuri ylitys. Anti-windup voi pysäyttää integroinnin silloin, kun se kasvattaisi jo kyllästynyttä ohjausta, tai korjata sisäistä tilaa pyydetyn ja toteutuneen komennon erotuksen perusteella. Rajoita **koko ohjauspyyntö** ja käsittele P-termin osuus oikein.

<a id="section-6"></a>
## 6. Robotin nivelen pitäminen paikallaan painovoimaa vastaan

Moottorin momenttivakio $K_t$ ilmoittaa syntyvän momentin **momenttia tuottavaa virtayksikköä** kohti. $K_t$:n yksikkö on N·m/A, virran A ja momentin N·m. Esimerkiksi $K_t=0.1\ \mathrm{N\cdot m/A}$ ja virta 2 A tuottavat 0.2 N·m, kun valmistajan virtamääritelmä otetaan huomioon.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Tarkastellaan vaakasuuntaisen akselin ympäri kiertyvää vipua, jossa massa $m$ sijaitsee etäisyydellä $L$ nivelestä. Kun kulma $\theta$ mitataan vaakatasosta, painovoiman aiheuttaman momentin itseisarvo on $mgL|\cos\theta|$. Paikallaan pysyttäessä moottorimomentin on vastustettava kuormamomenttia niin, että niiden etumerkillinen summa on nolla. Nivel voi siis tarvita nollasta poikkeavaa virtaa, vaikka asentovirhe olisi nolla. Mekaaninen jarru tai aidosti itselukittuva mekanismi voi pitää kuorman ilman virtaa, mutta **harmoninen eli strain-wave-vaihde ei ole itsessään itselukittuva**.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Ulkorottorisessa BLDC-moottorissa ulkokuori pyörii, kun taas sisäroottorisessa BLDC-moottorissa pyörivä osa on sisällä. **Roottori** tarkoittaa aina pyörivää osaa ja **staattori** paikallaan pysyvää osaa. Osien säteittäinen sijainti ei muuta näitä määritelmiä.

<a id="section-7"></a>
## 7. Tarkistukset ja rajoitukset

Kaikki virta-arvot ovat opetukseen tarkoitettuja idealisointeja, eivät oikean laitteiston ohjausohjeita. Todellinen käyttö edellyttää oikeita virtamääritelmiä, rajoja, enkooderin kalibrointia, lämpörajoja, suodatusta, anti-windupia, turvalukituksia ja turvallista testausta. Yhteen malliin sopivat PID-vahvistukset eivät ole yleispäteviä.

[Matematiikan perusteet](00-calculus-foundations.md) · [Trigonometriataulukko](../TRIGONOMETRY.md) · [Ensimmäisen kertaluvun dynamiikka](02-first-order-dynamics.md)
