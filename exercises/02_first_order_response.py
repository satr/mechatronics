"""Synthetic first-order speed response: time constant vs numerical step."""
import math

MAX_STEPS = 1_000_000  # Interactive example, not a high-volume simulation.


def time_constant(inertia, gain):
    if not (math.isfinite(inertia) and math.isfinite(gain)) or inertia <= 0 or gain <= 0:
        raise ValueError("inertia and gain must be finite and positive")
    tau = inertia / gain
    if not math.isfinite(tau) or tau <= 0:
        raise ValueError("inertia/gain is outside the finite floating-point range")
    return tau


def exact_velocity(t, target, tau, initial=0.0):
    if not all(map(math.isfinite, (t, target, tau, initial))) or t < 0 or tau <= 0:
        raise ValueError("t, target, tau, initial must be finite; t >= 0 and tau > 0")
    # Convex weights avoid an overflow in (initial - target) when both
    # endpoints are finite but have very large, opposite signs.
    exponent = -t / tau
    remaining = math.exp(exponent)
    completed = -math.expm1(exponent)  # Stable for very small t/tau.
    return remaining * initial + completed * target


def euler_velocity(duration, target, tau, dt, initial=0.0):
    if not all(map(math.isfinite, (duration, target, tau, dt, initial))) or duration < 0 or dt <= 0 or tau <= 0:
        raise ValueError("inputs must be finite; duration >= 0, dt > 0 and tau > 0")
    if duration == 0:
        return initial
    ratio = duration / dt
    if not math.isfinite(ratio) or ratio > MAX_STEPS:
        raise ValueError(f"integration exceeds {MAX_STEPS} steps")
    # Check the dimensionless count, not an absolute time residual.
    # A fixed 1e-9 s tolerance permits false matches for tiny intervals.
    n = round(ratio)
    if n < 1 or not math.isclose(ratio, n, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("duration must be an integer multiple of dt")
    result = initial
    fraction = dt / tau
    for _ in range(n):
        if 0.0 < fraction <= 1.0:
            # In this stable, non-overshooting range a convex update is
            # algebraically the same forward-Euler step. It avoids an
            # intermediate (target - result) overflow when two finite
            # speeds have large opposite signs.
            result = (1.0 - fraction) * result + fraction * target
        elif fraction == 0.0:
            # The dimensionless ratio has underflowed, but its product
            # with a large finite speed change may still be representable.
            # Scale each endpoint before multiplying by dt. Avoid both
            # prematurely discarding that increment and overflowing
            # target - result for opposite large speeds.
            result += (target / tau) * dt - (result / tau) * dt
        else:
            # For dt > tau the Euler step can genuinely overshoot.
            # Prefer the original difference calculation when finite;
            # if only the intermediate subtraction overflows, use the
            # algebraically equivalent affine form instead.
            difference = target - result
            if math.isfinite(difference):
                if math.isfinite(fraction):
                    # dt/tau is already known: multiply by the ratio
                    # rather than first multiplying two large finite
                    # numbers that can overflow before division.
                    result += difference * fraction
                else:
                    # For a nonrepresentable ratio, the staged product
                    # may still be finite for a very small difference.
                    result += difference * dt / tau
            else:
                result = (1.0 - fraction) * result + fraction * target
        if not math.isfinite(result):
            raise ValueError("Euler velocity exceeds the finite floating-point range")
    return result


def estimate_tau(samples, initial, steady_state, resolution=0.0):
    """Time of first observed threshold sample (not interpolated crossing).

    Samples must have finite, strictly increasing nonnegative timestamps.
    Validate the entire finite sequence, even after crossing; cap its length.
    """
    if not all(map(math.isfinite, (initial, steady_state, resolution))):
        raise ValueError("step values and resolution must be finite")
    if steady_state == initial:
        raise ValueError("step magnitude must be nonzero")
    if resolution < 0:
        raise ValueError("resolution must be nonnegative")
    # A quantization step as large as the entire response cannot resolve
    # a 63.2% crossing. It can otherwise trigger a false crossing at t=0.
    # A finite subtraction may overflow for opposite huge endpoints; +inf
    # correctly exceeds any finite resolution in that representable range.
    if resolution >= abs(steady_state - initial):
        raise ValueError("measurement resolution must be smaller than step change")
    remaining = math.exp(-1)
    threshold = initial * remaining + steady_state * (1 - remaining)
    # A rounded display can differ by half its least-significant unit.
    margin = resolution / 2
    first_crossing = None
    last_time = None
    # Validate the complete sequence, even after the first crossing. Early
    # return would silently accept later NaNs or out-of-order timestamps.
    for count, (t, value) in enumerate(samples, start=1):
        if count > MAX_STEPS:
            raise ValueError(f"sample sequence exceeds {MAX_STEPS} entries")
        if not (math.isfinite(t) and math.isfinite(value)) or t < 0:
            raise ValueError("sample times must be finite and nonnegative; values finite")
        if last_time is not None and t <= last_time:
            raise ValueError("sample times must be strictly increasing")
        last_time = t
        if first_crossing is None and (
            (value + margin >= threshold) if steady_state > initial
            else (value - margin <= threshold)
        ):
            first_crossing = t
    return first_crossing


if __name__ == "__main__":
    print("First-order response: target 10 mm/s, initial 0 mm/s")
    for tau in (0.5, 1, 2):
        v = euler_velocity(1, 10, tau, 0.01)
        print(f"  tau={tau:g}s: Euler={v:.4f}, exact={exact_velocity(1, 10, tau):.4f} mm/s")
    print("Same tau=1s; changing numerical dt only:")
    for dt in (0.1, 0.01):
        print(f"  dt={dt:g}s: {euler_velocity(1, 10, 1, dt):.4f} mm/s")
    print("Same tau for inertia/gain pairs (2/1 and 4/2):")
    for inertia, gain in ((2, 1), (4, 2)):
        tau = time_constant(inertia, gain)
        print(f"  J={inertia}, K={gain}, tau={tau:g}s, v(1s)={euler_velocity(1, 10, tau, 0.01):.4f}")
    # Whole-number sensor outputs are rounded; tolerate approximate 63.2% threshold.
    samples = [(0, 0), (1, 393), (2, 632), (3, 777), (4, 865)]
    print("  tau from rounded samples: approximately",
          estimate_tau(samples, 0, 1000, resolution=1.0), "s")