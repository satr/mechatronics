# Trigonometria: angoli, seno, coseno, tangente e arcotangente

**Lingue:** [en](../en/TRIGONOMETRY.md) · [fr](../fr/TRIGONOMETRY.md) · [de](../de/TRIGONOMETRY.md) · [it](TRIGONOMETRY.md) · [es](../es/TRIGONOMETRY.md) · [pt](../pt/TRIGONOMETRY.md) · [zh](../zh/TRIGONOMETRY.md) · [ja](../ja/TRIGONOMETRY.md) · [nb](../nb/TRIGONOMETRY.md) · [ru](../ru/TRIGONOMETRY.md) · [ko](../ko/TRIGONOMETRY.md) · [fi](../fi/TRIGONOMETRY.md) · [pl](../pl/TRIGONOMETRY.md)

**Unità usate qui (spiegate prima degli esempi):** `°` — grado; `rad` — radiante; `kg` — chilogrammo; `m` — metro; `m/s²` — metro / secondo² — accelerazione; `N·m` — newton · metro — momento torcente; `mm` — millimetro = 0.001 m; `N` — newton. [Glossario delle unità](UNITS.md).

[README](README.md) · [Calculus](notes/00-calculus-foundations.md) · [Integral table](INTEGRAL_TABLE.md)

<a id="unit-circle-values"></a>
## Circonferenza unitaria: seno e coseno

Un punto della circonferenza unitaria con angolo θ ha coordinate **(cos θ, sin θ)**. Gli angoli si misurano da +X in senso antiorario. Il coseno (cosine) è orizzontale, il seno (sine) verticale. Un unico disegno mostra 16 coppie esatte; una tabella aggiunge approssimazioni, tangente e arcotangente principale.

![Una circonferenza unitaria con 16 angoli e coppie esatte (cos θ, sin θ).](../../assets/figures/unit_circle_reference.svg)

*Una circonferenza unitaria con 16 angoli e coppie esatte (cos θ, sin θ).*

**Frazioni esatte e approssimazioni decimali:**

| θ | cos θ (esatto) | cos θ (decimale) | sin θ (esatto) | sin θ (decimale) | tan θ (esatto) | tan θ (decimale) | arctan(tan θ), principale |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| 0° | $1$ | 1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 30° | $\frac{\sqrt3}{2}$ | 0.8660 | $\frac12$ | 0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 45° | $\frac{\sqrt2}{2}$ | 0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 60° | $\frac12$ | 0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 90° | $0$ | 0.0000 | $1$ | 1.0000 | **indefinito** | — | — |
| 120° | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{2}$ | 0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 135° | $-\frac{\sqrt2}{2}$ | -0.7071 | $\frac{\sqrt2}{2}$ | 0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 150° | $-\frac{\sqrt3}{2}$ | -0.8660 | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |
| 180° | $-1$ | -1.0000 | $0$ | 0.0000 | $0$ | 0.0000 | $0^\circ$ |
| 210° | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\frac12$ | -0.5000 | $\frac{\sqrt3}{3}$ | 0.5774 | $30^\circ$ |
| 225° | $-\frac{\sqrt2}{2}$ | -0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $1$ | 1.0000 | $45^\circ$ |
| 240° | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $\sqrt3$ | 1.7321 | $60^\circ$ |
| 270° | $0$ | 0.0000 | $-1$ | -1.0000 | **indefinito** | — | — |
| 300° | $\frac12$ | 0.5000 | $-\frac{\sqrt3}{2}$ | -0.8660 | $-\sqrt3$ | -1.7321 | $-60^\circ$ |
| 315° | $\frac{\sqrt2}{2}$ | 0.7071 | $-\frac{\sqrt2}{2}$ | -0.7071 | $-1$ | -1.0000 | $-45^\circ$ |
| 330° | $\frac{\sqrt3}{2}$ | 0.8660 | $-\frac12$ | -0.5000 | $-\frac{\sqrt3}{3}$ | -0.5774 | $-30^\circ$ |

La tangente è **indefinita** a 90° e 270° perché cos θ = 0; anche arctan(tan θ) è indefinita. L’ultima colonna riporta il **valore principale** fra −90° e 90°, non sempre l’angolo originale: arctan(tan 135°) = −45° e arctan(tan 225°) = 45°. Le approssimazioni hanno quattro decimali. A 360° si ripetono i valori di 0°.

<a id="trigonometric-identities"></a>
### Identità trigonometriche utili

Uno spostamento di 90° scambia seno e coseno, talvolta invertendo il segno. Le parentesi sono indispensabili: cos(θ − 90°) è il coseno della differenza, non cos θ meno 90.

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

**Angoli negativi e periodicità:**

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

Segni nei quadranti (cos, sin, tan): I (+,+,+), II (−,+,−), III (−,−,+), IV (+,−,−). Gli angoli negativi ruotano in senso orario.

Per gli angoli inversi controllare il quadrante e l'intervallo principale.

