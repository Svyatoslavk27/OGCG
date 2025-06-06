import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Генерація випадкових точок
np.random.seed(42)
all_points = 3 * (np.random.rand(10000, 2) - 0.5)

# Побудова опуклої оболонки
hull = ConvexHull(all_points)
hull_points = all_points[hull.vertices]

# Знаходження трикутника найбільшої площі серед точок оболонки
def max_area_triangle(points):
    n = len(points)
    max_area = 0
    best_triangle = None
    for i in range(n):
        for j in range(i + 1, n):
            k = (j + 1) % n
            while True:
                next_k = (k + 1) % n
                area1 = 0.5 * abs(np.cross(points[j] - points[i], points[k] - points[i]))
                area2 = 0.5 * abs(np.cross(points[j] - points[i], points[next_k] - points[i]))
                if area2 > area1:
                    k = next_k
                else:
                    break
            area = 0.5 * abs(np.cross(points[j] - points[i], points[k] - points[i]))
            if area > max_area:
                max_area = area
                best_triangle = (i, j, k)
    return best_triangle, max_area

triangle_indices, area = max_area_triangle(hull_points)
triangle = hull_points[list(triangle_indices)]

# Вибір 10 внутрішніх точок
hull_idx = set(hull.vertices)
interior = np.array([p for i, p in enumerate(all_points) if i not in hull_idx])[:10]

# Обертання
def rotate_points(points, angle_deg):
    angle = np.radians(angle_deg)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    return points @ R.T

angle = -20
hull_rot = rotate_points(hull_points, angle)
triangle_rot = rotate_points(triangle, angle)
interior_rot = rotate_points(interior, angle)

# Візуалізація
plt.figure(figsize=(6, 6))
hull_closed = np.append(hull_rot, [hull_rot[0]], axis=0)
plt.plot(hull_closed[:, 0], hull_closed[:, 1], 'b-', linewidth=0.5)
plt.plot(hull_rot[:, 0], hull_rot[:, 1], 'r.', markersize=4)

# Підписи вершин оболонки
for i, (x, y) in enumerate(hull_rot):
    plt.text(x + 0.05, y + 0.05, str(i + 1), fontsize=9)

# Внутрішні точки
plt.plot(interior_rot[:, 0], interior_rot[:, 1], 'r.', markersize=3)
for i, (x, y) in enumerate(interior_rot):
    plt.text(x + 0.03, y - 0.03, f"P{i+1}", fontsize=9)

# Найбільший трикутник
plt.plot(*np.append(triangle_rot, [triangle_rot[0]], axis=0).T, 'g-', linewidth=0.6)
plt.fill(triangle_rot[:, 0], triangle_rot[:, 1], 'lime', alpha=0.3)

# Текст
plt.text(-3.0, 2.1, "Трикутник", fontsize=13, family='serif')
plt.text(-3.0, 1.8, "найбільшої  площі", fontsize=13, family='serif')
plt.text(-3.0, 1.5, "вписаний  в  опуклу", fontsize=13, family='serif')
plt.text(-3.0, 1.2, "оболонку", fontsize=13, family='serif')

plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()

# Друк площі
print(f"Максимальна площа трикутника: {area:.5f}")
