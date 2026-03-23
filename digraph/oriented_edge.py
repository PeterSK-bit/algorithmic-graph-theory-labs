from basics.edge_interface import EdgeInterface
from basics.vertex import Vertex

class OrientedEdge(EdgeInterface):
    def __init__(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self._u = u
        self._v = v
        self._weight = weight

    @property
    def u(self) -> int:
        return self._u
    
    @property
    def v(self) -> int:
        return self._v

    @property
    def weight(self):
        return self._weight
    
    def is_incident_to(self, vertex: Vertex) -> bool:
        return vertex == self.u or vertex == self.v

    def is_outgoing_from(self, vertex: Vertex) -> bool:
        return vertex == self.u

    def is_incoming_to(self, vertex: Vertex) -> bool:
        return vertex == self.v
    
    def __str__(self) -> str:
        return f"{self.u} -> {self.v} (weight: {self.weight})"