<a id="inverse-cosine-reference"></a>
### Arcocoseno e stima dell'angolo

Da 0° a 180° il coseno diminuisce da 1 a −1. Quindi arccos(0.19) è poco inferiore a 80°: cos 80°≈0.1736 e arccos(0.19)≈79.05°. Poiché cos(+θ)=cos(−θ), due configurazioni articolari con segni opposti possono essere possibili. Il valore principale di arccos è tra 0° e 180°.

![cos θ versus θ, with arccos(0.19) marked](../../assets/figures/arccos_reference_curve.svg)



## Schema: cateto opposto, adiacente e ipotenusa

![Tre triangoli rettangoli: seno = cateto opposto a diviso ipotenusa c, coseno = adiacente b diviso c, tangente = a diviso b.](../../assets/figures/trig_ratios.svg)

Nella figura, **a** è il cateto opposto all’angolo θ, **b** quello adiacente e **c** l’ipotenusa. Per un angolo acuto, $\sin\theta=a/c$, $\cos\theta=b/c$ e $\tan\theta=a/b$ (per $b\ne0$). Le **lunghezze dei lati non sono negative**; la figura non determina da sola il segno delle funzioni per angoli negativi o altri quadranti. Con l’angolo orientato dall’asse x positivo, $\sin(+60^\circ)=+\sqrt3/2$ mentre $\sin(-60^\circ)=-\sqrt3/2$.

## Meccanica: momento del peso su una leva

Per una massa m a distanza L dal perno, con braccio inclinato di θ sull’orizzontale, il **modulo** della coppia gravitazionale è mgL|cos θ|. Il segno dipende dalla convenzione di rotazione.

$$
|M_g|=mgL|\cos\theta|.
$$

Con m = 0.5 kg, L = 0.2 m, g = 9.81 m/s² e θ = 60°, il modulo è 0.4905 N·m; a 0° 0.981 N·m e a 90° zero (carico puntuale ideale).

## Esempio inverso: calcolare l’angolo

Un asse sale di 0.05 m in 0.1 m di corsa orizzontale: rapporto 0.5. Quindi θ = arctan(0.5) ≈ 26.565°. L’argomento non è un angolo in gradi.

$$
\tan\theta=\frac{0.05\ \mathrm{m}}{0.1\ \mathrm{m}}=0.5,\qquad \theta=\arctan(0.5)\approx26.565^\circ.
$$

Conversione: θ_rad = θ_deg·π/180. Le librerie numeriche in genere usano radianti.

$$
\theta_{\mathrm{rad}}=\theta_{\mathrm{deg}}\frac{\pi}{180}.
$$

### Direzione di un vettore: perché serve `atan2`

Per un vettore dall'origine a $(x,y)$, l'arcotangente ordinaria considera solo il rapporto $y/x$. I vettori $(1, -1)$ e $(-1, 1)$ hanno lo stesso rapporto, ma appartengono a **quadranti diversi**. Per $x=-1\ \mathrm{mm}$ e $y=+1\ \mathrm{mm}$ il rapporto da solo produce la direzione globale errata:

$$
\arctan\left(\frac{y}{x}\right)=\arctan(-1)=-45^\circ,\qquad
\operatorname{atan2}(+1, -1)=+135^\circ.
$$

`atan2(y, x)` usa i segni di **entrambe le componenti** per la direzione di un vettore non nullo. Gli argomenti devono avere la stessa unità di lunghezza. Quando $x=0$, $y/x$ è indefinito, ma `atan2` individua ancora la direzione sull'asse se $y\ne0$. A $(0, 0)$ la direzione è indefinita; $+180^\circ$ e $-180^\circ$ sono la stessa direzione. È essenziale nel calcolo degli [angoli dei sistemi di riferimento](notes/04-coordinate-frames.md).

## Teorema del coseno: geometria a due segmenti

![Two-link robot triangle OAB, exact link lengths and the law of cosines](../../assets/figures/two_link_cosine_law.svg)

Base O, giunto A e utensile B formano un triangolo: OA = L1, AB = L2 e OB = r, distanza diretta dalla base all'utensile. La figura usa L1 = 100 mm, L2 = 50 mm, r = 120 mm. L'angolo interno φ è diverso dall'angolo relativo del giunto θ2: φ = 180° − |θ2|. La figura mostra θ2 negativo; la configurazione riflessa ha θ2 positivo.

Il teorema del coseno è $r^2=L_1^2+L_2^2-2L_1L_2\cos\varphi$. Dato che $\cos(180^\circ-|\theta_2|)=-\cos\theta_2$, otteniamo $r^2=L_1^2+L_2^2+2L_1L_2\cos\theta_2$, quindi $\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}$. Qui $(14400-10000-2500)/10000=0.19$ e $|\theta_2|\approx79.05^\circ$. Per raggiungere un punto (X,Y) resta da trovare θ1.


[Calcolo](notes/00-calculus-foundations.md) · [Controllo in retroazione](notes/03-feedback-control.md)
