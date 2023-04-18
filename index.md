# Resturants in Newark

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Heni Patel (heni@udel.edu)
* Christopher Bennett (cbcolleg@udel.edu)
* Ella Wilkins (ellawlk@udel.edu)
* Sneha Nangelimalil (snehnang@udel.edu)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
import pprint
import json
```

# Problem #1: Get to the Closest Restaurant.

**Informal Description**: 
You've just arrived at a restaurant after a long day of work wanting to get inside.
Unfortunately, they had just closed their doors before you could even enter.

You realized that all of the other stores around you are probably closing at the same time too.

Given a city full of restaurants, we would like to know which one is the closest from any starting point.
Accounting for any traffic along the way, such as long traffic lights, pedestrians, or one-way streets.

> **Formal Description**:
>  * Input: Weighted Graph G representing 
>  all of the restaurants in the area. Weighted edges
>  represent distance between them.
> 
>  * Output: An adjacency matrix representing the shortest 
>  paths between all nodes.

**Graph Problem/Algorithm**: Floyd–Warshall algorithm/Dijkstra’s Algorithm


**Setup code**:

```
def dijkstra_graph():
    """
    You've just arrived at a restaurant after a long day of work wanting to get inside.
    Unfortunately, they had just closed their doors before you could even enter.

    You realized that all of the other stores around you are probably closing at the same time too.

    Given a city full of restaurants, we would like to know which one is the closest from any starting point.
    Accounting for any traffic along the way, such as long traffic lights, pedestrians, or one-way streets.
    """

    g = nx.Graph()

    vertices = ["FG", "CT", "I", "DP", "G", "DC", "EB", "MC", "DE", "WE",
                "CF", "UD", "WA", "TA", "K", "CG", "TW", "G2G", "Q", "DU"]

    labels = {"FG": "Five Guys", "CT": "Claymont", "I": "Insomnia", "DP": "Deer Park",
              "G": "Grotto's", "DC": "Drip Cafe", "EB": "Einstein Bagels", "MC": "Mcdonald's", "DE": "Denny's",
              "WE": "Wendy's", "CF": "Chick Fil-A", "UD": "UDairy", "WA": "Wawa", "TA": "Taverna", "K": "Kate's",
              "CG": "Cafe Gelato", "TW": "Tasty Wok", "G2G": "Greens To Go", "Q": "Quiznos", "DU": "Dunkin"}
    g.add_nodes_from(vertices)

    vertex_count = 0
    while vertex_count < len(vertices):
        edgeCount = vertex_count + 1
        while edgeCount < len(vertices):
            if vertices[vertex_count] not in vertices[edgeCount]:
                g.add_edge(vertices[vertex_count], vertices[edgeCount])
                node1 = vertices[vertex_count]
                node2 = vertices[edgeCount]
                g[node1][node2]['weight'] = edgeCount
            edgeCount += 8
        vertex_count += 1



    #nx.draw(g, with_labels=True, font_weight='bold')

    pos = nx.spring_layout(g)
    nx.draw(g, pos, node_size=800)
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, label_pos=0.5)
    nx.draw_networkx_labels(g, pos, labels=labels, font_size=7, font_color='black')
    plt.show()

```

**Visualization**:

<img title="a title" alt="Weighted graph showcasing 20 different restaurants" src="https://cdn.discordapp.com/attachments/1037446060227960945/1096921067639013516/image.png">

**Solution code:**

```python
    dist = nx.floyd_warshall(g)
    pprint.pprint(json.loads(json.dumps(dist)))
