from vertex import Vertex

class Edge:
    def __init__(self, u: Vertex, v: Vertex, weight: int = 1) -> None:
        self.u = u
        self.v = v
        self.weight = weight