
# Write the API for BFS below
from data.adt import Queue


class BFS:
    def __init__(self, g: Graph, s: int) -> None:
        self.__marked = [False] * g.V  # has dfs() visited this vertex?
        self.__edgeTo = [None] * g.V  # last vertex on known path to this vertex
        self.__s = s  # source vertex
        self.queue = Queue()
        self.bfs(g,s)
    def bfs(self, g: Graph, v: int) -> None:
        self.queue.enqueue(v)
        self.__marked[v] = True

        while not self.queue.isEmpty():
            v = self.queue.dequeue()
            for w in g.adj(v):
                if self.__marked[w] is False:
                    self.queue.enqueue(w)
                    self.__marked[w] = True

    # Write your code here

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
for i in range(1,6):
  print(i)