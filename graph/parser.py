from io import TextIOWrapper

from basics.vertex import Vertex
from graph.edge import Edge
from .graph import Graph

class Parser:
    def __init__(self, file: TextIOWrapper) -> None:
        self.file = file

    def find_biggest_vertex_number(self) -> int:
        biggest_number = -1

        for line in self.file.readlines():
            u, v, weight = map(int, line.split())
            biggest_number = max(biggest_number, u, v)
        
        self.file.seek(0)
        return biggest_number

    def parse_to_graph(self) -> Graph:
        edges = []
        for line in self.file.readlines():
            u, v, weight = map(int, line.split())
            edges.append(Edge(Vertex(u), Vertex(v), weight))
        return Graph.from_edges(edges)