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

import heapq
import math

import heapq

def dijkstra_with_path(graph, start, end):
    """
    Input:
        graph: A dictionary representing the adjacency list of the connected, directed, and weighted graph.
               The keys are node labels and the values are lists of tuples containing a neighbor and the edge weight.
        start: The starting node label (a key in the graph dictionary).
        end: The ending node label (a key in the graph dictionary).

    Output:
        Returns the shortest distance between the start and end nodes in the input graph.
    """

    # Step 1: Add the starting vertex s to the initially empty fringe with priority value 0
    # Step 2: Add all other vertices to the fringe with priority value of infinity

    previous_node_mapping = {}

    distance_mapping = {}
    for vertex in graph:
        distance_mapping[vertex] = math.inf
    distance_mapping[start] = 0

    priority_queue = [(0, start)]

    # Step 3: While the fringe is not empty: O(|V|)
    while len(priority_queue) > 0:
        # Step 3-1: Remove the vertex in the fringe with the minimum priority. O(log |V|)
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Step 3-2: For each of u's neighbors v: O(E_v)
        for neighbor, weight in graph[current_vertex]:
            temp_distance = current_distance + weight

            # Update only when path is better
            if temp_distance < distance_mapping[neighbor]:
                distance_mapping[neighbor] = temp_distance
                heapq.heappush(priority_queue, (temp_distance, neighbor))
                previous_node_mapping[neighbor] = current_vertex

    #  Find from end to start
    shortest_path = [end]

    while start not in shortest_path:
        end = previous_node_mapping[end]
        if start not in shortest_path:
            shortest_path.append(end)

    shortest_path_distance = 0

    # Reverse List so it shows start to end
    shortest_path = shortest_path[::-1]

    # From Graph find weights and total them up
    previous = start
    for current_vertex in shortest_path:
        if current_vertex == start:
            pass
        else:
            for neighbor, weight in graph[current_vertex]:
                if neighbor == previous:
                    shortest_path_distance += weight
                    previous = current_vertex

    return shortest_path_distance, shortest_path

test_case4 = {
    "A": [("B", 2), ("C", 3), ("D", 1)],
    "B": [("A", 2), ("D", 3), ("E", 5)],
    "C": [("A", 3), ("D", 4), ("F", 2)],
    "D": [("A", 1), ("B", 3), ("C", 4), ("E", 1), ("F", 6), ("G", 8)],
    "E": [("B", 5), ("D", 1), ("G", 6)],
    "F": [("C", 2), ("D", 6), ("G", 3)],
    "G": [("D", 8), ("E", 6), ("F", 3)],
}


# Test dijkstra_with_path
start_node = "A"
end_node = "G"

distance, path = dijkstra_with_path(test_case4, start_node, end_node)
