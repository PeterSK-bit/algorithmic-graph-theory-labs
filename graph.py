from vertex import Vertex
from edge import Edge

class Graph:
    def __init__(self, num_vertices: int = -1) -> None:
        self.vertices: list[Vertex] = []
        self.edges: list[Edge] = []
        
        if num_vertices > 0:
            for i in range(1, num_vertices + 1):
                self.vertices.append(Vertex(i))

    def add_edge_by_numbers(self, u: int, v: int, weight: int = 1) -> None:
        vertex_u = self.get_vertex_by_number(u)
        vertex_v = self.get_vertex_by_number(v)

        if vertex_u and vertex_v:
            self.add_edge(vertex_u, vertex_v, weight)
    
    def get_vertex_by_number(self, number: int) -> Vertex | None:
        for vertex in self.vertices:
            if vertex.number == number:
                return vertex
        print(f"Vertex with number {number} not found.")
        return None
    
    def add_edge(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.edges.append(Edge(u, v, weight))
    
    def vertex_degree(self, vertex: Vertex) -> int:
        degree = 0
        for edge in self.edges:
            if edge.is_incident_to_vertex(vertex):
                degree += 1
        return degree
    
    def print_valence_info(self) -> None:
        for vertex in self.vertices:
            print(f"Vertex {vertex.number} has degree {self.vertex_degree(vertex)}")
    
    def print_neighboring_edges(self, vertex: Vertex) -> None:
        print(f"Neighboring edges of vertex {vertex.number}:")
        for edge in self.edges:
            if edge.is_incident_to_vertex(vertex):
                #print(f"  Edge between {edge.u.number} and {edge.v.number} with weight {edge.weight}")
                print(f"{{{edge.u.number}, {edge.v.number}}}", end=" ")
        print()
    
    def print_info(self) -> None:
        print(f"Number of vertices: {len(self.vertices)}")
        print(f"Number of edges: {len(self.edges)}")