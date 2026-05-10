from digraph.flow_digraph import FlowDigraph
from digraph.flow_edge import FlowEdge

from collections import deque

class NetworkFlow:
    def __init__(self, graph: FlowDigraph) -> None:
        self.graph = graph

        self.incident_edges: dict[int, list[FlowEdge]] = {v: [] for v in self.graph.get_vertices()}
        for edge in self.graph.get_edges():
            self.incident_edges[edge.u].append(edge)
            self.incident_edges[edge.v].append(edge)

    def solve_ford_fulkerson(self, source: int, sink: int) -> int:
        if source not in self.graph.get_vertices() or sink not in self.graph.get_vertices():
            raise ValueError("Source and sink must be vertices in the graph.")
        if source == sink:
            return 0

        max_flow = 0

        while True:
            x = {v: float('inf') for v in self.graph.get_vertices()}
            x[source] = 0

            parent_edge: dict[int, tuple[FlowEdge, bool]] = {}

            E = deque([source])

            # search for an augmenting path
            while E:
                r = E.popleft()

                for edge in self.incident_edges[r]:
                    if edge.u == r:
                        # right direction
                        residual = edge.capacity - edge.flow
                        if residual > 0 and x[edge.v] == float('inf'):
                            x[edge.v] = r
                            parent_edge[edge.v] = (edge, True)
                            E.append(edge.v)
                    else:
                        # reverse direction
                        if edge.flow > 0 and x[edge.u] == float('inf'):
                            x[edge.u] = -r
                            parent_edge[edge.u] = (edge, False)
                            E.append(edge.u)

                    if x[sink] != float('inf'):
                        break

            # no augmenting path, max flow reached, exit
            if x[sink] == float('inf'):
                break

            # bottleneck capacity
            bottleneck = float('inf')
            v = sink
            while v != source:
                edge, is_forward = parent_edge[v]
                if is_forward:
                    residual = edge.capacity - edge.flow
                else:
                    residual = edge.flow
                bottleneck = min(bottleneck, residual)
                v = abs(x[v])

            # augment along the path
            v = sink
            while v != source:
                edge, is_forward = parent_edge[v]
                if is_forward:
                    edge.flow += bottleneck
                else:
                    edge.flow -= bottleneck
                v = abs(x[v])

            max_flow += bottleneck

        return max_flow

    def solve_cheapest_flow(self, source, sink):
        pass