```

**Output**

```
{'CF': {'CF': 0,
        'CG': 45,
        'CT': 10,
        'DC': 24,
        'DE': 19,
        'DP': 15,
        'DU': 19,
        'EB': 30,
        'FG': 11,
        'G': 19,
        'G2G': 28,
        'I': 12,
        'K': 38,
        'MC': 27,
        'Q': 28,
        'TA': 32,
        'TW': 43,
        'UD': 11,
        'WA': 23,
        'WE': 10},
 'CG': {'CF': 45,
        'CG': 0,
        'CT': 35,
        'DC': 21,
        'DE': 30,
        'DP': 30,
        'DU': 52,
        'EB': 15,
        'FG': 36,
        'G': 26,
        'G2G': 33,
        'I': 33,
        'K': 15,
        'MC': 22,
        'Q': 51,
        'TA': 29,
        'TW': 16,
        'UD': 44,
        'WA': 42,
        'WE': 39},
 'CT': {'CF': 10,
        'CG': 35,
        'CT': 0,
        'DC': 14,
        'DE': 19,
        'DP': 5,
        'DU': 21,
        'EB': 20,
        'FG': 1,
        'G': 9,
        'G2G': 18,
        'I': 2,
        'K': 28,
        'MC': 27,
        'Q': 18,
        'TA': 22,
        'TW': 35,
        'UD': 13,
        'WA': 17,
        'WE': 10},
 'DC': {'CF': 24,
        'CG': 21,
        'CT': 14,
        'DC': 0,
        'DE': 21,
        'DP': 9,
        'DU': 31,
        'EB': 6,
        'FG': 15,
        'G': 5,
        'G2G': 32,
        'I': 12,
        'K': 14,
        'MC': 13,
        'Q': 32,
        'TA': 18,
        'TW': 29,
        'UD': 23,
        'WA': 21,
        'WE': 24},
 'DE': {'CF': 19,
        'CG': 30,
        'CT': 19,
        'DC': 21,
        'DE': 0,
        'DP': 24,
        'DU': 38,
        'EB': 15,
        'FG': 18,
        'G': 26,
        'G2G': 17,
        'I': 21,
        'K': 35,
        'MC': 8,
        'Q': 27,
        'TA': 39,
        'TW': 24,
        'UD': 30,
        'WA': 36,
        'WE': 9},
 'DP': {'CF': 15,
        'CG': 30,
        'CT': 5,
        'DC': 9,
        'DE': 24,
        'DP': 0,
        'DU': 22,
        'EB': 15,
        'FG': 6,
        'G': 4,
        'G2G': 23,
        'I': 3,
        'K': 23,
        'MC': 22,
        'Q': 23,
        'TA': 17,
        'TW': 38,
        'UD': 14,
        'WA': 12,
        'WE': 15},
 'DU': {'CF': 19,
        'CG': 52,
        'CT': 21,
        'DC': 31,
        'DE': 38,
        'DP': 22,
        'DU': 0,
        'EB': 37,
        'FG': 22,
        'G': 26,
        'G2G': 37,
        'I': 19,
        'K': 45,
        'MC': 44,
        'Q': 19,
        'TA': 39,
        'TW': 54,
        'UD': 30,
        'WA': 34,
        'WE': 29},
 'EB': {'CF': 30,
        'CG': 15,
        'CT': 20,
        'DC': 6,
        'DE': 15,
        'DP': 15,
        'DU': 37,
        'EB': 0,
        'FG': 21,
        'G': 11,
        'G2G': 32,
        'I': 18,
        'K': 20,
        'MC': 7,
        'Q': 38,
        'TA': 24,
        'TW': 23,
        'UD': 29,
        'WA': 27,
        'WE': 24},
 'FG': {'CF': 11,
        'CG': 36,
        'CT': 1,
        'DC': 15,
        'DE': 18,
        'DP': 6,
        'DU': 22,
        'EB': 21,
        'FG': 0,
        'G': 10,
        'G2G': 17,
        'I': 3,
        'K': 29,
        'MC': 26,
        'Q': 19,
        'TA': 23,
        'TW': 34,
        'UD': 14,
        'WA': 18,
        'WE': 9},
 'G': {'CF': 19,
       'CG': 26,
       'CT': 9,
       'DC': 5,
       'DE': 26,
       'DP': 4,
       'DU': 26,
       'EB': 11,
       'FG': 10,
       'G': 0,
       'G2G': 27,
       'I': 7,
       'K': 19,
       'MC': 18,
       'Q': 27,
       'TA': 13,
       'TW': 34,
       'UD': 18,
       'WA': 16,
       'WE': 19},
 'G2G': {'CF': 28,
         'CG': 33,
         'CT': 18,
         'DC': 32,
         'DE': 17,
         'DP': 23,
         'DU': 37,
         'EB': 32,
         'FG': 17,
         'G': 27,
         'G2G': 0,
         'I': 20,
         'K': 46,
         'MC': 25,
         'Q': 18,
         'TA': 40,
         'TW': 17,
         'UD': 31,
         'WA': 35,
         'WE': 26},
 'I': {'CF': 12,
       'CG': 33,
       'CT': 2,
       'DC': 12,
       'DE': 21,
       'DP': 3,
       'DU': 19,
       'EB': 18,
       'FG': 3,
       'G': 7,
       'G2G': 20,
       'I': 0,
       'K': 26,
       'MC': 25,
       'Q': 20,
       'TA': 20,
       'TW': 37,
       'UD': 11,
       'WA': 15,
       'WE': 12},
 'K': {'CF': 38,
       'CG': 15,
       'CT': 28,
       'DC': 14,
       'DE': 35,
       'DP': 23,
       'DU': 45,
       'EB': 20,
       'FG': 29,
       'G': 19,
       'G2G': 46,
       'I': 26,
       'K': 0,
       'MC': 27,
       'Q': 46,
       'TA': 14,
       'TW': 31,
       'UD': 37,
       'WA': 27,
       'WE': 38},
 'MC': {'CF': 27,
        'CG': 22,
        'CT': 27,
        'DC': 13,
        'DE': 8,
        'DP': 22,
        'DU': 44,
        'EB': 7,
        'FG': 26,
        'G': 18,
        'G2G': 25,
        'I': 25,
        'K': 27,
        'MC': 0,
        'Q': 35,
        'TA': 31,
        'TW': 16,
        'UD': 36,
        'WA': 34,
        'WE': 17},
 'Q': {'CF': 28,
       'CG': 51,
       'CT': 18,
       'DC': 32,
       'DE': 27,
       'DP': 23,
       'DU': 19,
       'EB': 38,
       'FG': 19,
       'G': 27,
       'G2G': 18,
       'I': 20,
       'K': 46,
       'MC': 35,
       'Q': 0,
       'TA': 40,
       'TW': 35,
       'UD': 31,
       'WA': 35,
       'WE': 18},
 'TA': {'CF': 32,
        'CG': 29,
        'CT': 22,
        'DC': 18,
        'DE': 39,
        'DP': 17,
        'DU': 39,
        'EB': 24,
        'FG': 23,
        'G': 13,
        'G2G': 40,
        'I': 20,
        'K': 14,
        'MC': 31,
        'Q': 40,
        'TA': 0,
        'TW': 45,
        'UD': 25,
        'WA': 13,
        'WE': 32},
 'TW': {'CF': 43,
        'CG': 16,
        'CT': 35,
        'DC': 29,
        'DE': 24,
        'DP': 38,
        'DU': 54,
        'EB': 23,
        'FG': 34,
        'G': 34,
        'G2G': 17,
        'I': 37,
        'K': 31,
        'MC': 16,
        'Q': 35,
        'TA': 45,
        'TW': 0,
        'UD': 48,
        'WA': 50,
        'WE': 33},
 'UD': {'CF': 11,
        'CG': 44,
        'CT': 13,
        'DC': 23,
        'DE': 30,
        'DP': 14,
        'DU': 30,
        'EB': 29,
        'FG': 14,
        'G': 18,
        'G2G': 31,
        'I': 11,
        'K': 37,
        'MC': 36,
        'Q': 31,
        'TA': 25,
        'TW': 48,
        'UD': 0,
        'WA': 12,
        'WE': 21},
 'WA': {'CF': 23,
        'CG': 42,
        'CT': 17,
        'DC': 21,
        'DE': 36,
        'DP': 12,
        'DU': 34,
        'EB': 27,
        'FG': 18,
        'G': 16,
        'G2G': 35,
        'I': 15,
        'K': 27,
        'MC': 34,
        'Q': 35,
        'TA': 13,
        'TW': 50,
        'UD': 12,
        'WA': 0,
        'WE': 27},
 'WE': {'CF': 10,
        'CG': 39,
        'CT': 10,
        'DC': 24,
        'DE': 9,
        'DP': 15,
        'DU': 29,
        'EB': 24,
        'FG': 9,
        'G': 19,
        'G2G': 26,
        'I': 12,
        'K': 38,
        'MC': 17,
        'Q': 18,
        'TA': 32,
        'TW': 33,
        'UD': 21,
        'WA': 27,
        'WE': 0}}
