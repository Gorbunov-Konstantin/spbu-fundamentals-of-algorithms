from typing import Any
import queue
import networkx as nx
import numpy as np
from src.plotting import plot_graph
from time import perf_counter

def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    unvisited_set = set(G.nodes())
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes
    dist = {n: np.inf for n in G}  # key = node, value = distance
    dist[source_node] = 0
    q = queue.PriorityQueue()
    shortest_paths[source_node] = source_node
    q.put((0, source_node))
    while unvisited_set:
        (current_dist, current_node) = q.get()
        if current_node in unvisited_set:
            unvisited_set.remove(current_node)
            for node in G.neighbors(current_node):
                dis = current_dist+G.edges[node, current_node]["weight"]
                if dist[node] > dis:
                    dist[node] = dis
                    shortest_paths[node] = shortest_paths[current_node] + node
                    q.put((dis,node))

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    t_start = perf_counter()
    shortest_paths = dijkstra_sp(G, source_node="0")
    t_end = perf_counter()
    print(t_end-t_start)
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
