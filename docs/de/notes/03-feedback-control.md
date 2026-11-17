# 3. Regelung: PID, Abtastung, Sättigung und Haltemoment

**Sprachen:** [en](../../en/notes/03-feedback-control.md) · [fr](../../fr/notes/03-feedback-control.md) · [de](03-feedback-control.md) · [it](../../it/notes/03-feedback-control.md) · [es](../../es/notes/03-feedback-control.md) · [pt](../../pt/notes/03-feedback-control.md) · [zh](../../zh/notes/03-feedback-control.md) · [ja](../../ja/notes/03-feedback-control.md) · [nb](../../nb/notes/03-feedback-control.md) · [ru](../../ru/notes/03-feedback-control.md) · [ko](../../ko/notes/03-feedback-control.md) · [fi](../../fi/notes/03-feedback-control.md) · [pl](../../pl/notes/03-feedback-control.md)

**Hier verwendete Einheiten (vor den Beispielen erklärt):** `rpm` — Umdrehung pro Minute; `A` — Ampere; `s` — Sekunde; `rpm/s` — Umdrehung pro Minute / Sekunde — Winkelbeschleunigung; `A/rpm` — Ampere / (Umdrehung pro Minute) — Verstärkung pro Geschwindigkeit; `A/(rpm·s)` — Ampere / (Umdrehung pro Minute · Sekunde) — Integralverstärkung; `A·s/rpm` — Ampere · Sekunde / (Umdrehung pro Minute) — Differentialverstärkung; `N·m` — Newton · Meter — Drehmoment; `kg` — Kilogramm; `m` — Meter; `N` — Newton. [Einheitenverzeichnis](../UNITS.md).

[README](../README.md) · [Math foundations](00-calculus-foundations.md) · [First-order dynamics](02-first-order-dynamics.md) · [Trigonometry](../TRIGONOMETRY.md)

> **Lernmodell:** Diese vereinfachten Algorithmen dürfen nicht an reale Motoren oder Maschinen angeschlossen werden.

## Inhalt

