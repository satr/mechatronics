"""Offline numerical correctness checks for synthetic models."""
import importlib
import math
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "exercises"))
motion = importlib.import_module("01_motion_and_integral")
response = importlib.import_module("02_first_order_response")
energy = importlib.import_module("03_rotation_energy")


class NumericalTests(unittest.TestCase):
    def test_derivative(self):
        self.assertAlmostEqual(motion.forward_derivative(1, 0.01), 4.02)
        self.assertAlmostEqual(motion.forward_derivative(1, 0.1), 4.2)

    def test_finite_difference_rejects_unresolved_steps(self):
        # float(1) + 1e-17 equals 1: the old formula silently returned zero.
        with self.assertRaisesRegex(ValueError, "time resolution"):
            motion.forward_derivative(1.0, 1e-17)
        # Here time changes but x=2*t**2 underflows at both endpoints.
        with self.assertRaisesRegex(ValueError, "position difference"):
            motion.forward_derivative(1e-200, 1e-200)
        # A truly zero secant across symmetric x(t)=2*t**2 is legitimate.
        self.assertEqual(motion.forward_derivative(-0.5, 1.0), 0.0)
        self.assertAlmostEqual(motion.forward_derivative(1.0, 0.01), 4.02)

    def test_integration(self):
        self.assertAlmostEqual(motion.euler_displacement(2, 0.5), 3.0)
        self.assertAlmostEqual(motion.euler_displacement(2, 0.1), 3.8)
        self.assertAlmostEqual(motion.euler_displacement(2, 0.01), 3.98)
        self.assertAlmostEqual(motion.trapezoid_displacement(2, 0.5), 4.0)

    def test_time_constant(self):
        self.assertEqual(response.time_constant(2, 1), 2)
        self.assertEqual(response.time_constant(4, 2), 2)
        self.assertEqual(response.time_constant(1, 2), 0.5)

    def test_equal_response_for_equal_tau(self):
        self.assertEqual(response.euler_velocity(1, 10, 2, 0.01),
                         response.euler_velocity(1, 10, response.time_constant(4, 2), 0.01))

    def test_euler_convergence(self):
        exact = response.exact_velocity(1, 10, 1)
        coarse = response.euler_velocity(1, 10, 1, 0.1)
        fine = response.euler_velocity(1, 10, 1, 0.01)
        self.assertAlmostEqual(exact, 10 * (1 - math.exp(-1)))
        self.assertLess(abs(fine - exact), abs(coarse - exact))

    def test_euler_convex_step_avoids_false_overflow(self):
        # Both endpoints and the Euler update stay finite even though the
        # naive intermediate target - result would overflow to infinity.
        high, low = 1e308, -1e308
        actual = response.euler_velocity(1, high, 1, 0.1, initial=low)
        expected_fraction = 1.0 - 2.0 * (0.9 ** 10)
        self.assertTrue(math.isfinite(actual))
        self.assertTrue(math.isclose(actual / high, expected_fraction,
                                     rel_tol=1e-12, abs_tol=0.0))
        self.assertEqual(response.euler_velocity(1, high, 1, 0.5,
                                                 initial=low), 5e307)
        self.assertEqual(response.euler_velocity(1, low, 1, 0.5,
                                                 initial=high), -5e307)
        self.assertEqual(response.euler_velocity(1, high, 1, 1,
                                                 initial=low), high)
        # With dt > tau, the method can overshoot; preserve this behavior.
        self.assertAlmostEqual(response.euler_velocity(3, 10, 1, 1.5),
                               7.5)

    def test_euler_extreme_underflowed_fraction_and_overshoot(self):
        # dt/tau rounds to zero, but a tiny finite step can remain
        # representable when multiplied by a large target.
        self.assertEqual(
            response.euler_velocity(1e-300, 1e308, 1e308, 1e-300),
            1e-300)
        # Opposite finite endpoints previously produced an infinite
        # intermediate subtraction; the actual update is unchanged at
        # the resolution of the large starting value.
        self.assertEqual(
            response.euler_velocity(1e-300, 1e308, 1e308, 1e-300,
                                    initial=-1e308),
            -1e308)
        # A step beyond tau can overshoot without itself overflowing.
        self.assertTrue(math.isclose(
            response.euler_velocity(1.1, 1e308, 1.0, 1.1,
                                    initial=-1e308),
            1.2e308, rel_tol=1e-15))
        # Equal large endpoints are still a fixed point even for
        # an amplifying Euler step: do not introduce inf-inf.
        self.assertEqual(
            response.euler_velocity(1.1, 1e308, 1.0, 1.1,
                                    initial=1e308),
            1e308)

    def test_overshooting_euler_avoids_false_intermediate_product_overflow(self):
        # The Euler step is 2e300, but (1e300 * 1e308) overflows before
        # the old implementation divides by tau=5e307.
        self.assertEqual(
            response.euler_velocity(1e308, 1e300, 5e307, 1e308),
            2e300)
        self.assertEqual(
            response.euler_velocity(1e308, -1e300, 5e307, 1e308),
            -2e300)
        # Preserve behavior when dt/tau itself is not representable
        # but scaling the tiny difference before division is valid.
        self.assertEqual(
            response.euler_velocity(1e308, 5e-324, 1e-100, 1e308),
            4.940656458412465e-324 * 1e308 / 1e-100)

    def test_energy_scaling(self):
        self.assertEqual(energy.rotational_energy(2, 10), 100)
        self.assertEqual(energy.rotational_energy(4, 10), 200)
        self.assertEqual(energy.rotational_energy(2, 20), 400)

    def test_subnormal_inertia_does_not_falsely_zero_finite_energy(self):
        # Half of the smallest subnormal float rounds to zero. The energy
        # itself can nevertheless be a clearly representable finite number.
        tiny = math.ulp(0.0)
        omega = 1e154
        expected = (tiny * omega) * (0.5 * omega)
        self.assertGreater(expected, 0.0)
        for signed in (omega, -omega):
            actual = energy.rotational_energy(tiny, signed)
            self.assertTrue(math.isclose(actual, expected, rel_tol=1e-12,
                                         abs_tol=0.0))
        # Also avoid large relative errors from halving an odd subnormal.
        self.assertTrue(math.isclose(
            energy.rotational_energy(3 * tiny, omega), 3 * expected,
            rel_tol=1e-12, abs_tol=0.0))
        # Retain the original normal-magnitude calculation and range limit.
        self.assertTrue(math.isclose(
            energy.rotational_energy(1e308, 1.8), 1.62e308, rel_tol=1e-12))
        with self.assertRaisesRegex(ValueError, "energy exceeds"):
            energy.rotational_energy(1e308, 2.0)

    def test_tau_estimation_from_precise_samples(self):
        self.assertEqual(response.estimate_tau([(0, 0), (1, 393.5), (2, 632.2), (3, 777.0)], 0, 1000), 2)

    def test_tau_estimation_from_rounded_samples(self):
        samples = [(0, 0), (1, 393), (2, 632), (3, 777)]
        self.assertEqual(response.estimate_tau(samples, 0, 1000, resolution=1), 2)

    def test_tau_estimation_rejects_unresolved_sensor_step(self):
        # A 10 rpm response cannot have a meaningful 63.2% estimate when
        # its display resolution is 10 or 100 rpm. The old implementation
        # sometimes reported tau=0 from the initial sample alone.
        samples = [(0, 0), (1, 3), (2, 6), (3, 10)]
        for resolution in (10, 100):
            with self.subTest(resolution=resolution):
                with self.assertRaisesRegex(ValueError, "smaller than step"):
                    response.estimate_tau(samples, 0, 10, resolution)
                with self.assertRaisesRegex(ValueError, "smaller than step"):
                    response.estimate_tau(
                        [(0, 10), (1, 7), (2, 4), (3, 0)],
                        10, 0, resolution)
        # A sufficiently fine resolution still allows the first crossing
        # to be reported as a sample-limited estimate.
        self.assertEqual(response.estimate_tau(
            samples, 0, 10, resolution=1), 2)
        # Finite extreme opposite endpoints may have an infinite difference;
        # the comparison should not reject their valid finite resolution.
        self.assertEqual(response.estimate_tau(
            [(0, -1e308), (1, 1e308)], -1e308, 1e308,
            resolution=1.0), 1)

    def test_tau_samples_validate_complete_ordered_data(self):
        # An early threshold crossing must not hide invalid later samples.
        for samples in (
            [(0, 0), (2, 700), (1, 750)],
            [(0, 0), (2, 700), (2, 760)],
            [(0, 0), (2, 700), (3, float("nan"))],
            [(0, 0), (2, 700), (3, float("inf"))],
            [(0, 0), (2, 700), (-1, 730)],
        ):
            with self.subTest(samples=samples), self.assertRaises(ValueError):
                response.estimate_tau(samples, 0, 1000)
        self.assertEqual(
            response.estimate_tau([(0, 0), (1, 393), (2, 632),
                                   (3, 777)], 0, 1000, resolution=1), 2)
        self.assertEqual(
            response.estimate_tau([(0, 1000), (1, 607), (2, 368),
                                   (3, 223)], 1000, 0, resolution=1), 2)
        self.assertIsNone(response.estimate_tau([(0, 0), (1, 300)], 0, 1000))
        self.assertIsNone(response.estimate_tau([], 0, 1000))

    def test_tau_sample_count_is_bounded(self):
        from unittest.mock import patch
        with patch.object(response, "MAX_STEPS", 3):
            with self.assertRaisesRegex(ValueError, "sample sequence exceeds"):
                response.estimate_tau(
                    [(0, 0), (1, 400), (2, 700), (3, 900)], 0, 1000)

    def test_extreme_finite_input_behavior(self):
        # Intermediate subtraction of 1e308 - (-1e308) would overflow, but
        # a convex interpolation for the exact first-order response is finite.
        target, initial = 1e308, -1e308
        result = response.exact_velocity(1, target, 1, initial)
        expected = math.exp(-1) * initial - math.expm1(-1) * target
        self.assertTrue(math.isfinite(result))
        self.assertAlmostEqual(result / 1e308, expected / 1e308)
        self.assertEqual(response.exact_velocity(0, target, 1, initial), initial)
        self.assertEqual(response.exact_velocity(1e308, target, 1e-308, initial), target)
        self.assertEqual(response.estimate_tau([(0, initial), (2, target)],
                                               initial, target), 2)
        for call in (
            lambda: motion.position(1e308),
            lambda: motion.velocity(1e308),
            lambda: motion.forward_derivative(1e154, 1e-308),
            lambda: motion.trapezoid_displacement(1e308, 1e308),
        ):
            with self.assertRaises(ValueError):
                call()

    def test_nonfinite_inputs_and_bounded_loop_counts(self):
        nonfinite = (float("nan"), float("inf"), float("-inf"))
        for bad in nonfinite:
            with self.subTest(bad=repr(bad)):
                for call in (
                    lambda: motion.forward_derivative(1, bad),
                    lambda: motion.forward_derivative(bad, 0.1),
                    lambda: motion.euler_displacement(2, bad),
                    lambda: motion.trapezoid_displacement(bad, 0.1),
                    lambda: response.time_constant(bad, 1),
                    lambda: response.time_constant(1, bad),
                    lambda: response.exact_velocity(bad, 10, 1),
                    lambda: response.exact_velocity(1, bad, 1),
                    lambda: response.euler_velocity(1, 10, bad, 0.1),
                    lambda: response.euler_velocity(1, 10, 1, bad),
                    lambda: response.estimate_tau([(0, 0)], 0, 100, resolution=bad),
                    lambda: response.estimate_tau([(0, bad)], 0, 100),
                    lambda: energy.rotational_energy(bad, 10),
                    lambda: energy.rotational_energy(1, bad),
                ):
                    with self.assertRaises(ValueError):
                        call()
        with self.assertRaisesRegex(ValueError, "exceeds"):
            motion.euler_displacement(2, 1e-12)
        with self.assertRaisesRegex(ValueError, "exceeds"):
            motion.trapezoid_displacement(2, 1e-12)
        with self.assertRaisesRegex(ValueError, "exceeds"):
            response.euler_velocity(1, 10, 1, 1e-12)
        with self.assertRaises(ValueError):
            response.time_constant(1e308, 1e-308)
        with self.assertRaises(ValueError):
            energy.rotational_energy(1e308, 1e308)
        self.assertEqual(response.euler_velocity(0, 10, 1, 0.1), 0.0)
        self.assertEqual(energy.rotational_energy(0, 1.0), 0.0)

    def test_small_durations_reject_noninteger_step_count(self):
        # Before this regression, abs(n*dt-duration) <= 1e-9 accepted
        # 2 * 6e-11 s as if it exactly equalled 1e-10 s.
        for call in (
            lambda: motion.euler_displacement(1e-10, 6e-11),
            lambda: motion.trapezoid_displacement(1e-10, 6e-11),
            lambda: response.euler_velocity(1e-10, 10, 1e-9, 6e-11),
        ):
            with self.assertRaisesRegex(ValueError, "integer multiple"):
                call()

        # Exact small ratios must still be usable without widening tolerance.
        self.assertTrue(math.isclose(
            motion.euler_displacement(1e-10, 5e-11), 5e-21,
            rel_tol=1e-12, abs_tol=0.0))
        self.assertTrue(math.isclose(
            motion.trapezoid_displacement(1e-10, 5e-11), 1e-20,
            rel_tol=1e-12, abs_tol=0.0))
        self.assertAlmostEqual(
            response.euler_velocity(1e-10, 10, 1e-9, 5e-11), 0.975)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            response.time_constant(0, 1)
        with self.assertRaises(ValueError):
            motion.euler_displacement(2, 0)


if __name__ == "__main__":
    unittest.main()