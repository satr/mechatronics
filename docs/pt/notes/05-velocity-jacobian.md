# 5. Rotação, velocidade linear e singularidades

**Languages:** [en](../../en/notes/05-velocity-jacobian.md) · [fr](../../fr/notes/05-velocity-jacobian.md) · [de](../../de/notes/05-velocity-jacobian.md) · [it](../../it/notes/05-velocity-jacobian.md) · [es](../../es/notes/05-velocity-jacobian.md) · [pt](05-velocity-jacobian.md) · [zh](../../zh/notes/05-velocity-jacobian.md) · [ja](../../ja/notes/05-velocity-jacobian.md) · [nb](../../nb/notes/05-velocity-jacobian.md) · [ru](../../ru/notes/05-velocity-jacobian.md) · [ko](../../ko/notes/05-velocity-jacobian.md) · [fi](../../fi/notes/05-velocity-jacobian.md) · [pl](../../pl/notes/05-velocity-jacobian.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `rad` — radiano; `rad/s` — radiano / segundo — velocidade angular; `mm/rad` — milímetro / radiano — coeficiente jacobiano (comprimento por ângulo); `°` — grau. [Glossário de unidades](../UNITS.md).

[README](../README.md) · [Trigonometry](../TRIGONOMETRY.md#unit-circle-values) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)

> Apenas modelo didático ideal; não utilizar para controlar máquinas.

A extremidade de um braço em rotação descreve um arco. A velocidade instantânea é tangente ao arco e perpendicular ao braço. Começamos pela geometria, depois as derivadas e, opcionalmente, a matriz jacobiana (Jacobian matrix).

## Conteúdo

1. [Rotação e velocidade tangencial](#section-1)
2. [Origem das derivadas](#section-2)
3. [Exemplos de velocidade e sinais](#section-3)
4. [Dois segmentos: ângulos relativos e absolutos](#section-4)
5. [Singularidades dobrada e estendida](#section-5)
6. [Três deslocamentos perto da dobra](#section-6)
7. [Apêndice: matriz jacobiana e exemplos resolvidos](#section-7)

<a id="section-1"></a>
## 1. Rotação e velocidade tangencial

Considere um segmento rígido de comprimento $L$ girando em torno do pivô fixo $O$. Seja $\Delta Q$ a variação do ângulo **em radianos** durante $\Delta t>0$. Se o sentido de rotação não muda nesse intervalo, a ponta percorre um arco de circunferência. O **comprimento do arco** é exatamente $\Delta s=L|\Delta Q|$. A **distância orientada ao longo do arco** é $L\Delta Q$: o sinal indica o sentido da rotação. Não se deve confundir essa distância com o deslocamento em linha reta (a corda) entre as posições da ponta.

$$
\Delta s=L\lvert\Delta Q\rvert,\qquad
\Delta s_{\mathrm{signed}}=L\Delta Q
$$

Dividindo o comprimento do arco pelo tempo decorrido, obtemos a **rapidez média** nesse intervalo:

$$
\overline{v}=\frac{\Delta s}{\Delta t}
=L\left\lvert\frac{\Delta Q}{\Delta t}\right\rvert
$$

Para chegar à **rapidez instantânea**, tomamos o limite $\Delta t\to0$. A velocidade angular é $\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t$ em rad/s; logo, o módulo da velocidade linear é $v=L|\omega|$. O vetor velocidade é **tangente à circunferência**, perpendicular ao segmento. Para $Q=45^\circ$ e rotação anti-horária ($\omega>0$), a ponta se move para a esquerda e para cima: componente horizontal negativa e vertical positiva.

$$
v=L\lvert\dot Q\rvert
$$

![Velocidade tangencial e componentes com sinal em Q=45°.](../../../assets/figures/link_tangent_velocity.svg)

*Velocidade tangencial e componentes com sinal em Q=45°.*

<a id="section-2"></a>
## 2. Origem das derivadas

As coordenadas dependem de Q, e Q depende do tempo. A regra da cadeia (chain rule) multiplica a variação de posição por radiano pelos radianos por segundo.

$$
x(t)=L\cdot\cos\bigl(Q(t)\bigr),\qquad y(t)=L\cdot\sin\bigl(Q(t)\bigr)
$$

$$
v_x=\frac{\mathrm{d}x}{\mathrm{d}t}
=\frac{\mathrm{d}x}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=-L\cdot\sin(Q)\cdot\dot{Q}
$$

$$
v_y=\frac{\mathrm{d}y}{\mathrm{d}t}
=\frac{\mathrm{d}y}{\mathrm{d}Q}\cdot\frac{\mathrm{d}Q}{\mathrm{d}t}
=L\cdot\cos(Q)\cdot\dot{Q}
$$

A velocidade angular $\dot Q=\mathrm{d}Q/\mathrm{d}t$ mede-se em rad/s e não é o próprio ângulo. Com L em mm, vx e vy estão em mm/s. As derivadas trigonométricas exigem radianos.


$$
\omega=\dot{Q},\qquad \omega_1=\dot{Q}_1,\qquad \omega_2=\dot{Q}_2
$$

<a id="section-3"></a>
## 3. Exemplos de velocidade e sinais

Com L=150 mm, Q=45° e ω=+0.1 rad/s, as componentes têm módulos iguais: esquerda e cima. Inverter ω inverte os sinais. Com Q=0°, vy=15 mm/s e vx=0.

$$
Q=45^\circ:\quad v_x=-150\frac{\sqrt2}{2}\cdot0.1\approx-10.61\ \mathrm{mm/s}
$$

$$
v_y=+150\frac{\sqrt2}{2}\cdot0.1\approx+10.61\ \mathrm{mm/s}
$$

$$
\sqrt{v_x^2+v_y^2}=L\lvert\dot Q\rvert=15\ \mathrm{mm/s}
$$

O ponto sobre $Q$ indica a **derivada no tempo** $\dot Q$, e não uma multiplicação pelo ângulo. Trocar $\omega$ por $-\omega$ inverte os sinais das duas componentes sem alterar o módulo $L|\omega|$.

<a id="section-4"></a>
## 4. Dois segmentos: ângulos relativos e absolutos

Q1 é o ângulo absoluto desde +X; Q2 é o ângulo relativo do cotovelo. O ângulo absoluto do segundo segmento é Q1+Q2 e sua velocidade angular é ω₁+ω₂.

$$
X=L_1\cdot\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)
$$

$$
Y=L_1\cdot\sin(Q_1)+L_2\cdot\sin(Q_1+Q_2)
$$

$$
v_x=-L_1\cdot\sin(Q_1)\cdot\dot{Q}_1
-L_2\cdot\sin(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

$$
v_y=L_1\cdot\cos(Q_1)\cdot\dot{Q}_1
+L_2\cdot\cos(Q_1+Q_2)\cdot(\dot{Q}_1+\dot{Q}_2)
$$

As duas articulações contribuem para a velocidade da ponta: no primeiro segmento aparece $\dot Q_1$ e no segundo, $\dot Q_1+\dot Q_2$. Usar somente $\dot Q_2$ para o segundo seria incorreto, pois seu ângulo é relativo ao primeiro segmento.

<a id="section-5"></a>
## 5. Singularidades dobrada e estendida

Com L1=100 mm e L2=50 mm, o alcance ideal fica entre 50 e 150 mm. Nas posições totalmente dobrada (Q2=180°) e estendida (Q2=0°), a velocidade radial instantânea é zero para velocidades articulares finitas.

$$
r^2=L_1^2+L_2^2+2L_1L_2\cos(Q_2)
$$

$$
\lvert L_1-L_2\rvert\le r\le L_1+L_2
$$

$$
\frac{\mathrm{d}r}{\mathrm{d}Q_2}
=-\frac{L_1L_2\sin(Q_2)}{r}
$$

Esta fórmula da derivada exige $r>0$. Se os dois segmentos tiverem o mesmo comprimento ($L_1=L_2$), na posição completamente dobrada sobre a base ($Q_2=180^\circ$) teremos $r=0$: a fórmula dividiria por zero. Nessa posição, a distância radial não é diferenciável em relação a um desvio **com sinal** do ângulo do cotovelo. O caso especial não ocorre com os comprimentos desiguais $L_1=100$ mm e $L_2=50$ mm usados aqui.

Limites articulares e colisões podem reduzir a área de trabalho real. Alcançar uma posição não garante a orientação desejada da ferramenta nem espaço livre para evitar obstáculos.

<a id="section-6"></a>
## 6. Três deslocamentos perto da dobra

Com o primeiro segmento fixo, δ é o pequeno desvio em radianos desde a dobra. O deslocamento ao longo do eixo fixo do primeiro segmento difere da alteração do raio.

$$
\Delta x_{\mathrm{axis}}=L_2\bigl(1-\cos(\delta)\bigr)
\approx\frac{L_2\delta^2}{2}
$$

$$
\Delta y_{\mathrm{perp}}=L_2\cdot\sin(\delta)\approx L_2\delta
$$

$$
\Delta r=\sqrt{(L_1-L_2)^2+2L_1L_2\bigl(1-\cos(\delta)\bigr)}-(L_1-L_2)
$$

$$
L_1>L_2>0:\qquad
\Delta r\approx\frac{L_1L_2}{2(L_1-L_2)}\delta^2
$$

A identidade 1−cosδ=2sin²(δ/2) e sin(δ/2)≈δ/2 explicam o quadrado e o fator 1/2. O aumento radial é ≈50δ² mm, o axial ≈25δ² mm.

As aproximações só valem para $\delta$ pequeno em radianos. Se $\delta$ for reduzido à metade, tanto a variação axial como a radial, que são quadráticas, caem aproximadamente **para um quarto**; a variação transversal cai **pela metade**. Exigir velocidade radial constante e não nula para $\delta\to0$ implicaria velocidade articular ilimitada na cinemática inversa ideal. Um braço real pode começar a abrir-se com velocidade angular finita e velocidade radial inicialmente nula.

$$
1-\cos(\delta)=2\sin^2\left(\frac{\delta}{2}\right)
\approx2\left(\frac{\delta}{2}\right)^2=\frac{\delta^2}{2}
$$

![Deslocamentos axial, transversal e radial perto da dobra.](../../../assets/figures/folded_displacement_curves.svg)

*Deslocamentos axial, transversal e radial perto da dobra.*

Uma velocidade radial positiva constante perto da dobra exige velocidades angulares cada vez maiores quando δ→0. Exatamente na dobra, velocidades articulares finitas não geram imediatamente velocidade radial.

$$
\left.\frac{\mathrm{d}r}{\mathrm{d}\delta}\right|_{L_1=100,L_2=50}
=\frac{5000\sin(\delta)}{r}
\approx100\delta\ \mathrm{mm/rad}
$$

$$
v_r\approx(100\delta)\dot\delta\ \mathrm{mm/s},
\qquad
\dot\delta\approx\frac{1\ \mathrm{mm/s}}{100\ \mathrm{mm/rad}\cdot\delta}
$$

![Velocidade angular necessária junto à singularidade.](../../../assets/figures/folded_radial_speed.svg)

*Velocidade angular necessária junto à singularidade.*

<a id="section-7"></a>
## 7. Apêndice: matriz jacobiana e exemplos resolvidos

A matriz jacobiana (Jacobian matrix) relaciona velocidades articulares e velocidade cartesiana. Seu determinante L1L2 sin Q2 se anula com os segmentos colineares. O modelo não inclui colisões nem limites.

$$
v_x=J_{11}\cdot\omega_1+J_{12}\cdot\omega_2
$$

$$
v_y=J_{21}\cdot\omega_1+J_{22}\cdot\omega_2
$$

| Coeficiente | Geometria da transformação de velocidades |
| --- | --- |
| $J_{11}$ | $-L_1\sin(Q_1)-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{12}$ | $-L_2\cdot\sin(Q_1+Q_2)$ |
| $J_{21}$ | $L_1\cos(Q_1)+L_2\cdot\cos(Q_1+Q_2)$ |
| $J_{22}$ | $L_2\cdot\cos(Q_1+Q_2)$ |



**Derivação do determinante.** Cada coeficiente é uma derivada parcial da coordenada X ou Y da ferramenta em relação ao ângulo Q1 ou Q2 em radianos. Com comprimentos em mm, a unidade é mm/rad; multiplicar por rad/s produz mm/s.

$$
J_{11}=\frac{\partial X}{\partial Q_1},\qquad
J_{12}=\frac{\partial X}{\partial Q_2}
$$

$$
J_{21}=\frac{\partial Y}{\partial Q_1},\qquad
J_{22}=\frac{\partial Y}{\partial Q_2}
$$

$$
\det J=J_{11}J_{22}-J_{12}J_{21}
$$

$$
\det J=L_1L_2\bigl[\sin(Q_1+Q_2)\cos(Q_1)
-\sin(Q_1)\cos(Q_1+Q_2)\bigr]
$$

$$
\det J=L_1L_2\sin\bigl((Q_1+Q_2)-Q_1\bigr)
$$

Ao desenvolver os dois produtos do determinante, os termos com L2 ao quadrado se cancelam. A identidade da diferença de senos elimina Q1.

$$
\det J=L_1L_2\sin(Q_2)
$$

![As duas contribuições das juntas somam-se como vetores para obter a velocidade da ferramenta.](../../../assets/figures/two_link_jacobian_velocity.svg)

*As duas contribuições das juntas somam-se como vetores para obter a velocidade da ferramenta.*

### Exemplos totalmente resolvidos

1. Um segmento de $L=150$ mm aponta para a direita quando $Q=0^\circ$. Com $\omega=+0.1$ rad/s, $\sin0^\circ=0$ e $\cos0^\circ=1$; portanto $v_x=-150\cdot0\cdot0.1=0$ e $v_y=150\cdot1\cdot0.1=+15$ mm/s. A ponta move-se para cima.
2. Com $Q=45^\circ$ e $\omega=-0.1$ rad/s, invertemos o sentido da rotação: $v_x=-150\sin45^\circ\cdot(-0.1)\approx+10.61$ mm/s e $v_y=150\cos45^\circ\cdot(-0.1)\approx-10.61$ mm/s. A ponta vai para baixo e à direita, mas a rapidez permanece $L|\omega|=15$ mm/s.
3. Para $L_1=100$ mm, $L_2=50$ mm, $Q_1=30^\circ$, $Q_2=60^\circ$, $\omega_1=0.1$ rad/s e $\omega_2=0.2$ rad/s, o segundo segmento tem orientação absoluta $Q_1+Q_2=90^\circ$ e velocidade angular $\omega_1+\omega_2=0.3$ rad/s. Assim, $v_x=-100\sin30^\circ\cdot0.1-50\sin90^\circ\cdot0.3=-5-15=-20$ mm/s e $v_y=100\cos30^\circ\cdot0.1+50\cos90^\circ\cdot0.3\approx+8.66$ mm/s.
4. Perto da dobra, com $\delta=0.02$ rad, a variação axial ao longo do eixo **fixo** é aproximadamente $25\delta^2=25\cdot0.02^2=0.010$ mm, a transversal é $50\delta=1.000$ mm e o aumento radial é $50\delta^2=0.020$ mm. Os dois termos quadráticos não têm o mesmo coeficiente.

[Trigonometry](../TRIGONOMETRY.md) · [Coordinate frames](04-coordinate-frames.md) · [Calculus foundations](00-calculus-foundations.md)
