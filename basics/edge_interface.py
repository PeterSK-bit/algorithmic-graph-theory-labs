from abc import ABC, abstractmethod

from basics.vertex import Vertex

class EdgeInterface(ABC):
    @property
    @abstractmethod
    def u(self) -> int:
        pass

    @property
    @abstractmethod
    def v(self) -> int:
        pass

    @property
    @abstractmethod
    def weight(self) -> int:
        pass
    
    @property
    @abstractmethod
    def weight(self) -> int:
        pass

    @abstractmethod
    def is_incident_to(self, vertex: Vertex) -> bool:
        pass