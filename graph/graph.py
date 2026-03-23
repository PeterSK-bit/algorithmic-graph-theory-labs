from basics.graph_interface import GraphInterface

from basics.vertex import Vertex
from .edge import Edge

class Graph(GraphInterface):
    def __init__(self, num_vertices: int = -1, edges: list[Edge] = None) -> None:
        self.edges: list[Edge] = edges if edges is not None else []
        
        if self.edges:
            self.vertices = list({v for edge in self.edges for v in (edge.u, edge.v)})
        elif num_vertices >= 0:
            self.vertices = [Vertex(i) for i in range(1, num_vertices + 1)]
        else:
            raise ValueError("Either num_vertices must be non-negative or edges must be provided.")
        
        self._num_vertices = len(self.vertices)

    @property
    def num_vertices(self) -> int:
        return self._num_vertices
    
    @num_vertices.setter
    def num_vertices(self, value: int) -> None:
        if not isinstance(value, int):
            print("Number of vertices must be an integer.")
            return
        if value < 0:
            print("Number of vertices cannot be negative.")
            return
        self._num_vertices = value

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

    def get_vertices(self):
        return self.vertices
    
    def add_edge(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.edges.append(Edge(u, v, weight))

    def get_edges(self) -> list[Edge]:
        return self.edges
    
    def vertex_degree(self, vertex: Vertex) -> int:
        degree = 0
        for edge in self.edges:
            if edge.is_incident_to_vertex(vertex):
                degree += 1
        return degree
    
    def get_neighbors(self, vertex: Vertex | int) -> list[tuple[Vertex, int]]:
        if isinstance(vertex, int):
            if ((temp:=self.get_vertex_by_number(vertex)) is None):
                print(f"Vertex with number {vertex} not found.")
                return []
            vertex = temp
        
        neighbors = []
        for edge in self.edges:
            if edge.is_incident_to_vertex(vertex):
                neighbor = edge.u if edge.v == vertex else edge.v
                if neighbor not in neighbors:
                    neighbors.append((neighbor, edge.weight))
        return neighbors
    
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