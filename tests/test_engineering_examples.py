"""Pure standard-library regression tests for mechanical calculus and feedback examples.

These are mathematical examples only; no physical hardware is accessed.
"""
import math
import unittest


class PracticalCalculus(unittest.TestCase):
    def test_derivative_limit_and_first_order(self):
        a = 2.0   # mm/s² in x=a*t²
        t = 1.0   # s
        for h in (0.1, 0.01, 0.001):
            secant = (a * (t + h)**2 - a * t**2) / h
            self.assertAlmostEqual(secant, a * (2*t+h))
        self.assertAlmostEqual(2*a*t, 4.0)

    def test_position_speed_acceleration(self):
        pos = lambda t: 2 + 3*t + 2*t*t   # mm with t in s
        vel = lambda t: 3 + 4*t           # mm/s
        self.assertEqual(pos(2), 16)
        self.assertEqual(vel(2), 11)
        self.assertAlmostEqual((vel(2.001)-vel(1.999)) / 0.002, 4)

    def test_flywheel_power_from_chain_rule(self):
        inertia, speed, accel = 0.01, 10.0, 2.0
        torque = inertia*accel
        self.assertAlmostEqual(torque, 0.02)
        self.assertAlmostEqual(torque*speed, 0.2)

    def test_logarithm_response_90_percent(self):
        tau = 0.5
        time = -tau * math.log(0.1)
        self.assertAlmostEqual(time, 1.151292546497023)
        self.assertAlmostEqual(1-math.exp(-time/tau), 0.9)

    def test_axis_displacement_and_spring_work(self):
        self.assertEqual(3*2+2*2**2, 14)     # mm
        self.assertEqual(2+14, 16)           # mm absolute position
        stiffness, extension = 200, 0.01
        self.assertAlmostEqual(stiffness*extension**2/2, 0.01)  # J
        self.assertNotAlmostEqual((stiffness*extension)*extension, 0.01)

    def test_trigonometry_and_gravity_lever(self):
        for degrees, s, c in [
            (0, 0, 1), (30, 0.5, math.sqrt(3)/2),
            (45, math.sqrt(2)/2, math.sqrt(2)/2),
            (60, math.sqrt(3)/2, 0.5), (90, 1, 0)]:
            theta=math.radians(degrees)
            self.assertAlmostEqual(math.sin(theta), s)
            self.assertAlmostEqual(math.cos(theta), c)
            if degrees != 90:
                self.assertAlmostEqual(math.degrees(math.atan(math.tan(theta))),degrees)
        self.assertAlmostEqual(0.5*9.81*0.2*math.cos(math.radians(60)),0.4905)
        self.assertAlmostEqual(math.degrees(math.atan(0.05/0.1)),26.56505117707799)

    def test_integral_state_persists(self):
        z=0.0
        out=[]
        for rpm in [950,950,950,1000,1020,1020]:
            error=1000-rpm
            z+=error*1.0
            out.append((z,0.002*z))
        self.assertEqual([x[0] for x in out],[50,100,150,150,130,110])
        for (_,actual),expected in zip(out,[0.1,0.2,0.3,0.3,0.26,0.22]):
            self.assertAlmostEqual(actual,expected)

    def test_sampling_step_cancels_for_constant_error(self):
        a=sum(20*0.01 for _ in range(100))
        b=sum(20*0.1 for _ in range(10))
        self.assertAlmostEqual(a,20)
        self.assertAlmostEqual(b,20)
        self.assertEqual(sum(20 for _ in range(100))/sum(20 for _ in range(10)),10)

    def test_motor_torque_constant_and_saturation(self):
        k_t, current, maximum = 0.1,2.0,2.0
        self.assertAlmostEqual(k_t*current,0.2)
        self.assertEqual(min(max(5.0,-maximum),maximum),2.0)

if __name__=='__main__':
    unittest.main()
