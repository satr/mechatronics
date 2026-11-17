"""Validate that local Python installations are not interpreted as course files."""
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "training_validator", ROOT / "tools" / "validate_repository.py"
)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidatorScopeTests(unittest.TestCase):
    def test_project_markdown_is_scanned(self):
        for relative in ("README.md", "docs/en/README.md",
                         "docs/ru/notes/06-ros2-foundations.md",
                         "MAINTENANCE.md"):
            with self.subTest(relative=relative):
                self.assertTrue(validator.is_project_markdown(ROOT / relative))

    def test_untracked_dependencies_and_build_outputs_are_ignored(self):
        for directory in (".venv", "venv", "build", "install", "log",
                          "node_modules", ".tox", "__pycache__"):
            with self.subTest(directory=directory):
                self.assertFalse(validator.is_project_markdown(
                    ROOT / directory / "dependencies" / "README.md"
                ))

    def test_privacy_scan_covers_source_code_and_original_assets(self):
        for relative in ("README.md", "ros2/Dockerfile",
                         "ros2/demo_pkg/telemetry_demo/publisher.py",
                         "ros2/compose.yaml", "assets/figures/ros2-topic-service.svg",
                         "tools/check_executable_sources.py", "notebooks/first_order_response.ipynb"):
            with self.subTest(relative=relative):
                self.assertTrue(validator.is_privacy_scannable(ROOT / relative))
        self.assertFalse(validator.is_privacy_scannable(
            ROOT / ".venv" / "lib" / "site-packages" / "package.py"
        ))

    def test_privacy_validator_scans_its_own_source(self):
        self.assertTrue(validator.is_privacy_scannable(
            ROOT / "tools" / "validate_repository.py"
        ))
        source = (ROOT / "tools" / "validate_repository.py").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('if path.name == "validate_repository.py":', source)
        self.assertNotIn("banned_terms", source)

    def test_release_documentation_is_not_duplicated(self):
        guide = (ROOT / "WRITING_STYLE.md").read_text(encoding="utf-8")
        self.assertEqual(guide.count("# Writing for understanding"), 1)
        self.assertNotIn("all twelve editions", guide)
        self.assertIn("balanced `$...$` delimiters", guide)
        self.assertIn("balanced `$$` delimiters", guide)
        self.assertNotIn("$...# Writing for understanding", guide)
        self.assertIn(".idea/", (ROOT / ".gitignore").read_text(encoding="utf-8"))
        root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Apache License 2.0", root_readme)
        self.assertNotIn("PolyForm Noncommercial", root_readme)

    def test_first_order_derivation_explains_equilibrium_in_all_locales(self):
        for lang in validator.LANGUAGES:
            with self.subTest(lang=lang):
                text = (ROOT / "docs" / lang / "notes" /
                        "02-first-order-dynamics.md").read_text(encoding="utf-8")
                self.assertIn("$u=v_0$", text)
                self.assertIn("$v(t)=u$", text)

    def test_calculus_foundations_define_euler_and_worked_answers(self):
        for lang in validator.LANGUAGES:
            with self.subTest(lang=lang):
                text = (ROOT / "docs" / lang / "notes" /
                        "00-calculus-foundations.md").read_text(encoding="utf-8")
                for required in (
                    r"\exp(x)=\mathrm{e}^{x}",
                    "2.71828",
                    "../SYMBOLS.md",
                    r"v(3\ \mathrm{s})=2+2\cdot3=8",
                    r"\tau\ln(10)",
                    r"\int_0^{2\ \mathrm{s}}",
                ):
                    self.assertIn(required, text)

    def test_github_heading_and_custom_anchors(self):
        body = (
            "# Introduction\n"
            "## Read in your language\n"
            "## Read in your language\n"
            "### A `code` example\n"
            "## This'll be a _Helpful_ Section!\n"
            "<a id=\"stable-anchor\"></a>\n"
            "<a name=\"legacy-name\"></a>\n"
            "```md\n# Not a heading\n```\n"
        )
        self.assertEqual(
            validator.markdown_anchor_ids(body),
            {"introduction", "read-in-your-language", "read-in-your-language-1",
             "a-code-example", "thisll-be-a-helpful-section", "stable-anchor",
             "legacy-name"},
        )

    def test_static_markup_checker_handles_source_without_rendering(self):
        safe_markdown = (
            '<a id="stable-anchor"></a>\n'
            '\x60literal <script> in inline code\x60\n'
            '\x60\x60\x60html\n<iframe src="example">\n\x60\x60\x60\n'
        )
        self.assertEqual(validator.active_markdown_issues(safe_markdown), [])
        self.assertEqual(validator.active_markdown_issues(
            '<a id="section-1"></a>\n'
            '[official guide](https://docs.python.org/3/)\n'
            '![locally stored diagram](../assets/figures/example.svg)\n'), [])
        self.assertEqual(validator.active_markdown_issues(
            '[guide][official]\n'
            '[official]: <https://docs.python.org/3/>\n'
            '![diagram][figure]\n'
            '[figure]: ../../assets/figures/example.svg\n'
            '`[fake]: data:image/svg+xml,example`\n'), [])
        for sample in (
            "<script>text</script>",
            '<iframe src="elsewhere"></iframe>',
            '<img src="https://example.invalid/a.svg">',
            '<video src="https://example.invalid/sample"></video>',
            '<audio src="https://example.invalid/sample"></audio>',
            '<span onload="handler()">text</span>',
            '<a href="https://example.invalid">raw HTML link</a>',
            '<span style="background: red">colored text</span>',
            "[open](javascript:example)",
            "[open](data:image/svg+xml,example)",
            "[open](file:///tmp/example)",
            "![image](data:image/svg+xml,example)",
            "[page][ref]\n[ref]: data:image/svg+xml,example\n",
            "![diagram][asset]\n[asset]: <file:///tmp/picture>\n",
            "[manual][doc]\n[doc]: blob:example\n",
            "<data:image/svg+xml,example>",
        ):
            with self.subTest(sample=sample):
                self.assertTrue(validator.active_markdown_issues(sample))

        safe_svg = (
            '<svg xmlns="http://www.w3.org/2000/svg"><defs>'
            '<clipPath id="c"><rect width="1" height="1"/></clipPath>'
            '</defs><g style="clip-path:url(#c)"><use href="#c"/></g></svg>'
        )
        self.assertEqual(validator.static_svg_issues(safe_svg), [])
        self.assertEqual(
            validator.static_svg_issues(
                '<?xml version="1.0" encoding="utf-8"?>' + safe_svg),
            [])
        for source in (
            '<svg xmlns="http://www.w3.org/2000/svg"><script/></svg>',
            '<svg xmlns="http://www.w3.org/2000/svg" onload="example()"/>',
            '<svg xmlns="http://www.w3.org/2000/svg"><image href="https://example.invalid/pic"/></svg>',
            '<svg xmlns="http://www.w3.org/2000/svg"><g style="fill:url(https://example.invalid/x)"/></svg>',
            '<!DOCTYPE svg SYSTEM "https://example.invalid/test.dtd"><svg/>',
            '<?xml-stylesheet href="https://example.invalid/x" type="text/xsl"?>'
            '<svg xmlns="http://www.w3.org/2000/svg"/>',
            '<?custom instruction="example"?><svg/>',
        ):
            with self.subTest(source=source):
                self.assertTrue(validator.static_svg_issues(source))

    def test_all_maintained_static_content_passes_markup_check(self):
        for path in sorted((ROOT / "assets" / "figures").rglob("*.svg")):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertEqual([], validator.static_svg_issues(
                    path.read_text(encoding="utf-8")))
        for path in validator.repository_markdown_files():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertEqual([], validator.active_markdown_issues(
                    path.read_text(encoding="utf-8")))

    def test_link_validation_ignores_inline_code_but_not_real_links(self):
        text = (
            "`[example](not-an-existing-file.md)`\n"
            "``![also-code](missing-image.svg)``\n"
            "```markdown\n[hidden](another-missing-file.md)\n```\n"
            "[real](../assets/figures/example.svg)\n"
            "![actual image](../assets/figures/example.svg)\n"
        )
        parsed = validator.markdown_prose(text)
        self.assertNotIn("not-an-existing-file.md", parsed)
        self.assertNotIn("missing-image.svg", parsed)
        self.assertNotIn("another-missing-file.md", parsed)
        self.assertIn("[real](../assets/figures/example.svg)", parsed)
        self.assertIn("![actual image](../assets/figures/example.svg)", parsed)
        self.assertEqual(
            [m.group(1) for m in validator.MARKDOWN_LINK.finditer(parsed)],
            ["../assets/figures/example.svg"])
        self.assertEqual(
            [m.group(2) for m in validator.IMAGE_LINK.finditer(parsed)],
            ["../assets/figures/example.svg"])

    def test_browser_runner_is_removed_and_no_longer_linked(self):
        self.assertFalse((ROOT / "web" / "python-runner.html").exists())
        self.assertFalse((ROOT / "tools" / "generate_browser_runner.py").exists())
        for doc in validator.repository_markdown_files():
            if doc.name == "CHANGELOG.md":  # Historical change log entries.
                continue
            with self.subTest(path=str(doc.relative_to(ROOT))):
                text = doc.read_text(encoding="utf-8")
                self.assertNotIn("web/python-runner.html", text)
                self.assertNotIn("tools/generate_browser_runner.py", text)

    def test_local_python_docs_reference_official_guides(self):
        for locale in validator.LANGUAGES:
            with self.subTest(locale=locale):
                doc = (ROOT / "docs" / locale / "exercises" / "README.md").read_text(
                    encoding="utf-8"
                )
                for expected in (
                    "https://www.python.org/downloads/",
                    "https://docs.python.org/3/library/venv.html",
                    "https://packaging.python.org/en/latest/tutorials/installing-packages/",
                    "python3 exercises/01_motion_and_integral.py",
                    "py -3 -m venv .venv",
                ):
                    self.assertIn(expected, doc)

    def test_locale_discovery_matches_existing_directories(self):
        self.assertEqual(set(validator.LANGUAGES),
                         {p.name for p in (ROOT / "docs").iterdir() if p.is_dir()})


if __name__ == "__main__":
    unittest.main()
