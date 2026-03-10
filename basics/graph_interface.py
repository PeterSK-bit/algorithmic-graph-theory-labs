from abc import ABC, abstractmethod

from basics.vertex import Vertex

class GraphInterface(ABC):
    @property
    @abstractmethod
    def num_vertices(self) -> int:
        pass

    @abstractmethod
    def get_neighbors(self, vertex: int) -> list[tuple[Vertex, int]]:
        pass