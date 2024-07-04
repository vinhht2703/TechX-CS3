from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, vertex1, vertex2):

        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def bfs(self, node):
        visited = set()
        queue = deque([node])

        while queue:

            vertex = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
            
                for nei in self.graph[vertex]:
                    if nei not in visited:
                        queue.append(nei)

graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(0,8)
graph.addEdge(2,3)
graph.addEdge(2,4)
graph.addEdge(2,6)
graph.addEdge(6,7)
graph.addEdge(6,5)
graph.addEdge(7,8)

graph.bfs(0)
