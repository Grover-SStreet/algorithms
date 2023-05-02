import heapq

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


# *Hint: Modify the Dijkstra's algorithm implementation to return the shortest path between two nodes in addition to the
# shortest distances. To do this, you will need to maintain a dictionary to store the previous node in the shortest path
# for each node. After finding the shortest distances, you can reconstruct the path by backtracking from the destination
# node to the source node using the previous nodes.*

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
    temp_adds = []
    priority_queue = []
    for neighbor, weight in graph[start]:
        priority_queue.append((weight, (start, neighbor)))

    heapq.heapify(priority_queue)

    while len(priority_queue) > 0:
        # Step 3-1: Remove the vertex in the fringe with the minimum priority. O(log |V|)
        current_distance, current_vertex = heapq.heappop(priority_queue)
        visiting_vertex = current_vertex[1]
        if visiting_vertex not in visited:
            for neighbor, weight in graph[visiting_vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, (visiting_vertex, neighbor)))

            visited.add(visiting_vertex)
            temp_adds.append(current_vertex)
        heapq.heapify(priority_queue)

    for element in temp_adds:
        for index in graph[element[0]]:
            if index[0] == element[1]:
                total_distance += index[1]

    return total_distance

print(prim(test_case1, 'A'))

# Minimum spanning tree total weight: 39
5
6
7
7
5
9
