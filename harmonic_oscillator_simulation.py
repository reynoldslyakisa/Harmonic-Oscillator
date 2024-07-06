import numpy as np
import matplotlib.pyplot as plt

def simulate_harmonic_oscillator(m, k, x0, v0, t_max, dt):
    t = np.arange(0, t_max, dt)
    x = np.zeros_like(t)
    v = np.zeros_like(t)

    x[0] = x0
    v[0] = v0

    for i in range(1, len(t)):
        a = -k / m * x[i-1]
        v[i] = v[i-1] + a * dt
        x[i] = x[i-1] + v[i] * dt

    return t, x

def main():
    m = 1.0  # mass in kg
    k = 1.0  # spring constant in N/m
    x0 = 1.0  # initial position in meters
    v0 = 0.0  # initial velocity in m/s
    t_max = 10.0  # simulation time in seconds
    dt = 0.01  # time step in seconds

    t, x = simulate_harmonic_oscillator(m, k, x0, v0, t_max, dt)

    plt.plot(t, x)
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Harmonic Oscillator Simulation')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
