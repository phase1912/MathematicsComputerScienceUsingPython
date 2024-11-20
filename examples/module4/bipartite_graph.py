import networkx as nx
import matplotlib.pyplot as plt


# Створення дводольного графа
bipartite_graph = nx.complete_bipartite_graph(2, 3)


# Розділення графа на дві групи вершин
group1_nodes = {0, 1}
group2_nodes = {3, 2, 4}


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(bipartite_graph)


# Визначення кольорів вершин для різних груп
node_colors = [0 if node in group1_nodes else 1 for node in bipartite_graph.nodes()]


# Візуалізація дводольного графа
nx.draw(bipartite_graph, pos, with_labels=True, font_size=10, node_size=700, node_color=node_colors, cmap=plt.cm.Paired)


plt.title("Bipartite Graph with Node Colors")
plt.show()