from interfaces.edge_interface import EdgeInterface

class OrientedEdge(EdgeInterface):
    def __init__(self, u: int, v: int, weight: int = 1) -> None:
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
    
    def is_incident_to(self, vertex: int) -> bool:
        return vertex == self.u or vertex == self.v

    def is_outgoing_from(self, vertex: int) -> bool:
        return vertex == self.u

    def is_incoming_to(self, vertex: int) -> bool:
        return vertex == self.v
    
    def __str__(self) -> str:
        return f"{self.u} --{self.weight}-> {self.v}"