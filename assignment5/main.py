import heapq
import math

test_case4 = {
    "A": [("B", 2), ("C", 3), ("D", 1)],
    "B": [("A", 2), ("D", 3), ("E", 5)],
    "C": [("A", 3), ("D", 4), ("F", 2)],
    "D": [("A", 1), ("B", 3), ("C", 4), ("E", 1), ("F", 6), ("G", 8)],
    "E": [("B", 5), ("D", 1), ("G", 6)],
    "F": [("C", 2), ("D", 6), ("G", 3)],
    "G": [("D", 8), ("E", 6), ("F", 3)],
}

starting_point = 'A'
end_point = 'G'


# *Hint: Modify the Dijkstra's algorithm implementation to return the shortest path between two nodes in addition to the
# shortest distances. To do this, you will need to maintain a dictionary to store the previous node in the shortest path
# for each node. After finding the shortest distances, you can reconstruct the path by backtracking from the destination
# node to the source node using the previous nodes.*


import heapq


def prim(graph, start):
    """
    Input:
        graph: A dictionary representing the adjacency list of the connected, undirected, and weighted graph.
               The keys are node labels and the values are lists of tuples containing a neighbor and the edge weight.
        start: The starting node label (a key in the graph dictionary).

    Output:
        Returns the total weight of the minimum spanning tree (MST) of the input graph.
    """

    # your code here
    visited = []
    visited.append(start)

    node_mapping = {}

    priority_queue = [(0, start)]