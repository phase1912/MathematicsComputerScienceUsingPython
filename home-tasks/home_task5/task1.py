from sympy import symbols, diff, sqrt

# Задаємо змінну
x = symbols('x')

# Функції
f1 = x**3 / 3 + x**2 / 2 - 2 * x
f2 = sqrt(x**2 + 1)
f3 = 1 / sqrt(x**2 + 1)

# Визначаємо похідні
f1_prime = diff(f1, x)
f2_prime = diff(f2, x)
f3_prime = diff(f3, x)

# Точки для обчислення
points = [1, -1/2]

# Обчислення значень похідних у точках
print("Результати обчислень:")
for func_name, derivative in [
    ("f1'(x)", f1_prime),
    ("f2'(x)", f2_prime),
    ("f3'(x)", f3_prime)
]:
    print(f"\n{func_name}: {derivative}")
    for point in points:
        value = derivative.subs(x, point).evalf()
        print(f"  {func_name} в точці x = {point}: {value}")