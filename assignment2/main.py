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


from data.adt import Stack


class RecursiveDFS:
    def __init__(self, g: Graph, s: int) -> None:
        self.__marked = [False] * g.V  # has dfs() visited this vertex?
        self.__edgeTo = [None] * g.V  # last vertex on known path to this vertex
        self.__s = s  # source vertex
        self.dfs(g, s)  # doing dfs right in the constructor

    def dfs(self, g: Graph, v: int) -> None:
        self.__marked[v] = True  # mark the vertex
        for w in g.adj(v):  # see the vertices adjacent to v
            if self.__marked[w] is False:  # if not visited yet
                self.__edgeTo[w] = v
                self.dfs(g, w)

    def hasPathTo(self, v: int) -> bool:
        return self.__marked[v]

    def pathTo(self, v: int) -> Stack:
        if self.hasPathTo(v) is False:
            return None
        path = Stack()
        while v != self.__s:
            path.push(v)
            v = self.__edgeTo[v]
        path.push(self.__s)
        return path


def hasCycle(g: Graph) -> bool:
    for v in range(g.V):
        initial_list = g.graph_adjacency[v]
        for item in initial_list:
            list_2 = g.graph_adjacency[item]
            if item not in list_2:
                for third_item in list_2:
                    if third_item != v:
                        list_3 = g.graph_adjacency[third_item]
                        if v in list_3:
                            return True
    return False


graph_ex = Graph("data/example_G.txt")
assert(hasCycle(graph_ex) == True)

graph_tc_1 = Graph("data/tc_1.txt")
assert(hasCycle(graph_tc_1) == True)

graph_tc_2 = Graph("data/tc_2.txt")
assert(hasCycle(graph_tc_2) == True)

graph_tc_3 = Graph("data/tc_3.txt")
assert(hasCycle(graph_tc_3) == False)