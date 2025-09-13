import matplotlib.pyplot as plt, numpy as np

a, b, c = -0.1, 1.2, 22
f = lambda t: a*t**2 + b*t + c
hours = [0, 12, 24]
temps = [f(h) for h in hours]

print("Iteration 2:", list(zip(hours, [round(t,2) for t in temps])))

x = np.linspace(0, 24, 100)
plt.plot(x, f(x), "g")
plt.scatter(hours, temps, color="g")
plt.title("Iteration 2")
plt.xlabel("Time (hours)"); plt.ylabel("Temperature (°C)")
plt.show()
