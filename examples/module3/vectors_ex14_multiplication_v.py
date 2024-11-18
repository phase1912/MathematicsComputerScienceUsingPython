from examples.module3.draw_vectors import draw_vectors, calculate_vectors_components

vectors = [((0, 0), (1, 3)), ((0, 0), (2, 6))]
colors = ['green', 'red']


draw_vectors(vectors, colors, 'Добуток на скаляр')

vector_components = calculate_vectors_components(vectors)
print(vector_components)