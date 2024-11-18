import matplotlib.pyplot as plt
import numpy as np

def calculate_vectors_components(vectors):
    """
    Функція для визначення компонент декількох векторів.


    Параметри:
    - vectors: Список кортежів (start_point, end_point), де start_point та end_point - це координати початкової та кінцевої точок вектора.


    Повертає:
    - components: Список кортежів (x_components, y_components), де x_components та y_components - це компоненти по X та Y для кожного вектора.
    """
    components = []


    for start_point, end_point in vectors:
        x_component = end_point[0] - start_point[0]
        y_component = end_point[1] - start_point[1]
        components.append((x_component, y_component))


    return components

def draw_vectors(vectors, colors=None, title=None):
    """
    Функція для малювання декількох векторів на площині засобами бібліотеки Matplotlib.


    Параметри:
    - vectors: Список кортежів (start_point, end_point), де start_point та end_point - це координати початкової та кінцевої точок вектора.
    - colors: Список кольорів для векторів (за замовчуванням використовується 'blue' для всіх векторів).
    """
    num_vectors = len(vectors)


    if colors is None:
        colors = ['blue'] * num_vectors


    if title is None:
        title = 'Декілька векторів на площині'


    # Створення нового рисунка та осей
    fig, ax = plt.subplots()


    for i in range(num_vectors):
        start_point, end_point = vectors[i]


        # Визначення вектора та його довжини
        vector = np.array([end_point[0] - start_point[0], end_point[1] - start_point[1]])
        length = np.linalg.norm(vector)


        # Нормалізація вектора
        # normalized_vector = vector / length
        normalized_vector = vector


        # Додавання стрілки до осей
        ax.arrow(start_point[0], start_point[1], normalized_vector[0], normalized_vector[1],
                 head_width=0.1, head_length=0.1, fc=colors[i], ec=colors[i])


    # Налаштування візуалізації
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)


    # Відображення графіка
    plt.show()