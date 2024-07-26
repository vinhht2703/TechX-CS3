from collections import deque

class Graph:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.numVertices = numRows * numCols
        self.adjList = [[] for _ in range(self.numVertices)]

    def addEdge(self, v1, v2):
        if v2 not in self.adjList[v1]:
            self.adjList[v1].append(v2)
        if v1 not in self.adjList[v2]:  # Đảm bảo liên kết vô hướng
            self.adjList[v2].append(v1)

    def addRectangleEdges(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                current = row * self.numCols + col
                # Kiểm tra và thêm cạnh tới đỉnh ở bên phải
                if col < self.numCols - 1:
                    self.addEdge(current, current + 1)
                # Kiểm tra và thêm cạnh tới đỉnh ở bên dưới
                if row < self.numRows - 1:
                    self.addEdge(current, current + self.numCols)

    def findAllShortestPaths(self, start, end):
        if start < 0 :
            return False

        queue = deque([[start]])
        shortest_paths = []
        visited = set([start])
        min_length = None

        while queue:
            path = queue.popleft()
            current = path[-1]

            for neighbor in self.adjList[current]:
                if neighbor in visited and (min_length is not None and len(path) >= min_length):
                    continue
                
                new_path = list(path)
                new_path.append(neighbor)

                if neighbor == end:
                    # shortest_paths.append(new_path)
                    shortest_paths.append(new_path[1]) # for game

                    min_length = len(new_path)
                else:
                    queue.append(new_path)
                    visited.add(neighbor)

        
        
        return shortest_paths

 

# Sử dụng
graph = Graph(6, 6)
graph.addRectangleEdges()

start_point = 35
end_point = 1

# Gọi hàm và in ra tất cả các đường đi ngắn nhất
paths = graph.findAllShortestPaths(start_point, end_point)

