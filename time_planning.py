from typing import Optional

from digraph.activity_digraph import ActivityDigraph


class TimePlanning:
    def __init__(self, activity_digraph: "ActivityDigraph"):
        self.digraph = activity_digraph
        self._check_data_consistency()
        self._compute_cpm()

    def _check_data_consistency(self):
        activity_ids = {act.id for act in self.digraph.activities}
        for act in self.digraph.activities:
            for succ in act.successors:
                if succ not in activity_ids:
                    raise ValueError(f"Activity {act.id} has undefined successor {succ}")

    def _topological_sort(self) -> list[int]:
        in_degree = {
            act.id: len(self.digraph.get_predecessors(act.id))
            for act in self.digraph.activities
        }
        queue = [act_id for act_id, deg in in_degree.items() if deg == 0]
        result = []

        while queue:
            u = queue.pop(0)
            result.append(u)
            for v in self.digraph.get_successors(u):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(result) != len(self.digraph.activities):
            raise ValueError("Cycle detected in activity graph")

        return result

    def _compute_cpm(self):
        topo_order = self._topological_sort()

        # Forward pass: ES, EF
        for act_id in topo_order:
            act = self.digraph.get_activity(act_id)
            preds = self.digraph.get_predecessors(act_id)
            if not preds:
                act.es = 0
            else:
                act.es = max(self.digraph.get_activity(p).ef for p in preds)
            act.ef = act.es + act.duration

        self.project_duration = max(act.ef for act in self.digraph.activities)

        # Backward pass: LF, LS, slack
        for act in self.digraph.activities:
            act.lf = self.project_duration

        for act_id in reversed(topo_order):
            act = self.digraph.get_activity(act_id)
            succs = self.digraph.get_successors(act_id)
            if succs:
                act.lf = min(self.digraph.get_activity(s).ls for s in succs)
            act.ls = act.lf - act.duration
            act.slack = act.ls - act.es
            act.is_critical = (act.slack == 0)

    def get_earliest_start(self, activity_id: int) -> int:
        return self.digraph.get_activity(activity_id).es

    def get_earliest_finish(self, activity_id: int) -> int:
        return self.digraph.get_activity(activity_id).ef

    def get_latest_start(self, activity_id: int) -> int:
        return self.digraph.get_activity(activity_id).ls

    def get_latest_finish(self, activity_id: int) -> int:
        return self.digraph.get_activity(activity_id).lf

    def get_time_reserve(self, activity_id: int) -> int:
        return self.digraph.get_activity(activity_id).slack

    def is_critical(self, activity_id: int) -> bool:
        return self.digraph.get_activity(activity_id).is_critical

    def get_critical_path(self) -> list[int]:
        sources = self.digraph.sources
        sinks = self.digraph.sinks

        def dfs(current: int, path: list[int]) -> Optional[list[int]]:
            if current in sinks and self.digraph.get_activity(current).is_critical:
                return path + [current]

            for succ in self.digraph.get_successors(current):
                if self.digraph.get_activity(succ).is_critical:
                    result = dfs(succ, path + [current])
                    if result:
                        return result
            return None

        for source in sources:
            if self.digraph.get_activity(source).is_critical:
                path = dfs(source, [])
                if path:
                    return path
        return []

    def get_project_duration(self) -> int:
        return self.project_duration

    def get_activity_table(self) -> dict:
        """Return full CPM data for all activities."""
        return {
            act.id: {
                "duration": act.duration,
                "successors": act.successors,
                "es": act.es,
                "ef": act.ef,
                "ls": act.ls,
                "lf": act.lf,
                "slack": act.slack,
                "critical": act.is_critical,
            }
            for act in self.digraph.activities
        }

    def __str__(self) -> str:
        lines = ["CPM Analysis:", f"Project duration: {self.project_duration}", ""]
        lines.append(
            f"{'ID':>4} {'Dur':>4} {'ES':>4} {'EF':>4} {'LS':>4} {'LF':>4} {'Slack':>6} {'Critical':>8}"
        )
        lines.append("-" * 50)

        for act in sorted(self.digraph.activities, key=lambda a: a.id):
            crit = "YES" if act.is_critical else ""
            lines.append(
                f"{act.id:>4} {act.duration:>4} {act.es:>4} {act.ef:>4} "
                f"{act.ls:>4} {act.lf:>4} {act.slack:>6} {crit:>8}"
            )

        path = self.get_critical_path()
        lines.append("")
        lines.append(f"Critical path: {' -> '.join(str(x) for x in path)}")

        return "\n".join(lines)