import json
import heapq

# Đọc file JSON
with open('./data.json', 'r') as file:
    data = json.load(file)

class Graph:
    def __init__(self):
        self.graph = {}  # Lưu trữ đồ thị dưới dạng {đỉnh: {đỉnh_kề: trọng_số}, ...}

    def add_vertex(self, key):
        if key not in self.graph:
            self.graph[key] = { "nei": {}}  # Thêm đỉnh mới với vị trí và danh sách cạnh trống

    def add_edge(self, src, dest, weight):
            # Thêm cạnh từ src đến dest với trọng số
            self.graph[src]["nei"][dest] = weight

    def load_from_json(self, data):
        for node in data:
            key = node["key"]
           
            self.add_vertex(key)
            for nei in node["nei"]:
                for dest, weight in nei.items():
                    self.add_edge(key, int(dest), weight)

    def print_graph(self):
        for vertex, info in self.graph.items():
            print(f"Đỉnh {vertex} có các cạnh: {info['nei']}")

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.graph}

        previous = {vertex: None for vertex in self.graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:

            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex == end:
                break

            for neighbor, weight in self.graph[current_vertex]["nei"].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path


# Sử dụng lớp Graph
graph = Graph()
graph.load_from_json(data)

path = graph.dijkstra(1, 11)
print(path)