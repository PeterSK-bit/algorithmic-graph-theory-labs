from digraph.activity import Activity
#from digraph.oriented_edge import OrientedEdge


class ActivityDigraph:
    def __init__(self, activities: list[Activity]) -> None:
        self._activities = activities
        
        """ NOT USED RN
        self.vertices = [a.id for a in activities]
        self._num_vertices = len(self.vertices)

        self.edges: list[OrientedEdge] = []
        for act in activities:
            for successor in act.successors:
                self.edges.append(OrientedEdge(act.id, successor))
        """

        self._predecessors: dict[int, list[int]] = {a.id: [] for a in activities}
        for act in activities:
            for succ in act.successors:
                self._predecessors[succ].append(act.id)

        self.sources = [act.id for act in self.activities if not self._predecessors[act.id]]
        self.sinks = [act.id for act in self.activities if not act.successors]
    
    @property
    def activities(self) -> list[Activity]:
        return self._activities
    
    @property
    def sources(self) -> list[int]:
        return self._sources
    
    @sources.setter
    def sources(self, value: list[int]) -> None:
        self._sources = value
    
    @property
    def sinks(self) -> list[int]:
        return self._sinks
    
    @sinks.setter
    def sinks(self, value: list[int]) -> None:
        self._sinks = value

        
    def get_activity(self, activity_id: int) -> Activity:
        for act in self._activities:
            if act.id == activity_id:
                return act
        raise ValueError(f"Activity {activity_id} not found")

    def get_predecessors(self, activity_id: int) -> list[int]:
        return self._predecessors.get(activity_id)
    
    def get_successors(self, activity_id: int) -> list[int]:
        for act in self.activities:
            if act.id == activity_id:
                return act.successors
        raise ValueError(f"Activity {activity_id} not found")