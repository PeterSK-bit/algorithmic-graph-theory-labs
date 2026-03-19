from basics.edge_interface import EdgeInterface

from ..basics.vertex import Vertex

class Edge(EdgeInterface):
    def __init__(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.u = u
        self.v = v
        self._weight = weight

    @property
    def weight(self):
        return self._weight
    
    def is_incident_to_vertex(self, vertex: Vertex) -> bool:
        return self.u == vertex or self.v == vertex