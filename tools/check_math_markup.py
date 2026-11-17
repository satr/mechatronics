"""Conservative source-only audit of GitHub MathJax markup."""
from __future__ import annotations

import re
from validate_repository import markdown_prose


def _balanced_tex(fragment: str) -> list[str]:
    issues = []
    depth = 0
    for pos, char in enumerate(fragment):
        if char in "{}" and not (pos and fragment[pos - 1] == "\\"):
            depth += 1 if char == "{" else -1
            if depth < 0:
                issues.append("TeX closing brace without opening brace")
                depth = 0
    if depth:
        issues.append("Unbalanced TeX braces")
    if len(re.findall(r"\\left\b", fragment)) != len(re.findall(r"\\right\b", fragment)):
        issues.append("Mismatched TeX left/right delimiters")
    if re.search(r"(?<!\\)\\\\(?:frac|int|sum|mathrm|sqrt|theta|omega)\b", fragment):
        issues.append("Double-escaped TeX control sequence")
    return issues


def math_markup_issues(markdown: str) -> list[str]:
    """Inspect Markdown as inert data; never render or execute formulas."""
    prose = markdown_prose(markdown)
    issues = []
    in_display = False
    display_parts = []
    for line_number, line in enumerate(prose.splitlines(), 1):
        if line.strip() == "$$":
            if in_display:
                issues.extend(f"line {line_number}: {msg}" for msg in
                              _balanced_tex("\n".join(display_parts)))
                display_parts = []
            in_display = not in_display
            continue
        if in_display:
            display_parts.append(line)
            continue
        positions = [m.start() for m in re.finditer(r"(?<!\\)\$", line)]
        if len(positions) % 2:
            issues.append(f"line {line_number}: unpaired inline math dollar")
        for start, end in zip(positions[::2], positions[1::2]):
            if end == start + 1:
                issues.append(f"line {line_number}: empty inline math")
            issues.extend(f"line {line_number}: {msg}"
                          for msg in _balanced_tex(line[start + 1:end]))
        if re.search(r"(?<!\\)\$\$", line):
            issues.append(f"line {line_number}: display math $$ must be on separate lines")
    if in_display:
        issues.append("Unclosed display-math $$ block")
    return issues
