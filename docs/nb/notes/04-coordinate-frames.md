# 4. Robotens koordinatsystemer og plan kinematikk

**Languages:** [en](../../en/notes/04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Enheter på denne siden (forklart før eksemplene):** `mm` — millimeter = 0.001 m; `°` — grad. [Enhetsoversikt](../UNITS.md).

[README](../README.md) · [Trigonometri](../TRIGONOMETRY.md) · [Matematiske symboler](../SYMBOLS.md) · [Tilbakekobling](03-feedback-control.md)

> **Læremodell:** Ikke bruk disse forenklede formlene til å styre ekte maskiner.

## Innhold
1. [Hvorfor koordinatsystemer er nødvendige](#section-1)
2. [Rotere og forskyve et punkt](#section-2)
3. [Kjeder av koordinatsystemer](#section-3)
4. [Foroverkinematikk med to lenker](#section-4)
5. [To albueposisjoner og rekkevidde](#section-5)
6. [Oppgaver med fullstendige løsninger](#section-6)
7. [Modellens grenser og matrisenotasjon](#section-7)

<a id="section-1"></a>
## 1. Hvorfor koordinatsystemer er nødvendige

Et **koordinatsystem (coordinate frame)** består av origo og akser med retning. **Verdenskoordinatsystemet (world frame)** W kan være festet til robotbasen, mens **verktøykoordinatsystemet (tool frame)** T følger verktøyet. Samme fysiske punkt får ulike tallkoordinater i de to systemene. Posisjon angir et punkt, orientering beskriver aksenes retning. Å endre koordinatsystem betyr ikke i seg selv at roboten beveger seg.

Bruk samme enhet for alle lengder (her mm). Positive vinkler i 2D måles mot klokken fra verdens +X. Indeks w betyr verden, l betyr lokal. Vi antar stive lenker.

<a id="section-2"></a>
## 2. Rotere og forskyve et punkt

![Verdens- og lokale akser rotert +90°, med P og Q.](../../../assets/figures/world_local_frames.svg)

*Verdens- og lokale akser rotert +90°, med P og Q.*

Figuren viser T med origo på (100 mm, 50 mm) i verden, og lokale akser rotert +90°. Lokal +x peker langs verdens +Y, lokal +y langs verdens −X. Dermed blir lokal P=(0 mm, 10 mm) til (90 mm, 50 mm) i verden, mens Q=(20 mm, 0 mm) blir (100 mm, 70 mm).

Med lokalt punkt $(x_l,y_l)$, origo $(t_x,t_y)$ i verden og vinkel $\theta$, **roter først og forskyv deretter**:

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

Fortegnet til $\sin\theta$ og $\cos\theta$ avhenger av vinkelretningen. Ved $\theta=0^\circ$ legger vi bare til origos forskyvning. Dette er ikke motorkommandoer.

<a id="section-3"></a>
## 3. Kjeder av koordinatsystemer

Rammer kan kobles som **W → T → S** (verden → verktøy → sensor). Med T som over: Hvis S har origo på (20 mm, 0 mm) i T og parallelle akser, er S-origo i verden (100 mm, 70 mm). Punktet (0 mm, 10 mm) i S blir (90 mm, 70 mm) i verden. Gå fra barnets til foreldrens ramme trinnvis.

For kolonnevektorer gjelder $T_{WS}=T_{WT}T_{TS}$, der $T_{AB}$ omregner koordinater **fra B til A**. Rekkefølgen på matriser er viktig.

**Fullstendig matriseutregning (kolonnevektorer):** Verktøyrammen T er rotert +90° fra W og har verdensposisjon (100 mm, 50 mm). Sensorrammen S har ingen ekstra rotasjon og ligger ved (20 mm, 0 mm) i T, samme sted som Q i forrige figur. Rotasjonskomponentene er dimensjonsløse, og translasjonene måles i mm:

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

I matriseproduktet roteres sensorens lokale forskyvning (20 mm, 0 mm) først til (0 mm, 20 mm) i W og legges så til (100 mm, 50 mm). Punktet (0 mm, 10 mm) i S blir derfor (90 mm, 70 mm) i W. Å legge 20 mm direkte til verdens-X er feil fordi forskyvningen er oppgitt **i T**. Den siste homogene koordinaten 1 er dimensjonsløs, ikke en lengde. Dette er koordinatmatematikk; [ROS 2 tf2](06-ros2-foundations.md#section-7) publiserer og slår opp tidsstemplede transformasjoner, men løser ikke invers kinematikk.

<a id="section-4"></a>
## 4. Foroverkinematikk med to lenker

![To lenker: første vinkel 30°, andre relative vinkel 60°.](../../../assets/figures/two_link_fk.svg)

*To lenker: første vinkel 30°, andre relative vinkel 60°.*

En plan arm har lenkelengder $L_1,L_2$. Den første leddvinkelen $\theta_1$ måles fra verdens +X. Den andre $\theta_2$ måles **relativt til første lenke**. Derfor har den andre lenken absolutt vinkel $\theta_1+\theta_2$. Verktøyposisjonen er summen av lenkevektorene:

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

For L1=100 mm, L2=50 mm, $\theta_1=30^\circ$, $\theta_2=60^\circ$ er albueleddet på (86.60 mm, 50 mm). Andre lenke peker rett opp med absolutt vinkel 90°, og verktøyet står på (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. To albueposisjoner og rekkevidde

![To leddposisjoner gir det samme endepunktet.](../../../assets/figures/two_link_elbow_solutions.svg)

*To leddposisjoner gir det samme endepunktet.*

**Invers kinematikk (inverse kinematics)** finner vinkler til et bestemt målpunkt. To lenker på 100 mm hver når (100 mm, 100 mm) både med $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ og $(+90^\circ,-90^\circ)$. Den andre vinkelen er relativ, ikke absolutt.

![Ideelt ringformet arbeidsområde fra 50 mm til 150 mm.](../../../assets/figures/two_link_workspace.svg)

*Ideelt ringformet arbeidsområde fra 50 mm til 150 mm.*

Uten leddgrenser eller kollisjoner gjelder $|L_1-L_2|\le r\le L_1+L_2$. For 100 mm og 50 mm er det ideelle **arbeidsområdet (reachable workspace)** en ring med indre radius 50 mm og ytre 150 mm. Reelle hindringer kan gjøre området mindre.

<a id="section-6"></a>
## 6. Oppgaver med fullstendige løsninger

Alle **seks oppgavene nedenfor har svar og begrunnelse**. Det er ingen personlige spørsmål som står ubesvart.

<a id="worked-1"></a>
### 6.1. Lokalt punkt P i rotert ramme

**Oppgave.** T har verdensposisjon (100 mm, 50 mm), rotert +90°. Finn verdenskoordinatene til P=(0 mm, 10 mm).

**Løsning.** Lokal +y peker langs verdens −X, så X reduseres med 10 mm.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Svar:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Punkt Q langs lokal x-akse

**Oppgave.** Bruk samme T og finn Q=(20 mm, 0 mm) i verden.

**Løsning.** Lokal +x peker langs verdens +Y, så bare Y øker med 20 mm.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Svar:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Foroverkinematikk med to lenker

**Oppgave.** L1=100 mm, L2=50 mm, θ1=30°, relativ θ2=60°. Finn verktøyet.

**Løsning.** Den andre lenkens absolutte retning er 30°+60°=90°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Svar:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. To inverse løsninger

**Oppgave.** To 100-mm-lenker skal nå (100 mm, 100 mm). Finn to vinkelpar.

**Løsning.** Én stilling går høyre og opp, den andre opp og høyre.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Sjekk rekkevidde uten vinkler

**Oppgave.** L1=100 mm, L2=50 mm. Er (0 mm, 120 mm) og (0 mm, 0 mm) innenfor rekkevidde?

**Løsning.** Sammenlign avstanden med differansen og summen av lenkelengdene.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

(0 mm, 120 mm) er **innenfor rekkevidde**, siden 50 ≤ 120 ≤ 150. Origo (0 mm, 0 mm) er **utenfor rekkevidde**, fordi avstanden er null.

<a id="worked-6"></a>
### 6.6. Cosinus til den relative albuevinkelen

**Oppgave.** L1=100 mm, L2=50 mm, r=120 mm. Beregn cos θ2.

**Løsning.** Cosinus angir bøyens størrelse, men speilede albueposisjoner har motsatte fortegn.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

Den indre trekantvinkelen er $\varphi=180^\circ-|\theta_2|$. Bare radius gir ikke $\theta_1$. Se illustrasjonen i [Trigonometri](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. Modellens grenser og matrisenotasjon

Modellen har stive 2D-lenker, ideelle enkodere og ingen kollisjoner. I virkeligheten finnes leddgrenser, slark, elastisitet, målefeil, kamerakalibrering og 3D-bevegelse. En enkoder måler leddvinkel, ikke direkte verdensposisjon. Eksemplene må ikke styre ekte maskiner.

**Valgfri homogen matrise 3×3** kombinerer rotasjon og forskyvning for punkt-kolonnevektoren $[x_l,y_l,1]^T$. For en ren forskyvningsvektor er siste koordinat 0.

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

[Trigonometri](../TRIGONOMETRY.md) · [Matematiske symboler](../SYMBOLS.md) · [Tilbakekobling](03-feedback-control.md)

[Neste: rotasjon, hastighet og singulariteter](05-velocity-jacobian.md)
