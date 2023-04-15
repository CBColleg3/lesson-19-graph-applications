import networkx as nx
import matplotlib.pyplot as plt
import pprint


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

    dist = nx.floyd_warshall(g)
    pprint.pprint(dist)


if __name__ == "__main__":
    dijkstra_graph()
