from digraph.digraph import Digraph
from digraph.flow_edge import FlowEdge

class FlowDigraph(Digraph):
    """
    Directed graph specialised for network-flow algorithms.
    Automatically constructs the residual reverse edges.
    """

    def __init__(self, vertices: list[int], edges: list[FlowEdge]) -> None:
        super().__init__(vertices, edges)

        self.forward_edges = edges
    
    def get_edges(self) -> tuple[FlowEdge]:
        return tuple(self.forward_edges)