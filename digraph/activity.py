class Activity:
    def __init__(self, id: int, duration: int, successors: list[int]) -> None:
        self.id = id
        self.duration = duration
        self.successors = successors

        es: int = 0  # Earliest Start
        ef: int = 0  # Earliest Finish
        ls: int = 0  # Latest Start
        lf: int = 0  # Latest Finish
        slack: int = 0  # Time Reserve
        is_critical: bool = False