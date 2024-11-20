import networkx as nx
import matplotlib.pyplot as plt


# Створення орієнтованого графа
directed_graph = nx.DiGraph()
directed_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(directed_graph)


# Візуалізація орієнтованого графа
nx.draw(directed_graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray', arrowsize=20, connectionstyle="arc3,rad=0.1")


plt.title("Directed Graph")
plt.show()