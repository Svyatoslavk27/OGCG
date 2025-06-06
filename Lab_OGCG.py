import numpy as np
import matplotlib.pyplot as plt

# Вихідна оболонка з 10 точок
convex_hull_points = np.array([
    [0.0, -1.2], [0.85, -0.85], [1.5, -0.2], [1.25, 0.5], [0.75, 1.07],
    [-0.05, 1.25], [-0.8, 1.1], [-1.25, 0.44], [-1.25, 0.0], [-1.15, -0.4]
])

# 10 внутрішніх точок
interior_points = np.array([
    [-1.02, 0.25], [-0.6, 0.4], [-0.7, 0.13], [-0.3, 0.28], [-0.89, -0.25],
    [0.52, 0.43], [0.64, 0.43], [-0.33, -0.1], [-0.05, -0.1], [-0.58, -0.78]
])

convex_hull_rounded = convex_hull_points.copy()

# Вибраний трикутник: точки 1, 3, 7
triangle_indices = [0, 2, 6]
triangle = convex_hull_rounded[triangle_indices]

# Поворот
def rotate_points(points, angle_degrees):
    angle = np.radians(angle_degrees)
    R = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])
    return points @ R.T

angle = -20
hull_rot = rotate_points(convex_hull_rounded, angle)
triangle_rot = rotate_points(triangle, angle)
interior_rot = rotate_points(interior_points, angle)

# Побудова
plt.figure(figsize=(6, 6))
hull_closed = np.append(hull_rot, [hull_rot[0]], axis=0)
plt.plot(hull_closed[:, 0], hull_closed[:, 1], 'b-', linewidth=0.5)
plt.plot(hull_rot[:, 0], hull_rot[:, 1], 'r.', markersize=4)

# Підписи точок
for i, (x, y) in enumerate(hull_rot):
    plt.text(x + 0.05, y + 0.05, str(i + 1), fontsize=10)

# Внутрішні точки
plt.plot(interior_rot[:, 0], interior_rot[:, 1], 'r.', markersize=3)

# Підписи внутрішніх точок
for i, (x, y) in enumerate(interior_rot):
    plt.text(x + 0.03, y - 0.03, f"P{i+1}", fontsize=9, color='black')

# Трикутник
plt.plot(*np.append(triangle_rot, [triangle_rot[0]], axis=0).T, 'g-', linewidth=0.6)
plt.fill(triangle_rot[:, 0], triangle_rot[:, 1], 'lime', alpha=0.3)

# Текст
plt.text(-2.0, 2.1, "Трикутник", fontsize=13, family='serif')
plt.text(-2.0, 1.8, "найбільшої        площі", fontsize=13, family='serif')
plt.text(-2.0, 1.5, "вписаний      в     опуклу", fontsize=13, family='serif')
plt.text(-2.0, 1.2, "оболонку", fontsize=13, family='serif')

plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
