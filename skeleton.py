from enum import Enum

from basics.graph_interface import GraphInterface
from basics.edge_interface import EdgeInterface

class SkeletonType(Enum):
    CHEAPEST = 1
    MOST_EXPENSIVE = 2

class Skeleton:
    def __init__(self, graph: GraphInterface, skeleton_type: SkeletonType):
        self.graph: GraphInterface = graph
        self.skeleton_type: SkeletonType = skeleton_type
        self.skeleton: GraphInterface = self.initialize_skeleton()

    def initialize_skeleton(self) -> GraphInterface:
        edges = self.graph.get_edges()

        match self.skeleton_type:
            case SkeletonType.CHEAPEST:
                sorted_edges = sorted(edges, key=lambda e: e.weight)
            case SkeletonType.MOST_EXPENSIVE:
                sorted_edges = sorted(edges, key=lambda e: e.weight, reverse=True)
            case _:
                raise ValueError("Invalid skeleton type")
            
        num_of_vertices: int = 0
        roots: dict[int, list[EdgeInterface]] = {
            index + 1 : [edge] for index, edge in enumerate(sorted_edges)
        }

        for k, v in roots.items():
            print(f"{k}: {[edge.weight for edge in v]}")
        


    def get_skeleton(self) -> GraphInterface:
        return self.skeleton