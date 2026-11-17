"""Regression tests for the conservative executable-example AST policy."""
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "executable_source_policy", ROOT / "tools" / "check_executable_sources.py"
)
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class ExecutableExampleSecurityTests(unittest.TestCase):
    def test_actual_published_examples_match_policy(self):
        self.assertEqual([], policy.check())

    def test_accidental_dangerous_source_is_rejected_without_running_it(self):
        source_path = ROOT / "exercises" / "new_example.py"
        suspicious_sources = (
            "import os\n",
            "from subprocess import run\n",
            "from math import *\n",
            "eval('2 + 2')\n",
            "exec('pass')\n",
            "__import__('os')\n",
            "getattr(object, '__class__')\n",
            "value.__class__\n",
            "value.__dict__\n",
            "value.__init__()\n",
            "open('private.txt').read()\n",
            "import math\nmath.__dict__\n",
            "x = obj.system('example')\n",
        )
        for source in suspicious_sources:
            with self.subTest(source=source):
                self.assertTrue(policy.audit_source(source, source_path))

    def test_allowlisted_plotting_packages_cannot_read_or_write_files(self):
        path = ROOT / "exercises" / "plot_notebook.py"
        # The policy parses these strings as data only. None of the
        # file operations are executed by this test.
        sources = (
            "import numpy as np\nnp.load('sample.npy')\n",
            "import numpy as np\nnp.save('sample.npy', [1])\n",
            "import numpy as np\nnp.loadtxt('sample.csv')\n",
            "import numpy as np\nnp.savetxt('sample.csv', [1])\n",
            "import numpy as np\nnp.memmap('sample.bin')\n",
            "import numpy as np\nnp.fromfile('sample.bin')\n",
            "import numpy as np\nnp.array([1]).tofile('sample.bin')\n",
            "import matplotlib.pyplot as plt\nplt.imread('image.png')\n",
            "import matplotlib.pyplot as plt\nplt.savefig('plot.svg')\n",
            "import matplotlib.pyplot as plt\nplt.imsave('image.png', [])\n",
            "import numpy as np\nnp.lib.format.open_memmap('image.dat')\n",
        )
        for source in sources:
            with self.subTest(source=source):
                self.assertTrue(
                    any("prohibited attribute" in finding for finding
                        in policy.audit_source(source, path)))
        for source in (
            "import math\nprint(math.exp(-1))\n",
            "import numpy as np\nt = np.linspace(0, 1, 11)\n",
            "import matplotlib.pyplot as plt\nplt.plot([0, 1], [0, 1])\nplt.show()\n",
        ):
            with self.subTest(allowed=source):
                self.assertEqual([], policy.audit_source(source, path))

    def test_from_import_cannot_hide_forbidden_scientific_file_apis(self):
        path = ROOT / "exercises" / "numerical_example.py"
        suspicious = (
            "from numpy import load\nload('sample.npy')\n",
            "from numpy import load as reader\nreader('sample.npy')\n",
            "from numpy import savez as export\nexport('sample.npz')\n",
            "from numpy import fromfile as read_input\n",
            "from matplotlib.pyplot import savefig as write_plot\n",
            "from matplotlib.pyplot import imread\n",
            "from math import __dict__ as exposed\n",
        )
        for source in suspicious:
            with self.subTest(source=source):
                errors = policy.audit_source(source, path)
                self.assertTrue(any("prohibited from-import symbol" in e
                                    for e in errors), errors)

        for source in (
            "from math import exp, log\nresult = exp(-1) + log(2)\n",
            "from numpy import linspace as grid\nvalues = grid(0, 1, 5)\n",
            "from matplotlib.pyplot import plot as draw\ndraw([1, 2])\n",
        ):
            with self.subTest(allowed=source):
                self.assertEqual([], policy.audit_source(source, path))

    def test_super_constructor_is_allowed_but_direct_dunder_access_is_not(self):
        path = ROOT / "ros2" / "demo_pkg" / "telemetry_demo" / "publisher.py"
        self.assertEqual([], policy.audit_source(
            "class Example:\n    def __init__(self):\n        super().__init__()\n", path
        ))

    def test_allowed_minimal_examples(self):
        cases = (
            (ROOT / "exercises" / "math_example.py",
             "import math\nprint(math.sqrt(9))\n"),
            (ROOT / "ros2" / "demo_pkg" / "launch" / "demo.launch.py",
             "from launch import LaunchDescription\n"),
            (ROOT / "ros2" / "demo_pkg" / "setup.py",
             "from setuptools import setup\nsetup(name='example')\n"),
        )
        for path, source in cases:
            with self.subTest(path=str(path)):
                self.assertEqual([], policy.audit_source(source, path))

    def test_new_executable_files_are_in_discovery_scope(self):
        relative = {p.relative_to(ROOT).as_posix() for p in policy.audited_files()}
        self.assertIn("exercises/01_motion_and_integral.py", relative)
        self.assertIn("exercises/plot_models.py", relative)
        self.assertEqual(policy.EXERCISE_IMPORTS,
                         policy.allowed_imports(ROOT / "exercises" / "nested" / "new.py"))
        self.assertIn("ros2/demo_pkg/setup.py", relative)
        self.assertIn("ros2/demo_pkg/launch/demo.launch.py", relative)


if __name__ == "__main__":
    unittest.main()
