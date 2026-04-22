from digraph.activity import Activity
from digraph.oriented_edge import OrientedEdge


class ActivityDigraph:
    def __init__(self, activities: list[Activity]) -> None:
        self.activities = activities
        
        self.vertices = [a.id for a in activities]
        self._num_vertices = len(self.vertices)

        self.edges: list[OrientedEdge] = []
        for act in activities:
            for dep in act.depends_on:
                self.edges.append(OrientedEdge(dep, act.id))