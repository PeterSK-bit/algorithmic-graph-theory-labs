from vertex import Vertex

class Edge:
    def __init__(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.u = u
        self.v = v
        self.weight = weight
    
    def is_incident_to_vertex(self, vertex: Vertex) -> bool:
        return self.u == vertex or self.v == vertex