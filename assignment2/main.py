# import the bag implementation from homework 1
from data.adt import Bag
from data.adt import Stack


# define Graph
class Graph:
    def __init__(self, in_file: str) -> None:
        # read the input file
        with open(in_file, 'r') as f:
            lines = f.readlines()

        # the line is V
        self.vertex_num = int(lines[0])  # number of vertices
        self.edge_num = int(lines[1])  # number of edges

        # create adjacency lists, each element in this list is a Bag object from HW1
        self.graph_adjacency = [Bag() for _ in range(self.vertex_num)]

        # read each lines to get the edges
        for line in lines[2:]:
            v, w = line.split()
            self.__addEdge(int(v), int(w))

    # return the number of vertices
    @property
    def V(self):
        return self.vertex_num

    # return the number of edges
    @property
    def E(self):
        return self.edge_num

    # add edge v-w to this graph
    def __addEdge(self, v: int, w: int) -> None:
        self.graph_adjacency[v].add(w)
        if v != w:  # if self-loop, only add edge one time
            self.graph_adjacency[w].add(v)

    # return all the vertices adjacent to v
    def adj(self, v: int) -> Bag:
        return self.graph_adjacency[v]

    # string representation of the graph - print()
    def __str__(self):
        s = f"{self.vertex_num} vertices, {self.edge_num} edges \n"
        for v in range(self.V):
            s += f"{v} : "
            for w in self.adj(v):
                s += f"{w} "
            s += "\n"
        return s


def degree(graph: Graph, v: int) -> int:
    return len(graph.graph_adjacency[v])


def maxDegree(graph: Graph) -> int:
    max_degree = 0
    for item in graph.graph_adjacency:
        if len(item) > max_degree:
            max_degree = len(item)
    return max_degree


def numberOfSelfLoops(graph: Graph) -> int:
    count = 0
    for item in range(len(graph.graph_adjacency)):
        if item in graph.adj(item):
            count += 1

    return count


graph_ex = Graph("data/example_G.txt")
assert (numberOfSelfLoops(graph_ex) == 0)

graph_tc_1 = Graph("data/tc_1.txt")
assert (numberOfSelfLoops(graph_tc_1) == 0)

graph_tc_2 = Graph("data/tc_2.txt")
assert (numberOfSelfLoops(graph_tc_2) == 0)

graph_tc_3 = Graph("data/tc_3.txt")
assert (numberOfSelfLoops(graph_tc_3) == 3)

# Write the API for StackDFS below
from data.adt import Stack


def dfs(self, g: Graph, v: int) -> None:
    self.__marked[v] = True  # mark the vertex
    node = self.stack.pop()

    for w in g.adj(node):  # see the vertices adjacent to v
        if self.__marked[w] is False:  # if not visited yet
            self.stack.push(w)

    while not self.stack.isEmpty():
        node = self.stack.pop()
        self.__marked[node] = True
        for w in g.adj(node):
            self.__edgeTo[w] = node


# 1 is [0, 4, 1]
# None 4 3 0 0 1

# spot W 4 initializing v with 0
# spot W 1 initializing v with 4
# spot W 5 initializing v with 1
# spot W 3 initializing v with 0
# spot W 2 initializing v with 3

# EdgeTo looks like [None, 4, 3, 0, 0, 1]
# The path to vertex
#
# from data.adt import Stack
#
#
# class StackDFS:
#     def __init__(self, g: Graph, s: int) -> None:
#         self.__marked = [False] * g.V  # has dfs() visited this vertex?
#         self.__edgeTo = [None] * g.V  # last vertex on known path to this vertex
#         self.__s = s  # source vertex
#         self.dfs(g, s)
#
#     def dfs(self, g: Graph, s: int) -> None:
#         # CLOSE
#         stack = Stack()
#         stack.push(s)
#         push_back = len(g.adj(s))
#         counter = 0
#         self.__marked[s] = True
#
#         while not stack.isEmpty() and counter < push_back:
#             v = stack.pop()
#             for w in g.adj(v):  # see the vertices adjacent to v
#                 if self.__marked[w] is False:  # if not visited yet
#                     stack.push(w)
#                     self.__edgeTo[w] = v
#                     print(f"spot W {w} initializing v with {v}")
#                     self.__marked[w] = True  # mark the vertex
#                     break
#                 else:
#                     stack.push(s)
#                     counter +=1
#
#     def hasPathTo(self, v: int) -> bool:
#         return self.__marked[v]
#
#     def pathTo(self, v: int) -> Stack:
#         if self.hasPathTo(v) is False: return None
#         path = Stack()
#         while v != self.__s:
#             path.push(v)
#             v = self.__edgeTo[v]
#         path.push(self.__s)
#         return path
#
#
# # create the graph given in the example
# graph_ex = Graph("data/example_G.txt")
#
# # run dfs
# dfs_ex = StackDFS(graph_ex, 0)
#
# # print the path to vertex i
# print("The path to vertex ")
# for i in range(1, 6):
#     print(f" - {i} is {dfs_ex.pathTo(i)}")


# Write the API for BFS below
from data.adt import Queue


class BFS:
    def __init__(self, g: Graph, s: int) -> None:
        self.__marked = [False] * g.V  # has dfs() visited this vertex?
        self.__edgeTo = [None] * g.V  # last vertex on known path to this vertex
        self.__s = s  # source vertex
        self.bfs(g, s)

    def bfs(self, g: Graph, s: int) -> None:
        # Write your code here

        queue = Queue()
        queue.enqueue(s)
        self.__marked[s] = True

        while not queue.isEmpty():
            v = queue.dequeue()
            for w in g.adj(v):  # see the vertices adjacent to v
                if self.__marked[w] is False:  # if not visited yet
                    queue.enqueue(w)
                    self.__edgeTo[w] = v
                    print(f"spot W {w} initializing v with {v}")
                    self.__marked[w] = True  # mark the vertex


    def hasPathTo(self, v: int) -> bool:
        return self.__marked[v]

    def pathTo(self, v: int):
        if self.hasPathTo(v) is False:
            return None
        path = Stack()
        while v != self.__s:
            path.push(v)
            v = self.__edgeTo[v]
        path.push(self.__s)
        return path


# create the graph given in the example
graph_ex = Graph("data/example_G.txt")

# run dfs
bfs_ex = BFS(graph_ex, 0)

# print the path to vertex i
print("The path to vertex ")
for i in range(1, 6):
    print(f" - {i} is {bfs_ex.pathTo(i)}")
