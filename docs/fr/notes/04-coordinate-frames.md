# 4. Repères du robot et cinématique plane

**Languages:** [en](../../en/notes/04-coordinate-frames.md) · [fr](04-coordinate-frames.md) · [de](../../de/notes/04-coordinate-frames.md) · [it](../../it/notes/04-coordinate-frames.md) · [es](../../es/notes/04-coordinate-frames.md) · [pt](../../pt/notes/04-coordinate-frames.md) · [zh](../../zh/notes/04-coordinate-frames.md) · [ja](../../ja/notes/04-coordinate-frames.md) · [nb](../../nb/notes/04-coordinate-frames.md) · [ru](../../ru/notes/04-coordinate-frames.md) · [ko](../../ko/notes/04-coordinate-frames.md) · [fi](../../fi/notes/04-coordinate-frames.md) · [pl](../../pl/notes/04-coordinate-frames.md)

**Unités utilisées ici (définies avant les exemples):** `mm` — millimètre = 0.001 m; `°` — degré. [Glossaire des unités](../UNITS.md).

[README](../README.md) · [Trigonométrie](../TRIGONOMETRY.md) · [Symboles mathématiques](../SYMBOLS.md) · [Régulation](03-feedback-control.md)

> **Modèle pédagogique:** Ne pas employer ces formules simplifiées pour commander un robot réel.

