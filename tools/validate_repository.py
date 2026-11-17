"""Offline validation: local links, locale parity, educational structure, privacy hygiene."""
from __future__ import annotations

import re
import math
import os
# Every parsed SVG is bounded in size and checked for DTD/entity declarations.
import xml.etree.ElementTree as ET  # nosemgrep: python.lang.security.use-defused-xml.use-defused-xml
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
REQUIRED = ("README.md", "CHEATSHEET.md", "SYMBOLS.md", "UNITS.md", "INTEGRAL_TABLE.md", "TRIGONOMETRY.md", "notes/03-feedback-control.md", "notes/04-coordinate-frames.md", "notes/05-velocity-jacobian.md", "notes/00-calculus-foundations.md", "notes/01-motion-calculus.md",
            "notes/02-first-order-dynamics.md", "notes/06-ros2-foundations.md", "exercises/README.md",
            "SAFETY.md", "LICENSING.md")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGE_LINK = re.compile(r"!\[([^\]\n]*)\]\(([^)\s]+)\)")
TABLE_ROW = re.compile(r"^\|.*\|$")
EXPLICIT_ANCHOR = re.compile(r'<a\s+(?:id|name)="([^"]+)"\s*>\s*</a>')
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
# Installed tools and generated build outputs are not part of the course.
PRIVACY_SOURCE_EXTENSIONS = frozenset({
    ".md", ".py", ".sh", ".yaml", ".yml", ".xml", ".cfg",
    ".html", ".svg", ".ipynb", ".txt", ".toml", ".json", ".ini",
})
PRIVACY_SOURCE_NAMES = frozenset({"Dockerfile", ".gitignore", "LICENSE"})
SKIP_MARKDOWN_DIRS = frozenset({
    ".git", ".venv", "venv", ".tox", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", "__pycache__", "node_modules", "build", "install", "log", "dist",
})


def is_project_markdown(path: Path) -> bool:
    """Exclude ignored local dependencies/build outputs without needing Git metadata."""
    relative = path.relative_to(ROOT)
    return path.suffix.lower() == ".md" and not (
        SKIP_MARKDOWN_DIRS.intersection(relative.parts[:-1])
    )


def is_privacy_scannable(path: Path) -> bool:
    """Include source/docs and original SVGs, but never local build outputs."""
    relative = path.relative_to(ROOT)
    return (path.suffix.lower() in PRIVACY_SOURCE_EXTENSIONS
            or path.name in PRIVACY_SOURCE_NAMES) and not (
                SKIP_MARKDOWN_DIRS.intersection(relative.parts[:-1])
            )


def repository_privacy_files():
    """Walk source text, pruning third-party environments before descent."""
    for directory, subdirs, filenames in os.walk(ROOT):
        subdirs[:] = [name for name in subdirs if name not in SKIP_MARKDOWN_DIRS]
        for name in filenames:
            path = Path(directory) / name
            if is_privacy_scannable(path):
                yield path


def repository_markdown_files():
    """Walk project docs while pruning dependency trees before descending into them."""
    for directory, subdirs, filenames in os.walk(ROOT):
        subdirs[:] = [name for name in subdirs if name not in SKIP_MARKDOWN_DIRS]
        for name in filenames:
            path = Path(directory) / name
            if is_project_markdown(path):
                yield path


def non_code(text: str) -> str:
    """Exclude fenced code blocks to avoid mistaking link examples for actual links."""
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)


INLINE_CODE_SPAN = re.compile(r"(?<!`)(`+)(?!`)([^\n]*?)\1(?!`)")


def markdown_prose(text: str) -> str:
    """Exclude fenced and inline code before interpreting Markdown links.

    Both code examples and real hyperlinks may contain brackets and
    parentheses. Only the latter should be subject to link resolution.
    """
    return INLINE_CODE_SPAN.sub("", non_code(text))


# Guard against common active-content injection in source-controlled docs.
# This signature check is not a general HTML sanitizer.
ACTIVE_HTML_TAGS = frozenset({
    "script", "iframe", "object", "embed", "form", "meta", "base",
    "link", "style", "svg", "math", "img", "foreignobject",
    "video", "audio", "source", "track", "picture", "frame", "frameset",
    "applet", "portal", "input", "button", "textarea", "select", "template",
    "canvas",
})
ACTIVE_SVG_TAGS = frozenset({
    "script", "foreignobject", "iframe", "object", "embed", "image",
    "animate", "animatetransform", "animatemotion", "set", "a",
})
INLINE_HTML_TAG = re.compile(r"<\s*([a-z][\w:-]*)\b[^>]*>", re.I)
EVENT_HANDLER_ATTRIBUTE = re.compile(r"\bon[a-z]+\s*=", re.I)
# Normal Markdown links can express destinations without raw HTML. Keep
# raw HTML only for harmless explicit anchors and inline formatting.
RESOURCE_HTML_ATTRIBUTE = re.compile(
    r"\b(?:href|src|xlink:href|srcset|action|formaction|poster|style|data)\s*=",
    re.I,
)
UNSAFE_LINK_SCHEME = re.compile(r"^(?:javascript|vbscript|file|data|blob)\s*:", re.I)
# [text][ref] and ![alt][ref] resolve through [ref]: destination
# definitions rather than an inline (...). Check definitions as data.
REFERENCE_LINK_DESTINATION = re.compile(
    r"(?m)^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*<?([^>\s]+)>?",
)
UNSAFE_AUTOLINK = re.compile(
    r"<\s*(?:javascript|vbscript|file|data|blob)\s*:", re.I,
)
CSS_RESOURCE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I | re.S)
MAX_SVG_SOURCE_BYTES = 1_000_000


def active_markdown_issues(markdown: str) -> list[str]:
    """Inspect Markdown outside code fences and inline code, without rendering."""
    body = markdown_prose(markdown)
    issues = []
    for match in INLINE_HTML_TAG.finditer(body):
        name = match.group(1).lower()
        if name in ACTIVE_HTML_TAGS:
            issues.append(f"active HTML element <{name}> in Markdown")
        if EVENT_HANDLER_ATTRIBUTE.search(match.group(0)):
            issues.append("HTML inline event handler in Markdown")
        if RESOURCE_HTML_ATTRIBUTE.search(match.group(0)):
            issues.append("raw HTML resource or style attribute in Markdown")
    for link in MARKDOWN_LINK.finditer(body):
        if UNSAFE_LINK_SCHEME.match(link.group(1)):
            issues.append("unsafe Markdown link scheme")
    for image in IMAGE_LINK.finditer(body):
        if UNSAFE_LINK_SCHEME.match(image.group(2)):
            issues.append("unsafe Markdown image scheme")
    for definition in REFERENCE_LINK_DESTINATION.finditer(body):
        if UNSAFE_LINK_SCHEME.match(definition.group(1)):
            issues.append("unsafe Markdown reference destination scheme")
    if UNSAFE_AUTOLINK.search(body):
        issues.append("unsafe Markdown autolink scheme")
    if "javascript:" in body.lower() or "data:text/html" in body.lower():
        issues.append("active URL scheme in Markdown")
    return issues


def static_svg_issues(markup: str) -> list[str]:
    """Allow only passive local SVG visuals and same-document #fragment uses."""
    issues = []
    if len(markup.encode("utf-8")) > MAX_SVG_SOURCE_BYTES:
        return ["SVG source exceeds size limit"]
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b", markup, re.I):
        return ["SVG document-type/entity declarations forbidden"]
    if re.search(r"<\?(?!xml(?:\s|\?>))", markup, re.I):
        issues.append("SVG processing instruction other than XML declaration")
    try:
        root = ET.fromstring(markup)
    except ET.ParseError:
        return issues + ["invalid SVG XML"]
    if root.tag.rsplit("}", 1)[-1].lower() != "svg":
        issues.append("SVG document root must be svg")
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1].lower()
        if tag in ACTIVE_SVG_TAGS:
            issues.append(f"active or external SVG element {tag}")
        for key, value in element.attrib.items():
            attr = key.rsplit("}", 1)[-1].lower()
            if attr.startswith("on") and len(attr) > 2:
                issues.append(f"SVG inline event handler {attr}")
            if attr in {"href", "src"} and not value.startswith("#"):
                issues.append(f"SVG external resource reference {attr}")
            if "javascript:" in value.lower() or "data:" in value.lower():
                issues.append("SVG active URL scheme")
        if tag == "style" and element.text and "@import" in element.text.lower():
            issues.append("SVG external stylesheet import")
    for _, target in CSS_RESOURCE.findall(markup):
        if not target.strip().startswith("#"):
            issues.append("SVG CSS resource reference is not local #fragment")
    return issues


