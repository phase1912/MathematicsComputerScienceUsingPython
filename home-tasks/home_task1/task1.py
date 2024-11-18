import numpy as np

# Код оголошення векторів (не можна змінювати)
a = np.array([[1, 2, 3, 4, 5]])
b = np.array([[1/2, 1, 2, 3, 4]])

# 1. Сума a і b
sum_ab = a + b
print("Сума a і b:\n", sum_ab)

# 2. Різниця a і b
diff_ab = a - b
print("Різниця a і b:\n", diff_ab)

# 3. Сума a і b.T (транспонованого)
sum_ab_t = a + b.T
print("Сума a і b.T:\n", sum_ab_t)
# Пояснення: результат є матрицею, оскільки розміри векторів (1х5) та (5х1) не збігаються, і при додаванні матриця розширюється.

# 4. Матричний добуток (dot product) a і b.T
dot_ab_t = np.dot(a, b.T)
print("Матричний добуток a і b.T:\n", dot_ab_t)

# 5. Матричний добуток (dot product) a і b
try:
    dot_ab = np.dot(a, b)
    print("Матричний добуток a і b:\n", dot_ab)
except ValueError as e:
    print("Матричний добуток a і b неможливий:\n", e)
# Пояснення: Матричний добуток неможливий, оскільки розміри (1х5) і (1х5) несумісні для такого типу множення.

# 6. Добуток Адамара (Hadamard product) a і b
hadamard_ab = a * b
print("Добуток Адамара (Hadamard product) a і b:\n", hadamard_ab)
# Пояснення: Добуток Адамара виконується елемент за елементом, тому результат є вектором такого ж розміру.

# 7. Ділення a на b
division_ab = a / b
print("Ділення a на b:\n", division_ab)
# Пояснення: Ділення виконується елемент за елементом, тож результат є вектором такого ж розміру.

# 8. Ділення a на b.T
try:
    division_ab_t = a / b.T
    print("Ділення a на b.T:\n", division_ab_t)
except ValueError as e:
    print("Ділення a на b.T неможливе:\n", e)