- [1. Geschlossener Drehzahlregelkreis](#section-1)
- [2. P: proportionale Reaktion](#section-2)
- [3. I: aufsummierter Fehler und Stromsollwert](#section-3)
- [4. D: Fehleränderung und Sensorrauschen](#section-4)
- [5. Abtastzeit, Sättigung und Anti-Windup](#section-5)
- [6. Robotergelenk gegen Schwerkraft halten](#section-6)
- [7. Prüfungen und Grenzen](#section-7)

<a id="section-1"></a>
## 1. Geschlossener Drehzahlregelkreis

Ein **Regler mit Rückführung (feedback controller)** vergleicht Sollwert und Messwert. Bei 1000 rpm Soll und 950 rpm Ist beträgt der Fehler +50 rpm. Im Beispiel liefert PID einen **Sollwert für drehmomentbildenden Strom**, nicht die Änderung des zuvor gemessenen Stroms.

$$
\varepsilon(t)=\omega_{\mathrm{target}}-\omega_{\mathrm{measured}},
\qquad I_{\mathrm{set}}=u_P+u_I+u_D.
$$

Der Antrieb kann einen eigenen Stromregler enthalten, der Spannung oder PWM anpasst. Andere Systeme geben Drehmoment, Spannung oder PWM vor; Stromvorgabe ist nicht universell.

<a id="section-2"></a>
## 2. P: proportionale Reaktion

**P (proportional)** reagiert auf den **aktuellen** Fehler. Ohne Vorsteuerung (feedforward) benötigt die konstante Last ein Moment und damit einen Strom. Bei exakt null Fehler gibt P null aus. Deshalb kann ein reiner P-Regler eine **bleibende Regelabweichung (steady-state error)** haben.

$$
u_P=K_p\varepsilon,\quad [K_p]=\mathrm{A/rpm}.
$$

<a id="section-3"></a>
## 3. I: aufsummierter Fehler und Stromsollwert

**I (integral)** summiert den Fehler über Zeit und speichert nur einen Zustandswert, keine komplette Fehlerhistorie. Bei positivem Fehler wächst er, bei null bleibt er stehen, bei negativem sinkt er. So kann der Stromsollwert bei null Fehler positiv bleiben.

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

Beispiel: dt = 1 s, Kp = 0.02 A/rpm und Ki = 0.002 A/(rpm·s). Dreimal +50 rpm ergibt 50, 100, 150 rpm·s und I-Anteile 0.10, 0.20, 0.30 A. Bei null Fehler bleibt 0.30 A. Je eine Sekunde −20 rpm führt zu 0.26 und 0.22 A. −0.04 A ist die **Änderung pro Schritt**, kein neuer absoluter Stromsollwert.

Das Programm gibt nur den akkumulierten Integralwert, den I-Anteil und den gesamten Stromsollwert aus. Die Tabelle ergänzt Fehler und P-Anteil, damit jeder Rechenschritt nachvollziehbar ist. Zwischen den Abtastungen liegt jeweils 1 s; der Anfangswert des Integrals ist null.

| k | Gemessene Drehzahl (rpm) | ε (rpm) | z (rpm·s) | u_P (A) | u_I (A) | I_set (A) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 950 | +50 | 50 | +1.00 | +0.10 | +1.10 |
| 2 | 950 | +50 | 100 | +1.00 | +0.20 | +1.20 |
| 3 | 950 | +50 | 150 | +1.00 | +0.30 | +1.30 |
| 4 | 1000 | 0 | 150 | 0.00 | +0.30 | +0.30 |
| 5 | 1020 | −20 | 130 | −0.40 | +0.26 | −0.14 |
| 6 | 1020 | −20 | 110 | −0.40 | +0.22 | −0.18 |

Bei 1020 rpm beträgt der Fehler −20 rpm. Der P-Anteil ist −0.40 A, der I-Anteil bleibt zunächst +0.26 A: Zusammen ergibt das einen **vorzeichenbehafteten Stromsollwert von −0.14 A**. Im nächsten Schritt sind es −0.18 A. Die Änderung des I-Anteils um −0.04 A pro Schritt ist nicht der gesamte Sollwert. Die Werte gelten nur für das idealisierte Lernmodell.

<a id="section-4"></a>
## 4. D: Fehleränderung und Sensorrauschen

**D (derivative)** reagiert auf die **zeitliche Änderung des Fehlers**. Bei steigender Drehzahl und konstantem Sollwert sinkt der Fehler; ein negativer D-Anteil kann Überschwingen (overshoot) verringern. D ist nicht die Drehzahl. Ein Messsprung um 8 rpm in 0.01 s erzeugt scheinbar 800 rpm/s.

$$
u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t},\quad [K_d]=\mathrm{A\cdot s/rpm},\qquad
\frac{\Delta\omega}{\Delta t}=\frac{8\ \mathrm{rpm}}{0.01\ \mathrm{s}}=800\ \mathrm{rpm/s}.
$$

Die Fehlerableitung hat die Einheit rpm/s. Da der D-Anteil einen Stromsollwert in A liefert, muss `K_d` die Einheit rpm/s ausgleichen: Seine Einheit ist A·s/rpm, sodass das Produkt in A angegeben wird.

**Ableitungsfilterung (derivative filtering)** dämpft hochfrequentes Rauschen, bringt aber Verzögerung. Häufig wird die Messgröße statt des Sollwerts abgeleitet, um einen Derivativstoß bei Sollwertsprüngen zu vermeiden.

<a id="section-5"></a>
## 5. Abtastzeit, Sättigung und Anti-Windup

Die **Abtastzeit (sampling period)** gehört zur digitalen Regelung. Bei konstantem Fehler 20 rpm liefern 100 Schritte zu 0.01 s und 10 Schritte zu 0.1 s nach 1 s beide 20 rpm·s. Ohne dt sammelt der schnelle Regler das Zehnfache.

$$
z_{k+1}=z_k+\varepsilon_k\ \Delta t.
$$

Bei begrenztem Strom kann der angeforderte Wert über der Grenze liegen. Weiter integrieren verursacht **integral windup** und mögliches Überschwingen nach Lastabfall. **Anti-Windup** stoppt das in die Sättigung treibende Integrieren oder korrigiert den Zustand anhand der Differenz zwischen Soll- und Ist-Ausgang. Es zählt die **gesamte** P+I-Kommandogröße.

<a id="section-6"></a>
## 6. Robotergelenk gegen Schwerkraft halten

Die **Drehmomentkonstante Kt (motor torque constant)** beschreibt Moment pro drehmomentbildendem Ampere, in N·m/A. Bei Kt = 0.1 N·m/A und I = 2 A ergibt sich 0.2 N·m; die Herstellerdefinition des Stroms beachten.

$$
M_{\mathrm{motor}}=K_t I,\qquad [K_t]=\mathrm{N\cdot m/A}.
$$

Eine Masse m im Abstand L zu einer horizontalen Gelenkachse erzeugt den Betrag mgL|cos θ|. Im Stillstand müssen Motormoment und Lastmoment entgegengesetzt gleich groß sein. Daher kann bei Positionsfehler null Strom nötig sein. Eine Bremse oder eine tatsächlich selbsthemmende Übertragung kann stromlos halten; **Harmonic Drive** ist nicht grundsätzlich selbsthemmend.

$$
J\alpha=M_{\mathrm{motor}}+M_{\mathrm{load}},\quad
\alpha=0\ \Longrightarrow\ M_{\mathrm{motor}}=-M_{\mathrm{load}},
$$
$$
|M_g|=mgL|\cos\theta|.
$$

Bei einem BLDC **Outrunner** dreht die äußere Glocke, beim **Inrunner** der innere Rotor. Rotor bedeutet drehend und Stator fest, unabhängig von der radialen Anordnung.

<a id="section-7"></a>
## 7. Prüfungen und Grenzen

Dies sind idealisierte Rechenbeispiele, keine Reglervorgaben für reale Technik. Praktische Antriebe brauchen Grenzen, Filterung, sichere Prüfung und kalibrierte Rückführung.

[Math foundation](00-calculus-foundations.md) · [Trigonometry table](../TRIGONOMETRY.md) · [First-order dynamics](02-first-order-dynamics.md)
