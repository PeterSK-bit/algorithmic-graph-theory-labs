from typing import Optional


class Vertex:
    def __init__(self, number: int) -> None:
        self.number = number
        self.ti: float = float('inf')
        self.xi: Optional[Vertex] = None