```

**Interpretation of Results**:



# Problem #2: Lowest Delivery Cost

**Informal Description**: 
There is a wedding party that wants to have food from all 20 restaurants. But, the wedding is
in four hours and they do not have enough money to pick up all the food. The wedding part is hiring 
a food delivery service to go to every restaurant and pick up the food. The cost changes depending
on what order the delivery driver goes too. The wedding party is trying to find the minimal cost
to collect the food from all the restaurants. Below is the restaurant path that will give the minimal cost.

> **Formal Description**:
A Prims algorithm minimum spanning tree will be used to find the lowest cost for the delivery driver to
go to the 20 restuarant and pick up the food. The algorithm will find the lowest cost between each 
restaurant and take that path.
>  * Input: A connected undirected graph G = (V, E) of resturants with edge weights that 
represent the cost of distance traveled.
>  * Output: A minimal spanning tree representing the path that will give the lowest cost to pick up 
all the food from each restaurant.

**Graph Problem/Algorithm**: MST


**Setup code**:

```
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
import pprint
import json

#Create empty undirected graph
G = nx.Graph()

#Add edges
G.add_edge("Santa Fe", "May Flower", weight=1.3)
G.add_edge("May Flower", "Five Guys", weight=10)
G.add_edge("Five Guys", "2SPizza", weight=6.5)
G.add_edge("2SPizza", "Playa Bowls", weight=1.9)
G.add_edge("Taverna Newark", "Five Guys", weight=2.4)
G.add_edge("Oishii Sushi & Ramen", "Deer Park Tavern", weight=3.7)
G.add_edge("Indian Sizzler", "Oishii Sushi & Ramen", weight=4.4)
G.add_edge("Indian Sizzler", "Deer Park Tavern", weight=6.7)
G.add_edge("Taverna Newark", "Hamilton's", weight=9.3)
G.add_edge("Caffe Gelato", "m2o Burgers", weight=8.9)
G.add_edge("El Diablo", "Home Grown", weight=4.3)
G.add_edge("El Diablo", "Honey Grow", weight=9.0)
G.add_edge("m2o Burgers", "Home Grown", weight= 4.6)
G.add_edge("Honey Grow", "Roots", weight=3.1)
G.add_edge("Klondike Kate's", "Snap Custom Pizza", weight=6.5)
G.add_edge("2SPizza", "Snap Custom Pizza", weight=3.4)
G.add_edge("Klondike Kate's", "m2o Burgers", weight=2.9)
G.add_edge("QDOBA", "Mama's Pizza & Pasta", weight=7.8)
G.add_edge("El Diablo", "May Flower", weight=2.4)
G.add_edge("May Flower", "Roots", weight=9.2)
G.add_edge("Santa Fe", "Mama's Pizza & Pasta", weight=2.3)
G.add_edge("Santa Fe", "El Diablo", weight=6.4)
G.add_edge("Caffe Gelato", "Mama's Pizza & Pasta", weight=5.1)
G.add_edge("El Diablo", "2SPizza", weight=8.3)
G.add_edge("Deer Park Tavern", "Santa Fe", weight=7.6)
G.add_edge("QDOBA", "Home Grown", weight=7.9)
G.add_edge("Roots", "Hamilton's", weight=5.7)
G.add_edge("Playa Bowls", "Snap Custom Pizza", weight=0.5)
G.add_edge("QDOBA", "El Diablo", weight=6.6)
G.add_edge("Oishii Sushi & Ramen", "Mama's Pizza & Pasta", weight=1.9)

