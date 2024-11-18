import numpy as np
a = np.array([ 2, 1, -1])
print(a)

import numpy as np
a = np.array([ [2], [1], [-1]])
print(a)

import numpy as np
A = np.array([ [2, 1, -1], [0, 1, -4] ])
print(A)

import numpy as np
A = np.array([ [5, 5, 5], [5, 5, 5],[5, 5, 5] ])
print(A)

def print_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])


    if rows != cols:
        print("Матриця не є квадратною. Головна та побічна діагоналі не визначені.")
        return


    main_diagonal = [matrix[i][i] for i in range(rows)]
    anti_diagonal = [matrix[i][cols - 1 - i] for i in range(rows)]


    print("Головна діагональ:", main_diagonal)
    print("Побічна діагональ:", anti_diagonal)


# Приклад використання
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print_diagonals(matrix_example)

import numpy as np
matrix1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print(matrix1)

import numpy as np


# Створення одиничної матриці розміром 4x4
identity_matrix = np.eye(4)


print(identity_matrix)

#sum
import numpy as np
A = np.array([ [2, 1, -1], [0, 1, -4] ])
B = np.array([ [-2, 1, 0], [-3, 2, 2] ])
print(A+B)

#scalar
import numpy as np
A = np.array([ [2, 1, -1], [0, 1, -4] ])
print(3*A)

#*
import numpy as np
a = np.array([ [1,1], [1,1]])
b = np.array([ [1,1], [1,1]])
total = a.dot(b)
print(total)

import numpy as np
a = np.array([ [1, 2], [3, 4]])
b = np.array([ [5,6], [7,8] ])
total = a.dot(b)
print(total)

import numpy as np
a = np.array([ [1, 2], [3, 4], [5,6]])
b = np.array([ [7, 8, 9], [10, 11, 12] ])
total = a.dot(b)
print(total)

import numpy as np
a = np.array([ [1, 1], [2, 2], [3, 3], [4, 4], [5,5]  ])
b = np.array([ [1,1,1], [2,2,2] ])
print(a)
print(b)
total = a.dot(b)
print(total)

###########

import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib

########### Генерація зображення  ####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Розмір зображення
height = 100
width = 100

# Створення чорного зображення
image = np.zeros((height, width), dtype=np.uint8)

# Додавання цифри "1"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, '1', (width // 4, height // 2), font, 2, 255, 2, cv2.LINE_AA)

# Відображення та збереження зображення
plt.imshow(image, cmap='gray')
plt.title('Згенероване зображення з цифрою "1"')
plt.show()
#############################################

# Задаємо матрицю трансформації для зсуву (зсув на 10 пікселів вправо та 50 пікселів вниз)
M = np.float32([[1, 0, 10], [0, 1, 50]])

# Виконуємо афінне перетворення
result_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Показуємо оригінальне та змінене зображення
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Оригінал')
plt.subplot(122), plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)), plt.title('Зсунуте')

plt.show()