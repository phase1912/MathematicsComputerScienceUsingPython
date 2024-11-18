import numpy as np

# Вектор x
x = np.array([[2], [1]])

# 1. Масштабування
M1 = np.array([[0.5, 0], [0, 3]])
x1 = M1 @ x

# 2. Відображення
M2 = np.array([[-1, 0], [0, -1]])
x2 = M2 @ x

# 3. Перенесення
M3 = np.array([[1, 0, -3], [0, 1, 1]])
x_hom = np.array([[2], [1], [1]])  # Однорідні координати
x3 = M3 @ x_hom

# 4. Обертання на 60°
theta_60 = np.radians(60)
M4 = np.array([
    [np.cos(theta_60), -np.sin(theta_60)],
    [np.sin(theta_60), np.cos(theta_60)]
])
x4 = M4 @ x

# 5. Обертання на 30°
theta_30 = np.radians(30)
M5 = np.array([
    [np.cos(theta_30), -np.sin(theta_30)],
    [np.sin(theta_30), np.cos(theta_30)]
])
x5 = M5 @ x

# 6. Об'єднання
M_combined = M5 @ M4 @ M2 @ M1
x_final = M_combined @ x

# Вивід результатів
print("x1 (масштабування):\n", x1)
print("x2 (відображення):\n", x2)
print("x3 (перенесення):\n", x3[:2])  # Ігноруємо однорідну координату
print("x4 (обертання 60°):\n", x4)
print("x5 (обертання 30°):\n", x5)
print("x_final (об'єднане перетворення):\n", x_final)