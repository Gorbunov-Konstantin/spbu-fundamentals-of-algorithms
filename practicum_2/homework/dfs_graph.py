import queue
from typing import Any
import networkx as nx
from src.plotting import plot_graph
def visit(node: Any):
    print(f"Wow, it is {node} right here!")
def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}
    q = queue.LifoQueue()
    q.put(node)
    while not q.empty():
        node = q.get()
        if visited[node] != True:
            visit(node)
            visited[node] = True
            for n_neigh in G.neighbors(node):
                if visited[n_neigh] != True:
                    q.put(n_neigh)

def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}
    tried_to_visit = {n: False for n in G}
    q = queue.LifoQueue()
    q.put(node)

    while not q.empty():
        node = q.get()
        tried_to_visit[node] = 1

        if visited[node] == 0:
            all_pred = 1
            loop = 1

            for i in G.predecessors(node):
                if tried_to_visit[i] == 0: #loop check
                    loop = 0
                if visited[i] == 0:
                    all_pred = 0
                    if q.empty():
                        q.put(i)

            if all_pred:
                visit(node)
                visited[node] = 1
                for i in G.neighbors(node):
                    if visited[i] == 0:
                        q.put(i)

            elif loop == 1:
                print('loop')
                break


if __name__ == "__main__":
    G = nx.read_edgelist("graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")