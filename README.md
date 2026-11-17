# Mechatronics Training

> [!CAUTION]
> **DISCLAIMER — EDUCATIONAL MATERIAL, NOT VERIFIED ENGINEERING GUIDANCE.**
> This independent, AI-assisted repository may contain **errors, incorrect formulas, inaccurate translations, omissions, or unsafe assumptions**. Content is provided **AS IS**, without warranties of accuracy, completeness, safety, or fitness for any purpose. **You use it entirely at your own risk.** Independently verify all results against reliable references. **Do not use the models, examples, or code to control real machinery, drives, robots, or safety-critical systems.**

A self-contained introduction to motion, practical calculus (limits, derivatives, logarithms, and integrals), trigonometry, first-order dynamics, rotational energy, feedback control, robot coordinate frames, and ROS 2 distributed software. Each chapter explains assumptions and units, provides worked examples, and links to small, offline Python simulations.

This is a subject-focused reference. It includes no personal records, private conversations, or unrelated organizational details.

<a id="read-in-your-language"></a>

## Read in your language

| Language | Standard language code | Start here |
| --- | --- | --- |
| English (canonical edition) | `en` | [English](docs/en/README.md) |
| Français | `fr` | [Français](docs/fr/README.md) |
| Deutsch | `de` | [Deutsch](docs/de/README.md) |
| Italiano | `it` | [Italiano](docs/it/README.md) |
| Español | `es` | [Español](docs/es/README.md) |
| Português | `pt` | [Português](docs/pt/README.md) |
| 简体中文 | `zh` | [简体中文](docs/zh/README.md) |
| 日本語 | `ja` | [日本語](docs/ja/README.md) |
| Norsk bokmål | `nb` | [Norsk bokmål](docs/nb/README.md) |
| Русский | `ru` | [Русский](docs/ru/README.md) |
| 한국어 | `ko` | [한국어](docs/ko/README.md) |
| Suomi | `fi` | [Suomi](docs/fi/README.md) |
| Polski | `pl` | [Polski](docs/pl/README.md) |

**Language code or country code?** These directories use the standard language identifiers `zh` (Chinese) and `ja` (Japanese), not the country identifiers `CN` (China) and `JP` (Japan). To switch to a matching chapter, change only the language segment in a URL, for example `docs/ru/notes/01-motion-calculus.md` → `docs/ja/notes/01-motion-calculus.md`. Every translated documentation page also has a same-page language switcher.

The listed editions provide the maintained learning sequence and reference sections, with links to pages **in the same language**. Korean, Finnish, and Polish still require native-speaker semantic review. Formulas, numerical values, and code are shared. The English edition is the source of truth when translations differ.

<a id="how-to-navigate"></a>

