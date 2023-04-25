'''
Then for each problem:
1. An informal description of the problem, written for intelligent non-Computer Scientists
2. A formal description of the problem, written for other Computer Scientists
3. Which of the four main graph problems you are solving (DFS, BFS, SSSP/APSP, MST)
4. A visualization of the graph for the problem
5. The syntax-highlighted code used to load the data into `networkx` and to call the appropriate graph algorithm function
6. The preformatted output of the graph algorithm function
7. An interpretation of the results that meaningfully answer the question
---------------------------------------------------------------------------------------------------------------------
1. An informal description of the problem, written for intelligent non-Computer Scientists:
    A group of students are writing about diversity of cuisine on Staten Island. They are surveying the central area, and are breaking the restaurants into clusters based on similarity of cuisines. How can they split these restaurants up into these groups, utilizing the similiarity score between restaurants, and a certain threshold of how similar they can be?


2. A formal description of the problem, written for other Computer Scientists
    Let G = (V, E) be an undirected weighted graph, where V is the set of vertices representing restaurants and E is the set of edges representing the similarities between locations. Each edge e ∈ E has a non-negative weight w(e) representing the similarity between the two locations. 5 being the most similar, 2 being the least (no scores under 2 are shown).
    Using DFS and considering the weight of the edges, create a subgraph of restaurants based on similarity and a similarity threshold (how similar they can be). 

3. Which of the four main graph problems you are solving (DFS, BFS, SSSP/APSP, MST)
    DFS

4. A visualization of the graph for the problem
    ![Graph of Restaurants on Staten Island](ella-dfs.png)

5. The syntax-highlighted code used to load the data into `networkx` and to call the appropriate graph algorithm function

6. The preformatted output of the graph algorithm function

7. An interpretation of the results that meaningfully answer the question

'''
import networkx as nx
import matplotlib.pyplot as plt

#empty undirected graph
G = nx.Graph()

#add edges with weights
G.add_edge("Annadale Terrace", "District", weight=3)
G.add_edge("Annadale Bakery", "Mangia", weight=3)
G.add_edge("Mona Lisa Pizzeria", "The Square on Annadale", weight=5)
G.add_edge("Mangia", "Filoncino Cafe", weight=4)
G.add_edge("Richmond Republic", "District", weight=5)
G.add_edge("Campania", "Patrizias", weight=5)
G.add_edge("Ocean Sushi", "Tomo", weight=4)
G.add_edge("Burrito Bar", "Sofia's Taqueria", weight=4)
G.add_edge("DeLuca's", "Il Sogno", weight=5)
G.add_edge("DeLuca's", "La Fontana Sorellena", weight=5)
G.add_edge("La Fontana Sorellena", "Il Sogno", weight=5)
G.add_edge("The Pizza Parlor", "District", weight=4)
G.add_edge("The Pizza Parlor", "Richmond Republic", weight=4)
G.add_edge("Arirang", "Tomo", weight=3)
G.add_edge("Mona Lisa Pizzeria", "The Pizza Parlor", weight=3)
G.add_edge("Mangia", "Mona Lisa Pizzeria", weight=3)
G.add_edge("Mangia", "Campania", weight=3)
G.add_edge("Patrizias", "Arirang", weight=2)
G.add_edge("Il Sogno", "Campania", weight=3)
G.add_edge("M&M Deli", "Filoncino Cafe", weight=3)
G.add_edge("Sofia's Taqueria", "District", weight=2)
G.add_edge("Pastosa", "Mangia", weight=4)
G.add_edge("Richmond Republic", "Annadale Terrace", weight=3)
G.add_edge("DeLuca's", "Campania", weight=4)
G.add_edge("Pastosa", "Filoncino Cafe", weight=3)
G.add_edge("Il Sogno", "Patrizias", weight=3)
G.add_edge("The Pizza Parlor", "The Square on Annadale", weight=4)
G.add_edge("Mona Lisa Pizzeria", "Campania", weight=4)
G.add_edge("Campania", "The Pizza Parlor", weight=4)
G.add_edge("M&M Deli", "Mangia", weight=4)
G.add_edge("M&M Deli", "Pastosa", weight=3)

# case 1
threshold_c1 = 3
start_node_c1 = 'Tomo'
edges_c1 = ((u, v) for u, v, d in G.edges(data=True) if d['weight'] >= threshold_c1)
G_filtered_c1 = G.edge_subgraph(edges_c1)
subgraph_c1 = nx.dfs_tree(G_filtered_c1, source=start_node_c1)
print("\nRestaurants most similar to " + start_node_c1 + ": \n" + str(subgraph_c1.nodes()))

# case 2
threshold_c2 = 5
start_node_c2 = 'Mona Lisa Pizzeria'
edges_c2 = ((u, v) for u, v, d in G.edges(data=True) if d['weight'] >= threshold_c2)
G_filtered_c2 = G.edge_subgraph(edges_c2)
subgraph_c2 = nx.dfs_tree(G_filtered_c2, source=start_node_c2)
print("\nRestaurants most similar to " + start_node_c2 + ": \n" + str(subgraph_c2.nodes()))

# case 3
threshold_c3 = 5
start_node_c3 = 'Il Sogno'
edges_c3 = ((u, v) for u, v, d in G.edges(data=True) if d['weight'] >= threshold_c3)
G_filtered_c3 = G.edge_subgraph(edges_c3)
subgraph_c3 = nx.dfs_tree(G_filtered_c3, source=start_node_c3)
print("\nRestaurants most similar to " + start_node_c3 + ": \n" + str(subgraph_c3.nodes()))