def markdown_anchor_ids(body: str) -> set[str]:
    """Recognize explicit anchors and ordinary GitHub-style heading fragments.

    Covers standard ATX headings (including duplicate headings). For unusual
    Markdown/HTML constructs, prefer a stable explicit anchor in the document.
    """
    anchors = set(EXPLICIT_ANCHOR.findall(body))
    used = {}
    for line in non_code(body).splitlines():
        match = re.match(r"^[ ]{0,3}#{1,6}[ \t]+(.+?)\s*$", line)
        if not match:
            continue
        heading = re.sub(r"[ \t]+#+[ \t]*$", "", match.group(1)).strip()
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading)
        heading = heading.replace("*", "").replace("`", "").replace("~", "")
        heading = re.sub(r"[^\w -]", "", heading.lower())
        slug = heading.strip().replace(" ", "-")
        if not slug:
            continue
        count = used.get(slug, 0)
        anchors.add(slug if count == 0 else f"{slug}-{count}")
        used[slug] = count + 1
    return anchors


def check() -> list[str]:
    import importlib.util
    errors = []

    # Verify the independent unit-circle and velocity lesson diagrams.
    learning_figures = ("unit_circle_reference.svg", "trig_ratios.svg",
                        "arccos_reference_curve.svg", "link_tangent_velocity.svg",
                        "folded_displacement_curves.svg", "folded_radial_speed.svg")
    for figure in learning_figures:
        target = ROOT / "assets" / "figures" / figure
        if not target.is_file():
            errors.append(f"Missing new learning figure: {figure}")
            continue
        markup = target.read_text(encoding="utf-8")
        if "<svg" not in markup or "</svg>" not in markup or "<script" in markup.lower():
            errors.append(f"Invalid learning SVG: {figure}")
        for path_tag in re.findall(r"<path\b[^>]*?/?>", markup):
            if not re.search(r"\bfill\s*=", path_tag):
                errors.append(f"SVG path without explicit fill: {figure}")

    # The illustrated circle must have one independent two-function label per angle.
    circle_file = ROOT / "assets" / "figures" / "unit_circle_reference.svg"
    if circle_file.is_file():
        markup = circle_file.read_text(encoding="utf-8")
        cards = [int(n) for n in re.findall(r'<g class="angle-card" data-angle="(\d+)"', markup)]
        required_angles = (0, 30, 45, 60, 90, 120, 135, 150,
                           180, 210, 225, 240, 270, 300, 315, 330)
        if len(cards) != 16 or sorted(cards) != sorted(required_angles):
            errors.append("Unit circle must have 16 separate labeled angle cards")
        if markup.count('<polyline class="leader"') != 16:
            errors.append("Each unit-circle angle needs an individual point connector")

    for locale in LANGUAGES:
        trig = ROOT / "docs" / locale / "TRIGONOMETRY.md"
        note = ROOT / "docs" / locale / "notes" / "05-velocity-jacobian.md"
        for figure in ("unit_circle_reference.svg",
                       "arccos_reference_curve.svg"):
            if figure not in trig.read_text(encoding="utf-8"):
                errors.append(f"Missing trig visual {figure}: {locale}")
        trig_content = trig.read_text(encoding="utf-8")
        if trig_content.count("unit_circle_reference.svg") != 1:
            errors.append(f"Expected exactly one unit circle: {locale}")
        if trig_content.count("<a id=\"unit-circle-values\"></a>") != 1:
            errors.append(f"Missing main reference section: {locale}")
        if any(f"| {angle}° |" not in trig_content
               for angle in (0, 30, 45, 60, 90, 120, 135, 150,
                             180, 210, 225, 240, 270, 300, 315, 330)):
            errors.append(f"Incomplete 16-angle reference table: {locale}")

        reference_lines = trig_content.splitlines()
        header_index = next((i for i, line in enumerate(reference_lines)
                             if line.startswith("| θ |")), None)
        if header_index is None:
            errors.append(f"Missing consolidated reference table: {locale}")
        else:
            reference_table = []
            for line in reference_lines[header_index:]:
                if not line.startswith("|"):
                    break
                reference_table.append(line)
            if len(reference_table) != 18:
                errors.append(f"Expected header, separator and 16 reference rows: {locale}")
            if any(len(line.strip().strip("|").split("|")) != 8
                   for line in reference_table):
                errors.append(f"Expected eight separate trig reference columns: {locale}")
            for line in reference_table[2:]:
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) == 8:
                    for col_index in (2, 4):
                        if not re.fullmatch(r"-?\d+\.\d{4}", cells[col_index]):
                            errors.append(f"Invalid sine/cosine decimal: {locale}, {cells[0]}")
                    if cells[0] not in ("90°", "270°"):
                        if not re.fullmatch(r"-?\d+\.\d{4}", cells[6]):
                            errors.append(f"Invalid tangent decimal: {locale}, {cells[0]}")
                    elif cells[6] != "—":
                        errors.append(f"Undefined tangent must have an em dash: {locale}")

        for identity in (r"\cos(\theta-90^\circ)=\sin(\theta)",
                         r"\sin(\theta+90^\circ)=\cos(\theta)",
                         r"\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}"):
            if identity not in trig_content:
                errors.append(f"Missing trig identity {identity}: {locale}")
        if note.is_file():
            content = note.read_text(encoding="utf-8")
            if re.search(r"(?m)^\$$", content):
                errors.append(f"Broken single-dollar display math delimiter: {locale}")
            if r"\begin{bmatrix}" in content or r"\begin{aligned}" in content:
                errors.append(f"Unstable multiline matrix in velocity chapter: {locale}")
            if content.splitlines().count("$$") % 2 != 0:
                errors.append(f"Unbalanced display math delimiters: {locale}")
            if r"L\cdot\cos\bigl(Q(t)\bigr)" not in content:
                errors.append(f"Missing legible explicit cosine multiplication: {locale}")
            for section in range(1, 8):
                if f'id="section-{section}"' not in content:
                    errors.append(f"Missing velocity section {section}: {locale}")
            for figure in ("link_tangent_velocity.svg", "folded_displacement_curves.svg",
                           "folded_radial_speed.svg"):
                if figure not in content:
                    errors.append(f"Missing velocity visual {figure}: {locale}")
            for target_locale in LANGUAGES:
                if f"[{target_locale}](" not in content:
                    errors.append(f"Missing velocity language selector: {locale}/{target_locale}")
            if "L_1L_2\\sin(Q_2)" not in content:
                errors.append(f"Missing 2R Jacobian determinant: {locale}")

    # Discover the current maintained page set; all editions must provide
    # reciprocal same-page language links, including the ROS 2 chapter.
    localized_pages = (*REQUIRED, "DERIVATIVE_TABLE.md")
    for locale in LANGUAGES:
        for rel in localized_pages:
            current = ROOT / "docs" / locale / rel
            if not current.is_file():
                errors.append(f"Missing new-locale page: {locale}/{rel}")
                continue
            body = current.read_text(encoding="utf-8")
            for other in LANGUAGES:
                target = ROOT / "docs" / other / rel
                relative = __import__("os").path.relpath(
                    target, current.parent).replace("\\", "/")
                if f"[{other}]({relative})" not in body:
                    errors.append(
                        f"Missing new-locale same-page switch: {locale}/{rel} -> {other}")
            if rel == "README.md":
                for chapter in range(6):
                    names = ("00-calculus-foundations", "01-motion-calculus",
                             "02-first-order-dynamics", "03-feedback-control",
                             "04-coordinate-frames", "05-velocity-jacobian")
                    if f"notes/{names[chapter]}.md" not in body:
                        errors.append(f"Missing chapter index: {locale}/{names[chapter]}")
                for ref in ("INTEGRAL_TABLE.md", "DERIVATIVE_TABLE.md",
                            "TRIGONOMETRY.md", "SYMBOLS.md", "CHEATSHEET.md",
                            "SAFETY.md", "LICENSING.md", "exercises/README.md"):
                    if f"]({ref})" not in body:
                        errors.append(f"Missing reference index: {locale}/{ref}")
                if "> [!WARNING]" not in body:
                    errors.append(f"Missing warning: {locale}/README.md")
            if locale in ("ko", "fi") and rel == "INTEGRAL_TABLE.md":
                for example in ("14\\ \\mathrm{mm}", "0.01\\ \\mathrm{J}",
                                "\\ln2\\approx0.693"):
                    if example not in body:
                        errors.append(f"Missing solved integral example: {locale}/{example}")
            if rel == "SYMBOLS.md":
                for anchor in ("summation", "different-symbols",
                               "math-delimiters", "si-notation"):
                    if f'id="{anchor}"' not in body:
                        errors.append(f"Missing notation anchor: {locale}/{anchor}")
            if rel == "SAFETY.md" and "> [!CAUTION]" not in body:
                errors.append(f"Missing safety caution: {locale}")
            if rel == "LICENSING.md":
                if "Apache-2.0" not in body:
                    errors.append(f"Missing current license summary: {locale}/Apache-2.0")

    # Keep additional Korean/Finnish mathematical checks while their prose
    # editions remain condensed and need independent language review.
    for locale in ("ko", "fi"):
        trig = (ROOT / "docs" / locale / "TRIGONOMETRY.md").read_text(encoding="utf-8")
        for identity in (r"\cos(\theta-90^\circ)=\sin(\theta)",
                         r"\sin(\theta+90^\circ)=\cos(\theta)",
                         r"\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}"):
            if identity not in trig:
                errors.append(f"Missing Korean/Finnish trig identity {identity}: {locale}")
        for figure in ("unit_circle_reference.svg", "arccos_reference_curve.svg",
                       "trig_ratios.svg", "two_link_cosine_law.svg"):
            if figure not in trig:
                errors.append(f"Missing Korean/Finnish trig diagram {figure}: {locale}")
        for angle in (0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240,
                      270, 300, 315, 330):
            if f"| {angle}° |" not in trig:
                errors.append(f"Missing Korean/Finnish trig angle {angle}: {locale}")
        if trig.count('<a id="unit-circle-values"></a>') != 1:
            errors.append(f"Missing Korean/Finnish unit-circle anchor: {locale}")

    # Korean/Finnish editions must preserve every source teaching figure
    # and stable section links even before full prose parity is achieved.
    for locale in ("ko", "fi"):
        for chapter in range(6):
            names = ("00-calculus-foundations", "01-motion-calculus",
                     "02-first-order-dynamics", "03-feedback-control",
                     "04-coordinate-frames", "05-velocity-jacobian")
            filename = names[chapter] + ".md"
            original = (ROOT / "docs" / "en" / "notes" / filename).read_text(encoding="utf-8")
            translated = (ROOT / "docs" / locale / "notes" / filename).read_text(encoding="utf-8")
            figures = set(re.findall(r"figures/([a-z0-9_]+\\.svg)", original))
            for figure in figures:
                if f"figures/{figure}" not in translated:
                    errors.append(f"Missing teaching figure {figure}: {locale}/{filename}")
            sections = set(re.findall(r'<a id="(section-\\d+)"></a>', original))
            for section in sections:
                if f'<a id="{section}"></a>' not in translated:
                    errors.append(f"Missing source section anchor {section}: {locale}/{filename}")

    # Prevent orphaned duplicate inverse-tangent examples with inline $
    # delimiters after the law-of-cosines section.
    for locale in ("ko", "fi"):
        trig = (ROOT / "docs" / locale / "TRIGONOMETRY.md").read_text(encoding="utf-8")
        if any(line.startswith(chr(36) * 2) and line.strip() != chr(36) * 2
               for line in trig.splitlines()):
            errors.append(f"Inline display math delimiters: {locale}/TRIGONOMETRY.md")
        if not trig.count(r"\arctan(0.5)\approx0.46365\ \mathrm{rad}") == 1:
            errors.append(f"Missing correctly rendered radian arctangent example: {locale}")

    # Euler step count must be duration divided by duration, not 2/dt.
    for locale in ("en", "ko", "fi"):
        motion = (ROOT / "docs" / locale / "notes" / "01-motion-calculus.md").read_text(encoding="utf-8")
        if r"N=(2\ \mathrm{s})/dt" not in motion:
            errors.append(f"Missing dimensionally correct Euler step count: {locale}")
    for step, expected in ((.5, 3.), (.1, 3.8), (.01, 3.98)):
        n = round(2. / step)
        displacement = sum(2. * i * step * step for i in range(n))
        if not math.isclose(displacement, expected, abs_tol=1e-10):
            errors.append(f"Euler displacement calculation mismatch: dt={step}")

    # A translation must describe one 63.2 % response fraction, not
    # accidentally duplicate the percentage in its time-constant row.
    for locale in ("ko", "fi"):
        sheet = (ROOT / "docs" / locale / "CHEATSHEET.md").read_text(encoding="utf-8")
        row = next((line for line in sheet.splitlines() if line.startswith("| 시정수 |" if locale == "ko" else "| Aikavakio |")), "")
        if not row or row.count("63.2 %") != 1:
            errors.append(f"Incorrect time-constant percentage in {locale} cheat sheet")
        if "63.2 % muutoksesta" in row:
            errors.append("Duplicated percentage in Finnish time-constant row")

    # Separation by epsilon is undefined at zero error. All three
    # explanations must explicitly cover the constant-solution case.
    for locale in ("en", "ko", "fi"):
        dynamics = (ROOT / "docs" / locale / "notes" / "02-first-order-dynamics.md").read_text(encoding="utf-8")
        section = dynamics.split('<a id="time-constant-derivation"></a>')[-1]
        if r"$u=v_0$" not in section or r"$v(t)=u$" not in section:
            errors.append(f"Missing zero-error solution in first-order derivation: {locale}")
    for initial, target in ((10., 10.), (0., 10.)):
        for t in (0., 1., 2.):
            response = target + (initial-target)*math.exp(-t)
            if initial == target and response != target:
                errors.append("Zero-initial-error response must stay constant")

    # dr/dQ2 has a 1/r factor. Equal links folded at the base
    # produce a cusp in radial distance, not a valid 0/0 derivative.
    for locale in ("en", "ko", "fi"):
        jacobian = (ROOT / "docs" / locale / "notes" / "05-velocity-jacobian.md").read_text(encoding="utf-8")
        singularity = jacobian.split('<a id="section-5"></a>')[-1].split('<a id="section-6"></a>')[0]
        if not all(term in singularity for term in (r"$r>0$", r"$L_1=L_2$", r"$r=0$")):
            errors.append(f"Missing equal-link radius-derivative domain restriction: {locale}")
    link_length = 100.
    offset = 1e-4
    r_zero = math.hypot(link_length - link_length, 0.)
    r_plus = 2*link_length*abs(math.sin(offset/2))
    r_minus = 2*link_length*abs(math.sin(-offset/2))
    if not (r_zero == 0 and r_plus > r_zero and r_minus > r_zero
            and (r_plus-r_zero)/offset > 0
            and (r_zero-r_minus)/offset < 0):
        errors.append("Equal-link folded radial distance must have a cusp")

    # The zero-initial-speed exponential is a special case, not
    # the general first-order step response.
    for locale in ("en", "ko", "fi"):
        calculus = (ROOT / "docs" / locale / "notes" / "00-calculus-foundations.md").read_text(encoding="utf-8")
        section = calculus.split('<a id="section-5"></a>')[-1].split('<a id="section-6"></a>')[0]
        if r"\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau)" not in section:
            errors.append(f"Missing nonzero-initial-speed response: {locale}")
    for initial, target in ((0., 10.), (4., 10.), (10., 10.)):
        response_at_zero = target + (initial-target)*math.exp(0.)
        if not math.isclose(response_at_zero, initial, abs_tol=1e-12):
            errors.append("First-order response must reproduce its initial condition")

    # PID current commands must have consistent units: derivative of
    # speed error has rpm/s, so Kd needs A*s/rpm.
    for locale in ("en", "ko", "fi"):
        control = (ROOT / "docs" / locale / "notes" / "03-feedback-control.md").read_text(encoding="utf-8")
        derivative = control.split('<a id="section-4"></a>')[-1].split('<a id="section-5"></a>')[0]
        if r"[K_d]=\mathrm{A\cdot s/rpm}" not in derivative:
            errors.append(f"Missing PID derivative gain units: {locale}")
    kd = 0.0005  # A*s/rpm
    speed_change = 8.0  # rpm
    sample_period = 0.01  # s
    derivative_current = kd * speed_change / sample_period
    if not math.isclose(derivative_current, 0.4, abs_tol=1e-12):
        errors.append("PID derivative gain dimensional example mismatch")

    # Finnish mathematical derivations must not be translated as electrical wires.
    finnish_motion = (ROOT / "docs" / "fi" / "notes" / "01-motion-calculus.md").read_text(encoding="utf-8")
    if "Johdot, yksiköt" in finnish_motion or "Täydellinen johto yksikköineen" in finnish_motion:
        errors.append("Finnish calculus derivation mistranslated as electrical wire")
    if "Kaavojen johtaminen, yksiköt" not in finnish_motion or "Kaavan johtaminen yksikköineen" not in finnish_motion:
        errors.append("Finnish calculus derivation terminology missing")

    # The rotational torque law reuses u from a linear-speed example.
    # Both u and omega must be angular velocities for K(u-omega).
    for locale in ("en", "ko", "fi"):
        dynamics = (ROOT / "docs" / locale / "notes" / "02-first-order-dynamics.md").read_text(encoding="utf-8")
        section = dynamics.split('<a id="section-2"></a>')[-1].split('<a id="section-3"></a>')[0]
        if not all(term in section for term in (r"$u$", r"$\omega$", "rad/s", "mm/s")):
            errors.append(f"Missing rotational target velocity unit clarification: {locale}")
    # N*m*s/rad multiplied by rad/s must give N*m.
    torque_coefficient = 0.02  # N*m*s/rad
    angular_error = 5.0  # rad/s
    if not math.isclose(torque_coefficient * angular_error, 0.1, abs_tol=1e-12):
        errors.append("Angular torque gain dimensional example mismatch")

    # Protect the full arc-length -> average speed -> instantaneous speed
    # reasoning against partial translations and lost exact equalities.
    arc_derivation = (
        r"\Delta s=L\lvert\Delta Q\rvert",
        r"\Delta s_{\mathrm{signed}}=L\Delta Q",
        r"\overline{v}=\frac{\Delta s}{\Delta t}",
        r"\Delta t\to0",
        r"v=L\lvert\dot Q\rvert",
    )
    for locale in LANGUAGES:
        velocity = (ROOT / "docs" / locale / "notes" / "05-velocity-jacobian.md").read_text(encoding="utf-8")
        first = velocity.split('<a id="section-1"></a>')[-1].split('<a id="section-2"></a>')[0]
        if any(term not in first for term in arc_derivation) or "Δs≈LΔQ" in first:
            errors.append(f"Missing exact arc-to-speed derivation: {locale}")
    for angle in (-0.5, 0.5):
        radius = 150.
        arc_length = radius * abs(angle)
        signed_tangent = radius * angle
        if arc_length < 0 or not math.isclose(abs(signed_tangent), arc_length):
            errors.append("Arc length must equal absolute signed tangential displacement")

    # The numerical solver and exact model must agree at t=0 for
    # arbitrary initial speeds; invalid durations must still fail.
    solver_path = ROOT / "exercises" / "02_first_order_response.py"
    spec = importlib.util.spec_from_file_location("first_order_response", solver_path)
    solver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solver)
    for initial in (-5., 0., 7.):
        for target in (-10., 10.):
            exact = solver.exact_velocity(0., target, 2., initial)
            numerical = solver.euler_velocity(0., target, 2., 0.1, initial)
            if not math.isclose(exact, initial, abs_tol=1e-12) or numerical != initial:
                errors.append("Zero-duration Euler response must return initial velocity")
    try:
        solver.euler_velocity(-1., 10., 2., 0.1)
    except ValueError:
        pass
    else:
        errors.append("Negative Euler duration must be rejected")

    # The differentiation and integration examples intentionally use
    # different trajectories: x=2t² -> v=4t, versus v=2t -> x=t²+C.
    for locale in ("en", "ko", "fi"):
        motion = (ROOT / "docs" / locale / "notes" / "01-motion-calculus.md").read_text(encoding="utf-8")
        integral = motion.split('<a id="section-3"></a>')[-1].split('<a id="section-4"></a>')[0]
        if not all(expression in integral for expression in
                   (r"$x(t)=2t^2$", r"$v(t)=4t$", r"$v(t)=2t$", r"$x(t)=t^2+C$")):
            errors.append(f"Missing independent motion-example clarification: {locale}")
    for t in (0., 0.5, 2.):
        h = 1e-5
        differentiated = (2*(t+h)**2 - 2*(t-h)**2)/(2*h)
        integrated = ((t+h)**2 - (t-h)**2)/(2*h)
        if not math.isclose(differentiated, 4*t, abs_tol=1e-9):
            errors.append("Differentiation example mismatch")
        if not math.isclose(integrated, 2*t, abs_tol=1e-9):
            errors.append("Integration example mismatch")

    # GitHub's math renderer rejects \operatorname in these reference tables.
    # The course index must not mix an unordered item into its numbered TOC.
    for locale in LANGUAGES:
        derivative_table = (ROOT / "docs" / locale / "DERIVATIVE_TABLE.md").read_text(encoding="utf-8")
        if r"\operatorname{" in derivative_table:
            errors.append(f"Unsupported GitHub math operator in derivative table: {locale}")
        if r"\mathrm{arsinh}" not in derivative_table:
            errors.append(f"Missing renderable inverse hyperbolic sine in derivative table: {locale}")
        index = (ROOT / "docs" / locale / "README.md").read_text(encoding="utf-8")
        toc = index.split("INTEGRAL_TABLE.md)")[1].split("CHEATSHEET.md)")[0]
        if not re.search(r"(?m)^5\. \[.+\]\(DERIVATIVE_TABLE\.md\)$", toc):
            errors.append(f"Derivative table must be numbered item 5 in index: {locale}")
        if re.search(r"(?m)^-\s+\[.+\]\(DERIVATIVE_TABLE\.md\)$", toc):
            errors.append(f"Unexpected unordered derivative table entry: {locale}")
        numbered = [int(n) for n in re.findall(r"(?m)^(\d+)\. \[", index)]
        if numbered != list(range(1, len(numbered) + 1)):
            errors.append(f"Nonconsecutive numbered course index: {locale}")

    # The ROS 2 learning track must cover every supported language and
    # remain a self-contained, simulation-only addition to the course.
    for locale in LANGUAGES:
        chapter = ROOT / "docs" / locale / "notes" / "06-ros2-foundations.md"
        if not chapter.is_file():
            errors.append(f"Missing ROS 2 lesson: {locale}")
            continue
        body = chapter.read_text(encoding="utf-8")
        for i in range(1, 13):
            if body.count(f'<a id="section-{i}"></a>') != 1 or f'](#section-{i})' not in body:
                errors.append(f"Missing ROS 2 section or TOC link {i}: {locale}")
        for figure in ("ros2-topic-service.svg", "ros2-software-layers.svg"):
            if figure not in body:
                errors.append(f"Missing ROS 2 illustration {figure}: {locale}")
        for item in ("ros2_control", "tf2", "URDF", "QoS", "DDS",
                     "ros2 node list", "ros2 service call", "colcon",
                     "docker compose", "04-coordinate-frames.md", "05-velocity-jacobian.md"):
            if item not in body:
                errors.append(f"ROS 2 topic/command/link missing {item}: {locale}")
        toc = (ROOT / "docs" / locale / "README.md").read_text(encoding="utf-8")
        if not any(line.startswith("13. [") and line.endswith("](notes/06-ros2-foundations.md)") for line in toc.splitlines()):
            errors.append(f"Missing numbered ROS 2 course navigation: {locale}")
    for figure in ("ros2-topic-service.svg", "ros2-software-layers.svg"):
        try:
            markup = (ROOT / "assets" / "figures" / figure).read_text(encoding="utf-8")
            # Apply the same size, entity, and active-content checks used for
            # source-controlled SVGs before parsing the original example.
            unsafe = static_svg_issues(markup)
            if unsafe:
                errors.append(f"Unsafe ROS 2 SVG {figure}: {', '.join(unsafe)}")
                continue
            svg = ET.fromstring(markup)
            if not svg.tag.endswith("svg") or "viewBox" not in svg.attrib:
                errors.append(f"Malformed ROS 2 SVG: {figure}")
        except (OSError, ET.ParseError):
            errors.append(f"Unreadable ROS 2 SVG: {figure}")
    ros2 = ROOT / "ros2"
    for rel in ("README.md", "Dockerfile", "compose.yaml", "demo_pkg/package.xml",
                "demo_pkg/setup.py", "demo_pkg/setup.cfg", "demo_pkg/resource/telemetry_demo",
                "demo_pkg/launch/demo.launch.py", "demo_pkg/telemetry_demo/publisher.py",
                "demo_pkg/telemetry_demo/subscriber.py"):
        if not (ros2 / rel).is_file():
            errors.append(f"Missing ROS 2 demo asset: {rel}")

    # Independent numerical audit of the two-link worked examples. The
    # previous equation-parity check only proved the translations match;
    # it could not detect an error shared by the English original.
    def forward_2r(q1: float, q2: float, l1: float = 100., l2: float = 50.) -> tuple[float, float]:
        return (l1 * math.cos(q1) + l2 * math.cos(q1 + q2),
                l1 * math.sin(q1) + l2 * math.sin(q1 + q2))

    q1, q2 = math.radians(30), math.radians(60)
    x, y = forward_2r(q1, q2)
    if not (math.isclose(x, 86.6025403784, abs_tol=1e-8)
            and math.isclose(y, 100., abs_tol=1e-8)):
        errors.append("Forward-kinematics worked example fails independent calculation")

    l1, l2, radius = 100., 50., 120.
    cosine_elbow = (radius**2 - l1**2 - l2**2) / (2 * l1 * l2)
    if not (math.isclose(cosine_elbow, .19, abs_tol=1e-12)
            and math.isclose(math.degrees(math.acos(cosine_elbow)), 79.05, abs_tol=.01)):
        errors.append("Cosine-rule worked example has incorrect elbow angle")

    # Compare analytic Jacobian against centered finite differences at a
    # nonsingular pose, then verify the displayed velocity example.
    h = 1e-6
    j11 = (forward_2r(q1 + h, q2)[0] - forward_2r(q1 - h, q2)[0]) / (2*h)
    j12 = (forward_2r(q1, q2 + h)[0] - forward_2r(q1, q2 - h)[0]) / (2*h)
    j21 = (forward_2r(q1 + h, q2)[1] - forward_2r(q1 - h, q2)[1]) / (2*h)
    j22 = (forward_2r(q1, q2 + h)[1] - forward_2r(q1, q2 - h)[1]) / (2*h)
    analytic = (-l1*math.sin(q1)-l2*math.sin(q1+q2),
                -l2*math.sin(q1+q2),
                l1*math.cos(q1)+l2*math.cos(q1+q2),
                l2*math.cos(q1+q2))
    if not all(math.isclose(a, b, abs_tol=1e-7)
               for a, b in zip((j11, j12, j21, j22), analytic)):
        errors.append("Analytic Jacobian disagrees with numerical derivatives")
    vx, vy = j11*.1+j12*.2, j21*.1+j22*.2
    if not (math.isclose(vx, -20., abs_tol=1e-7)
            and math.isclose(vy, 8.66025403784, abs_tol=1e-7)):
        errors.append("Two-joint velocity worked example fails independent calculation")

    # Check the subtle distinction between fixed-axis displacement and
    # radial change near a folded singularity (25 vs 50 mm/rad²).
    delta = .02
    longitudinal = l2 * (1 - math.cos(delta))
    transverse = l2 * math.sin(delta)
    radial = math.hypot(l1 - l2 * math.cos(delta), l2 * math.sin(delta)) - (l1-l2)
    if not (math.isclose(longitudinal, .010, abs_tol=2e-6)
            and math.isclose(transverse, 1., abs_tol=1e-4)
            and math.isclose(radial, .020, abs_tol=1e-5)):
        errors.append("Folded-link displacement example fails independent calculation")

    # Confirm the worked numerical conclusions remain present in each
    # edition, not merely the shared symbolic display equations.
    for locale in ("en", "ko", "fi"):
        frames = (ROOT / "docs" / locale / "notes" / "04-coordinate-frames.md").read_text(encoding="utf-8")
        velocity = (ROOT / "docs" / locale / "notes" / "05-velocity-jacobian.md").read_text(encoding="utf-8")
        for value in ("86.60", "100", "0.19", "79.05"):
            if value not in frames:
                errors.append(f"Missing coordinate-frame worked result {value}: {locale}")
        for value in ("-20", "8.66", "0.010", "1.000", "0.020"):
            if value not in velocity.replace("−", "-"):
                errors.append(f"Missing Jacobian worked result {value}: {locale}")

    # Anti-windup is a conditional integration/back-calculation strategy,
    # not simply a promise that the integral term itself never saturates.
    ko_feedback = (ROOT / "docs" / "ko" / "notes" / "03-feedback-control.md").read_text(encoding="utf-8")
    ko_antiwindup = ko_feedback.split('<a id="section-5"></a>', 1)[-1].split('<a id="section-6"></a>', 1)[0]
    if "**안티 와인드업(anti-windup)**" not in ko_antiwindup:
        errors.append("Korean anti-windup definition missing from section 5")
    if ko_feedback.rstrip().endswith("적분 누적을 제한합니다."):
        errors.append("Orphaned Korean anti-windup glossary remains after final section")

    # Inline code must render, rather than showing literal backslashes
    # before backticks. Keep English glossary terms at the definition,
    # not appended as an orphan paragraph after the worked examples.
    for locale in ("ko", "fi"):
        dynamics = (ROOT / "docs" / locale / "notes" / "02-first-order-dynamics.md").read_text(encoding="utf-8")
        if chr(92) + chr(96) in dynamics:
            errors.append(f"Escaped backticks prevent inline code rendering: {locale}/02")
        if locale == "ko":
            if "- **시정수(time constant)**" not in dynamics:
                errors.append("Missing time-constant glossary at Korean definition")
        else:
            if "- **Aikavakio (time constant)**" not in dynamics:
                errors.append("Missing time-constant glossary at Finnish definition")
        if r"\mathrm{kg\cdot m^2}" in dynamics:
            errors.append(f"Malformed inertia SI unit markup: {locale}/02")

    # Equation-level parity: compare display equations after whitespace
    # normalization, preserving every mathematical operator and coefficient.
    # Chapters 01/02 contain deliberately localized math-text labels or
    # combined equations, so check their invariant numeric derivations below.
    def display_equations(body: str) -> list[str]:
        return [re.sub(r"\s+", "", match.group(1))
                for match in re.finditer(r"\$\$([\s\S]*?)\$\$", body)]

    invariant_chapters = (
        "00-calculus-foundations.md",
        "03-feedback-control.md",
        "04-coordinate-frames.md",
        "05-velocity-jacobian.md",
    )
    for chapter in invariant_chapters:
        original = (ROOT / "docs" / "en" / "notes" / chapter).read_text(encoding="utf-8")
        expected = display_equations(original)
        for locale in ("ko", "fi"):
            localized = (ROOT / "docs" / locale / "notes" / chapter).read_text(encoding="utf-8")
            actual = display_equations(localized)
            if actual != expected:
                errors.append(
                    f"Display equation parity mismatch: {locale}/{chapter}; "
                    f"English={len(expected)}, localized={len(actual)}")

    # Numerically significant equations in chapters with localized labels
    # must survive translation even when display-block layout differs.
    math_invariants = {
        "01-motion-calculus.md": (
            r"\sum_{n=0}^{N-1}", r"(4-2h)\ \mathrm{mm}",
            "motion-values-derivation",
        ),
        "02-first-order-dynamics.md": (
            r"\frac{dv}{dt}=\frac{u-v}{\tau}",
            r"\tau=\frac{J}{K}", r"\varepsilon(t)=u-v(t)",
            r"\exp\!\left(-\frac{t}{\tau}\right)",
            r"6.5132", r"6.3397", r"6.3212",
        ),
    }
    for chapter, invariants in math_invariants.items():
        for locale in ("ko", "fi"):
            localized = (ROOT / "docs" / locale / "notes" / chapter).read_text(encoding="utf-8")
            for invariant in invariants:
                if invariant not in localized:
                    errors.append(
                        f"Missing translated mathematical invariant: {locale}/{chapter}: {invariant}")

    # Keep the teaching triangles one-third smaller as rendered by default.
    triangles = (ROOT / "assets" / "figures" / "trig_ratios.svg").read_text(encoding="utf-8")
    if 'width="480" height="856"' not in triangles or 'viewBox="0 0 720 1284"' not in triangles:
        errors.append("Right-triangle SVG must render at 2/3 original size")

    # Require the full illustrated coordinate-frames course in every locale.
    geometry_figures = ("world_local_frames.svg", "two_link_fk.svg",
                        "two_link_elbow_solutions.svg", "two_link_workspace.svg")
    for figure in geometry_figures:
        target = ROOT / "assets" / "figures" / figure
        if not target.is_file():
            errors.append(f"Missing geometry figure: {figure}")
            continue
        markup = target.read_text(encoding="utf-8")
        if "<svg" not in markup or "</svg>" not in markup or "<script" in markup.lower():
            errors.append(f"Invalid SVG figure: {figure}")
        for path_tag in re.findall(r"<path\\b[^>]*?/>", markup):
            if not re.search(r"\bfill\s*=", path_tag):
                errors.append(f"Missing explicit fill on SVG path: {figure}")
    for locale in LANGUAGES:
        lesson = ROOT / "docs" / locale / "notes" / "04-coordinate-frames.md"
        if not lesson.is_file():
            errors.append(f"Missing coordinate frames lesson: {locale}")
            continue
        markup = lesson.read_text(encoding="utf-8")
        for index in range(1, 8):
            if f'id="section-{index}"' not in markup:
                errors.append(f"Missing coordinates section {index}: {locale}")
        for index in range(1, 7):
            if f'id="worked-{index}"' not in markup:
                errors.append(f"Missing coordinates solved example {index}: {locale}")
        for figure in geometry_figures:
            if f"../../../assets/figures/{figure}" not in markup:
                errors.append(f"Missing coordinates illustration {figure}: {locale}")
        for other in LANGUAGES:
            if f"[{other}](" not in markup:
                errors.append(f"Missing coordinates language switch {other}: {locale}")
        for formula in (
            r"x_w=t_x+x_l\cos\theta-y_l\sin\theta",
            r"X=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2)",
            r"T_{WS}=T_{WT}T_{TS}",
            "0.19", "86.60",
        ):
            if formula not in markup:
                errors.append(f"Missing coordinates formula/result {formula}: {locale}")
        if "{{" in markup or "<script" in markup.lower():
            errors.append(f"Unresolved or unsafe coordinate lesson: {locale}")

    paths = sorted(repository_markdown_files())
    seen_locales = {p.name for p in (ROOT / "docs").iterdir() if p.is_dir()}
    if "en" not in seen_locales:
        errors.append("Missing canonical English locale: docs/en")
    root_index = (ROOT / "README.md").read_text(encoding="utf-8")
    indexed_locales = set(re.findall(r"\]\(docs/([^/)]+)/README\.md\)", root_index))
    if indexed_locales != seen_locales:
        errors.append(f"Root language index/directory mismatch: "
                      f"unindexed={seen_locales - indexed_locales}, "
                      f"orphaned={indexed_locales - seen_locales}")

    for locale in LANGUAGES:
        derivative = ROOT / "docs" / locale / "DERIVATIVE_TABLE.md"
        if not derivative.is_file():
            errors.append(f"Missing derivative table: {locale}")
        else:
            content = derivative.read_text(encoding="utf-8")
            for formula in (r"\frac{u'v-uv'}{v^2}", r"\arctan(u)", r"\mathrm{arsinh}(u)", r"24x(3x^2+1)^3"):
                if formula not in content:
                    errors.append(f"Missing derivative formula/example: {locale}: {formula}")
    # Preserve every formula in the two principal reference tables. Compare
    # math-bearing table cells, not translated prose in adjacent columns.
    def reference_formulas(body: str, column: int) -> list[str]:
        formulas = []
        for line in body.splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) <= column:
                continue
            math = re.findall(r"\$([^$]+)\$", cells[column])
            if math:
                formulas.append(" ".join(re.sub(r"\s+", "", item) for item in math))
        return formulas

    for reference, formula_column in (
        ("DERIVATIVE_TABLE.md", 1),
        ("INTEGRAL_TABLE.md", 0),
    ):
        english = (ROOT / "docs" / "en" / reference).read_text(encoding="utf-8")
        expected = reference_formulas(english, formula_column)
        for locale in ("ko", "fi"):
            translated = (ROOT / "docs" / locale / reference).read_text(encoding="utf-8")
            actual = reference_formulas(translated, formula_column)
            if actual != expected:
                mismatch = next((i for i, (a, b) in enumerate(zip(expected, actual))
                                 if a != b), min(len(expected), len(actual)))
                errors.append(
                    f"Reference formula mismatch: {locale}/{reference} at row {mismatch+1}; "
                    f"English rows={len(expected)}, translated rows={len(actual)}")

    # Display equations must use $ on their own lines. A single-dollar
    # standalone line is not a display delimiter and breaks math rendering.
    for locale in ("ko", "fi"):
        for reference in ("DERIVATIVE_TABLE.md", "INTEGRAL_TABLE.md"):
            body = (ROOT / "docs" / locale / reference).read_text(encoding="utf-8")
            if any(line.strip() == chr(36) for line in body.splitlines()):
                errors.append(f"Malformed standalone math delimiter: {locale}/{reference}")

    # Prevent translated derivative examples from silently losing the
    # numeric result or rendering as invalid single-dollar display blocks.
    for locale in ("ko", "fi"):
        derivative = (ROOT / "docs" / locale / "DERIVATIVE_TABLE.md").read_text(encoding="utf-8")
        if derivative.splitlines().count(chr(36) * 2) != 8:
            errors.append(f"Expected four valid derivative display equations: {locale}")
        if r"$11\ \mathrm{mm/s}$" not in derivative:
            errors.append(f"Corrupted derivative velocity result (11 mm/s): {locale}")
        if f"(notes/00-calculus-foundations.md)" not in derivative:
            errors.append(f"Derivative reference points to outdated English-only calculus: {locale}")

    for locale in ("ko", "fi"):
        integral = ROOT / "docs" / locale / "INTEGRAL_TABLE.md"
        if not integral.is_file():
            errors.append(f"Missing new integral table: {locale}")
        else:
            content = integral.read_text(encoding="utf-8")
            if content.count("| $\\int") != 20:
                errors.append(f"Expected 20 integrals: {locale}")
            if any(f'id="section-{n}"' not in content for n in range(1, 7)):
                errors.append(f"Missing integral section anchors: {locale}")

    for locale in ("ko", "fi"):
        if not (ROOT / "docs" / locale / "README.md").is_file():
            errors.append(f"Missing new language index: {locale}")

    for required in ("MAINTENANCE.md", "WRITING_STYLE.md", "CONTRIBUTING.md", "CHANGELOG.md", ".github/workflows/validate.yml", "tools/generate_figures.py", "tools/generate_calculus_figure.py"):
        if not (ROOT / required).is_file():
            errors.append(f"Missing self-contained continuity or verification file: {required}")
    for fig in ("first_order_response.svg", "euler_vs_exact.svg", "control_loop.svg", "calculus_slope_area.svg"):
        p = ROOT / "assets" / "figures" / fig
        if not p.is_file():
            errors.append(f"Missing original visualization: {fig}")
        else:
            content = p.read_text(encoding="utf-8")
            if "<svg" not in content or re.search(r"<script\b", content, re.I):
                errors.append(f"Invalid or unsafe SVG visualization: {fig}")

    # New calculus reference must be complete and mirrored in each locale.
    for lang in LANGUAGES:
        base = ROOT / "docs" / lang
        primer = (base / "notes" / "00-calculus-foundations.md").read_text(encoding="utf-8")
        table = (base / "INTEGRAL_TABLE.md").read_text(encoding="utf-8")
        index = (base / "README.md").read_text(encoding="utf-8")
        if table.count("| $\\int") != 20:
            errors.append(f"Expected 20 integration reference entries: {lang}")
        if primer.count('id="section-') != 8 or table.count('id="section-') != 6:
            errors.append(f"Missing stable calculus section anchors: {lang}")
        for p in ("notes/00-calculus-foundations.md", "INTEGRAL_TABLE.md", "TRIGONOMETRY.md", "notes/03-feedback-control.md"):
            if p not in index:
                errors.append(f"Missing calculus index link to {p}: {lang}")
        for other in LANGUAGES:
            if any(f"[{other}](" not in page for page in (primer, table, (base / "TRIGONOMETRY.md").read_text(encoding="utf-8"), (base / "notes/03-feedback-control.md").read_text(encoding="utf-8"))):
                errors.append(f"Missing calculus language switch to {other}: {lang}")
        if "3136\\pi" not in primer or "14\\ \\mathrm{mm}" not in primer:
            errors.append(f"Missing verified sphere/integral numerical example: {lang}")
        trig = (base / "TRIGONOMETRY.md").read_text(encoding="utf-8")
        control = (base / "notes/03-feedback-control.md").read_text(encoding="utf-8")
        if any(key not in primer for key in (r"\lim_{h\to0}", r"\frac{d^2x}", r"\ln(0.1)", r"\int_0^{0.01", r"\frac{dE}{dt}")):
            errors.append(f"Missing revised practical calculus examples: {lang}")
        if any(key not in trig for key in ("| 0° |", "| 30° |", "| 45° |", "| 60° |", "| 90° |", r"\arctan(0.5)", "0.4905")):
            errors.append(f"Missing trigonometric values or applied examples: {lang}")
        if len([line for line in trig.splitlines() if line.startswith("| ") and line.split(" | ", 1)[0] in ("| 0°", "| 30°", "| 45°", "| 60°", "| 90°", "| 120°", "| 135°", "| 150°", "| 180°", "| 210°", "| 225°", "| 240°", "| 270°", "| 300°", "| 315°", "| 330°")]) != 16:
            errors.append(f"Expected sixteen trig angle rows: {lang}")
        if control.count('id="section-') != 7 or any(key not in control for key in (r"K_t", "windup", "0.26", "mgL")):
            # The localized prose may translate 'sampling period'; the mathematical content is invariant.
            if control.count('id="section-') != 7 or any(key not in control for key in (r"K_t", "windup", "0.26", "mgL")):
                errors.append(f"Missing feedback-control sequence: {lang}")
        if "calculus_slope_area.svg" not in primer:
            errors.append(f"Missing calculus diagram link: {lang}")
        for condition in (r"n\ne-1", r"a>0", r"\lvert x\rvert<a"):
            if condition not in table:
                errors.append(f"Missing formula domain guard {condition}: {lang}")
    # Calculus numerical examples are independently reproducible with standard Python.
    if not math.isclose(4*math.pi*10**2*1, 400*math.pi):
        errors.append("Incorrect volume growth example for r=10")
    if not math.isclose(4*math.pi*14**2*4, 3136*math.pi):
        errors.append("Incorrect time-dependent sphere example")

    # Numeric examples in the prose must agree with their defining equations.
    expected_fraction = (0.63212056, 0.86466472, 0.95021293)
    for n, expected in enumerate(expected_fraction, start=1):
        if not math.isclose(1-math.exp(-n), expected, abs_tol=1e-8):
            errors.append(f"Incorrect analytical time-constant example for n={n}")

    # Enforce clarity: error and Euler's number must not share an ambiguous symbol.
    for lang in LANGUAGES:
        chapter = (ROOT / "docs" / lang / "notes" / "02-first-order-dynamics.md").read_text(encoding="utf-8")
        cheat = (ROOT / "docs" / lang / "CHEATSHEET.md").read_text(encoding="utf-8")
        guide = (ROOT / "docs" / lang / "exercises" / "README.md").read_text(encoding="utf-8")
        if r"\varepsilon(t)" not in chapter or r"\exp" not in chapter:
            errors.append(f"Math notation not synchronized: {lang}")
        if r"e(t)=u-v(t)" in chapter or r"e^{-t/\tau}" in chapter:
            errors.append(f"Ambiguous speed error versus Euler number: {lang}")
        if chapter.count('id="time-constant-derivation"') != 1:
            errors.append(f"Repeated or missing time constant proof: {lang}")
        if r"\varepsilon(t)" not in cheat or r"\exp" not in cheat:
            errors.append(f"Cheat sheet not synchronized: {lang}")
        if any(name in guide for name in ("../../../web/python-runner.html", "pyodide.org")):
            errors.append(f"Discontinued browser execution link in {lang} exercise guide")
        for required in (
            "https://www.python.org/downloads/",
            "https://docs.python.org/3/library/venv.html",
            "https://packaging.python.org/en/latest/tutorials/installing-packages/",
            "python3 exercises/01_motion_and_integral.py",
        ):
            if required not in guide:
                errors.append(f"Missing official/local Python guidance {lang}: {required}")
        for file in ("01_motion_and_integral.py", "02_first_order_response.py", "03_rotation_energy.py"):
            if f"../../../exercises/{file}" not in guide:
                errors.append(f"Missing linked runnable source {file} in {lang}")
        for chapter_path in ("notes/01-motion-calculus.md", "notes/02-first-order-dynamics.md", "CHEATSHEET.md"):
            item = (ROOT / "docs" / lang / chapter_path).read_text(encoding="utf-8")
            for line in item.splitlines():
                if line.startswith("**") and "(distance traveled)" in line and line.count("(") >= 6:
                    errors.append(f"Unscannable inline glossary in {lang}/{chapter_path}")
                if line.startswith("**") and "(first-order system)" in line and line.count("(") >= 6:
                    errors.append(f"Unscannable inline glossary in {lang}/{chapter_path}")
    # The discontinued browser runner and generator must not be reintroduced.
    for retired in ("web/python-runner.html", "tools/generate_browser_runner.py"):
        if (ROOT / retired).exists():
            errors.append(f"Retired browser execution component still present: {retired}")
    for doc in repository_markdown_files():
        if doc.name != "CHANGELOG.md" and any(term in doc.read_text(encoding="utf-8")
                for term in ("web/python-runner.html", "tools/generate_browser_runner.py")):
            errors.append(f"Obsolete browser runner reference: {doc.relative_to(ROOT)}")
    notebook = ROOT / "notebooks" / "first_order_response.ipynb"
    if not notebook.is_file():
        errors.append("Missing standalone notebook")
    else:
        try:
            import json
            data = json.loads(notebook.read_text(encoding="utf-8"))
            if data.get("nbformat") != 4 or not data.get("cells"):
                errors.append("Invalid notebook format")
            else:
                for idx, cell in enumerate(data["cells"]):
                    if cell.get("cell_type") == "code":
                        compile("".join(cell.get("source", [])), f"notebook cell {idx}", "exec")
        except (ValueError, SyntaxError) as exc:
            errors.append(f"Notebook invalid: {exc}")
    dependencies = ROOT / "requirements.txt"
    if not dependencies.is_file():
        errors.append("Missing standard requirements.txt")
    else:
        declared = dependencies.read_text(encoding="utf-8")
        # Validate bounded package ranges and Python-version markers rather than
        # hard-coding exact old lower bounds after every Dependabot upgrade.
        specification = re.compile(
            r'^(numpy|matplotlib|jupyterlab)>=(\d+(?:\.\d+)*),<(\d+)'
            r'(?:; python_version (>=|<) "(\d+\.\d+)")?$'
        )
        declared_lines = [
            line.strip() for line in declared.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        parsed = []
        for line in declared_lines:
            match = specification.fullmatch(line)
            if match is None:
                errors.append(f"Invalid/unbounded Python dependency: {line}")
            else:
                parsed.append(match.groups())

        for version in ((3, 10), (3, 11), (3, 12)):
            required_packages = (
                (("numpy", "3"),) if version == (3, 10)
                else (("numpy", "3"), ("matplotlib", "4"), ("jupyterlab", "5"))
            )
            for name, major in required_packages:
                active = []
                for spec in parsed:
                    package, lower, upper, operator, marker = spec
                    if package != name:
                        continue
                    if marker is not None:
                        target_version = tuple(map(int, marker.split(".")))
                        if not (version >= target_version if operator == ">="
                                else version < target_version):
                            continue
                    active.append(spec)
                if len(active) != 1 or active[0][2] != major:
                    errors.append(f"Missing unique bounded {name} for Python {version}")
                if version == (3, 10) and active and name == "numpy":
                    minimum = tuple(map(int, active[0][1].split(".")))
                    if minimum >= (2, 5):
                        errors.append("NumPy minimum excludes Python 3.10")
    if (ROOT / "requirements-plot.txt").exists():
        errors.append("Deprecated requirements-plot.txt still present")
    for page in ROOT.rglob("*.md"):
        body = page.read_text(encoding="utf-8")
        if "requirements-plot.txt" in body and page.name != "CHANGELOG.md":
            errors.append(f"Stale dependency filename in {page.relative_to(ROOT)}")
    for lang in LANGUAGES:
        guide = (ROOT / "docs" / lang / "exercises" / "README.md").read_text(encoding="utf-8")
        for required in ('requirements.txt', 'python3 -m venv .venv',
                         'py -3 -m venv .venv', 'python3 exercises/02_first_order_response.py',
                         'python3 exercises/03_rotation_energy.py'):
            if required not in guide:
                errors.append(f"Missing local Python setup convention for {lang}: {required}")
    if (ROOT / 'README.md').read_text(encoding='utf-8').count('**Language code or country code?**') != 1:
        errors.append('Repeated language-code explanation in root README')

    # Keep the publication-wide mathematical number/unit style uniform.
    # Decimal point is an editorial choice (both dot and comma are accepted by BIPM).
    # Look at localized instructional pages, not examples of what NOT to write
    # in the root maintainer guidelines.
    for lang in LANGUAGES:
        locale = ROOT / "docs" / lang
        symbols = (locale / "SYMBOLS.md").read_text(encoding="utf-8")
        if 'id="si-notation"' not in symbols or '](#si-notation)' not in symbols:
            errors.append(f"Missing localized SI-notation guide: {lang}")
        for page in sorted(locale.rglob('*.md')):
            body = non_code(page.read_text(encoding="utf-8"))
            if re.search(r"(?<=\d),(?=\d)|\d\{,\}\d", body):
                errors.append(f"Decimal comma instead of decimal point: {page.relative_to(ROOT)}")
            # The narrow LaTeX spacing command appeared as a literal comma
            # in user-facing screenshots. Use an explicit space in this course.
            if r"\," in body:
                errors.append(f"Ambiguous LaTeX narrow-space command: {page.relative_to(ROOT)}")
            # Ignore inline code examples where incorrect notation is shown on purpose.
            ordinary = re.sub(r"`[^`\n]*`", "", body)
            if re.search(r"\b(?:mm|m|kg|N|s)\s+/\s+(?:s|m|mm|kg|rad)\b", ordinary):
                errors.append(f"Spaces adjacent to unit slash: {page.relative_to(ROOT)}")
        motion = (locale / "notes" / "01-motion-calculus.md").read_text(encoding="utf-8")
        if r"\mathrm{d}t" not in motion:
            errors.append(f"Missing upright differential in integral: {lang}")
        if "motion-values-derivation" not in motion or r"(4-2h)\ \mathrm{mm}" not in motion:
            errors.append(f"Missing explicit SI displacement derivation: {lang}")
        if "../SYMBOLS.md#si-notation" not in motion:
            errors.append(f"Motion lesson lacks localized SI-notation link: {lang}")

    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if root_readme.count('**Language code or country code?**') != 1:
        errors.append('Repeated or missing standard language-code explanation')
    if 'docs/en/SYMBOLS.md#si-notation' not in root_readme:
        errors.append('Missing SI style link in root README')

    # A copied localized page must allow a single-click switch to that exact page in every language.
    locale_pages = ("README.md", "CHEATSHEET.md", "SYMBOLS.md", "INTEGRAL_TABLE.md", "TRIGONOMETRY.md", "SAFETY.md", "LICENSING.md", "notes/00-calculus-foundations.md", "notes/01-motion-calculus.md", "notes/02-first-order-dynamics.md", "notes/03-feedback-control.md", "notes/06-ros2-foundations.md", "exercises/README.md")
    for lang in LANGUAGES:
        for rel in locale_pages:
            current = ROOT / "docs" / lang / rel
            if not current.is_file():
                errors.append(f"Missing localized page: {current.relative_to(ROOT)}")
                continue
            body = current.read_text(encoding="utf-8")
            for other in LANGUAGES:
                target = ROOT / "docs" / other / rel
                relative = __import__("os").path.relpath(target, current.parent).replace("\\", "/")
                if f"[{other}]({relative})" not in body:
                    errors.append(f"Missing same-page language switch: {lang}/{rel} -> {other}")
            if rel == "notes/01-motion-calculus.md" and r"\sum_{n=0}^{N-1}" in body and "../SYMBOLS.md#summation" not in body:
                errors.append(f"Sigma symbol not linked to explanation: {lang}")
    for lang in LANGUAGES:
        d = ROOT / "docs" / lang
        for file in REQUIRED:
            if not (d / file).is_file():
                errors.append(f"Missing locale file: {lang}/{file}")
        readme = (d / "README.md").read_text()
        if '> [!WARNING]' not in readme:
            errors.append(f"Missing prominent disclaimer: {lang}/README.md")
        cheat = (d / "CHEATSHEET.md").read_text(encoding='utf-8')
        if r'\lvert v(t)\rvert' not in cheat:
            errors.append(f"Unsafe table formula for path length: {lang}/CHEATSHEET.md")
        if lang == "zh" and r'\text{平均速率}' not in (d / "notes" / "01-motion-calculus.md").read_text():
            errors.append("Chinese formula labels are not localized")
        if lang == "ja" and r'\text{平均の速さ}' not in (d / "notes" / "01-motion-calculus.md").read_text():
            errors.append("Japanese formula labels are not localized")
        if '](SAFETY.md)' not in readme or '](LICENSING.md)' not in readme:
            errors.append(f"Safety/licensing localization links: {lang}/README.md")
        for chapter, count in (("01-motion-calculus.md", 6), ("02-first-order-dynamics.md", 7)):
            content = (d / "notes" / chapter).read_text()
            for i in range(1, count + 1):
                if f'id="section-{i}"' not in content or f'](#section-{i})' not in content:
                    errors.append(f"Missing or unlinked TOC anchor section {i} in {lang}/{chapter}")
            for anchor in (("power-rule-derivation", "motion-values-derivation") if chapter.startswith('01') else ("time-constant-derivation", "euler-values-derivation")):
                if f'id="{anchor}"' not in content or f'](#{anchor})' not in content:
                    errors.append(f"Missing explanation link or appendix {anchor}: {lang}/{chapter}")
            required_figure = "euler_vs_exact.svg" if chapter.startswith('01') else "first_order_response.svg"
            if required_figure not in content:
                errors.append(f"Missing graph {required_figure}: {lang}/{chapter}")
            if lang != "en" and ('(time constant)' not in content and chapter.startswith('02')):
                errors.append(f"Missing English term beside localized definition in {lang}/{chapter}")
            if lang != "en" and ('(velocity)' not in content and chapter.startswith('01')):
                errors.append(f"Missing English speed/velocity terms in {lang}/{chapter}")

    if '> [!CAUTION]' not in (ROOT / 'README.md').read_text():
        errors.append('Missing prominent disclaimer in root README')

    for path in paths:
        text = path.read_text(encoding='utf-8')
        # Count pipes across GFM table rows. Raw | inside $...$ breaks table cells.
        active_table = None
        for line_no, line in enumerate(non_code(text).splitlines(), start=1):
            if TABLE_ROW.match(line):
                count = len(re.findall(r"(?<!\\)\|", line))
                if active_table is not None and active_table != count:
                    errors.append(f"Markdown table column mismatch {path.relative_to(ROOT)}:{line_no}: {count} pipes vs {active_table}")
                active_table = count
                if len(re.findall(r"(?<!\\)\$", line)) % 2:
                    errors.append(f"Unpaired inline math dollar in table {path.relative_to(ROOT)}:{line_no}")
            else:
                active_table = None
        if len(re.findall(r"(?m)^\s*\$\$\s*$", non_code(text))) % 2:
            errors.append(f"Unclosed display math block {path.relative_to(ROOT)}")
        if re.search(r"\\mathrm\{\{", text):
            errors.append(f"Double-braced LaTeX unit formatting {path.relative_to(ROOT)}")
        link_prose = markdown_prose(text)
        for img in IMAGE_LINK.finditer(link_prose):
            target = img.group(2)
            if target.startswith(("http:", "https:")):
                errors.append(f"External image without stored license review {path.relative_to(ROOT)}: {target}")
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                errors.append(f"Missing relative image {path.relative_to(ROOT)}: {target}")
        for m in re.finditer(r"\[([^]\n]*)\]\([^)]*\)", link_prose):
            if "$" in m.group(1):
                errors.append(f"Raw dollar math delimiters inside link label: {path.relative_to(ROOT)}")
        for m in MARKDOWN_LINK.finditer(link_prose):
            raw = m.group(1)
            if raw.startswith(('http:', 'https:', 'mailto:', '#')):
                if raw.startswith('#') and unquote(raw[1:]) not in markdown_anchor_ids(text):
                    errors.append(f"Unknown fragment {raw} in {path.relative_to(ROOT)}")
                continue
            rel, _, fragment = unquote(raw).partition('#')
            resolved = (path.parent / rel).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"Link escapes repository {path.relative_to(ROOT)}: {raw}")
                continue
            if not resolved.is_file():
                errors.append(f"Broken link {path.relative_to(ROOT)}: {raw}")
                continue
            if fragment and fragment not in markdown_anchor_ids(resolved.read_text(encoding="utf-8")):
                errors.append(f"Missing linked fragment {path.relative_to(ROOT)}: {raw}")
            # Learning pages must point to learning pages in the *same* language.
            if 'docs' in path.parts:
                lang = path.relative_to(ROOT).parts[1]
                if resolved.suffix == '.md' and 'docs' in resolved.relative_to(ROOT).parts:
                    targetparts = resolved.relative_to(ROOT).parts
                    if targetparts[1] != lang:
                        # Same-page locale switches are intentionally cross-language.
                        original_parts = path.relative_to(ROOT).parts
                        same_page_other_locale = (targetparts[2:] == original_parts[2:]
                                                  and targetparts[1] in (*LANGUAGES, "ko", "fi"))
                        pending_translation_fallback = (lang in ("ko", "fi")
                            and targetparts[1] == "en"
                            and "English" in text)
                        if not same_page_other_locale and not pending_translation_fallback:
                            errors.append(f"Unexpected cross-language learning link {path.relative_to(ROOT)}: {raw}")
    # Scan non-Markdown source, config, generated HTML and original SVG assets
    # as well as the Markdown above. This checks repository text only, not
    # GitHub commit author metadata or untracked binary files.
    for path in repository_privacy_files():
        text = path.read_text(encoding="utf-8")
        # Example.invalid is the explicitly synthetic ROS package maintainer.
        if any(not address.lower().endswith("@example.invalid")
               for address in EMAIL.findall(text)):
            errors.append(f"Possible personal email in {path.relative_to(ROOT)}")
    # Check every source-controlled SVG, not only the selected six figures
    # above. A local viewer may interpret active markup differently from GitHub.
    for path in sorted((ROOT / "assets" / "figures").rglob("*.svg")):
        markup = path.read_text(encoding="utf-8")
        for issue in static_svg_issues(markup):
            errors.append(f"{issue}: {path.relative_to(ROOT)}")
    for path in repository_markdown_files():
        for issue in active_markdown_issues(path.read_text(encoding="utf-8")):
            errors.append(f"{issue}: {path.relative_to(ROOT)}")
    return errors


if __name__ == '__main__':
    problems = check()
    if problems:
        print('\n'.join('ERROR: '+e for e in problems))
        raise SystemExit(1)
    print(f'Validated {len(LANGUAGES)} localized editions, all internal Markdown links, '
          'chapter TOCs, disclaimers, and content privacy patterns.')
