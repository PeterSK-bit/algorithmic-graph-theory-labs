from interfaces.edge_interface import EdgeInterface

class Edge(EdgeInterface):
    def __init__(self, u: int, v: int, weight: int = 1) -> None:
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
    
    def is_incident_to(self, vertex: int) -> bool:
        return self.u == vertex or self.v == vertex
    
    def __str__(self) -> str:
        return f"{self.u} --{self.weight}-- {self.v}"