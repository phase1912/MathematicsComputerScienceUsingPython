import numpy as np

# Задаємо матрицю A та вектор B
A = np.array([
    [-1, 1, 2],
    [0, -1, -3],
    [4, -3, 2]
])
B = np.array([1, -4, 7])

# Функція для розв'язання системи матричним методом
def solve_inv_matrix(a, b, verbose=False):
    try:
        a_inv = np.linalg.inv(a)  # Обчислення оберненої матриці
        if verbose:
            print(f"Обернена матриця A: \n{a_inv}")
        x = np.dot(a_inv, b)  # Знаходимо розв'язок
        return x
    except np.linalg.LinAlgError as e:
        return f"Помилка: {e}"

# Функція для розв'язання системи методом Крамера
def solve_cramer(a, b, verbose=False):
    try:
        det_a = np.linalg.det(a)  # Обчислення визначника матриці A
        if np.isclose(det_a, 0):
            return "Система не має єдиного розв'язку (визначник = 0)."
        if verbose:
            print(f"Визначник матриці A: {det_a}")

        n = len(b)
        x = np.zeros(n)
        for i in range(n):
            a_temp = a.copy()
            a_temp[:, i] = b  # Замінюємо i-й стовпець на вектор B
            det_a_temp = np.linalg.det(a_temp)
            if verbose:
                print(f"Матриця A з заміною стовпця {i}: \n{a_temp}")
                print(f"Визначник зміненої матриці: {det_a_temp}")
            x[i] = det_a_temp / det_a  # Знаходимо x_i
        return x
    except np.linalg.LinAlgError as e:
        return f"Помилка: {e}"

# Вивід результатів
print(f"Вектор рішення (матричний метод): \n{solve_inv_matrix(A, B, verbose=True)}")
print(f"Вектор рішення (метод Крамера): \n{solve_cramer(A, B, verbose=True)}")