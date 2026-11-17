# Таблица производных

**Языки:** [en](../en/DERIVATIVE_TABLE.md) · [fr](../fr/DERIVATIVE_TABLE.md) · [de](../de/DERIVATIVE_TABLE.md) · [it](../it/DERIVATIVE_TABLE.md) · [es](../es/DERIVATIVE_TABLE.md) · [pt](../pt/DERIVATIVE_TABLE.md) · [zh](../zh/DERIVATIVE_TABLE.md) · [ja](../ja/DERIVATIVE_TABLE.md) · [nb](../nb/DERIVATIVE_TABLE.md) · [ru](DERIVATIVE_TABLE.md) · [ko](../ko/DERIVATIVE_TABLE.md) · [fi](../fi/DERIVATIVE_TABLE.md) · [pl](../pl/DERIVATIVE_TABLE.md)

**Единицы этой темы (объяснены до примеров):** `s` — секунда; `mm` — миллиметр = 0.001 m; `mm/s` — миллиметр / секунда — линейная скорость; `mm/s²` — миллиметр / секунда² — ускорение. [Полный справочник единиц](UNITS.md).

[Содержание курса](README.md) · [Таблица интегралов](INTEGRAL_TABLE.md) · [Основы математического анализа](notes/00-calculus-foundations.md)

Пусть $u$ и $v$ зависят от $x$, а $a$ — константа. Штрих обозначает производную по $x$; углы измеряются в радианах. Производная определена там, где существует соответствующий предел. Для сложной функции применяется цепное правило (chain rule). Здесь $u'=\frac{\mathrm{d}u}{\mathrm{d}x}$ и $v'=\frac{\mathrm{d}v}{\mathrm{d}x}$.

## Правила

| Функция | Производная | Условия |
| --- | --- | --- |
| $c$ | $0$ | $c$ константа |
| $x$ | $1$ | — |
| $x^n$ | $nx^{n-1}$ | действительное $n$; где функция определена и дифференцируема |
| $u+v$ | $u'+v'$ | — |
| $au$ | $au'$ | $a$ константа |
| $uv$ | $u'v+uv'$ | правило произведения |
| $\frac{u}{v}$ | $\frac{u'v-uv'}{v^2}$ | $v\ne0$ |
| $f(u)$ | $f'(u)u'$ | цепное правило |
| $\frac{1}{u}$ | $-\frac{u'}{u^2}$ | $u\ne0$ |
| $\sqrt{u}$ | $\frac{u'}{2\sqrt{u}}$ | $u>0$ |
| $\exp(u)$ | $\exp(u)u'$ | — |
| $a^u$ | $a^u\ln(a)u'$ | $a>0$ |
| $\ln(u)$ | $\frac{u'}{u}$ | $u>0$ |
| $\ln\lvert u\rvert$ | $\frac{u'}{u}$ | $u\ne0$ |
| $\sin(u)$ | $\cos(u)u'$ | — |
| $\cos(u)$ | $-\sin(u)u'$ | — |
| $\tan(u)$ | $\frac{u'}{\cos^2(u)}$ | $\cos(u)\ne0$ |
| $\arcsin(u)$ | $\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arccos(u)$ | $-\frac{u'}{\sqrt{1-u^2}}$ | $-1<u<1$ |
| $\arctan(u)$ | $\frac{u'}{1+u^2}$ | — |
| $\mathrm{arsinh}(u)$ | $\frac{u'}{\sqrt{1+u^2}}$ | — |

## Примеры

**Цепное правило (chain rule):** Для $y=(3x^2+1)^4$ обозначим $u=3x^2+1$. Тогда $u'=6x$ и

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=4u^3u'=24x(3x^2+1)^3.
$$

**Скорость и ускорение:** Пусть положение задано как $x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2$. Производная положения по времени даёт скорость, а производная скорости — ускорение:

$$
v(t)=\frac{\mathrm{d}x}{\mathrm{d}t}=3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t,
$$

$$
a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=4\ \mathrm{mm/s^2}.
$$

При $t=2\ \mathrm{s}$ скорость равна $11\ \mathrm{mm/s}$. Это математический пример, а не инструкция по управлению оборудованием.

**Производная обратной функции (inverse function):** Если $y=f^{-1}(x)$, функция $f$ дифференцируема в точке $y$ и $f'(y)\ne0$, то на локально обратимой ветви $(f^{-1})'(x)=1/f'(y)$.
