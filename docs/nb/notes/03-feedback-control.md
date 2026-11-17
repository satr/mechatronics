# 3. Tilbakekoblet regulering: PID, sampling og holdemoment

**Språk:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](../../de/notes/03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Enheter på denne siden (forklart før eksemplene):** `rpm` — omdreining per minutt; `A` — ampere; `s` — sekund; `rpm/s` — omdreining per minutt / sekund — vinkelakselerasjon; `A/rpm` — ampere / (omdreining per minutt) — forsterkning per hastighet; `A/(rpm·s)` — ampere / (omdreining per minutt · sekund) — integralforsterkning; `A·s/rpm` — ampere · sekund / (omdreining per minutt) — derivatforsterkning; `N·m` — newton · meter — dreiemoment; `kg` — kilogram; `m` — meter; `N` — newton. [Enhetsoversikt](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Læringsmodell:** Ikke koble disse forenklede algoritmene til virkelige motorer eller maskiner.

## Innhold

- [1. Lukket hastighetsregulering](#section-1)
- [2. P: proporsjonal respons](#section-2)
- [3. I: oppsamlet feil og strømreferanse](#section-3)
- [4. D: feilendring og sensorstøy](#section-4)
- [5. Sampling, metning og anti-windup](#section-5)
- [6. Holde et robotledd mot tyngdekraften](#section-6)
- [7. Kontroller og begrensninger](#section-7)

<a id="section-1"></a>
## 1. Lukket hastighetsregulering

En **tilbakekoblet regulator (feedback controller)** sammenligner ønsket verdi med sensormåling. Ved 1000 rpm ønsket og 950 rpm målt blir feilen +50 rpm. I dette eksemplet er PID-utgangen et **settpunkt for momentdannende strøm**, ikke beskjed om å legge et antall ampere til målt strøm.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

Driven kan ha egen strømregulator som justerer spenning eller PWM. Andre arkitekturer gir moment, spenning eller PWM; strømreferanse er ikke universell.

<a id="section-2"></a>
## 2. P: proporsjonal respons

**P (proportional)** reagerer på feilen **nå**. Uten foroverkompensering (feedforward) krever konstant last moment og strøm. Ved feil lik null er P-bidraget null. En P-regulator kan derfor få **stasjonært avvik (steady-state error)**.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: oppsamlet feil og strømreferanse

**I (integral)** summerer feilen over tid i ett lagret tall, ikke en liste over gamle feil. Ved positiv feil øker verdien, ved null forblir den, ved negativ feil minker den. Dermed kan strømreferansen være positiv ved null hastighetsfeil.

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

Eksempel med dt = 1 s, Kp = 0.02 A/rpm, Ki = 0.002 A/(rpm·s): Tre feil på +50 rpm gir 50, 100, 150 rpm·s og I-kommandoer 0.10, 0.20, 0.30 A. Ved null feil holder den 0.30 A. Én og to sekunder med −20 rpm gir 0.26 og 0.22 A. −0.04 A er **endringen per steg**, ikke det nye absolutte settpunktet.

Programmet skriver bare ut det akkumulerte integralet, I-leddet og samlet strømreferanse. Tabellen viser også feilen og P-leddet, slik at hvert regnetrinn kan kontrolleres. Det går 1 s mellom målingene, og integralet starter på null.

| k | Målt turtall (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

Ved 1020 rpm er feilen −20 rpm: P-leddet er −0.40 A, mens I-leddet ennå er +0.26 A. Summen blir en **strømreferanse med fortegn på −0.14 A**, og neste måling gir −0.18 A. Endringen i I-leddet (−0.04 A per steg) er ikke den samlede kommandoen. Tallene gjelder bare undervisningsmodellen, ikke innstillinger for en virkelig motorstyring.

<a id="section-4"></a>
## 4. D: feilendring og sensorstøy

**D (derivative)** reagerer på **hvor raskt feilen endres**. Ved konstant settpunkt og økende hastighet synker feilen; et negativt D-bidrag kan redusere oversving (overshoot). D er ikke selve hastigheten. Et målehopp på 8 rpm i 0.01 s ser ut som 800 rpm/s.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

Den deriverte feilen har enheten rpm/s. Siden D-leddet er et strømsettpunkt i A, må forsterkningen `K_d` kompensere for rpm/s: Enheten er A·s/rpm, slik at produktet får enheten A.

**Derivatfiltrering (derivative filtering)** demper rask støy, men gir også forsinkelse. Ofte deriveres målingen i stedet for settpunktet for å unngå store støt ved endret referanse.

<a id="section-5"></a>
## 5. Sampling, metning og anti-windup

Det digitale **samplingintervallet (sampling period)** betyr noe. Konstant feil 20 rpm i 1 s gir 20 rpm·s både ved 100 steg på 0.01 s og 10 steg på 0.1 s. Uten dt vil den raske regulatoren akkumulere ti ganger mer.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Når strømreferansen overstiger driverens grense kan I fortsette å øke: **integral windup**. Det kan gi stort oversving når lasten reduseres. **Anti-windup** stopper integrering som øker metningen eller korrigerer tilstanden etter forskjellen mellom ønsket og levert utgang. Det er den **totale** kommandoen med P som begrenses.

<a id="section-6"></a>
## 6. Holde et robotledd mot tyngdekraften

**Momentkonstanten Kt (motor torque constant)** angir moment per momentdannende ampere, i N·m/A. Kt = 0.1 N·m/A og strøm 2 A gir 0.2 N·m, med produsentens strømdefinisjon.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

En masse m på avstand L fra en horisontal leddakse gir tyngdemoment med størrelse mgL|cos θ|. Ved stillstand må motor- og lastmoment motvirke hverandre. Derfor kan strøm trenges selv med posisjonsfeil null. Mekanisk brems eller reelt selvhemmende gir kan holde uten strøm; **Harmonic Drive** er ikke automatisk selvhemmende.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

En BLDC **outrunner** har roterende ytterkappe, mens en **inrunner** har roterende indre rotor. Rotor er delen som roterer, stator står stille.

<a id="section-7"></a>
## 7. Kontroller og begrensninger

Alle strømverdier er teoretiske eksempler, ikke innstillinger for virkelig maskinvare. Reell bruk trenger grenser, filtrering, kalibrering og sikker validering.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
