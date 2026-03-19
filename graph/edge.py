from basics.edge_interface import EdgeInterface

from basics.vertex import Vertex

class Edge(EdgeInterface):
    def __init__(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self._u = u
        self._v = v
        self._weight = weight

    @property
    def u(self):
        return self._u

    @property
    def v(self):
        return self._v

    @property
    def weight(self):
        return self._weight
    
    def is_incident_to(self, vertex: Vertex) -> bool:
        return self.u == vertex or self.v == vertex