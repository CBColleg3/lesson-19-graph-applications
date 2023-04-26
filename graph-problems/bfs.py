# Python Environment Setup
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
import pprint
import json

# Create empty undirected graph
G = nx.Graph()

# Add edges
G.add_edge("Logan", "Clara")
G.add_edge("Clara", "Sandra")
G.add_edge("Sandra", "George")
G.add_edge("George", "Peter")
G.add_edge("Peter", "Franklin")
G.add_edge("Franklin", "Sandra")
G.add_edge("Sandra", "Peter")
G.add_edge("George", "Franklin")
G.add_edge("Sandra", "Aaron")
G.add_edge("Aaron", "Nyla")
G.add_edge("Nyla", "John")
G.add_edge("John", "Aaron")
G.add_edge("Hannah", "Clara")
G.add_edge("Ursula", "Clara")
G.add_edge("Hannah", "Ursula")
G.add_edge("Riley", "Ursula")
G.add_edge("Benjamin", "Hannah")
G.add_edge("Riley", "Benjamin")
G.add_edge("Benjamin", "Daniel")
G.add_edge("Mason", "Ophelia")
G.add_edge("Ophelia", "Daniel")
G.add_edge("Daniel", "Tina")
G.add_edge("Ophelia", "Isaac")
G.add_edge("Elizabeth", "Isaac")
G.add_edge("Isaac", "Quentin")
G.add_edge("Quentin", "Kamala")

# To visualize
nx.draw(G, with_labels = True)
plt.savefig("tables_graph.png")
plt.show()

# pos = nx.spring_layout(G, seed = 4, k = 0.45)
# labels = nx.get_edge_attributes(G, "weight")
# plt.figure(1, figsize = (12, 12))
# nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
# plt.savefig("tables_graph.png")
# plt.show()

print("Number of nodes = ", G.number_of_nodes())
print("Number of edges = ", G.number_of_edges())

edges = nx.bfs_edges(G, "Aaron")
nodes = ["Aaron"] + [v for u, v in edges]
print("\nBFS Order:")
for i in nodes:
    print(i)