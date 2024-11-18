import matplotlib.pyplot as plt
import numpy as np


# Створення векторів для координат осей
axis_x = np.array([1, 0])
axis_y = np.array([0, 1])


# Побудова системи координат і векторів
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, axis_x[0], axis_x[1], angles='xy', scale_units='xy', scale=1, color='r', label='Вісь X')
plt.quiver(0, 0, axis_y[0], axis_y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Вісь Y')


# Позначення початку координат
plt.scatter(0, 0, color='black', marker='o')


# Додавання підписів
plt.text(axis_x[0], axis_x[1], ' X', fontsize=12, color='r', va='bottom', ha='left')
plt.text(axis_y[0], axis_y[1], ' Y', fontsize=12, color='b', va='bottom', ha='left')


# Налаштування вигляду графіка
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Система координат з одиничними векторами')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()
plt.show()