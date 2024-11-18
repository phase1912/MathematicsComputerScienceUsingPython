import matplotlib.pyplot as plt
import numpy as np


# Створення ортогональних векторів
v1 = np.array([2, 1])
v2 = np.array([-1, 2])


# Обчислення скалярного добутку
dot_product = np.dot(v1, v2)


# Створення 2D-графіка
fig, ax = plt.subplots()
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Вектор v1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Вектор v2')


# Додавання підписів та гриду
ax.text(v1[0], v1[1], f'v1 ({v1[0]}, {v1[1]})', fontsize=12, ha='right', va='bottom', color='r')
ax.text(v2[0], v2[1], f'v2 ({v2[0]}, {v2[1]})', fontsize=12, ha='left', va='bottom', color='g')
ax.text(0.5, -0.5, f'Dot Product: {dot_product}', fontsize=12, ha='center', va='top')


ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim([-2, 3])
ax.set_ylim([-1, 3])
ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_title('Ортогональні вектори та їх скалярний добуток')


# Відображення графіка
plt.legend()
plt.show()