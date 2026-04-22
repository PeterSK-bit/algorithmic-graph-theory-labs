from abc import ABC, abstractmethod

from interfaces.vertex import Vertex
from interfaces.edge_interface import EdgeInterface

class GraphInterface(ABC):
    @classmethod
    @abstractmethod
    def from_edges(cls, edges: list) -> "GraphInterface":
        pass

    @classmethod
    @abstractmethod
    def from_num_vertices(cls, num_vertices: int) -> "GraphInterface":
        pass

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

    @abstractmethod
    def get_vertices(self) -> tuple[Vertex]:
        pass