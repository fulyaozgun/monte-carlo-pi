import random
import matplotlib.pyplot as plt

inside_x = []
inside_y = []

outside_x = []
outside_y = []

total_points = 5000

inside_circle = 0

for i in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        inside_circle += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

pi_estimate = 4 * inside_circle / total_points

print("Estimated Pi:", pi_estimate)

plt.scatter(inside_x, inside_y, s=1)
plt.scatter(outside_x, outside_y, s=1)

plt.title(f"Monte Carlo Pi Estimate = {pi_estimate}")
plt.axis("equal")

plt.show()
