from typing import Any
import queue
from time import perf_counter
import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set() # set of edges constituting MST
    q = queue.PriorityQueue()
    rest_set.remove(start_node)
    current_node = start_node
    edge2 = current_node
    while rest_set:
        for node in G.neighbors(current_node):
            if node in rest_set:
                q.put((G[current_node][node]["weight"],current_node,node))
        while edge2 == current_node:
            (w, e1, e2) = q.get()
            if e2 in rest_set:
                weight, edge1, edge2 = w, e1, e2
        mst_edges.add((edge1,edge2))
        current_node = edge2
        rest_set.remove(current_node)
    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    t_start = perf_counter()
    mst_edges = prim_mst(G, start_node="0")
    t_end = perf_counter()
    print(t_end - t_start)
    plot_graph(G, highlighted_edges=list(mst_edges))
