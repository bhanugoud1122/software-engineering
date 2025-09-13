import matplotlib.pyplot as plt
import numpy as np

a, b, c = [float(input(f"Enter coefficient {x}: ")) for x in "abc"]
t_val = float(input("Enter time t (hour/day): "))
T_val = a*t_val**2 + b*t_val + c
print(f"Predicted temperature at t={t_val}: {T_val:.2f}°C")

t = np.linspace(0, 10, 100)
plt.plot(t, a*t**2 + b*t + c, label="Temperature Curve")
plt.scatter(t_val, T_val, color="red", s=100, label=f"t={t_val}")
plt.xlabel("t (hours/days)"); plt.ylabel("Temperature (°C)")
plt.title("Version 2"); plt.legend(); plt.grid(True); plt.show()