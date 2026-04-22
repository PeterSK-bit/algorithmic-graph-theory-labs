import heapq
from typing import Optional

from digraph.digraph import Digraph


class LabelSetAlgorithm:
    def __init__(self, graph: Digraph) -> None:
        self.graph = graph

    def run(self, root: int) -> None:
        if not self.graph.contains_vertex(root):
            raise ValueError(f"Vertex {root} not found in the graph.")

        self.ti: dict[int, float] = {v: float('inf') for v in self.graph.vertices()}
        self.xi: dict[int, Optional[int]] = {v: None for v in self.graph.vertices()}

        self.ti[root] = 0.0
        E = [(0.0, root)]

        while E:
            r_dist, r = heapq.heappop(E)

            if r_dist > self.ti[r]:
                continue

            for v, weight in self.graph.get_neighbors(r):
                new_dist = self.ti[r] + weight
                if self.ti[v] > new_dist:
                    self.ti[v] = new_dist
                    self.xi[v] = r
                    heapq.heappush(E, (self.ti[v], v))

    def get_shortest_path(self, target: int) -> tuple[float, list[int]]:
        if not self.graph.contains_vertex(target):
            raise ValueError(f"Vertex {target} not found in the graph.")
        if not hasattr(self, 'ti') or target not in self.ti:
            raise RuntimeError("Run the algorithm before querying paths.")
        if self.ti[target] == float('inf'):
            return float('inf'), []

        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.xi[current]
        return self.ti[target], path[::-1]