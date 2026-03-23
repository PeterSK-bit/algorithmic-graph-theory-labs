from typing import Optional


class Vertex:
    def __init__(self, number: int) -> None:
        self.number = number
        self.ti: float = float('inf')
        self.xi: Optional[Vertex] = None

    def __lt__(self, other):
        return self.ti < other.ti
    
    def __str__(self) -> str:
        return f"Vertex({self.number})"