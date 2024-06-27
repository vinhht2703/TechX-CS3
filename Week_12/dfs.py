class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]

    def dfs(self, node, visited=None):  #  8
        if visited is None:
            visited = set()  # [5,6,2,3,4,0,1,7]

        visited.add(node)  # {2, 0 ,1,...}
        print(node)
        for neighbor in self.graph.get(node, []):  # [0,7]
            if neighbor not in visited:
                self.dfs(neighbor, visited)  # deque


# 1: [2,3,5]

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(0, 8)
graph.addEdge(2, 3)
graph.addEdge(2, 4)
graph.addEdge(2, 6)
graph.addEdge(6, 7)
graph.addEdge(6, 5)
graph.addEdge(7, 8)

# print(graph)
graph.dfs(0)
