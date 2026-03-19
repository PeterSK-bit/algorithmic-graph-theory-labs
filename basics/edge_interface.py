from abc import ABC, abstractmethod

from basics.vertex import Vertex

class EdgeInterface(ABC):
    @property
    @abstractmethod
    def weight(self) -> int:
        pass

    @abstractmethod
    def is_incident_to(self, vertex: Vertex) -> bool:
        pass