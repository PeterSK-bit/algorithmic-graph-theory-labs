from digraph.digraph import Digraph
from digraph.flow_edge import FlowEdge

class FlowDigraph(Digraph):
    """
    Directed graph specialised for network-flow algorithms.
    Automatically constructs the residual reverse edges.
    """

    def __init__(self, vertices: list[int], edges: list[FlowEdge]) -> None:
        residual_edges: list[FlowEdge] = []
        for e in edges:
            rev = FlowEdge(e.v, e.u, weight=e.weight, capacity=0)
            e.rev = rev
            rev.rev = e
            residual_edges.append(rev)

        all_edges = edges + residual_edges
        super().__init__(vertices, all_edges)

        self.forward_edges = edges
    
    def get_edges(self) -> tuple[FlowEdge]:
        return tuple(self.forward_edges)