## Sommaire
1. [Pourquoi les repères sont nécessaires](#section-1)
2. [Rotation et translation d’un point](#section-2)
3. [Enchaîner plusieurs repères](#section-3)
4. [Cinématique directe à deux segments](#section-4)
5. [Deux configurations et espace atteignable](#section-5)
6. [Exercices avec solutions expliquées](#section-6)
7. [Limites et notation matricielle](#section-7)

<a id="section-1"></a>
## 1. Pourquoi les repères sont nécessaires

Un **repère (coordinate frame)** possède une origine et des axes orientés. Le **repère mondial (world frame)** W peut être fixé à la base, tandis que le **repère de l’outil (tool frame)** T accompagne l’outil. Un même point physique a des coordonnées différentes selon le repère. La position désigne un point ; l’orientation indique la direction des axes. Transformer des coordonnées ne déplace pas nécessairement le robot.

Conserver la même unité pour toutes les longueurs (ici mm). En 2D, les angles positifs se mesurent dans le sens antihoraire depuis +X mondial. w signifie mondial, l local. Le modèle suppose des segments rigides.

<a id="section-2"></a>
## 2. Rotation et translation d’un point

![Axes du monde et de l’outil après une rotation de +90° ; points P et Q.](../../../assets/figures/world_local_frames.svg)

*Axes du monde et de l’outil après une rotation de +90° ; points P et Q.*

L’origine de T est (100 mm, 50 mm) dans W et les axes tournent de +90°. Le +x local pointe vers +Y mondial, le +y local vers −X mondial. Le point local P=(0 mm, 10 mm) est donc (90 mm, 50 mm) dans W ; Q=(20 mm, 0 mm) devient (100 mm, 70 mm).

Pour un point local $(x_l,y_l)$, l’origine mondiale $(t_x,t_y)$ et l’angle $\theta$, **effectuer la rotation puis la translation** :

$$
x_w=t_x+x_l\cos\theta-y_l\sin\theta
$$

$$
y_w=t_y+x_l\sin\theta+y_l\cos\theta
$$

Les signes de $\sin\theta$ et $\cos\theta$ dépendent de l’angle orienté. Pour $\theta=0^\circ$, on ajoute simplement le déplacement de l’origine. Ce calcul ne commande pas un moteur.

<a id="section-3"></a>
## 3. Enchaîner plusieurs repères

On peut composer les repères **W → T → S** (monde → outil → capteur). Si S a son origine à (20 mm, 0 mm) dans T et ses axes parallèles à T, l’origine de S dans W vaut (100 mm, 70 mm). Un point (0 mm, 10 mm) dans S vaut (90 mm, 70 mm) dans W. Transformer d’abord vers le repère parent.

Pour des vecteurs-colonnes : $T_{WS}=T_{WT}T_{TS}$, où $T_{AB}$ convertit les coordonnées **du repère B au repère A**. Inverser l’ordre des matrices modifie généralement le résultat.

**Calcul matriciel complet (vecteurs-colonnes) :** le repère outil T est tourné de +90° et son origine est (100 mm, 50 mm) dans W. Le capteur S est sans rotation supplémentaire et son origine est (20 mm, 0 mm) dans T, au même endroit que Q dans le schéma précédent. Les éléments de rotation sont sans dimension ; les translations sont exprimées en mm :

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

Dans le produit matriciel, le décalage local (20 mm, 0 mm) du capteur devient (0 mm, 20 mm) dans W, puis s'ajoute à (100 mm, 50 mm). Le point (0 mm, 10 mm) de S devient ainsi (90 mm, 70 mm) dans W. Ajouter directement 20 mm à X dans W serait faux : le décalage est défini **dans T**. La dernière coordonnée 1 est une convention homogène sans dimension. C'est un calcul géométrique ; [tf2 dans ROS 2](06-ros2-foundations.md#section-7) publie et recherche des transformations horodatées, mais ne résout pas la cinématique inverse.

<a id="section-4"></a>
## 4. Cinématique directe à deux segments

![Deux segments : premier angle 30°, second angle relatif 60°.](../../../assets/figures/two_link_fk.svg)

*Deux segments : premier angle 30°, second angle relatif 60°.*

Pour un bras plan à deux segments $L_1,L_2$, $\theta_1$ est l’angle du premier avec +X mondial. L’angle $\theta_2$ se mesure **par rapport au premier segment**. Le second a donc une orientation absolue $\theta_1+\theta_2$ et la position de l’outil est la somme des deux vecteurs :

$$
X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)
$$

$$
Y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2)
$$

Avec L1=100 mm, L2=50 mm, $\theta_1=30^\circ$ et $\theta_2=60^\circ$, le coude est à (86.60 mm, 50 mm). Le second segment pointe verticalement vers le haut et l’outil se trouve à (86.60 mm, 100 mm).

<a id="section-5"></a>
## 5. Deux configurations et espace atteignable

![Deux configurations de joints pour une seule position finale.](../../../assets/figures/two_link_elbow_solutions.svg)

*Deux configurations de joints pour une seule position finale.*

La **cinématique inverse (inverse kinematics)** cherche les angles nécessaires pour atteindre un point. Avec deux segments de 100 mm, les couples $(\theta_1,\theta_2)=(0^\circ,+90^\circ)$ et $(+90^\circ,-90^\circ)$ atteignent tous deux (100 mm, 100 mm). Le second angle reste relatif au premier segment.

![Couronne de positions atteignables entre 50 mm et 150 mm.](../../../assets/figures/two_link_workspace.svg)

*Couronne de positions atteignables entre 50 mm et 150 mm.*

Pour des joints libres sans collisions, $|L_1-L_2|\le r\le L_1+L_2$. Deux segments de 100 mm et 50 mm couvrent idéalement une **couronne** entre 50 mm et 150 mm de rayon. Les limites mécaniques réelles peuvent réduire cette zone.

<a id="section-6"></a>
## 6. Exercices avec solutions expliquées

Les **six exercices ci-dessous comportent tous une solution et son explication**. Aucun exercice n’est laissé comme question personnelle sans réponse.

<a id="worked-1"></a>
### 6.1. Point P dans le repère tourné

**Problème.** T se trouve à (100 mm, 50 mm) dans W, tourné de +90°. Trouver les coordonnées mondiales de P=(0 mm, 10 mm).

**Solution.** Le +y local est orienté vers −X mondial : soustraire 10 mm à X.

$$
x_w=100+0\cdot0-10\cdot1=90\ \mathrm{mm}
$$

$$
y_w=50+0\cdot1+10\cdot0=50\ \mathrm{mm}
$$

**Réponse:** (90 mm, 50 mm).

<a id="worked-2"></a>
### 6.2. Point Q sur l’axe local x

**Problème.** Même repère T : trouver les coordonnées mondiales de Q=(20 mm, 0 mm).

**Solution.** Le +x local pointe vers +Y mondial : augmenter Y de 20 mm.

$$
x_w=100+20\cdot0-0\cdot1=100\ \mathrm{mm}
$$

$$
y_w=50+20\cdot1+0\cdot0=70\ \mathrm{mm}
$$

**Réponse:** (100 mm, 70 mm).

<a id="worked-3"></a>
### 6.3. Cinématique directe à deux segments

**Problème.** L1=100 mm, L2=50 mm, θ1=30°, θ2 relatif=60°. Trouver l’outil.

**Solution.** L’orientation absolue du second segment est 30°+60°=90°.

$$
X=100\cos30^\circ+50\cos90^\circ=50\sqrt3\approx86.60\ \mathrm{mm}
$$

$$
Y=100\sin30^\circ+50\sin90^\circ=100\ \mathrm{mm}
$$

**Réponse:** (86.60 mm, 100 mm).

<a id="worked-4"></a>
### 6.4. Deux solutions pour une seule cible

**Problème.** Deux segments de 100 mm doivent atteindre (100 mm, 100 mm). Donner deux couples d’angles.

**Solution.** Un trajet va à droite puis vers le haut ; l’autre fait l’inverse.

$$
(\theta_1,\theta_2)=(0^\circ,+90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

$$
(\theta_1,\theta_2)=(+90^\circ,-90^\circ)\ \Longrightarrow\ (X,Y)=(100, 100)\ \mathrm{mm}
$$

<a id="worked-5"></a>
### 6.5. Atteignabilité sans calculer les angles

**Problème.** L1=100 mm, L2=50 mm : vérifier (0 mm, 120 mm) et (0 mm, 0 mm).

**Solution.** Comparer les distances avec la différence et la somme des longueurs.

$$
r_{\min}=|100-50|=50\ \mathrm{mm},\qquad r_{\max}=100+50=150\ \mathrm{mm}
$$

$$
r_{(0, 120)}=\sqrt{0^2+120^2}=120\ \mathrm{mm}
$$

Ainsi (0 mm, 120 mm) est **atteignable** car 50 ≤ 120 ≤ 150. L’origine (0 mm, 0 mm) est **inatteignable** car son rayon est zéro.

<a id="worked-6"></a>
### 6.6. Cosinus de l’angle relatif du coude

**Problème.** L1=100 mm, L2=50 mm, r=120 mm : calculer cos θ2.

**Solution.** La loi des cosinus donne le module du coude, mais les deux configurations symétriques ont des angles relatifs de signes opposés.

$$
\cos\theta_2=\frac{r^2-L_1^2-L_2^2}{2L_1L_2}
=\frac{14400-10000-2500}{10000}=\frac{1900}{10000}=0.19
$$

$$
\theta_2\approx\pm79.05^\circ
$$

L’angle intérieur du triangle vaut $\varphi=180^\circ-|\theta_2|$. La distance seule ne détermine pas $\theta_1$. Voir le schéma dans [Trigonométrie](../TRIGONOMETRY.md).

<a id="section-7"></a>
## 7. Limites et notation matricielle

Cette géométrie idéale suppose des segments rigides dans un plan. Les robots réels ont des butées, collisions, jeux, déformations, erreurs de codeurs et calibrations de caméra. Un codeur mesure un angle de joint, pas directement la position mondiale de l’outil. Ces exemples ne doivent pas commander une machine.

**Notation matricielle facultative.** La matrice homogène 3×3 applique une rotation et une translation au point-colonne $[x_l,y_l,1]^T$. Un vecteur de déplacement pur prend la troisième coordonnée 0.

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

[Trigonométrie](../TRIGONOMETRY.md) · [Symboles mathématiques](../SYMBOLS.md) · [Régulation](03-feedback-control.md)

[Suite : rotation, vitesse et singularités](05-velocity-jacobian.md)
