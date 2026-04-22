class Activity:
    def __init__(self, id: int, duration: int, depends_on: list[int]) -> None:
        self.id = id
        self.duration = duration
        self.depends_on = depends_on