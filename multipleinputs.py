import matplotlib.pyplot as plt
import numpy as np

with open("multiple.txt", "r") as f:
    for i, line in enumerate(f, 1):
        a, b, c, t_val = map(float, line.strip().split())
        T_val = a*t_val**2 + b*t_val + c
        print(f"a={a}, b={b}, c={c}, t={t_val} -> T={T_val:.2f}°C")

        t = np.linspace(0, 10, 100)
        plt.plot(t, a*t**2 + b*t + c, label=f"Set {i}: a={a}, b={b}, c={c}")
        plt.scatter(t_val, T_val, s=80, label=f"t={t_val}, T={T_val:.2f}°C")

plt.xlabel("t (hours/days)")
plt.ylabel("Temperature (°C)")
plt.title("Version 4 - Multiple Inputs")
plt.legend()
plt.grid(True)
plt.show()