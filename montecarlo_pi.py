import random

inside_circle = 0
total_points = 100000

for i in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_estimate = 4 * inside_circle / total_points

print("Estimated Pi:", pi_estimate)
