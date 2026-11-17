# Mechatronics Training — 日本語

**このページの言語を切り替える:** [en](../en/README.md) · [fr](../fr/README.md) · [de](../de/README.md) · [it](../it/README.md) · [es](../es/README.md) · [pt](../pt/README.md) · [zh](../zh/README.md) · [ja](README.md) · [nb](../nb/README.md) · [ru](../ru/README.md) · [ko](../ko/README.md) · [fi](../fi/README.md) · [pl](../pl/README.md)

> [!WARNING]
> **注意：** 本教材は AI を利用して作成されており、誤り、不正確な翻訳、誤った仮定が含まれる可能性があります。利用は自己責任で行い、数式と計算を独立に確認してください。**実機のモーターや工作機械の制御に使用しないでください。**

運動、微分積分、数値積分、一次遅れ系、回転慣性および回転運動エネルギーについての独立した学習資料です。

## 目次

1. [微積分の基礎：導関数・微分・積分](notes/00-calculus-foundations.md)
2. [運動・微分・積分](notes/01-motion-calculus.md)
3. [一次系の動特性と回転](notes/02-first-order-dynamics.md)
4. [積分公式表](INTEGRAL_TABLE.md)
5. [導関数一覧](DERIVATIVE_TABLE.md)
6. [公式早見表](CHEATSHEET.md)
7. [Python 演習](exercises/README.md)
8. [数式の記号と表記](SYMBOLS.md) · [単位一覧](UNITS.md)
9. [三角関数表と力学の例](TRIGONOMETRY.md)
10. [フィードバック制御：PID と保持トルク](notes/03-feedback-control.md)
11. [ロボットの座標系：位置と回転](notes/04-coordinate-frames.md)
12. [回転、速度、特異姿勢](notes/05-velocity-jacobian.md)
13. [ROS 2：アーキテクチャ、ノード、Docker 実習](notes/06-ros2-foundations.md)

[リポジトリ／言語選択](../../README.md) · [安全性と正確性](SAFETY.md) · [ライセンス](LICENSING.md)

## 要点

短い項目を一つずつ読み、計算を再現し、オフラインのシミュレーションを実行して自分の言葉で説明してください。ここでの理想化モデルは実機の検証済みモデルではありません。

技術用語を初めて紹介するとき、対応する英語を括弧内に示します。


各章に図とグラフがあります。章末の詳しい説明で 4t と 63.2 % の導出を確認できます。


**Python / Python と仮想環境の準備（Windows/macOS/Linux）:** [exercises/README.md](exercises/README.md).

## GUI なし ROS 2 Jazzy：仮想関節

[GUI なし ROS 2 Jazzy：仮想関節](notes/07-ros2-control-lab.md) — URDF · TF2 · ros2_control · mock hardware · ARM64.

**ROS 2 ロボット構成：**[五段階と Mermaid 図](notes/08-ros2-robot-architecture.md)。

**Compose 不要：**[公式 ROS イメージを直接起動する](../../ros2/PLAIN_DOCKER.md)。
