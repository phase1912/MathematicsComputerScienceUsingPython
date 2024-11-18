from examples.module3.draw_vectors import calculate_vectors_components

# Приклад використання функції з декількома векторами
vectors = [((1, 2), (4, 6)), ((2, 3), (5, 2)), ((0, 0), (-2, 4))]


vector_components = calculate_vectors_components(vectors)
print(vector_components)