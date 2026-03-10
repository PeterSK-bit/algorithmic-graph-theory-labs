import heapq

from basics.vertex import Vertex
from digraph.digraph import Digraph

class LabelSetAlgorithm:
    def __init__(self, graph: Digraph) -> None:
        self.graph = graph

    def run(self, root: int) -> None:
        root_vertex: Vertex = self.graph.get_vertex_by_number(root)
        if root_vertex is None:
            raise ValueError(f"Vertex {root} not found in the graph.")
        
        root_vertex.ti = 0
        E = [root_vertex,]
        heapq.heapify(E)
        while E:
            r = heapq.heappop(E)
            for v, weight in self.graph.get_neighbors(r):
                if v.ti > r.ti + weight:
                    v.ti = r.ti + weight
                    v.xi = r
                    heapq.heappush(E, v)

    def get_shortest_path(self, target: int) -> tuple[int, list[int]]:
        target_vertex: Vertex = self.graph.get_vertex_by_number(target)
        if target_vertex is None:
            raise ValueError(f"Vertex {target} not found in the graph.")
        if target_vertex.ti == float('inf'):
            return float('inf'), []
        
        path = []
        current_vertex = target_vertex
        while current_vertex is not None:
            path.append(current_vertex.number)
            current_vertex = current_vertex.xi
        return target_vertex.ti, path[::-1]