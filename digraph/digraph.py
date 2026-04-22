from interfaces.graph_interface import GraphInterface

from digraph.oriented_edge import OrientedEdge

class Digraph(GraphInterface):
    def __init__(self, vertices: list[int], edges: list[OrientedEdge]) -> None:
        self.vertices = vertices
        self.edges = edges
        self._num_vertices = len(vertices)

    @classmethod
    def from_edges(cls, edges: list[OrientedEdge]) -> "Digraph":
        vertices = set()
        for edge in edges:
            vertices.add(edge.u)
            vertices.add(edge.v)
        return cls(list(vertices), edges)

    @classmethod
    def from_num_vertices(cls, num_vertices: int) -> "Digraph":
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

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        if self.contains_vertex(u) and self.contains_vertex(v):
            self.add_edge(u, v, weight)
    
    def contains_vertex(self, number: int) -> bool:
        return any(vertex == number for vertex in self.vertices)
    
    def get_vertices(self) -> list[int]:
        return self.vertices
    
    def get_neighbors(self, vertex: int) -> list[tuple[int, int]]:
        """
        Returns a list of tuples (neighbor_vertex_number, edge_weight) for all neighbors of the given vertex.
        """
        return [(edge.v, edge.weight) for edge in self.edges if edge.u == vertex]
    
    def vertex_degree(self, vertex: int) -> int:
        degree = 0
        for edge in self.edges:
            if edge.is_incident_to_vertex(vertex):
                degree += 1
        return degree
    
    def print_valence_info(self) -> None:
        for vertex in self.vertices:
            print(f"Vertex {vertex.number} has degree {self.vertex_degree(vertex)}")
    
    def print_neighboring_edges(self, vertex: int) -> None:
        print(f"Neighboring edges of vertex {vertex}:")
        for edge in self.edges:
            if edge.is_incident_to_vertex(vertex):
                #print(f"  Edge between {edge.u.number} and {edge.v.number} with weight {edge.weight}")
                print(f"({edge.u}, {edge.v})", end=" ")
        print()
    
    def print_info(self) -> None:
        print(f"Number of vertices: {len(self.vertices)}")
        print(f"Number of edges: {len(self.edges)}")

    """
    TODO: Move to separate class for algorithms

    def shortest_path_basic_algorithm(self, vertex: int) -> None:
        base = self.get_vertex_by_number(vertex)

        if base is None:
            print(f"Vertex with number {vertex} not found in digraph.")
            return

        base.ti = 0

        updated = True
        while updated:
            updated = False
            for edge in self.edges:
                if edge.v.ti > edge.u.ti + edge.weight:
                    edge.v.ti = edge.u.ti + edge.weight
                    edge.v.xi = edge.u
                    updated = True

        print("Shortest paths from vertex", vertex)
        for v in self.vertices:
            self._shortest_path_print(vertex, v.number)
    
    def _shortest_path_print(self, start: int, end: int) -> None:
        base = self.get_vertex_by_number(start)
        target = self.get_vertex_by_number(end)

        if base is None:
            print(f"Vertex with number {start} not found in digraph.")
            return

        if target is None:
            print(f"Vertex with number {end} not found in digraph.")
            return

        next = target.xi
        path = [target.number]

        while next is not None:
            path.append(next.number)
            next = next.xi
        
        path.reverse()

        print(f"Shortest path from vertex {start} to vertex {end}: {' -> '.join(map(str, path))} with total weight {target.ti}")
        """