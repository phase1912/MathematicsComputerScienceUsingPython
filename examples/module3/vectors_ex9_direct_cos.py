import matplotlib.pyplot as plt
import numpy as np


# Функція для обчислення модуля вектора
def compute_vector_magnitude(vector):
    return np.sqrt(np.sum(vector ** 2))


# Функція для обчислення напрямних косинусів
def compute_direction_cosines(vector):
    magnitude = compute_vector_magnitude(vector)
    cosine_alpha = vector[0] / magnitude
    cosine_beta = vector[1] / magnitude
    cosine_gamma = vector[2] / magnitude
    return cosine_alpha, cosine_beta, cosine_gamma


# Створення вектора
vector_a = np.array([2, 3, 4])


# Обчислення напрямних косинусів
cosine_alpha, cosine_beta, cosine_gamma = compute_direction_cosines(vector_a)


# Вивід результату
print(f"Вектор A: {vector_a}")
print(f"Напрямні косинуси: α={cosine_alpha:.2f}, β={cosine_beta:.2f}, γ={cosine_gamma:.2f}")


# Візуалізація вектора на площині
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, vector_a[0], vector_a[1], vector_a[2], color='b', label='Вектор A')


# Додавання підписів із напрямними косинусами
ax.text(vector_a[0] / 2, vector_a[1] / 2, vector_a[2] / 2, f'α={cosine_alpha:.2f}\nβ={cosine_beta:.2f}\nγ={cosine_gamma:.2f}',
        color='r')


# Налаштування вигляду графіка
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])
ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_zlabel('Вісь Z')
ax.set_title('Напрямні косинуси вектора на площині')


plt.legend()
plt.show()