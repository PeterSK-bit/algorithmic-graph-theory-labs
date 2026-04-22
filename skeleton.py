from enum import Enum

from interfaces.graph_interface import GraphInterface
from interfaces.vertex import Vertex

class SkeletonType(Enum):
    CHEAPEST = 1
    MOST_EXPENSIVE = 2

class Skeleton:
    def __init__(self, graph: GraphInterface, skeleton_type: SkeletonType):
        self.graph: GraphInterface = graph
        self.skeleton_type: SkeletonType = skeleton_type
        self.skeleton: GraphInterface = self.initialize_skeleton()

    @staticmethod
    def _find_root_key(roots: dict[int, list[Vertex]], vertex: Vertex) -> int:
        for key, vertices in roots.items():
            if vertex in vertices:
                return key
        return -1

    def initialize_skeleton(self) -> GraphInterface:
        edges = self.graph.get_edges()

        match self.skeleton_type:
            case SkeletonType.CHEAPEST:
                sorted_edges = sorted(edges, key=lambda e: e.weight)
            case SkeletonType.MOST_EXPENSIVE:
                sorted_edges = sorted(edges, key=lambda e: e.weight, reverse=True)
            case _:
                raise ValueError("Invalid skeleton type")
            
        roots: dict[int, list[Vertex]] = {
            index : [vertex] for index, vertex in enumerate(self.graph.get_vertices())
        }
        edges_in_skeleton = []

        for edge in sorted_edges:
            root_u = self._find_root_key(roots, edge.u)
            root_v = self._find_root_key(roots, edge.v)

            if root_u != root_v:
                edges_in_skeleton.append(edge)
                roots[min(root_u, root_v)] += roots[max(root_u, root_v)]
                del roots[max(root_u, root_v)]

        if len(edges_in_skeleton) != len(self.graph.get_vertices()) - 1:
            raise ValueError("The skeleton does not connect all vertices")

        return self.graph.from_edges(edges_in_skeleton)

    def get_skeleton(self) -> GraphInterface:
        return self.skeleton