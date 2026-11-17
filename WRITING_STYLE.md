# Writing for understanding

For ROS 2 architecture diagrams, each functional stage used in prose must be labeled identically in the Mermaid source: Perception, Coordinate Transformation, Motion Planning, Motion Control, Feedback. Name real ROS nodes, packages and interfaces inside each stage, not as invented counterparts for logical functions. One shared diagram may have translated companion pages and localized English/native terminology, but avoid multiple unsynchronized Mermaid copies. Differentiate model description (URDF), transforms (TF2), requested joint commands and measured feedback, including servo-local feedback independent of /joint_states.

A lesson must stand on its own without a tutor. Any practice task in the text must include a complete worked answer, not a question to an individual reader. For geometry, show a clear original figure where that makes relationships easier to understand. Label coordinate frames, units, origins, angle directions and relative versus absolute angles, and explain every non-obvious numerical step. Localized editions must include equivalent explanations, figures, and solutions.

Write as a patient technical instructor for someone meeting the idea for the first time.

- Start with **what a quantity means physically** before showing its symbols.
- Explain why an unfamiliar number or coefficient appears the first time it occurs. A one-line explanation often saves a reader from rereading earlier chapters.
- Keep one name for one concept. Give technical terms in the reader's language and the original English term in parentheses on first use.
- Use everyday, direct sentences. Do not inflate simple explanations with academic filler, unnecessary claims, or vague metaphors.
- A derivation matters, but it need not interrupt a beginner's first reading. Give a direct link to the **optional derivation at the end** of the chapter.
- Show values, assumptions, units and examples that can be independently recomputed.
- Keep evidence separate from interpretation. Never turn an assumption into an established fact, or a synthetic exercise into an engineering specification.
- Use natural language for each translation, but use the repository-wide decimal **point** (not comma), identical international SI unit symbols, localized explanations of unit names, localized technical labels inside formulas, and English technical equivalents at first mention.
- Keep translated editions useful on their own; English remains a canonical reference, not a substitute for proper localization.

## The short review before publishing a chapter

Read it as a newcomer: Is it clear why the next sentence follows from the previous one? Are non-obvious constants explained or linked? Are diagrams accurate? Do all formulas render inside GitHub? Can the reader navigate without a chat or other context? Does the material remain safe to publish publicly?

## Math and symbols

Avoid introducing the same letter for two different meanings. For first-order examples use $\varepsilon(t)$ for speed error and $\exp(z)=\mathrm{e}^{z}$ for Euler’s number; define both before the equation. In mathematical explanations use rendered fractions; reserve slash notation for programming. Keep the detailed proof of the exponential and its percentages in one appendix, linked from the first occurrence.

## Consistent decimal and SI notation

Use the decimal point in all languages: `0.5`, not `0,5` or `0{,}5`. Use `63.2 %`, with a space before the percent sign in accord with the current SI Brochure. Write `1 s` (space between value and unit), `10 mm/s` (no spaces around the slash), and `kg·m²` or `N·m·s/rad` (centered multiplication dot). In rendered mathematics use `\mathrm{s}`, `\mathrm{mm/s}`, and `\mathrm{kg}\cdot\mathrm{m}^2`. Avoid `\,` as an invisible spacing command in beginner-facing equations because it has been mistaken for punctuation; prefer `\ ` between a value and its unit and before `\mathrm{d}t`. Reserve comma/semicolon for an actual list of quantities, never for multiplying units. For inline mathematics, use balanced `$...$` delimiters; for display mathematics, use balanced `$$` delimiters on separate lines. Check the rendered result directly when a browser is available. Source checks and successful CI do not prove appearance on every device. Render the formula and check it by sight. This convention is shared by all maintained language editions; the BIPM SI Brochure allows both decimal markers, and this repository chooses the point.

## Readable terminology and enumerations

A long comma-separated sequence of glossary pairs is hard to scan. Use a short heading followed by a bullet list, one localized term plus its English equivalent per bullet. Use tables only when the reader needs to compare two or more attributes. Apply the same structure in all supported language editions.

## Executable examples and installation

List runnable source files as simple Markdown bullets and show their local invocation. Do not provide a browser runner or external execution service. Link official Python installation and venv documentation; for macOS/Linux use `python3` and for Windows use `py -3`. The base scripts require only the standard library; optional plots/notebooks can use an isolated venv with `requirements.txt`.


## Basic calculus course and reference

Present derivative and integration rules in progressive, categorized sections. Keep formula tables readable with conditions beside each formula; introduce physical intuition and precise units before symbolic shortcuts.

## Mobile-readable mathematical figures and GitHub formulas

- Use one legible sans-serif font family across SVG text (Arial, Helvetica, sans-serif); keep headings, line widths and letter sizes moderate and consistent. Avoid giant lettering inside a figure.
- Avoid combining Unicode diacritics such as dotted Q in SVG or prose; use ω for angular speed in diagrams and the LaTeX command \dot{Q} in equations. If a graph shows linear speed, distinguish v from components with descriptive labels.
- Write trigonometric arguments in parentheses, with explicit multiplication where needed: L\cdot\cos(Q(t)), not a visually merged LcosQ(t). State whether angles are degrees or radians.
- For GitHub/mobile, prefer short standalone equations and scalar-first explanation over giant matrix expressions inside \underbrace. Define individual Jacobian coefficients and give a readable Markdown fallback.
- Never substitute single-dollar delimiters for multiline display math. Tests should detect unbalanced math fences and raw display markup. Structural SVG checks do not guarantee readability on every device.
- One trigonometry reference should have one unit circle and one complete source table, not duplicate same-content circles and tables. Document the principal arctangent range in any arctan(tan θ) table.
- For the multi-panel right-triangle figure, use an intrinsic rendered size of 480×856 with a 720×1284 viewBox. This scales the panel, fonts and strokes to two-thirds of the previous rendered size; keep source geometry intact.
- In the unit-circle SVG, place all 16 angles in distinct non-overlapping cards connected to their actual points. Each card shows cos and sin separately, with a signed exact fraction and decimal approximation; never substitute a shared quadrant list for per-angle labels. Keep the single numerical reference table in each localized chapter.
