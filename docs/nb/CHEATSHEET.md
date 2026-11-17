# Kort formelsamling

**Les denne siden på:** [en](../en/CHEATSHEET.md) · [fr](../fr/CHEATSHEET.md) · [de](../de/CHEATSHEET.md) · [it](../it/CHEATSHEET.md) · [es](../es/CHEATSHEET.md) · [pt](../pt/CHEATSHEET.md) · [zh](../zh/CHEATSHEET.md) · [ja](../ja/CHEATSHEET.md) · [nb](CHEATSHEET.md) · [ru](../ru/CHEATSHEET.md) · [ko](../ko/CHEATSHEET.md) · [fi](../fi/CHEATSHEET.md) · [pl](../pl/CHEATSHEET.md)

**Enheter på denne siden (forklart før eksemplene):** `s` — sekund; `m` — meter; `m/s` — meter / sekund — lineær hastighet; `rad/s` — radian / sekund — vinkelhastighet; `kg·m²` — kilogram · meter² — treghetsmoment; `N·m` — newton · meter — dreiemoment; `N·m·s/rad` — newton · meter · sekund / radian — forsterkning per hastighet; `J` — joule; `mm` — millimeter = 0.001 m; `mm/s` — millimeter / sekund — lineær hastighet; `%` — prosent (en hundredel). [Enhetsoversikt](UNITS.md).

[Innhold](README.md) · [Bevegelse, derivasjon og integrasjon](notes/01-motion-calculus.md) · [Førsteordensdynamikk og rotasjon](notes/02-first-order-dynamics.md) · [Python-øvelser](exercises/README.md)

> **Advarsel:** Dette KI-assisterte lærematerialet kan inneholde feil, unøyaktige oversettelser og ugyldige forutsetninger. Bruk skjer på eget ansvar. Kontroller alle beregninger uavhengig, og bruk aldri eksemplene til å styre virkelige motorer eller maskiner.

| Kort oppsummering | Kort formelsamling |
| --- | --- |
| Forflytning | $\Delta x=x_2-x_1$ |
| Tilbakelagt strekning | $s=\int_{t_1}^{t_2}\lvert v(t)\rvert\ \mathrm{d}t\ge 0$ |
| Gjennomsnittlig hastighet (vektor) | $\overline{v}=\frac{\Delta x}{\Delta t}$ |
| Gjennomsnittsfart | $\frac{s}{\Delta t}$ |
| Momentan hastighet | $v(t)=\frac{dx}{dt}$ |
| Eksplisitt Euler-metode | $x_{n+1}=x_n+v_n\ dt$ |
| Førsteordensdynamikk | $\frac{dv}{dt}=\frac{u-v}{\tau}$ |
| Hastighetsfeil | $\varepsilon(t)=u-v(t)$ |
| Tidskonstant | $t=\tau$: $1-\exp(-1)\approx63.2\ \%$ |
| Resulterende dreiemoment | $M=J\alpha$ |
| Treghetsmoment og forsterkning | $\tau=\frac{J}{K}$ (Bare for den idealiserte dreiemomentmodellen) |
| Rotasjonsenergi | $E=\frac{1}{2}J\omega^2$ |

**Notasjon:** $\varepsilon$ er hastighetsfeilen (speed error); $\mathrm{e}\approx2.71828$ er Eulers tall (Euler’s number); $\exp(z)=\mathrm{e}^{z}$.

**Enheter (SI):**

| Symbol | Størrelse | SI-enhet |
| --- | --- | --- |
| `t, dt, τ` | Tid | s (second) |
| `x` | Posisjon | m (meter) |
| `v` | Fart | m/s (meter per second) |
| `ω` | Vinkelhastighet | rad/s (radian per second) |
| `J` | Treghetsmoment | kg·m² (kilogram square meter) |
| `M` | Dreiemoment | N·m (newton meter) |
| `K` | Momentforsterkning | N·m·s/rad |
| `E` | Energi | J (joule) |

Midtpunktet `·` betyr multiplikasjon. $u$ er lineær eller vinkelhastighet avhengig av modellen.

## Forbehold

Ikke bland fart med hastighet med retning, strekning med forflytning eller $dt$ med $\tau$. $\tau=\frac{J}{K}$ gjelder bare under modellforutsetningene; mekanisk energi er ikke totalt elektrisk energiforbruk.

**Engelske faguttrykk:**

- tilbakelagt strekning (distance traveled)
- forflytning (displacement)
- fart (speed)
- hastighetsvektor (velocity)
- derivasjon (derivative)
- integral (integral)
- numerisk integrasjon (numerical integration)
- eksplisitt Euler-metode (explicit Euler method)

**Engelske faguttrykk:**

- førsteordenssystem (first-order system)
- tidskonstant (time constant)
- tidssteg (time step)
- treghetsmoment (moment of inertia)
- dreiemoment (torque)
- regulatorforsterkning (controller gain)
- vinkelakselerasjon (angular acceleration)
- systemidentifikasjon (system identification)
- rotasjonsenergi (rotational kinetic energy)

Se [mer om derivasjon](notes/01-motion-calculus.md#section-6) og [modellbegrensninger](notes/02-first-order-dynamics.md#section-7).


[Hvorfor akkurat disse prosentene? Se utregningen.](notes/02-first-order-dynamics.md#time-constant-derivation)

[Se hvordan 3, 3.8 og 3.98 beregnes.](notes/01-motion-calculus.md#motion-values-derivation)


## Symboler og notasjon

**Σ / ∑ (summasjon / summation)** betyr å legge sammen ledd: $\sum_{n=1}^{3}n=1+2+3=6$. [Flere symboler](SYMBOLS.md).


## Integraltabell

[0. Grunnlag for derivasjon, differensialer og integraler](notes/00-calculus-foundations.md) · [Integraltabell](INTEGRAL_TABLE.md)


## Tilbakekoblet regulering: PID og holdemoment

| $\varepsilon=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}}$ | $u_P=K_p\varepsilon$, $u_I=K_i\int\varepsilon\ \mathrm{d}t$ |
| --- | --- |
| $M_{\mathrm{motor}}=K_t I$ | $\lvert M_g\rvert=mgL\lvert\cos\theta\rvert$ |

[Tilbakekoblet regulering: PID og holdemoment](notes/03-feedback-control.md) · [Trigonometrisk tabell og eksempler fra mekanikk](TRIGONOMETRY.md)

<a id="joint-velocity"></a>
## Rotasjon, hastighet og Jacobi-matrisen

Vinkelhastigheter måles i rad/s, lineære hastigheter i mm/s når lengder oppgis i mm.

$$
v_x=-L\sin Q\cdot\dot Q,\qquad v_y=L\cos Q\cdot\dot Q
$$

$$
\det J=L_1L_2\sin Q_2
$$

[Rotasjon, hastighet og Jacobi-matrisen](notes/05-velocity-jacobian.md)
