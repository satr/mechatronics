# Tabela de integrais

**Ler em:** [en](../en/INTEGRAL_TABLE.md) · [fr](../fr/INTEGRAL_TABLE.md) · [de](../de/INTEGRAL_TABLE.md) · [it](../it/INTEGRAL_TABLE.md) · [es](../es/INTEGRAL_TABLE.md) · [pt](INTEGRAL_TABLE.md) · [zh](../zh/INTEGRAL_TABLE.md) · [ja](../ja/INTEGRAL_TABLE.md) · [nb](../nb/INTEGRAL_TABLE.md) · [ru](../ru/INTEGRAL_TABLE.md) · [ko](../ko/INTEGRAL_TABLE.md) · [fi](../fi/INTEGRAL_TABLE.md) · [pl](../pl/INTEGRAL_TABLE.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `s` — segundo; `mm` — milímetro = 0.001 m; `mm/s` — milímetro / segundo — velocidade linear; `mm/s²` — milímetro / segundo² — aceleração; `N` — newton; `m` — metro; `N/m` — newton / metro — rigidez; `J` — joule. [Glossário de unidades](UNITS.md).

[README](README.md) · [0. Fundamentos de derivadas, diferenciais e integrais](notes/00-calculus-foundations.md) · [Símbolos](SYMBOLS.md)

Todas as integrais indefinidas incluem +C, a constante de integração. a é constante; trabalham-se intervalos em que a função integranda está definida. Os ângulos são medidos em radianos.

Comece por polinómios; integrais trigonométricas e com raízes podem ficar para mais tarde.

## Conteúdo

- [Potências e logaritmos](#section-1)
- [Funções exponenciais](#section-2)
- [Funções trigonométricas](#section-3)
- [Expressões racionais e trigonometria inversa](#section-4)
- [Referência adicional: radicais e recíprocas](#section-5)
- [Escolher e verificar uma fórmula](#section-6)

<a id="section-1"></a>
## 1. Potências e logaritmos

| Fórmula | Condições / explicação |
| --- | --- |
| $\int 1\ \mathrm{d}x=x+C$ | todos os $x$ reais |
| $\int x^n\ \mathrm{d}x=\frac{x^{n+1}}{n+1}+C$ | $n\ne-1$; respeitar o domínio real das potências |
| $\int\frac{1}{x}\ \mathrm{d}x=\ln\lvert x\rvert+C$ | $x\ne0$ |

<a id="section-2"></a>
## 2. Funções exponenciais

| Fórmula | Condições / explicação |
| --- | --- |
| $\int \mathrm{e}^{x}\ \mathrm{d}x=\mathrm{e}^{x}+C$ | todos os $x$ reais |
| $\int a^x\ \mathrm{d}x=\frac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |

<a id="section-3"></a>
## 3. Funções trigonométricas

| Fórmula | Condições / explicação |
| --- | --- |
| $\int\sin x\ \mathrm{d}x=-\cos x+C$ | $x$ em radianos |
| $\int\cos x\ \mathrm{d}x=\sin x+C$ | $x$ em radianos |
| $\int\frac{1}{\cos^2 x}\ \mathrm{d}x=\tan x+C$ | $\cos x\ne0$ |
| $\int\frac{1}{\sin^2 x}\ \mathrm{d}x=-\cot x+C$ | $\sin x\ne0$ |

<a id="section-4"></a>
## 4. Expressões racionais e trigonometria inversa

| Fórmula | Condições / explicação |
| --- | --- |
| $\int\frac{1}{1+x^2}\ \mathrm{d}x=\arctan x+C$ | todos os $x$ reais |
| $\int\frac{1}{\sqrt{1-x^2}}\ \mathrm{d}x=\arcsin x+C$ | $\lvert x\rvert<1$ |
| $\int\frac{1}{a^2+x^2}\ \mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C$ | $a>0$ |
| $\int\frac{1}{a^2-x^2}\ \mathrm{d}x=\frac{1}{2a}\ln\left\lvert\frac{a+x}{a-x}\right\rvert+C$ | $a>0$, $x\ne\pm a$ |
| $\int\frac{1}{\sqrt{a^2-x^2}}\ \mathrm{d}x=\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |

<a id="section-5"></a>
## 5. Referência adicional: radicais e recíprocas

| Fórmula | Condições / explicação |
| --- | --- |
| $\int\frac{1}{\sqrt{x^2+a^2}}\ \mathrm{d}x=\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{a^2-x^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$ | $a>0$, $\lvert x\rvert<a$ |
| $\int\sqrt{x^2+a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2+a^2}+\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2+a^2}\right\rvert+C$ | $a>0$ |
| $\int\sqrt{x^2-a^2}\ \mathrm{d}x=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left\lvert x+\sqrt{x^2-a^2}\right\rvert+C$ | $a>0$, $\lvert x\rvert>a$ |
| $\int\frac{1}{\sin x}\ \mathrm{d}x=\ln\left\lvert\tan\frac{x}{2}\right\rvert+C$ | $\sin x\ne0$; intervalos sem singularidades |
| $\int\frac{1}{\cos x}\ \mathrm{d}x=\ln\left\lvert\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right\rvert+C$ | $\cos x\ne0$; intervalos sem singularidades |

## Verificar uma fórmula

Derive o lado direito para verificar a fórmula. Nas potências, inverta a regra da derivada.

O argumento de um logaritmo deve ser adimensional; aqui x é adimensional salvo indicação de escala. Respeite o sinal escolhido e o domínio.

<a id="section-6"></a>
## 6. Escolher e verificar uma fórmula

Identifique primeiro a variável após o diferencial (dx, dt ou dθ). Um coeficiente só é constante se não depender dessa variável. Em integrais indefinidas acrescente C; nas definidas calcule F(b) − F(a). Verifique derivando.

### Exemplo A — deslocamento a partir da velocidade

Para v(t) = 3 mm/s + (4 mm/s²)t de 0 a 2 s, integre cada termo:

$$
\int_0^{2\ \mathrm{s}}\left(3\ \mathrm{mm/s}+(4\ \mathrm{mm/s^2})t\right)\mathrm{d}t
=\left[(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2\right]_0^{2\ \mathrm{s}}
=14\ \mathrm{mm}.
$$

O resultado é 14 mm, não 14 mm/s: integrar velocidade no tempo dá deslocamento.

### Exemplo B — trabalho de uma força variável

Uma mola F(x) = kx com k = 200 N/m, alongada de 0 a 0.01 m:

$$
\int_0^{0.01\ \mathrm{m}}(200\ \mathrm{N/m})x\ \mathrm{d}x
=\left[(100\ \mathrm{N/m})x^2\right]_0^{0.01\ \mathrm{m}}=0.01\ \mathrm{J}.
$$

O trabalho é 0.01 J. Não use a força final para todo o percurso.

### Exemplo C — logaritmo de uma relação simples

Uma primitiva de 1/x é ln|x|. Para x sem dimensão de 1 a 2:

$$
\int_1^2\frac1x\ \mathrm{d}x=[\ln x]_1^2=\ln2-\ln1=\ln2\approx0.693.
$$

Resultado ln 2 ≈ 0.693. x é uma razão, não comprimento.
