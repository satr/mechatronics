# Mechatronics Training — Português

**Ler esta página em:** [en](../en/README.md) · [fr](../fr/README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](README.md) · [zh](../zh/README.md) · [ja](../ja/README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](../ko/README.md) · [fi](../fi/README.md) · [pl](../pl/README.md)

> [!WARNING]
> **Aviso:** Este material educativo com assistência de IA pode conter erros, traduções imprecisas ou pressupostos incorretos. A utilização é por conta e risco de quem o consulta. Confirme os cálculos de forma independente e nunca utilize os exemplos para controlar máquinas reais.

Introdução autónoma ao movimento, derivadas e integrais, métodos numéricos, sistemas de primeira ordem e energia de rotação.

## Índice

1. [Fundamentos de derivadas, diferenciais e integrais](notes/00-calculus-foundations.md)
2. [Movimento, derivadas e integrais](notes/01-motion-calculus.md)
3. [Dinâmica de primeira ordem e rotação](notes/02-first-order-dynamics.md)
4. [Tabela de integrais](INTEGRAL_TABLE.md)
5. [Tabela de derivadas](DERIVATIVE_TABLE.md)
6. [Resumo de fórmulas](CHEATSHEET.md)
7. [Exercícios Python](exercises/README.md)
8. [Símbolos e notação](SYMBOLS.md) · [Glossário de unidades](UNITS.md)
9. [Tabela trigonométrica e exemplos mecânicos](TRIGONOMETRY.md)
10. [Controlo por realimentação: PID e binário de sustentação](notes/03-feedback-control.md)
11. [Referenciais do robô: posição e rotação](notes/04-coordinate-frames.md)
12. [Rotação, velocidade e singularidades](notes/05-velocity-jacobian.md)
13. [ROS 2: arquitetura, nodes e exercício Docker](notes/06-ros2-foundations.md)

[Repositório / escolha da língua](../../README.md) · [Segurança e precisão](SAFETY.md) · [Licenças](LICENSING.md)

## Revisão rápida

Leia uma secção curta, repita os cálculos, execute a simulação local e explique o resultado pelas suas próprias palavras. Um modelo idealizado não representa um equipamento real validado.

**Aviso:** Este material educativo com assistência de IA pode conter erros, traduções imprecisas ou pressupostos incorretos. A utilização é por conta e risco de quem o consulta. Confirme os cálculos de forma independente e nunca utilize os exemplos para controlar máquinas reais.

Os termos técnicos ingleses aparecem entre parênteses na primeira apresentação.


Os capítulos incluem gráficos e diagramas. As secções finais explicam a origem de 4t e 63.2 %.


**Python / Instalar Python e criar um ambiente virtual (Windows/macOS/Linux):** [exercises/README.md](exercises/README.md).

## ROS 2 Jazzy sem GUI: junta virtual

[ROS 2 Jazzy sem GUI: junta virtual](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**Arquitetura ROS 2:** [Cinco etapas e diagrama Mermaid](notes/08-ros2-robot-architecture.md).

**Sem Compose:** [Executar diretamente a imagem ROS oficial](../../ros2/PLAIN_DOCKER.md).
