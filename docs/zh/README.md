# Mechatronics Training — 简体中文

**切换此页语言:** [en](../en/README.md) · [fr](../fr/README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](../pt/README.md) · [zh](README.md) · [ja](../ja/README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](../ko/README.md) · [fi](../fi/README.md) · [pl](../pl/README.md)

> [!WARNING]
> **警告：** 本仓库是人工智能辅助编写的教学资料，可能存在事实错误、公式错误、翻译不准确或不成立的假设。使用者自行承担风险，必须独立验证计算结果。**切勿使用示例程序控制真实机器、电机或机器人。**

关于运动学基础、微积分、数值积分、一阶动态系统、转动惯量与旋转动能的独立学习资料。

## 目录

1. [微积分基础：导数、微分与积分](notes/00-calculus-foundations.md)
2. [运动、导数与积分](notes/01-motion-calculus.md)
3. [一阶动力学与旋转运动](notes/02-first-order-dynamics.md)
4. [积分公式表](INTEGRAL_TABLE.md)
5. [导数公式表](DERIVATIVE_TABLE.md)
6. [公式速查表](CHEATSHEET.md)
7. [Python 练习](exercises/README.md)
8. [数学符号与记法](SYMBOLS.md) · [完整单位表](UNITS.md)
9. [三角函数表及机械例题](TRIGONOMETRY.md)
10. [反馈控制：PID 与保持转矩](notes/03-feedback-control.md)
11. [机器人坐标系：位置与旋转](notes/04-coordinate-frames.md)
12. [旋转、速度与奇异位形](notes/05-velocity-jacobian.md)
13. [ROS 2：架构、节点与 Docker 实验](notes/06-ros2-foundations.md)

[仓库首页／语言选择](../../README.md) · [安全与准确性](SAFETY.md) · [许可协议](LICENSING.md)

## 要点回顾

每次学习一个简短主题，重新计算例题，运行离线仿真，并用自己的话解释结果。理想化模型并非经过验证的实际设备模型。

首次介绍技术概念时，在括号中标注对应的英文术语。


各章包含示意图与计算图表。末尾选读部分说明 4t 与 63.2 % 的推导过程。


**Python / 安装 Python 和虚拟环境（Windows/macOS/Linux）:** [exercises/README.md](exercises/README.md).

## ROS 2 Jazzy 无 GUI：虚拟关节

[ROS 2 Jazzy 无 GUI：虚拟关节](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**ROS 2 机器人架构：**[五阶段和 Mermaid 图](notes/08-ros2-robot-architecture.md)。

**无需 Compose：**[直接运行官方 ROS 镜像](../../ros2/PLAIN_DOCKER.md)。
