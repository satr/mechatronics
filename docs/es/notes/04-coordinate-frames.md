# 4. Sistemas de coordenadas del robot y cinemática plana

**Languages:** [en](../../en/notes/04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Unidades empleadas aquí (definidas antes de los ejemplos):** `mm` — milímetro = 0.001 m; `°` — grado. [Glosario de unidades](../UNITS.md).

[README](../README.md) · [Trigonometría](../TRIGONOMETRY.md) · [Símbolos matemáticos](../SYMBOLS.md) · [Control realimentado](03-feedback-control.md)

> **Modelo educativo:** Estas fórmulas ideales no deben usarse para controlar máquinas reales.

## Contenido
1. [Por qué se usan sistemas de coordenadas](#section-1)
2. [Rotar y trasladar un punto](#section-2)
3. [Componer distintos sistemas](#section-3)
4. [Cinemática directa de dos eslabones](#section-4)
5. [Dos soluciones y región alcanzable](#section-5)
6. [Ejercicios resueltos paso a paso](#section-6)
7. [Limitaciones y matrices](#section-7)

<a id="section-1"></a>
## 1. Por qué se usan sistemas de coordenadas

Un **sistema de coordenadas (coordinate frame)** tiene origen y ejes orientados. El **sistema global (world frame)** W puede fijarse a la base y el **sistema de la herramienta (tool frame)** T se mueve con ella. El mismo punto físico tiene distintas coordenadas numéricas según el sistema. Posición indica el punto; orientación, la dirección de los ejes. Una transformación no mueve necesariamente el robot.

Todas las longitudes usan la misma unidad (mm). Los ángulos positivos se miden en sentido antihorario desde +X global. Los subíndices w y l indican mundo y local. Se supone un mecanismo rígido en 2D.

<a id="section-2"></a>
## 2. Rotar y trasladar un punto

![Ejes del mundo y de la herramienta girados +90°, puntos P y Q.](../../../assets/figures/world_local_frames.svg)

*Ejes del mundo y de la herramienta girados +90°, puntos P y Q.*

El origen T está en (100 mm, 50 mm) global, con giro +90°. Su +x local apunta hacia +Y global y +y local hacia −X global. Por tanto, P=(0 mm, 10 mm) local pasa a (90 mm, 50 mm) global, y Q=(20 mm, 0 mm) a (100 mm, 70 mm).

Para un punto local $(x_l,y_l)$, origen $(t_x,t_y)$ en el mundo y giro $\theta$, **primero rotar y luego trasladar**:

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

El signo de $\sin\theta$ y $\cos\theta$ depende del ángulo dirigido. Con $\theta=0^\circ$ solo se suma el desplazamiento del origen. Esto transforma coordenadas, no manda mover un motor.

<a id="section-3"></a>
## 3. Componer distintos sistemas

Los sistemas se encadenan **W → T → S** (mundo → herramienta → sensor). Si S tiene origen (20 mm, 0 mm) en T y ejes paralelos, su origen global es (100 mm, 70 mm). El punto (0 mm, 10 mm) en S se transforma en (90 mm, 70 mm) global. Empezamos por el sistema hijo.

Con vectores columna, $T_{WS}=T_{WT}T_{TS}$ y $T_{AB}$ transforma **de B a A**. El orden de las matrices afecta al resultado.

**Cálculo matricial completo (vectores columna):** T está girado +90° respecto de W y su origen global es (100 mm, 50 mm). S no añade rotación y su origen en T es (20 mm, 0 mm), el mismo lugar que Q en el dibujo anterior. Los coeficientes de rotación no tienen unidades; las traslaciones están en mm:

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

Al multiplicar, el desplazamiento local (20 mm, 0 mm) se gira y pasa a ser (0 mm, 20 mm) en W, antes de sumarse a (100 mm, 50 mm). Por eso el punto (0 mm, 10 mm) en S tiene coordenadas (90 mm, 70 mm) en W. Sumar 20 mm directamente a la X global sería un error: el desplazamiento está expresado **en T**. El último 1 es una coordenada homogénea adimensional. Esto es geometría; [tf2 de ROS 2](06-ros2-foundations.md#section-7) publica y consulta transformaciones con marca temporal, pero no resuelve la cinemática inversa.

<a id="section-4"></a>
## 4. Cinemática directa de dos eslabones

![Primer ángulo 30°, segundo ángulo relativo 60°.](../../../assets/figures/two_link_fk.svg)

*Primer ángulo 30°, segundo ángulo relativo 60°.*

Un brazo plano tiene eslabones $L_1,L_2$. $\theta_1$ se mide desde +X global y $\theta_2$ **respecto al primero**. La dirección absoluta del segundo es $\theta_1+\theta_2$. La posición de la herramienta es la suma de los vectores:

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

Con L1=100 mm, L2=50 mm, $\theta_1=30^\circ$, $\theta_2=60^\circ$, el codo está en (86.60 mm, 50 mm). El segundo eslabón apunta verticalmente y la herramienta está en (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. Dos soluciones y región alcanzable

![Dos configuraciones para una misma posición del extremo.](../../../assets/figures/two_link_elbow_solutions.svg)

*Dos configuraciones para una misma posición del extremo.*

La **cinemática inversa (inverse kinematics)** obtiene ángulos para una posición. Dos eslabones de 100 mm llegan a (100 mm, 100 mm) tanto con $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ como con $(+90^\circ,-90^\circ)$. El segundo ángulo es relativo.

![Región ideal en forma de anillo de radios 50–150 mm.](../../../assets/figures/two_link_workspace.svg)

*Región ideal en forma de anillo de radios 50–150 mm.*

Sin límites articulares ni colisiones, $|L_1-L_2|\le r\le L_1+L_2$. Con eslabones de 100 mm y 50 mm, la región ideal es un **anillo** de radios 50 mm y 150 mm. Los obstáculos reales pueden reducirla.

<a id="section-6"></a>
## 6. Ejercicios resueltos paso a paso

Los **seis ejercicios tienen soluciones y explicaciones completas**. No queda ninguna pregunta personal sin respuesta.

<a id="worked-1"></a>
### 6.1. Punto local P en sistema girado

**Problema.** T en (100 mm, 50 mm), girado +90°. Encontrar P=(0 mm, 10 mm) global.

**Solución.** El +y local apunta a −X global: restar 10 mm a X.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Respuesta:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Punto Q sobre el eje x local

**Problema.** Con el mismo T, encontrar Q=(20 mm, 0 mm) global.

**Solución.** El +x local apunta a +Y global: sumar 20 mm a Y.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Respuesta:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Cinemática directa de dos eslabones

**Problema.** L1=100 mm, L2=50 mm, θ1=30°, θ2 relativo=60°. Hallar la herramienta.

**Solución.** La dirección absoluta del segundo eslabón es 30°+60°=90°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Respuesta:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. Dos soluciones inversas

**Problema.** Dos eslabones de 100 mm deben alcanzar (100 mm, 100 mm). Hallar dos pares de ángulos.

**Solución.** Una postura va a la derecha y luego arriba; la otra invierte el orden.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Comprobar el alcance sin ángulos

**Problema.** L1=100 mm, L2=50 mm. Verificar (0 mm, 120 mm) y (0 mm, 0 mm).

**Solución.** Comparamos la distancia con diferencia y suma de longitudes.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

(0 mm, 120 mm) es **alcanzable** pues 50 ≤ 120 ≤ 150. El origen (0 mm, 0 mm) **no es alcanzable** porque su distancia es cero.

<a id="worked-6"></a>
### 6.6. Coseno del ángulo relativo del codo

**Problema.** L1=100 mm, L2=50 mm, r=120 mm: calcular cos θ2.

**Solución.** El coseno determina el valor absoluto del ángulo, pero el signo cambia al reflejar el codo.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

El ángulo interior del triángulo es $\varphi=180^\circ-|\theta_2|$. El radio no determina por sí solo $\theta_1$. Véase el diagrama en [Trigonometría](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. Limitaciones y matrices

El modelo supone eslabones rígidos en 2D. Los robots reales tienen topes, colisiones, holguras, deformación, errores de encoders y calibración de cámaras. Un encoder mide el ángulo articular, no directamente la posición global. No se deben controlar máquinas con estos ejemplos.

La **matriz homogénea 3×3** opcional combina rotación y traslación para el punto columna $[x_l,y_l,1]^T$. Un vector libre de desplazamiento usa 0 como última coordenada.

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

[Trigonometría](../TRIGONOMETRY.md) · [Símbolos matemáticos](../SYMBOLS.md) · [Control realimentado](03-feedback-control.md)

[Siguiente: rotación, velocidad y singularidades](05-velocity-jacobian.md)
