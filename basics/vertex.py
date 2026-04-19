from typing import Optional


class Vertex:
    def __init__(self, number: int) -> None:
        self.number = number
        self.ti: float = float('inf')
        self.xi: Optional[Vertex] = None

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)

    def __lt__(self, other):
        return self.ti < other.ti
    
    def __str__(self) -> str:
        return f"Vertex({self.number})"