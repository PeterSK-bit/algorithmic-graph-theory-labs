from digraph.oriented_edge import OrientedEdge


class FlowEdge(OrientedEdge):
    def __init__(self, u: int, v: int, weight: int = 1, capacity: int = 0) -> None:
        super().__init__(u, v, weight)
        self.capacity = capacity
        self.flow = 0
        self.rev: FlowEdge | None = None

    @property
    def residual(self) -> int:
        """Remaining capacity in the forward direction."""
        return self.capacity - self.flow