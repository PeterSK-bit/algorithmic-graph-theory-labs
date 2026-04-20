from io import TextIOWrapper

from digraph.digraph import Digraph
from digraph.oriented_edge import OrientedEdge
from basics.vertex import Vertex

class Parser:
    def __init__(self, file: TextIOWrapper):
        self.file = file

    def find_biggest_vertex_number(self) -> int:
        biggest_number = -1

        for line in self.file.readlines():
            u, v, weight = map(int, line.split())
            biggest_number = max(biggest_number, u, v)
        
        self.file.seek(0)
        return biggest_number

    def parse_to_graph(self) -> Digraph:
        edges = []
        for line in self.file.readlines():
            u, v, weight = map(int, line.split())
            edges.append(OrientedEdge(Vertex(u), Vertex(v), weight))
        return Digraph.from_edges(edges)
    
    def parse_to_activities(self) -> dict[int, int]:
        activities = {}
        for line in self.file.readlines():
            u, v, weight = map(int, line.split())
            activities[u] = weight
        return activities