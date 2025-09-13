import matplotlib.pyplot as plt, numpy as np

a, b, c = -0.18, 1.4, 23
f = lambda t: a*t**2 + b*t + c
times = [0, 6, 12, 18, 24]
temps = [f(t) for t in times]

print("Increment 2:", list(zip(times, [round(v,2) for v in temps])))

x = np.linspace(0, 24, 100)
plt.plot(x, f(x), "g")
plt.scatter(times, temps, color="g")
plt.title("Increment 2")
plt.xlabel("Time"); plt.ylabel("Temp (°C)")
plt.show()
