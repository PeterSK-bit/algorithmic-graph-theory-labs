from graph.graph import Graph
from graph.edge import Edge

class GraphColoring:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

        self.incident_vertices: dict[int, list[Edge]] = {v: [] for v in self.graph.get_vertices()}
        for edge in self.graph.get_edges():
            self.incident_vertices[edge.u].append(edge.v)
            self.incident_vertices[edge.v].append(edge.u)
    
    def sequential_coloring(self) -> dict[int, int]:
        coloring: dict[int, int] = {}

        for vertex in self.graph.get_vertices():
            neighbor_colors = {coloring[neighbor] for neighbor in self.incident_vertices[vertex] if neighbor in coloring}
            color = 1
            while color in neighbor_colors:
                color += 1
            coloring[vertex] = color

        return coloring
    
    def parallel_coloring(self) -> dict[int, int]:
        vertices = sorted(self.graph.get_vertices(), key=lambda v: len(self.incident_vertices[v]), reverse=True)
        coloring: dict[int, int] = {}

        for vertex in vertices:
            neighbor_colors = {coloring[neighbor] for neighbor in self.incident_vertices[vertex] if neighbor in coloring}
            color = 1
            while color in neighbor_colors:
                color += 1
            coloring[vertex] = color

        return coloring