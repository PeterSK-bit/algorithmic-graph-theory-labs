from enum import Enum

from basics.graph_interface import GraphInterface

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
        
        if self.skeleton_type == SkeletonType.CHEAPEST:
            sorted_edges = sorted(edges, key=lambda e: e.weight)
        elif self.skeleton_type == SkeletonType.MOST_EXPENSIVE:
            sorted_edges = sorted(edges, key=lambda e: e.weight, reverse=True)
        else:
            raise ValueError("Invalid skeleton type")

    def get_skeleton(self) -> GraphInterface:
        return self.skeleton