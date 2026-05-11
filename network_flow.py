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

    def solve_cheapest_flow(self, source: int, sink: int) -> tuple[int, int]:
        """
        Cheapest maximum flow.
        Phase 1: max flow (Ford-Fulkerson).
        Phase 2: cancel negative-cost cycles in residual graph.
        Returns (max_flow_value, minimum_total_cost).
        """
        # krok 1
        max_flow = self.solve_ford_fulkerson(source, sink)

        vertices = self.graph.get_vertices()

        # krok 2
        while True:
            dist = {v: 0 for v in vertices}
            parent = {v: None for v in vertices}   # parent[v] = (prev_vertex, edge, is_forward)

            improved_node = None

            # detect negative cycle using Bellman-Ford
            for _ in range(len(vertices)):
                improved_node = None
                for u in vertices:
                    for edge in self.incident_edges[u]:
                        if edge.u == u:
                            if edge.residual > 0:
                                v = edge.v
                                nd = dist[u] + edge.weight
                                if nd < dist[v]:
                                    dist[v] = nd
                                    parent[v] = (u, edge, True)
                                    improved_node = v
                        else:
                            if edge.flow > 0:
                                v = edge.u
                                nd = dist[u] - edge.weight   # negative cost for undoing
                                if nd < dist[v]:
                                    dist[v] = nd
                                    parent[v] = (u, edge, False)
                                    improved_node = v

                if improved_node is None:
                    break

            # krok 3
            if improved_node is None:
                break

            # krok 4
            # Trace back |V| times to guarantee we are on the cycle
            cycle_node = improved_node
            for _ in range(len(vertices)):
                cycle_node = parent[cycle_node][0]

            # Extract the cycle edges
            cycle: list[tuple[FlowEdge, bool]] = []
            v = cycle_node
            while True:
                u, edge, is_forward = parent[v]
                cycle.append((edge, is_forward))
                v = u
                if v == cycle_node:
                    break

            # Find reserve (bottleneck) of the cycle
            bottleneck = float('inf')
            for edge, is_forward in cycle:
                if is_forward:
                    reserve = edge.capacity - edge.flow
                else:
                    reserve = edge.flow
                bottleneck = min(bottleneck, reserve)

            # Augment flow around the cycle
            for edge, is_forward in cycle:
                if is_forward:
                    edge.flow += bottleneck
                else:
                    edge.flow -= bottleneck


        total_cost = 0
        for edge in self.graph.get_edges():
            total_cost += edge.flow * edge.weight

        return max_flow, total_cost