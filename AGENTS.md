# Instructions for AI contributors

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SAFETY.md](SAFETY.md) first. Maintain this as a **domain-only** educational repository. No information about individuals, their applications, university plans, private chats, or educational histories belongs here, including metadata, examples, filenames, or commit messages.

The English learning content is canonical; all supported localized pages must remain content-consistent with their English counterparts, including formulas, values, assumptions, warnings, relative intra-language links, **and every intermediate step of a derivation**. Do not replace exact equalities with approximations or turn multi-step solutions into answer-only lists. For motion examples, always distinguish displacement from distance traveled and mean signed velocity from mean path speed, with the same worked numbers in translations. Never claim a translation is verified without checking it. Never insert personal progress logs. Use synthetic experiments only and validate numerical results. Before a commit, run the executable-source AST policy, repository tests, and link/privacy validation. Security-scanner edits themselves require independent review; a self-modified CI scanner is not a trust boundary.

License original code, text, translations, and illustrations under Apache License 2.0 unless explicitly stated otherwise; preserve third-party license terms and attribution, and don't claim ownership of third-party content. Keep the conspicuous disclaimer in all README editions. Do not copy external content beyond applicable quotation limits or rights.

**ROS 2 architecture naming rule:** The canonical editable Mermaid diagram is in [ros2/ROBOT_ARCHITECTURE.md](ros2/ROBOT_ARCHITECTURE.md). Maintain exactly five functional stage subgraphs with these labels and order: **Perception, Coordinate Transformation, Motion Planning, Motion Control, Feedback**. Use precisely these English labels in every localized terminology table; add local translations in a separate column. Do not conflate function with ROS node identity, URDF with motor commands, TF2 lookup with transform publication, trajectory control with the existing mock forward controller, or measured hardware state with a requested command. URDF is a side input outside the five stages. Extend the single Mermaid source and synchronize all `docs/<locale>/notes/08-ros2-robot-architecture.md` explanatory pages, chapters 06–07 and localized indexes; never copy private learning status into public content.

## Pedagogical structure


**Standalone lesson rule:** Chapters in the repository must teach without relying on an interactive conversation. Include enough reasoning, explicit coordinate/angle conventions, meaningful diagrams when geometry is spatial, and fully worked answers to practice exercises. Never publish a question addressed to a specific reader with no solution. Link a figure directly beside the explanation it clarifies and provide localized alt text and captions. Keep numerical examples reproducible and cross-check labels against formulas.

Write as a patient technical tutor: explain physical intuition first; define terms with original English equivalents in localized pages; move from general to specific and easy to difficult; include stable tables of contents and cross-links; place optional depth after the main lesson and link to it from early sections. Avoid mixing personal project context into public files.

## Self-contained continuity and publishing rules

This repository must remain usable by a new contributor or AI assistant **without access to any private account, conversation, memory, or external document**. Read [MAINTENANCE.md](MAINTENANCE.md) for the repeatable learning-content workflow and [WRITING_STYLE.md](WRITING_STYLE.md) for the teaching style.

When a newly explained concept improves the general course, update its English lesson and the same teaching point in **every supported translation**, including the matching cheat sheets and local links. Translate safety warnings completely and show full numerical output calculations in worked examples. Record subject-facing changes in [CHANGELOG.md](CHANGELOG.md); never publish private learners' progress.

At first use, justify or link non-arbitrary values (such as 63.2% after one time constant or the factor 4 in the derivative of 2t²). Localize natural-language formula labels, keep source SI symbols and correct dimensional meaning, and refer optional advanced proofs to the chapter's closing section. Treat plots and SVGs as source-controlled learning assets; test that they exist and render.


## Mathematical notation and executable examples

- Use **Greek `\varepsilon(t)` for a changing speed error**, never the letter `e(t)` when the same lesson uses Euler’s number. Define `\exp(z)=\mathrm{e}^{z}` and `\mathrm{e}\approx2.71828` at the FIRST use of the exponential response in every language. Use `\exp(-t/\tau)` throughout the mathematics, alongside `math.exp(-t / tau)` or `numpy.exp(...)` only in Python code.
- Prefer **rendered fractions** `\frac{a}{b}` inside `$...$` or `$$...$$` rather than `a/b` in mathematical explanations and formula tables. Python source must use `/`. Prefer one displayed equation per conceptual step instead of long combined lines when possible. Do not convert ordinary paths, code snippets, or SI unit names into math.
- Place the definition of a mathematical symbol before its first appearance. Present the exponential derivation and the 63.2%/86.5%/95.0% calculation as ONE connected explanation in an optional end-of-chapter section, and link to it from the introductory example. Do not repeat a similar half-explanation earlier and then introduce new symbols several pages later.
- The three reviewed core exercises are local Python scripts using only the standard library. Do not add browser-based runners, remote execution services, external API calls, secrets, private data or physical actuator interfaces.
- Keep local Python instructions short in the root README and each localized exercise index, with official Python documentation links. Optional plots use NumPy and Matplotlib; update the requirements and notebook references together.

## Language switchers and symbol definitions

Do not omit the same-page language switcher in any localized educational Markdown file. Keep standard `zh` and `ja` language codes; never replace them with country codes `CN` and `JP`. Define `\sum`, `\varepsilon`, `\tau` and every other non-obvious symbol on first use and link to the local `SYMBOLS.md`. Do not put `$...$` mathematical markup inside Markdown link labels.

## Required SI/decimal review

All translated pages use **decimal points** (e.g. `0.5`, never `0,5` or `0{,}5`). International SI unit symbols remain unchanged by translation. Put a space between a number and unit (`4 mm`), centered dots between multiplied unit symbols (`kg·m²`, `N·m·s/rad`), and never spaces around `/` in unit symbols (`mm/s`). Do not write misleading `\,` spacing commands in beginner-facing equations. Write a differential as `\mathrm{d}t`, not comma `,dt`. Check numeric and dimensional examples and run repository validation before publishing.

## Local Python examples

Link directly to the reviewed Python source files, not a hosted REPL or browser runner. Core examples need no third-party dependencies. Link official Python installation and venv documentation; optional libraries belong in a local isolated environment. Do not suggest that a browser sandbox can safely execute arbitrary code.

## Basic calculus course and reference

Ensure `docs/<locale>/notes/00-calculus-foundations.md` and `docs/<locale>/INTEGRAL_TABLE.md` exist in every supported locale, with localized language switchers and references. Check mathematical conditions and domains, including positive parameters and dimensionless logarithm arguments. Do not copy screenshots or any attribution/watermarks.


## Practical calculus and feedback chapters

Keep `docs/<lang>/notes/00-calculus-foundations.md`, `INTEGRAL_TABLE.md`, `TRIGONOMETRY.md`, and `notes/03-feedback-control.md` complete in every supported edition. Each has same-page language switcher, correct SI units and local links. Give engineering examples before abstract derivations; keep sphere as optional chain-rule example. Tan 90° is undefined; arctan takes a dimensionless ratio.

For PID, distinguish absolute commanded current from the integral term's change, keep finite dt in discrete integration, handle saturation of the **total** output, and state the defined torque-producing current for Kt. No executable examples may interface with real equipment.
