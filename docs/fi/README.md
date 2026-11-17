# Mekatroniikan oppimateriaali — Suomi

**Kielet:** [en](../en/README.md) · [fr](../fr/README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](../pt/README.md) · [zh](../zh/README.md) · [ja](../ja/README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](../ko/README.md) · [fi](README.md) · [pl](../pl/README.md)

> [!WARNING]
> **Varoitus:** Tekoälyavusteinen opetusmateriaali voi sisältää virheitä, puutteita tai virheellisiä oletuksia. Tarkista kaavat ja yksiköt itsenäisesti. Älä käytä esimerkkejä oikeiden laitteiden ohjaamiseen.

## Sisältö

1. [Differentiaali- ja integraalilaskennan perusteet](notes/00-calculus-foundations.md)
2. [Liike, nopeus, derivaatat ja integraalit](notes/01-motion-calculus.md)
3. [Ensimmäisen kertaluvun dynamiikka ja pyörivät järjestelmät](notes/02-first-order-dynamics.md)
4. [Integraalitaulukko](INTEGRAL_TABLE.md)
5. [Derivaattojen taulukko](DERIVATIVE_TABLE.md)
6. [Kaavakooste](CHEATSHEET.md)
7. [Python-harjoitukset](exercises/README.md)
8. [Symbolit ja merkintätavat](SYMBOLS.md) · [Yksikköluettelo](UNITS.md)
9. [Trigonometria ja mekaniikan esimerkit](TRIGONOMETRY.md)
10. [Takaisinkytkentäsäätö: PID ja pitomomentti](notes/03-feedback-control.md)
11. [Robotin koordinaatistot: paikka ja kierto](notes/04-coordinate-frames.md)
12. [Pyöriminen, nopeus ja singulariteetit](notes/05-velocity-jacobian.md)
13. [ROS 2: arkkitehtuuri, solmut ja Docker-harjoitus](notes/06-ros2-foundations.md)

[Repositorion etusivu](../../README.md) · [Turvallisuus ja tarkkuus](SAFETY.md) · [Lisenssit](LICENSING.md)

## Opiskelutapa

Lue lyhyt jakso, toista laskelma itse, suorita siihen liittyvä offline-Python-esimerkki ja selitä tulos omin sanoin. Erota idealisoitu malli todellisesta fysikaalisesta järjestelmästä. Tarkista oletukset ennen kaavojen uudelleenkäyttöä.

Lukujen valinnaiset liitteet sisältävät tarkempia johtoja ja soveltuvuusrajoja. Mukana on myös kaavioita ja numeerisia kuvaajia. Johdot luvuille $4t$ ja 63.2 % löytyvät lukujen lisätietolinkeistä.

**Pythonin asennus ja virtuaaliympäristö (Windows/macOS/Linux):** [Harjoitusten ohjeet](exercises/README.md).

Kaikki oppiluvut 00–05 ja keskeiset matematiikan viitesivut on laajennettu suomeksi. **Englanninkielinen alkuperäinen on vertailukohta**, ja käännösten kieliasu sekä kaikkien yksityiskohtien vastaavuus edellyttävät vielä erillistä tarkistusta.

## ROS 2 Jazzy ilman GUI:ta: virtuaalinivel

[ROS 2 Jazzy ilman GUI:ta: virtuaalinivel](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**ROS 2 -robottiarkkitehtuuri:** [Viisi vaihetta ja Mermaid-kaavio](notes/08-ros2-robot-architecture.md).

**Ilman Composea:** [Käynnistä virallinen ROS-image suoraan](../../ros2/PLAIN_DOCKER.md).
