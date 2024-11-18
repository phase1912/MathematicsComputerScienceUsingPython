import numpy as np


def calculate_cosine_angle(vector1, vector2):
    """
    Функція для визначення косинусного кута між двома векторами.


    Параметри:
    - vector1: Кортеж (x1, y1) з координатами кінця першого вектора.
    - vector2: Кортеж (x2, y2) з координатами кінця другого вектора.


    Повертає:
    - cosine_angle: Косинус кута між векторами.
    """
    dot_product = np.dot(vector1, vector2)
    magnitude_vector1 = np.linalg.norm(vector1)
    magnitude_vector2 = np.linalg.norm(vector2)


    cosine_angle = dot_product / (magnitude_vector1 * magnitude_vector2)
    return cosine_angle


# Приклад використання функції з двома векторами
vector1 = (3, 4)
vector2 = (1, 2)


cosine_angle = calculate_cosine_angle(vector1, vector2)
angle_degrees = np.degrees(np.arccos(cosine_angle))


print(f"Косинусний кут між векторами: {cosine_angle:.2f}")
print(f"Кут між векторами у градусах: {angle_degrees:.2f}")