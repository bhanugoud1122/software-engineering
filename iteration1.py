import matplotlib.pyplot as plt, numpy as np

a, b, c = -0.2, 1.5, 24
f = lambda t: a*t**2 + b*t + c
hours = [0, 12, 24]
temps = [f(h) for h in hours]

print("Iteration 1:", list(zip(hours, [round(t,2) for t in temps])))

x = np.linspace(0, 24, 100)
plt.plot(x, f(x), "b")
plt.scatter(hours, temps, color="b")
plt.title("Iteration 1")
plt.xlabel("Time (hours)"); plt.ylabel("Temperature (°C)")
plt.show()
