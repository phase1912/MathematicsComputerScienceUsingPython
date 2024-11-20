import numpy as np

# Координати векторів
a = np.array([1, 1/3, 0])
b = np.array([0, 2, 1/4])
c = np.array([1/2, 1/2, 1])

# Об'єм
V = np.abs(np.linalg.det([a, b, c]))
print("Об'єм:", V)

# Довжини ребер
length_a = np.linalg.norm(a)
length_b = np.linalg.norm(b)
length_c = np.linalg.norm(c)

# Площа повної поверхні
S = 2 * (length_a * length_b + length_a * length_c + length_b * length_c)
print("Площа повної поверхні:", S)

# Косинуси кутів
cos_ab = np.dot(a, b) / (length_a * length_b)
cos_ac = np.dot(a, c) / (length_a * length_c)
cos_bc = np.dot(b, c) / (length_b * length_c)

# Кути
angle_ab = np.arccos(cos_ab)
angle_ac = np.arccos(cos_ac)
angle_bc = np.arccos(cos_bc)
print("Кут між a і b:", np.degrees(angle_ab))
print("Кут між a і c:", np.degrees(angle_ac))
print("Кут між b і c:", np.degrees(angle_bc))