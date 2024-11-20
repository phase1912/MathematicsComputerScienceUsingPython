import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray')
    plt.title(title)
    plt.show()

# 3. Ациклічний граф
acyclic_graph = nx.DiGraph()
acyclic_graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
visualize_graph(acyclic_graph, "Acyclic Graph")