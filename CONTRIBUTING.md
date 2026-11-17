# Contributing and maintenance rules

1. **Public-topic-only content:** Do not commit personal names, email addresses, application or interview details, individual learning progress, addresses, private documents, account IDs, personal project URLs, or institutional affiliation claims. No biographical history in examples.
2. **English canonical:** Update the English edition first. Translate the same meaning into every supported language. Keep the same set of maintained localized document paths in each locale, including the course index, reference tables, lessons, exercises, safety and licensing pages; preserve localized intra-language links.
3. **Safety and quality:** Validate every formula, numerical result, unit, model assumption, and exercise output. Avoid implying that toy simulations operate real hardware.
4. **Accuracy notice:** Keep a prominent disclaimer in the root README and in every localized README. Translations must not suggest certification, endorsement, guarantees, or validated industrial use.
5. **Provenance:** Do not reproduce substantial externally sourced text or third-party visuals/code without documented rights. Provide links for further reading and track permitted incorporations in SOURCES.md. Cite ideas where appropriate; linking is not permission to copy.
6. **Tests:** Run `python3 tools/check_executable_sources.py`, `python3 -m unittest discover -s tests -v`, then `python3 tools/validate_repository.py`. The AST policy checks executable educational examples before tests import or run them; a separate trusted-base PR audit reads changed example blobs without running submitted code. These are conservative warning mechanisms, not a sandbox or proof of safety. Verify all internal Markdown links and scan for accidental private-data patterns before every release. The validator skips installed dependencies and build folders such as `.venv/`; maintained Markdown, source code, configuration and original SVGs outside those folders are included in the privacy scan. This does not replace a review of Git history or binary assets.
7. **Security:** Review [SECURITY.md](SECURITY.md) before changes to executable Python, Docker, dependencies or CI. Avoid checking out untrusted PR code in privileged workflows; review security-policy changes independently.
8. **Scope:** Keep any private learner-specific progress, conversation history, preferences, universities, and interview schedules in a separate private store outside the repository. This Git repository remains safe in principle to publish subject to review of commit history, repository metadata, Git author attribution, and all future contributions.

The English original and translated editions must not claim anything about a particular learner or organization.

## Learning-document structure

1. Start with physical intuition and the everyday meaning of a term.
2. Include a short summary and a table of contents for chapters with several sections.
3. Introduce one quantity at a time, with units and a small worked example.
4. Place formulas after explaining what they describe and when they apply.
5. Move derivations, stability restrictions, numerical details, and limitations to an **optional appendix at the end**, linked from the earlier beginner-friendly text.
6. On first use of a nontrivial technical term in localized text, add the English term in parentheses. Keep bilingual glossaries consistent across all locales.
7. Keep links between learning documents within the reader's language; links to shared Python files and canonical legal documents may leave the locale.
8. Maintain canonical English first, and update all supported translations with matching mathematical claims, example numbers and optional details.

## Ongoing maintenance without private context

For subsequent lessons and forks, use the self-contained steps in [MAINTENANCE.md](MAINTENANCE.md), the editorial rules in [WRITING_STYLE.md](WRITING_STYLE.md), and the generic [CHANGELOG.md](CHANGELOG.md). No contributor needs access to anyone's private notes, interviews, institution, or external AI conversation. Maintain all supported languages together, including chart captions, mathematical text labels and internal links; do not silently publish a partial translation as complete.

## Numbers and units

Use decimal **point** in every language. Write `4 mm`, `10 mm/s`, and `N·m·s/rad`; never a comma between unit factors, a decimal comma, or spaces around `/`. Refer to [WRITING_STYLE.md](WRITING_STYLE.md) and the localized `SYMBOLS.md` for examples.

### Language coverage

The currently supported locales are the directories in `docs/` listed in the [root language index](README.md#read-in-your-language). Korean and Finnish remain subject to native-speaker semantic review; check their actual indexes and chapter coverage rather than assuming specific pages are missing. All future changes must update every supported locale or explicitly track and disclose outstanding translations; do not present partial coverage as complete. See [MAINTENANCE.md](MAINTENANCE.md).
