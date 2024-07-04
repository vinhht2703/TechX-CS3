import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):

        if from_node in self.edges:
            self.edges[from_node].append(to_node)
        else:
            self.edges[from_node] = [to_node]

        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, start, end):
    visited = {start: 0}
    path = {}
    heap = [(0, start)]
    nodes = set(graph.nodes)

    while nodes and heap:

        current_weight, min_node = heapq.heappop(heap)

        try:
            nodes.remove(min_node)
        except KeyError:
            pass

        for edge in graph.edges.get(min_node, []):

            weight = current_weight + graph.distances[(min_node, edge)]

            if edge not in visited or weight < visited[edge]:

                visited[edge] = weight
                path[edge] = min_node
                heapq.heappush(heap, (weight, edge))

    route = []
    
    while end != start:
        
        if end in path:
            route.append(end)
            end = path[end]
        else:
            print("Không có đường đi")
            return None
    route.append(start)
    route.reverse()
    return route, visited[route[-1]]


grap = Graph()
grap.add_node('A')
grap.add_node('B')
grap.add_node('C')
grap.add_node('D')
grap.add_node('E')
grap.add_node('F')

grap.add_edge('A', 'B', 2)
grap.add_edge('A', 'C', 4)  
grap.add_edge('B', 'D', 9)
grap.add_edge('B', 'C', 1)
grap.add_edge('D', 'F', 1)
grap.add_edge('C', 'E', 3)
grap.add_edge('E', 'D', 2)
grap.add_edge('E', 'F', 5)

routes, total = dijkstra(grap, 'A', 'F')
print(f' {routes}: time={total}')


# directed => có hướng
# A - B : 2
# A - C : 4
# test = {("A", "B"): 2, ("A", "C"): 4}