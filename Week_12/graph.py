class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def getNeighbor(self, vertex):
        return self.graph[vertex]

    def getGraph(self):
        print(str(self.graph))


graph = Graph()
graph.addVertex(0, 1)
graph.addVertex(0, 2)
graph.addVertex(0, 8)
graph.addVertex(2, 3)
graph.addVertex(2, 4)
graph.addVertex(2, 6)
graph.addVertex(6, 5)
graph.addVertex(8, 7)
graph.addVertex(7, 6)

graph.getGraph()
print(graph.getNeighbor(0))