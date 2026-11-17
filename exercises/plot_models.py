"""Offline plots for idealized, synthetic mechanical models."""
import numpy as np
import matplotlib.pyplot as plt


def show_energy():
    speeds = np.linspace(0.0, 20.0, 201)
    for inertia in (2.0, 4.0):
        plt.plot(speeds, 0.5 * inertia * speeds**2,
                 label=f"J={inertia} kg*m²")
    plt.xlabel("Angular velocity (rad/s)")
    plt.ylabel("Rotational kinetic energy (J)")
    plt.title("Rotational kinetic energy — idealized model")
    plt.legend()
    plt.grid(True)
    plt.show()


def show_step_response():
    times = np.linspace(0.0, 6.0, 301)
    for tau in (0.5, 1.0, 2.0):
        plt.plot(times, 10 * (1 - np.exp(-times / tau)),
                 label=f"tau={tau:g} s")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (mm/s)")
    plt.title("Ideal first-order step response")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    show_energy()
    show_step_response()