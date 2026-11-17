# 3. Commande en boucle fermée : PID, échantillonnage et couple de maintien

**Langues:** [en](../../en/notes/03-feedback-control.md) · [fr](03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Unités utilisées ici (définies avant les exemples):** `rpm` — tour par minute; `A` — ampère; `s` — seconde; `rpm/s` — tour par minute / seconde — accélération angulaire; `A/rpm` — ampère / (tour par minute) — gain par unité de vitesse; `A/(rpm·s)` — ampère / (tour par minute · seconde) — gain intégral; `A·s/rpm` — ampère · seconde / (tour par minute) — gain dérivé; `N·m` — newton · mètre — moment de force; `kg` — kilogramme; `m` — mètre; `N` — newton. [Glossaire des unités](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Modèle pédagogique:** Ne reliez pas ces algorithmes simplifiés à de vrais moteurs ou machines.

## Sommaire

- [1. Boucle de vitesse fermée](#section-1)
- [2. P : réaction proportionnelle](#section-2)
- [3. I : erreur accumulée et consigne de courant](#section-3)
- [4. D : variation de l’erreur et bruit du capteur](#section-4)
- [5. Échantillonnage, saturation et anti-windup](#section-5)
- [6. Maintien d’une articulation sous gravité](#section-6)
- [7. Vérifications et limites](#section-7)

<a id="section-1"></a>
## 1. Boucle de vitesse fermée

Un **régulateur en boucle fermée (feedback controller)** compare la consigne à la mesure du capteur. Pour une consigne de 1000 rpm et une mesure de 950 rpm, l’erreur est +50 rpm. Dans cet exemple, la sortie PID est une **consigne de courant créant du couple**, et non une variation à ajouter au courant mesuré.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

Le variateur peut inclure une boucle de courant qui ajuste tension ou PWM. Selon le système, la sortie du contrôleur peut être une consigne de couple, tension ou PWM ; le courant n’est pas universel.

<a id="section-2"></a>
## 2. P : réaction proportionnelle

La partie **P (proportional)** réagit à l’erreur **actuelle**. Dans un modèle sans compensation anticipée (feedforward), une charge constante exige un couple et un courant non nuls. Lorsque l’erreur devient nulle, P est nul : une **erreur permanente (steady-state error)** peut subsister avec P seul.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I : erreur accumulée et consigne de courant

La partie **I (integral)** accumule l’erreur dans le temps sous forme d’un seul état, pas d’une liste d’historique. Erreur positive : augmentation ; erreur nulle : maintien ; erreur négative : diminution. Elle peut ainsi conserver une commande non nulle à vitesse correcte.

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

Exemple : dt = 1 s, Kp = 0.02 A/rpm, Ki = 0.002 A/(rpm·s). Trois erreurs +50 rpm donnent des intégrales 50, 100, 150 rpm·s et des commandes I de 0.10, 0.20, 0.30 A. Une erreur nulle conserve 0.30 A ; après une seconde à −20 rpm : 0.26 A, puis 0.22 A. −0.04 A est la **variation par pas**, pas la nouvelle consigne totale.

Le programme affiche l'intégrale accumulée, le terme I et la consigne totale de courant. Le tableau ajoute l'erreur et le terme P pour rendre chaque calcul vérifiable. Les échantillons sont espacés de 1 s et l'intégrale commence à zéro.

| k | Vitesse mesurée (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

À 1020 rpm, l'erreur vaut −20 rpm : P vaut −0.40 A, tandis que I vaut encore +0.26 A. Leur somme est une **consigne signée de −0.14 A**, puis −0.18 A à l'échantillon suivant. La variation du terme I (−0.04 A par pas) n'est pas la consigne totale. Ces valeurs appartiennent au modèle pédagogique, pas à un réglage de variateur réel.

<a id="section-4"></a>
## 4. D : variation de l’erreur et bruit du capteur

La partie **D (derivative)** réagit à la **vitesse de variation de l’erreur**. Si la vitesse augmente vers une consigne constante, la dérivée de l’erreur est négative et peut réduire le dépassement (overshoot). Ce n’est pas la vitesse elle-même. Un saut de mesure de 8 rpm en 0.01 s donne artificiellement 800 rpm/s.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

La dérivée de l’erreur a pour unité rpm/s. Comme la contribution D est une consigne de courant en A, le gain `K_d` doit compenser rpm/s : son unité est A·s/rpm et le produit s’exprime en A.

Le **filtrage de dérivée (derivative filtering)** atténue le bruit rapide mais ajoute du retard. On dérive souvent la mesure plutôt que la consigne afin d’éviter les impulsions lors des changements de consigne.

<a id="section-5"></a>
## 5. Échantillonnage, saturation et anti-windup

Le **pas d’échantillonnage (sampling period)** compte : 100 pas de 0.01 s ou 10 pas de 0.1 s intégrant la même erreur constante de 20 rpm pendant 1 s donnent tous deux 20 rpm·s. Omettre dt ferait accumuler dix fois plus au contrôleur rapide.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Si le courant demandé dépasse le maximum du variateur, l’intégrale peut continuer de croître : **integral windup**. Après baisse de charge, le dépassement peut être important. L’**anti-windup** évite l’accumulation qui aggrave la saturation ou corrige l’état interne selon la différence entre sortie demandée et appliquée. La limite concerne la commande **totale**, y compris P.

<a id="section-6"></a>
## 6. Maintien d’une articulation sous gravité

La **constante de couple Kt (motor torque constant)** vaut le couple par ampère de courant produisant du couple : N·m/A. Exemple : Kt = 0.1 N·m/A et I = 2 A donnent 0.2 N·m, avec la convention de courant du fabricant.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Pour une masse m à distance L d’un pivot horizontal, le module du couple de gravité est mgL|cos θ|. À l’arrêt, les couples signés du moteur et de la charge se compensent : il peut donc falloir du courant à erreur de position nulle. Un frein ou un véritable système autobloquant peut maintenir sans courant ; un réducteur **Harmonic Drive** n’est pas intrinsèquement autobloquant.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Un BLDC **outrunner** a un rotor extérieur, un **inrunner** un rotor intérieur. Le rotor tourne ; le stator reste immobile, quelle que soit leur position radiale.

<a id="section-7"></a>
## 7. Vérifications et limites

Les courants cités sont des exemples théoriques, jamais des réglages pour équipement réel. Toute mise en œuvre exige limites, filtrage, protection, calibration et validation.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
