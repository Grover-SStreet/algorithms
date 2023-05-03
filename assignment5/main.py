import heapq

test_case2 = {
    "A": [("B", 3), ("D", 1)],
    "B": [("A", 3), ("C", 5), ("D", 2)],
    "C": [("B", 5), ("D", 3), ("E", 1)],
    "D": [("A", 1), ("B", 2), ("C", 3), ("E", 2)],
    "E": [("C", 1), ("D", 2)],
}

test_case1 = {
    "A": [("B", 7), ("D", 5)],
    "B": [("A", 7), ("C", 8), ("D", 9), ("E", 7)],
    "C": [("B", 8), ("E", 5)],
    "D": [("A", 5), ("B", 9), ("E", 15), ("F", 6)],
    "E": [("B", 7), ("C", 5), ("D", 15), ("F", 8), ("G", 9)],
    "F": [("D", 6), ("E", 8), ("G", 11)],
    "G": [("E", 9), ("F", 11)],
}
starting_point = 'A'


# def kruskal(graph):
#     """
#     Input:
#         graph: A dictionary representing the adjacency list of the connected, undirected, and weighted graph.
#                The keys are node labels and the values are lists of tuples containing a neighbor and the edge weight.
#
#     Output:
#         Returns the total weight of the minimum spanning tree (MST) of the input graph.
#     """
#     # your code here
#
#     priority_queue = []
#     mst_mapping = []
#
#     total_weight = 0
#
#     # Step 1: Sort all the edges in non-decreasing order of their weight.
#     for vertex in graph:
#         for edge in graph[vertex]:
#             priority_queue.append((edge[1], (vertex, edge[0])))
#     priority_queue.sort()
#
#     # Create a disjoint set of the vertices:
#     disjointed_sets = []
#     for vertex in graph:
#         if set(vertex) not in disjointed_sets:
#             disjointed_sets.append({vertex})
#         for edge in graph[vertex]:
#             if set(edge[0]) not in disjointed_sets:
#                 disjointed_sets.append({edge[0]})
#
#     # Process the edges in order of weight.
#     while len(priority_queue) > 0:
#         weight, current_vertex = heapq.heappop(priority_queue)
#         set_index_one = None
#         set_index_two = None
#         for index in range(0, len(disjointed_sets)):
#             if current_vertex[0] in disjointed_sets[index]:
#                 set_index_one = index
#             if current_vertex[1] in disjointed_sets[index]:
#                 set_index_two = index
#
#         if set_index_one is None or set_index_two is None:
#             x=3
#         if set_index_one != set_index_two and set_index_one:
#             mst_mapping.append((weight, current_vertex))
#
#             left_data = disjointed_sets[set_index_one]
#             right_data = disjointed_sets[set_index_two]
#
#             disjointed_sets.remove(left_data)
#             disjointed_sets.remove(right_data)
#
#             combined_set_data = left_data.union(right_data)
#             disjointed_sets.append(combined_set_data)
#
#     for record in mst_mapping:
#         total_weight += record[0]
#     return total_weight

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
    total_distance = 0

    visited = {start}
    mst_mapping = []
    priority_queue = []
    for neighbor, weight in graph[start]:
        priority_queue.append((weight, (start, neighbor)))

    heapq.heapify(priority_queue)

    while len(priority_queue) > 0 or len(visited) != len(graph.keys()):
        # Step 3-1: Remove the vertex in the fringe with the minimum priority. O(log |V|)
        current_distance, current_vertex = heapq.heappop(priority_queue)
        visiting_vertex = current_vertex[1]
        if visiting_vertex not in visited:
            for neighbor, weight in graph[visiting_vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, (visiting_vertex, neighbor)))

            visited.add(visiting_vertex)
            mst_mapping.append(current_vertex)
        priority_queue.sort()

    for element in mst_mapping:
        for index in graph[element[0]]:
            if index[0] == element[1]:
                total_distance += index[1]

    return total_distance
print(prim(test_case1,'A'))
# print(kruskal(test_case2))
