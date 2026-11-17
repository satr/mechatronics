"""Pure-math regression tests for the introductory calculus examples."""
import math
import unittest

class CalculusExamples(unittest.TestCase):
    def test_power_rule(self):
        dt = 1e-5
        position = lambda t: 3 * t*t
        measured = (position(2+dt)-position(2-dt))/(2*dt)
        self.assertAlmostEqual(measured, 12.0, places=7)

    def test_sphere_chain_rule(self):
        r = 10.0
        dr_dt = 1.0
        dV_dt = 4 * math.pi * r*r * dr_dt
        self.assertAlmostEqual(dV_dt, 1256.6370614359173)
        self.assertAlmostEqual(4 * math.pi * 14**2 * 4, 3136 * math.pi)

    def test_definite_integral_velocity(self):
        v0, a, duration = 4, 2, 3
        dx = v0*duration + a*duration**2/2
        self.assertEqual(dx, 21)
        self.assertEqual(3*3**2-3*0**2, 27)

    def test_antiderivative(self):
        dt=1e-5
        F=lambda t:2*t**3
        self.assertAlmostEqual((F(2+dt)-F(2-dt))/(2*dt), 6*2**2, places=7)

if __name__ == "__main__":
    unittest.main()
