# 4. Referenciais do robô e cinemática plana

**Languages:** [en](../../en/notes/04-coordinate-frames.md) · [fr](../../fr/notes/04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `mm` — milímetro = 0.001 m; `°` — grau. [Glossário de unidades](../UNITS.md).

[README](../README.md) · [Trigonometria](../TRIGONOMETRY.md) · [Símbolos matemáticos](../SYMBOLS.md) · [Controlo por realimentação](03-feedback-control.md)

> **Modelo didático:** Não usar esta geometria idealizada para comandar máquinas reais.

## Conteúdo
1. [Por que usar referenciais](#section-1)
2. [Rotação e translação de um ponto](#section-2)
3. [Encadear referenciais](#section-3)
4. [Cinemática direta de dois elos](#section-4)
5. [Duas configurações e espaço alcançável](#section-5)
6. [Exercícios com soluções completas](#section-6)
7. [Limites e matrizes](#section-7)

<a id="section-1"></a>
## 1. Por que usar referenciais

Um **referencial (coordinate frame)** possui origem e eixos orientados. O **referencial global (world frame)** W pode ficar fixo na base, enquanto o **referencial da ferramenta (tool frame)** T se move com ela. O mesmo ponto físico tem coordenadas diferentes nos dois sistemas. Posição define o ponto; orientação define os eixos. Uma conversão de coordenadas não provoca necessariamente movimento.

Usar a mesma unidade para todos os comprimentos (mm). Ângulos positivos em 2D são anti-horários a partir de +X global. Os índices w e l referem-se a mundo e local. Os elos são considerados rígidos.

<a id="section-2"></a>
## 2. Rotação e translação de um ponto

![Eixos mundiais e locais após rotação +90°, pontos P e Q.](../../../assets/figures/world_local_frames.svg)

*Eixos mundiais e locais após rotação +90°, pontos P e Q.*

A origem T está em (100 mm, 50 mm) no mundo, rodada +90°. O +x local aponta para +Y global, enquanto o +y local aponta para −X global. Assim P=(0 mm, 10 mm) local corresponde a (90 mm, 50 mm) no mundo e Q=(20 mm, 0 mm) a (100 mm, 70 mm).

Para o ponto local $(x_l,y_l)$, origem $(t_x,t_y)$ e ângulo $\theta$, **rodar primeiro e transladar depois**:

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

Os sinais de $\sin\theta$ e $\cos\theta$ dependem do ângulo orientado. Com $\theta=0^\circ$ basta somar a posição da origem. Isto não é um comando para um motor.

<a id="section-3"></a>
## 3. Encadear referenciais

Os referenciais formam a cadeia **W → T → S** (mundo → ferramenta → sensor). Se S tem origem (20 mm, 0 mm) em T e eixos paralelos a T, a sua origem global é (100 mm, 70 mm). O ponto (0 mm, 10 mm) em S resulta em (90 mm, 70 mm) no mundo. Converter primeiro do filho para o pai.

Com vetores coluna, $T_{WS}=T_{WT}T_{TS}$; $T_{AB}$ transforma coordenadas **de B para A**. A ordem das matrizes importa.

**Cálculo matricial completo (vetores coluna):** T está rodado +90° em relação a W e tem origem global (100 mm, 50 mm). S não tem rotação adicional e a sua origem em T é (20 mm, 0 mm), coincidente com Q na figura anterior. Os elementos de rotação não têm unidades; as translações estão em mm:

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

O produto transforma primeiro o deslocamento local (20 mm, 0 mm) do sensor em (0 mm, 20 mm) no mundo, somando-o depois a (100 mm, 50 mm). Assim, o ponto (0 mm, 10 mm) em S torna-se (90 mm, 70 mm) em W. Somar 20 mm diretamente à coordenada X global seria errado, pois o deslocamento é expresso **em T**. O último 1 é uma coordenada homogénea sem dimensão. É matemática de coordenadas; o [tf2 de ROS 2](06-ros2-foundations.md#section-7) publica e consulta transformações com instantes de tempo, não resolve cinemática inversa.

<a id="section-4"></a>
## 4. Cinemática direta de dois elos

![Primeiro ângulo 30°, segundo ângulo relativo 60°.](../../../assets/figures/two_link_fk.svg)

*Primeiro ângulo 30°, segundo ângulo relativo 60°.*

Um braço plano tem elos $L_1,L_2$. $\theta_1$ mede-se a partir de +X global, e $\theta_2$ **relativamente ao primeiro elo**. A direção absoluta do segundo é $\theta_1+\theta_2$. A posição da ferramenta soma os vetores dos elos:

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

Com L1=100 mm, L2=50 mm, $\theta_1=30^\circ$, $\theta_2=60^\circ$, o cotovelo está em (86.60 mm, 50 mm). O segundo elo está vertical e a ferramenta em (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. Duas configurações e espaço alcançável

![Duas configurações alcançam o mesmo ponto.](../../../assets/figures/two_link_elbow_solutions.svg)

*Duas configurações alcançam o mesmo ponto.*

A **cinemática inversa (inverse kinematics)** encontra ângulos para uma posição desejada. Dois elos de 100 mm atingem (100 mm, 100 mm) com $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ e com $(+90^\circ,-90^\circ)$. O segundo ângulo continua a ser relativo.

![Anel ideal de alcance entre 50 mm e 150 mm.](../../../assets/figures/two_link_workspace.svg)

*Anel ideal de alcance entre 50 mm e 150 mm.*

Sem limites ou colisões, $|L_1-L_2|\le r\le L_1+L_2$. Para elos de 100 mm e 50 mm, a área ideal é um **anel** entre raios 50 mm e 150 mm. Obstáculos podem restringir a área real.

<a id="section-6"></a>
## 6. Exercícios com soluções completas

Todos os **seis exercícios têm soluções explicadas**. Não há perguntas pessoais sem resposta.

<a id="worked-1"></a>
### 6.1. Ponto local P num referencial rodado

**Problema.** T em (100 mm, 50 mm), rodado +90°; encontrar P=(0 mm, 10 mm) global.

**Solução.** O +y local aponta para −X global: subtrair 10 mm de X.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Resposta:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Ponto Q sobre o eixo x local

**Problema.** No mesmo T, encontrar Q=(20 mm, 0 mm) global.

**Solução.** O +x local aponta para +Y global: somar 20 mm a Y.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Resposta:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Cinemática direta de dois elos

**Problema.** L1=100 mm, L2=50 mm, θ1=30°, θ2 relativo=60°. Encontrar a ferramenta.

**Solução.** A orientação absoluta do segundo elo é 30°+60°=90°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Resposta:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. Duas soluções da cinemática inversa

**Problema.** Dois elos de 100 mm devem chegar a (100 mm, 100 mm). Dois pares de ângulos?

**Solução.** Uma configuração anda para a direita e depois para cima; a outra faz o contrário.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Verificação de alcance

**Problema.** L1=100 mm, L2=50 mm: verificar (0 mm, 120 mm) e (0 mm, 0 mm).

**Solução.** A distância deve estar entre a diferença e a soma dos comprimentos.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

(0 mm, 120 mm) é **alcançável** porque 50 ≤ 120 ≤ 150. A origem (0 mm, 0 mm) é **inalcançável** porque a distância é zero.

<a id="worked-6"></a>
### 6.6. Cosseno do ângulo relativo do cotovelo

**Problema.** L1=100 mm, L2=50 mm, r=120 mm: calcular cos θ2.

**Solução.** O cosseno fixa o módulo da flexão, mas duas configurações espelhadas têm sinais opostos.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

O ângulo interior do triângulo é $\varphi=180^\circ-|\theta_2|$. Só a distância não determina $\theta_1$. Ver o diagrama em [Trigonometria](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. Limites e matrizes

O modelo considera elos rígidos em 2D. Máquinas reais apresentam limites, colisões, folgas, flexibilidade, erros de encoder e calibração de sensores. Um encoder mede ângulos, não a posição global diretamente. Estes exemplos não servem para controlar máquinas.

A **matriz homogénea 3×3** opcional combina rotação e translação para o ponto coluna $[x_l,y_l,1]^T$. Vetores livres de deslocamento usam 0 como última coordenada.

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

[Trigonometria](../TRIGONOMETRY.md) · [Símbolos matemáticos](../SYMBOLS.md) · [Controlo por realimentação](03-feedback-control.md)

[A seguir: rotação, velocidade e singularidades](05-velocity-jacobian.md)
