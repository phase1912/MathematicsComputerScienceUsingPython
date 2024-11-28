import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve

# Аналітична частина
# Задаємо змінну
x = symbols('x')

# Функція
y = -3 * x**2 + 30 * x

# Похідна функції
y_prime = diff(y, x)

# Знаходимо критичні точки (розв'язок рівняння y' = 0)
critical_points = solve(y_prime, x)
critical_values = {point: y.subs(x, point) for point in critical_points}

# Програмна частина
# Перетворення аналітичної функції в числову для графіка
def y_func(x):
    return -3 * x**2 + 30 * x

def y_prime_func(x):
    return -6 * x + 30

# Створення масиву значень для графіка
x_vals = np.linspace(0, 10, 500)
y_vals = y_func(x_vals)
y_prime_vals = y_prime_func(x_vals)

# Точка максимуму
x_max = float(critical_points[0])
y_max = float(critical_values[int(x_max)])

# Побудова графіка
plt.figure(figsize=(10, 6))

# Графік функції
plt.plot(x_vals, y_vals, label="$y(x) = -3x^2 + 30x$", color="blue")
# Графік похідної
plt.plot(x_vals, y_prime_vals, label="$y'(x)$", color="orange", linestyle="--")
# Точка максимуму
plt.scatter([x_max], [y_max], color="red", label=f"Максимум ({x_max}, {y_max})", zorder=5)

# Декорації
plt.axhline(0, color="black", linewidth=0.7, linestyle="--")
plt.axvline(x_max, color="gray", linewidth=0.7, linestyle="--")
plt.title("Графік функції та її похідної")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

# Вивід результатів
print("Аналітичне розв'язання:")
print(f"Функція: {y}")
print(f"Похідна: {y_prime}")
print(f"Критична точка (максимум): x = {x_max}, y = {y_max}")