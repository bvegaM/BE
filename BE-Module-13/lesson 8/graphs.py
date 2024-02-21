class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)  # For undirected graph
    
    def display(self):
        for vertex in self.vertices:
            print(vertex, "->", " -> ".join(map(str, self.vertices[vertex])))
    
    def has_path(self, start, end, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        if start == end:
            return True
        for neighbor in self.vertices[start]:
            if neighbor not in visited:
                if self.has_path(neighbor, end, visited):
                    return True
        return False

# Example usage
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

graph.display()
print("Path exists between 1 and 3:", graph.has_path(1, 3))