from io import TextIOWrapper

from digraph.digraph import Digraph
from digraph.oriented_edge import OrientedEdge

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
        return Digraph.from_edges([OrientedEdge(*map(int, line.split())) for line in self.file.readlines()])
        