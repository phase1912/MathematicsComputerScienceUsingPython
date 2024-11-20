import networkx as nx
import matplotlib.pyplot as plt


# Створення бінарного дерева
G = nx.DiGraph()


# Додавання вершин
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])


# Додавання ребер
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])


# Візуалізація бінарного дерева
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (1, -3)}


nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, edge_color='gray', arrows=True)
plt.show()