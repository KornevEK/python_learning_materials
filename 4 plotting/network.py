import networkx as nx

def draw(edges, tree=None):
    G = nx.Graph() # nx.DiGraph()
    #G.add_edge("a", "b")
    G.add_weighted_edges_from(edges) # G.add_edges_from(edges)
    pos = nx.kamada_kawai_layout(G) # nx.spring_layout(G)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color="y")
    nx.draw_networkx_edges(G, pos, width=1, edge_color="k")
    if tree is not None:
        nx.draw_networkx_edges(G, pos, edgelist=tree, width=6, alpha=0.5, edge_color="r")

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
