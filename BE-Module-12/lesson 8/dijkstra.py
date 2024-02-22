import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
    
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight  # For undirected graph
    
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]  # Priority queue of (distance, vertex)
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances

# Example usage
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 5)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 1, 2)

distances = graph.dijkstra(3)
print("Shortest distances from vertex 1:", distances)