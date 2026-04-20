from digraph import Digraph

class TimePlanning:
    def __init__(self, digraph: Digraph, activities: dict[int, int]):
        self.digraph = digraph
        self.activities = activities

        self._check_data_consistency()

    def _check_data_consistency(self):
        vertices_numbers = [v.number for v in self.digraph.get_vertices()]
        for activity in self.activities.keys():
            if activity not in vertices_numbers:
                raise ValueError(f"Activity {activity} is not in the digraph vertices.")
        vertices_numbers.remove(activity)

        if len(vertices_numbers) > 0:
            raise ValueError(f"Vertices {vertices_numbers} are not in the activities list.")