print("Number of nodes = ", G.number_of_nodes())
print("Number of edges = ", G.number_of_edges())

#To visualize
plt.figure(1)
pos=nx.spring_layout(G, iterations=6000)
nx.draw_networkx(G, pos, arrows=False, with_labels=True)

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.02)

plt.axis("off")
plt.tight_layout()
plt.show()
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
sorted(sorted(e) for e in edgelist)
print(edgelist)
```

**Output**

```
Number of nodes =  20
Number of edges =  30
[('Indian Sizzler', 'Oishii Sushi & Ramen'), ('Oishii Sushi & Ramen', "Mama's Pizza & Pasta"), 
("Mama's Pizza & Pasta", 'Santa Fe'), 
('Santa Fe', 'May Flower'), ('May Flower', 'El Diablo'), ('Oishii Sushi & Ramen', 'Deer Park Tavern'), 
('El Diablo', 'Home Grown'), ('Home Grown', 'm2o Burgers'), ('m2o Burgers', "Klondike Kate's"), 
("Mama's Pizza & Pasta", 'Caffe Gelato'), ("Klondike Kate's", 'Snap Custom Pizza'), 
('Snap Custom Pizza', 'Playa Bowls'), ('Playa Bowls', '2SPizza'), ('2SPizza', 'Five Guys'), 
('Five Guys', 'Taverna Newark'), ('El Diablo', 'QDOBA'), ('El Diablo', 'Honey Grow'), ('Honey Grow', 'Roots'), 
('Roots', "Hamilton's")]
```

**Interpretation of Results**: