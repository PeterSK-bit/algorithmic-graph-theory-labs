from basics.edge_interface import EdgeInterface
from basics.vertex import Vertex

class OrientedEdge(EdgeInterface):
    def __init__(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.u = u
        self.v = v
        self._weight = weight

    @property
    def weight(self):
        return self._weight
    
    def is_incident_to(self, vertex: Vertex) -> bool:
        return vertex == self.u or vertex == self.v

    def is_outgoing_from(self, vertex: Vertex) -> bool:
        return vertex == self.u

    def is_incoming_to(self, vertex: Vertex) -> bool:
        return vertex == self.v