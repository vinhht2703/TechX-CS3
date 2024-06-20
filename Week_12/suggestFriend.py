lstUser = [
    {"id": 1, "name": "Ronaldo"},
    {"id": 2, "name": "Messi"},
    {"id": 3, "name": "MP3"},
    {"id": 4, "name": "Yasuo"},
    {"id": 5, "name": "Duy"},
    {"id": 6, "name": "An"},
]


# 1: 2, 3
# 2: 4
# 3: 5, 6


class FriendRelationGraph:
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

    def getFriends(self, vertex):
        return self.graph[vertex]

    def getGraph(self):
        print(str(self.graph))

    def getFriendSuggestions(self, vertex):
        graph = self.graph
        suggestions = set()
        if vertex in graph:
            for id in graph[vertex]:
                suggestions.update(self.getFriends(id))
        
        for user in lstUser:
            curUserId = user["id"]
            if curUserId != vertex and curUserId in suggestions:
                print(user)


graph = FriendRelationGraph()
graph.addVertex(1, 2)
graph.addVertex(1, 3)
graph.addVertex(2, 4)
graph.addVertex(3, 5)
graph.addVertex(3, 6)
# graph.getGraph()
# print(graph.getFriends(1))

userId = 2
graph.getFriendSuggestions(userId)


