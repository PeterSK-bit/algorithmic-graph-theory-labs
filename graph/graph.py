from interfaces.graph_interface import GraphInterface

from .edge import Edge

class Graph(GraphInterface):
    def __init__(self, vertices: list[int], edges: list[Edge]) -> None:
        self.vertices = vertices
        self.edges = edges
        self._num_vertices = len(vertices)

    @classmethod
    def from_edges(cls, edges: list[Edge]) -> "Graph":
        vertices = set()
        for edge in edges:
            vertices.add(edge.u)
            vertices.add(edge.v)
        return cls(list(vertices), edges)

    @classmethod
    def from_num_vertices(cls, num_vertices: int) -> "Graph":
        return cls([i for i in range(1, num_vertices + 1)], [])

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
        if self.contains_vertex(u) and self.contains_vertex(v):
            self.add_edge(u, v, weight)

    def contains_vertex(self, number: int) -> bool:
        return any(vertex == number for vertex in self.vertices)

    def get_vertices(self):
        return self.vertices

    def get_edges(self) -> list[Edge]:
        return self.edges
    
    def get_neighbors(self, vertex: int | int) -> list[tuple[int, int]]:
        """"
        Returns a list of tuples (neighbor_vertex_number, edge_weight) for all neighbors of the given vertex.
        """
        neighbors = set()
        for edge in self.edges:
            if edge.is_incident_to(vertex):
                neighbor = edge.u if edge.v == vertex else edge.v
                neighbors.add((neighbor, edge.weight))
        return list(neighbors)