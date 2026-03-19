from abc import ABC, abstractmethod

from basics.vertex import Vertex
from basics.edge_interface import EdgeInterface

class GraphInterface(ABC):
    @property
    @abstractmethod
    def num_vertices(self) -> int:
        pass

    @abstractmethod
    def get_neighbors(self, vertex: int) -> list[tuple[Vertex, int]]:
        pass

    @abstractmethod
    def get_edges(self) -> tuple[EdgeInterface]:
        pass