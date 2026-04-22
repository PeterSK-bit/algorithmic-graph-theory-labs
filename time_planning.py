from digraph.activity_digraph import ActivityDigraph, Activity


class TimePlanning:
    def __init__(self, activity_digraph: ActivityDigraph):
        self.digraph = activity_digraph

        self.durations: dict[int, int] = {
            act.id: act.duration for act in activity_digraph.activities
        }

        self._check_data_consistency()

    def _check_data_consistency(self):
        vertices = set(self.digraph.vertices)
        activities = set(self.durations.keys())

        missing_in_digraph = activities - vertices
        if missing_in_digraph:
            raise ValueError(
                f"Activities {sorted(missing_in_digraph)} are not in the digraph vertices."
            )

        missing_in_activities = vertices - activities
        if missing_in_activities:
            raise ValueError(
                f"Vertices {sorted(missing_in_activities)} have no duration data."
            )

    def get_duration(self, activity_id: int) -> int:
        return self.durations[activity_id]

    def get_dependencies(self, activity_id: int) -> list[int]:
        for act in self.digraph.activities:
            if act.id == activity_id:
                return act.depends_on
        raise ValueError(f"Activity {activity_id} not found")