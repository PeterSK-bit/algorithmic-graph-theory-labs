from basics.vertex import Vertex
from digraph.oriented_edge import OrtientedEdge

class Digraph:
    def __init__(self, num_vertices: int = -1) -> None:
        self.vertices: list[Vertex] = []
        self.edges: list[OrtientedEdge] = []
        
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
        self.edges.append(OrtientedEdge(u, v, weight))
    
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
                print(f"({edge.u.number}, {edge.v.number})", end=" ")
        print()
    
    def print_info(self) -> None:
        print(f"Number of vertices: {len(self.vertices)}")
        print(f"Number of edges: {len(self.edges)}")

    
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