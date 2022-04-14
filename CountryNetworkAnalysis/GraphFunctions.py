import networkx as nx
import matplotlib.pyplot as plt

def createGraph(edges, size):
    # create a graph
    G = nx.Graph()

    # create a plot
    plt.figure(figsize=(5,5))

    # add the nodes to the graph
    G.add_weighted_edges_from((edges, size))

    # draw the graph
    nx.draw(G, with_labels=True, node_size=size)
    plt.show()