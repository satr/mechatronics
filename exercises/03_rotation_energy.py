"""Rotational kinetic energy of a synthetic rigid rotor."""
import math


def rotational_energy(inertia, angular_velocity):
    if not math.isfinite(inertia) or inertia < 0:
        raise ValueError("inertia must be finite and nonnegative")
    if not math.isfinite(angular_velocity):
        raise ValueError("angular_velocity must be finite")
    if inertia == 0.0:
        return 0.0
    # Preserve tiny but representable energies. Halving a subnormal moment
    # of inertia first can underflow/round away before a large omega restores
    # the final product to the normal floating-point range.
    if inertia < math.ldexp(1.0, -1022):  # smallest positive normal float
        result = (inertia * angular_velocity) * (0.5 * angular_velocity)
    else:
        result = (0.5 * inertia) * angular_velocity * angular_velocity
    if not math.isfinite(result):
        raise ValueError("energy exceeds the finite floating-point range")
    return result


if __name__ == "__main__":
    for inertia in (2, 4):
        for omega in (5, 10, 20):
            print(f"J={inertia} kg*m^2, omega={omega} rad/s, "
                  f"E={rotational_energy(inertia, omega):.1f} J")