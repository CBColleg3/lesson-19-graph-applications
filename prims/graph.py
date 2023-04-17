import networkx as nx
import matplotlib.pyplot as plt
import pprint
import json

#Create empty undirected graph
G = nx.Graph()

#Add nodes
#G.add_node("Santa Fe")
#G.add_node("May Flower")
#G.add_node("Five Guys")
#G.add_node("Taverna Newark")
# G.add_node("Hamilton's")
# G.add_node("Caffe Gelato")
# G.add_node("El Diablo")
# G.add_node("Honey Grow")
# G.add_node("Home Grown Cafe")
# G.add_node("Roots")
# G.add_node("Klondike Kate's Restaurant & Saloon")
# G.add_node("m2o Burgers & Salads")
# G.add_node("QDOBA Mexican Eats")
# G.add_node("Mama's Pizza & Pasta")
# G.add_node("Indian Sizzler")
# G.add_node("2SPizza")
# G.add_node("Snap Custom Pizza and Salads")
# G.add_node("Playa Bowls")
# G.add_node("Deer Park Tavern")
# G.add_node("Oishii Sushi & Ramen")


#Add edges
G.add_edge("Santa Fe", "May Flower", weight=1.3)
G.add_edge("May Flower", "Five Guys", weight=10)
G.add_edge("Five Guys", "2SPizza", weight=6.5)
G.add_edge("2SPizza", "Playa Bowls", weight=1.9)
#G.add_edge("Playa Bowls", "Oishii Sushi & Ramen")
G.add_edge("Taverna Newark", "Five Guys", weight=2.4)
G.add_edge("Oishii Sushi & Ramen", "Deer Park Tavern", weight=3.7)
G.add_edge("Indian Sizzler", "Oishii Sushi & Ramen", weight=4.4)
G.add_edge("Indian Sizzler", "Deer Park Tavern", weight=6.7)
G.add_edge("Indian Sizzler", "Mama's Pizza & Pasta", weight=5.0)
G.add_edge("Indian Sizzler", "Honey Grow", weight=7.8)
G.add_edge("Taverna Newark", "Hamilton's", weight=9.3)
G.add_edge("Caffe Gelato", "m2o Burgers & Salads", weight=8.9)
G.add_edge("El Diablo", "Home Grown Cafe", weight=4.3)
G.add_edge("El Diablo", "Honey Grow", weight=9.0)
G.add_edge("m2o Burgers & Salads", "Home Grown Cafe", weight= 4.6)
G.add_edge("Honey Grow", "Roots", weight=3.4)
G.add_edge("Klondike Kate's Restaurant & Saloon", "Snap Custom Pizza and Salads", weight=6.5)
G.add_edge("2SPizza", "Snap Custom Pizza and Salads", weight=3.4)
G.add_edge("Klondike Kate's Restaurant & Saloon", "m2o Burgers & Salads", weight=2.9)
G.add_edge("QDOBA Mexican Eats", "Mama's Pizza & Pasta", weight=7.8)
G.add_edge("Honey Grow", "Hamilton's", weight=2.4)
G.add_edge("May Flower", "Roots", weight=9.2)
G.add_edge("Santa Fe", "Mama's Pizza & Pasta", weight=2.3)
G.add_edge("Santa Fe", "El Diablo", weight=6.4)
G.add_edge("Caffe Gelato", "Mama's Pizza & Pasta", weight=5.1)
G.add_edge("El Diablo", "2SPizza", weight=8.3)
G.add_edge("Deer Park Tavern", "Santa Fe", weight=7.6)
G.add_edge("QDOBA Mexican Eats", "Home Grown Cafe", weight=7.9)
G.add_edge("Roots", "Hamilton's", weight=5.7)
G.add_edge("Playa Bowls", "Snap Custom Pizza and Salads", weight=0.5)
G.add_edge("QDOBA Mexican Eats", "El Diablo", weight=6.6)
G.add_edge("Oishii Sushi & Ramen", "Mama's Pizza & Pasta", weight=1.9)

print("Number of nodes = ", G.number_of_nodes())
print("Number of edges = ", G.number_of_edges())

print("G.nodes = ", G.nodes)
print("G.edges = ", G.edges)
print("G.degree = ", G.degree)
#print("G.adj = ", G.adj)

#To visualize
#nx.draw_networkx(G)
plt.figure(1)
pos=nx.spring_layout(G, iterations=1000)
nx.draw_networkx(G, pos, arrows=False, with_labels=True)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()


#Reference 
#https://www.youtube.com/watch?v=CPQeSmDGiOQ
#https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html