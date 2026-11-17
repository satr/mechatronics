"""Synthetic one-dimensional motion: derivative and numerical integration."""
import math

# Prevent an accidentally tiny dt from monopolizing an interactive session.
MAX_STEPS = 1_000_000


def _integration_steps(duration, dt):
    if not (math.isfinite(duration) and math.isfinite(dt)):
        raise ValueError("duration and dt must be finite")
    if duration <= 0 or dt <= 0:
        raise ValueError("duration and dt must be positive")
    ratio = duration / dt
    if not math.isfinite(ratio) or ratio > MAX_STEPS:
        raise ValueError(f"integration exceeds {MAX_STEPS} steps")
    # Compare the dimensionless step count: an absolute 1e-9 s tolerance
    # could wrongly accept non-divisible sub-nanosecond durations.
    n = round(ratio)
    if n < 1 or not math.isclose(ratio, n, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("duration must be a positive integer multiple of dt")
    return n


def _finite_result(value, quantity):
    if not math.isfinite(value):
        raise ValueError(f"{quantity} exceeds the finite floating-point range")
    return value


def position(t):
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    return _finite_result(2.0 * t * t, "position")


def velocity(t):
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    return _finite_result(4.0 * t, "velocity")


def forward_derivative(t, dt):
    if not (math.isfinite(t) and math.isfinite(dt)) or dt <= 0:
        raise ValueError("t must be finite; dt must be finite and positive")
    # A sub-ULP time step can round away entirely: t + dt == t.
    shifted = t + dt
    if shifted == t:
        raise ValueError("dt is below floating-point time resolution at t")
    delta = position(shifted) - position(t)
    # In this specific x(t)=2*t**2 example the exact finite difference is
    # 4*t+2*dt. It can be nonzero even when both computed x values underflow
    # to zero. Keep the finite-difference teaching method; reject false zeros.
    if delta == 0.0 and 4.0 * t + 2.0 * dt != 0.0:
        raise ValueError("position difference lost to floating-point precision")
    return _finite_result(delta / dt, "derivative")


def euler_displacement(duration, dt):
    """Integral of synthetic velocity v(t)=2*t, left-endpoint Euler.

    This is a separate example from position(t)=2*t**2.
    """
    n = _integration_steps(duration, dt)
    return _finite_result(sum(2.0 * i * dt * dt for i in range(n)),
                          "Euler displacement")


def trapezoid_displacement(duration, dt):
    n = _integration_steps(duration, dt)
    return _finite_result(sum(((2.0 * i * dt) + (2.0 * (i + 1) * dt)) * dt / 2
                              for i in range(n)), "trapezoidal displacement")


if __name__ == "__main__":
    print("Position x(t)=2t² (mm); derivative at t=1 s (mm/s):")
    for dt in (1.0, 0.1, 0.01):
        print(f"  dt={dt:g}s: {forward_derivative(1, dt):.4f} mm/s")
    print("Integrate v(t)=2t (mm/s) for 2 s; exact displacement 4 mm:")
    for dt in (0.5, 0.1, 0.01):
        print(f"  dt={dt:g}s: Euler={euler_displacement(2, dt):.4f}, "
              f"trapezoid={trapezoid_displacement(2, dt):.4f} mm")