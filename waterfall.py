import matplotlib.pyplot as plt
import numpy as np


a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(time):
    return a * (time ** 2) + b * time + c


print("=== WATERFALL MODE ===")

hours = list(range(0, 25, 6))      
temps = [quadratic_weather_model(h) for h in hours]

for h, t in zip(hours, temps):
    print(f"Time: {h} hrs -> Predicted Temp: {t:.2f}°C")


x = np.linspace(0, 24, 100)         
y = quadratic_weather_model(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label="Temperature Curve", color="blue")
plt.scatter(hours, temps, color="red", zorder=5, label="Predicted Points")
plt.title("Weather Modeling - Waterfall Mode")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()