**Notation in every language:** decimal numbers use a **point** (`0.5`, `3.8`, `63.2 %`); numbers and SI unit symbols have a separating space (`1 s`, `4 mm`); compound units use `·` for multiplication and no spaces around `/` (`kg·m²`, `N·m·s/rad`, `mm/s`). See the [SI/non-SI unit glossary](docs/en/UNITS.md) in all 13 languages and the [English symbol guide](docs/en/SYMBOLS.md#si-notation). Unit symbols stay internationally standardized while their names and physical meanings are introduced locally. The BIPM-recommended space also precedes `%`: `63.2 %`.

## How to navigate

The material is ordered **from intuitive physical concepts to mathematical models, then to numerical examples**. Each lesson starts with a short review and an on-page table of contents. Optional deeper explanations, dimensional checks, model limitations, and derivations come **at the end of the lesson**; earlier sections link to them so beginners can skip ahead only when ready.

```text
README.md                 Language selector and important disclaimer
docs/
  en/                     Canonical English edition
  fr/ de/ it/ es/ pt/      Translated editions
  zh/ ja/ nb/ ru/          Translated editions
  ko/ fi/ pl/              Translated editions (native-language review pending)
    README.md              Localized reading sequence and TOC
    CHEATSHEET.md          Short formula reference
    INTEGRAL_TABLE.md      Integration formulas and worked examples
    DERIVATIVE_TABLE.md    Derivative rules and worked examples
    TRIGONOMETRY.md        Trig functions and practical angles
    SYMBOLS.md             Greek letters, summation, math notation
    UNITS.md               SI and non-SI unit reference with local meanings
    notes/                 Lessons in increasing difficulty
    exercises/README.md    Shared Python exercise instructions
    SAFETY.md              Localized safety summary
    LICENSING.md           Localized licensing summary
ros2/                     Synthetic ROS 2 Jazzy Docker topic/service lab
exercises/                Language-neutral, offline Python simulations
tests/                    Numerical and repository validation
tools/                    Internal link, security-policy and privacy checks
```

Translations include the English technical term in parentheses next to its localized equivalent. English-language materials are the canonical source if versions disagree, **but are not guaranteed accurate**.

<a id="topics"></a>

## Topics

The [self-contained maintenance guide](MAINTENANCE.md) defines how to expand every translation after a useful new teaching point. New contributors can follow it without access to private files, memory, or external accounts.


1. [Calculus foundations: derivatives, differentials and integrals](docs/en/notes/00-calculus-foundations.md)
2. [Motion, velocity, derivatives and integrals](docs/en/notes/01-motion-calculus.md)
3. [First-order dynamics, time constants, torque and energy](docs/en/notes/02-first-order-dynamics.md)
4. [Derivative reference table](docs/en/DERIVATIVE_TABLE.md)
5. [Integral reference table](docs/en/INTEGRAL_TABLE.md)
6. [Trigonometry: sin, cos, tan and arctan](docs/en/TRIGONOMETRY.md)
7. [Feedback control: PID, sampling and holding torque](docs/en/notes/03-feedback-control.md)
8. [Short formula reference](docs/en/CHEATSHEET.md)
9. [Reproducible Python exercises](docs/en/exercises/README.md)
10. [Symbols and mathematical notation](docs/en/SYMBOLS.md)
11. [Robot coordinate frames: position and rotation](docs/en/notes/04-coordinate-frames.md)
12. [Rotation, velocity, Jacobians and singular configurations](docs/en/notes/05-velocity-jacobian.md)
13. [ROS 2: graph, topics, services, TF, URDF, controllers and a Docker lab](docs/en/notes/06-ros2-foundations.md)
14. [ROS 2 robot architecture: five stages, Mermaid and localized terminology](docs/en/notes/08-ros2-robot-architecture.md)

## ROS 2 practical track

[View the single editable five-stage Mermaid architecture diagram](ros2/ROBOT_ARCHITECTURE.md#one-editable-mermaid-diagram) or open [its Russian-language explanation](docs/ru/notes/08-ros2-robot-architecture.md) (13 language editions available). The diagram distinguishes perception, coordinate transformations, planning, commands, state feedback and URDF model data; the complete physical robot remains conceptual.

[Start ROS 2 in plain Docker without Compose](ros2/PLAIN_DOCKER.md), [read the complete ROS 2 architecture lesson](docs/en/notes/06-ros2-foundations.md) in any supported language, then run the [Jazzy Docker publisher/subscriber/service lab](ros2/README.md). The lab does not control physical devices. Offline tests use mocks; changes under `ros2/` additionally trigger a [live Docker smoke-test workflow](.github/workflows/ros2-live-smoke.yml) **on `main` after merge, not on unmerged pull requests**. Check the actual workflow result before treating container execution as verified. That CI test covers a single-container simulation, not multi-host DDS or any physical device.

## Contents

- [Languages and learning path](#how-to-navigate)
- [Study topics](#topics)
- [Install and run Python examples](#install-and-run-python-examples)
- [Accuracy and licensing](#scope-accuracy-and-licensing)

<a id="install-and-run-python-examples"></a>

## Install and run Python examples

Install Python 3.10+ using the [official Python downloads](https://www.python.org/downloads/); see the [official Python tutorial](https://docs.python.org/3/tutorial/index.html) for basic usage and the [venv documentation](https://docs.python.org/3/library/venv.html) for isolated environments. Read and review source files before running them.

From the repository root, the three basic examples need **only the standard library**; they do not require `pip`, `venv`, or external services:

```bash
python3 exercises/01_motion_and_integral.py
python3 exercises/02_first_order_response.py
python3 exercises/03_rotation_energy.py
```

On Windows, use `py -3` in place of `python3`. The scripts are synthetic and do not control equipment.

For **optional** plots or the local Jupyter notebook, create an isolated environment. From the repository root on macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python exercises/plot_models.py
```

On Windows:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe exercises\plot_models.py
```

The [requirements file](requirements.txt) contains the optional NumPy, Matplotlib and JupyterLab packages. It uses Python-version markers: the basic standard-library exercises work on Python 3.10+, and NumPy remains available on 3.10; the **optional Matplotlib and JupyterLab environment requires Python 3.11+** because their Python 3.10 transitive packages have unresolved vulnerability reports. Python 3.12+ can use the newest NumPy release family. Do not manually force incompatible releases. See the official [packaging guide](https://packaging.python.org/en/latest/tutorials/installing-packages/) for installing packages safely; do not override system Python protections. For source links, the optional notebook and validation instructions, see the [exercise index](docs/en/exercises/README.md) and [local notebook guide](notebooks/README.md).

<a id="scope-accuracy-and-licensing"></a>

## Scope, accuracy, and licensing

These are introductory **idealized** models, not a real actuator design, plant model, or certified educational course. Physical friction, load torque, current and voltage limits, delays, nonlinearities, and safety functions can invalidate the simple equations.

See [Security review and supported threat model](SECURITY.md), [Safety and accuracy](SAFETY.md), [Licensing](LICENSING.md), [Sources and attribution](SOURCES.md), [Contributing](CONTRIBUTING.md), [Maintenance](MAINTENANCE.md), and [Writing style](WRITING_STYLE.md). Unless explicitly stated otherwise, original documentation, translations, code, and illustrations are offered under **Apache License 2.0**. Third-party material retains its own rights and licenses. Mathematical facts and equations are not claimed as proprietary.
