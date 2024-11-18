import numpy as np


# Оголошення вихідної матриці
matrix = np.array([[1, 0, 3],
                   [-1, -1, 2],
                   [4, 7, 2]])


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернена матриця:")
print(inverse_matrix)

#############

import numpy as np


# Оголошення вихідної матриці
matrix = np.array([[1, 0, 3],
                   [-1, -1, 2],
                   [4, 7, 2]])


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернена матриця:")
print(inverse_matrix)

###################

import numpy as np


# Оголошення вихідної матриці
matrix = np.array([[1, 2, 1],
                   [3, -5, 3],
                   [2, 7, -1]])


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)
inverse_inverse_matrix = np.linalg.inv(inverse_matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернена матриця:")
print(inverse_matrix)


print("\nОбернена оберненої матриці:")
print(inverse_inverse_matrix)

#############

import numpy as np


# Оголошення вихідної матриці
matrix = np.array([[1, 2, 1],
                   [3, -5, 3],
                   [2, 7, -1]])


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)
inverse_inverse_matrix = np.linalg.inv(inverse_matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернена матриця:")
print(inverse_matrix)


print("\nОбернена оберненої матриці:")
print(inverse_inverse_matrix)

###########

import numpy as np


# Оголошення вихідної матриці
matrix = np.array([[1, 2, 1],
                   [3, -5, 3],
                   [2, 7, -1]])


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)
inverse_inverse_matrix = np.linalg.inv(inverse_matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернена матриця:")
print(inverse_matrix)


print("\nОбернена оберненої матриці:")
print(inverse_inverse_matrix)

##############

import numpy as np


print()


# Оголошення вихідної матриці
matrix = np.array([[1, 2, 1],
                   [3, -5, 3],
                   [2, 7, -1]])


# Обчислення визначника початкової матриці
det_matrix = np.linalg.det(matrix)


# Обчислення оберненої матриці
inverse_matrix = np.linalg.inv(matrix)
# Обчислення визначника оберненої матриці
det_inverse_matrix = np.linalg.det(inverse_matrix)


print("Вихідна матриця:")
print(matrix)


print("\nОбернене значення визначника початкової матриці:")
print(1/det_matrix)


print("\nВизначник оберненої матриці:")
print(det_inverse_matrix)