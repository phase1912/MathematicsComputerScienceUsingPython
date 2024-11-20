import networkx as nx
import matplotlib.pyplot as plt


# Створення псевдографа
pseudograph = nx.MultiDiGraph()
pseudograph.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 1)])


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(pseudograph)


# Візуалізація псевдографа
nx.draw(pseudograph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray', arrowsize=20, connectionstyle="arc3,rad=0.1")


plt.title("Pseudograph")
plt.show()