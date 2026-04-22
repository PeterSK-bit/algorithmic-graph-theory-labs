class Activity:
    def __init__(self, id: int, duration: int, successors: list[int]) -> None:
        self.id = id
        self.duration = duration
        self.successors = successors

        self.es: int = 0
        self.ef: int = 0
        self.ls: int = 0
        self.lf: int = 0
        self.slack: int = 0
        self.is_critical: bool = False