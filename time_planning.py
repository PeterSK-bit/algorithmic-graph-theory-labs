from typing import Optional

from digraph.activity_digraph import ActivityDigraph, Activity


class TimePlanning:
    def __init__(self, activity_digraph: ActivityDigraph):
        self.digraph = activity_digraph
        
        self.activities: dict[int, Activity] = {}
        for act in activity_digraph.activities:
            if not isinstance(act, Activity):
                act = Activity(act.id, act.duration, act.depends_on)
            self.activities[act.id] = act
        
        self.successors: dict[int, list[int]] = {act.id: [] for act in self.activities.values()}
        for act in self.activities.values():
            for dep in act.depends_on:
                self.successors[dep].append(act.id)
        
        self._check_data_consistency()
        self._compute_cpm()

    def _check_data_consistency(self):
        vertices = set(self.digraph.vertices)
        activities = set(self.activities.keys())

        missing_in_digraph = activities - vertices
        if missing_in_digraph:
            raise ValueError(f"Activities {sorted(missing_in_digraph)} are not in the digraph vertices.")

        missing_in_activities = vertices - activities
        if missing_in_activities:
            raise ValueError(f"Vertices {sorted(missing_in_activities)} have no duration data.")

    def _get_sources(self) -> list[int]:
        """Find activities with no predecessors (sources)."""
        return [act_id for act_id, act in self.activities.items() if not act.depends_on]

    def _get_sinks(self) -> list[int]:
        """Find activities with no successors (sinks)."""
        return [act_id for act_id, succs in self.successors.items() if not succs]

    def _topological_sort(self) -> list[int]:
        """Kahn's algorithm for topological ordering."""
        in_degree = {act_id: len(act.depends_on) for act_id, act in self.activities.items()}
        queue = [act_id for act_id, deg in in_degree.items() if deg == 0]
        result = []
        
        while queue:
            u = queue.pop(0)
            result.append(u)
            for v in self.successors[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        if len(result) != len(self.activities):
            raise ValueError("Cycle detected in activity graph")
        
        return result

    def _compute_cpm(self):
        """Compute ES, EF, LS, LF, slack, and critical path."""
        topo_order = self._topological_sort()
        
        # Forward pass: ES and EF
        for act_id in topo_order:
            act = self.activities[act_id]
            if not act.depends_on:
                act.es = 0
            else:
                act.es = max(
                    self.activities[dep].ef 
                    for dep in act.depends_on
                )
            act.ef = act.es + act.duration
        
        # Project duration
        self.project_duration = max(act.ef for act in self.activities.values())
        
        # Backward pass: LS and LF
        # Initialize LF to project duration for all, then tighten
        for act in self.activities.values():
            act.lf = self.project_duration
        
        # Process in reverse topological order
        for act_id in reversed(topo_order):
            act = self.activities[act_id]
            if self.successors[act_id]:
                act.lf = min(
                    self.activities[succ].ls 
                    for succ in self.successors[act_id]
                )
            act.ls = act.lf - act.duration
            act.slack = act.ls - act.es
            act.is_critical = (act.slack == 0)

    def get_earliest_start(self, activity_id: int) -> int:
        """ES: Earliest possible start time."""
        return self.activities[activity_id].es

    def get_earliest_finish(self, activity_id: int) -> int:
        """EF: Earliest possible finish time."""
        return self.activities[activity_id].ef

    def get_latest_start(self, activity_id: int) -> int:
        """LS: Latest necessary start time (without delaying project)."""
        return self.activities[activity_id].ls

    def get_latest_finish(self, activity_id: int) -> int:
        """LF: Latest necessary finish time (without delaying project)."""
        return self.activities[activity_id].lf

    def get_time_reserve(self, activity_id: int) -> int:
        """Slack / Float: How much an activity can be delayed without affecting project end."""
        return self.activities[activity_id].slack

    def is_critical(self, activity_id: int) -> bool:
        """Whether activity is on the critical path (zero slack)."""
        return self.activities[activity_id].is_critical

    def get_critical_path(self) -> list[int]:
        """Return the critical path as a list of activity IDs."""
        sources = self._get_sources()
        sinks = self._get_sinks()
        
        def dfs(current: int, path: list[int]) -> Optional[list[int]]:
            if current in sinks and self.activities[current].is_critical:
                return path + [current]
            
            for succ in self.successors[current]:
                if self.activities[succ].is_critical:
                    result = dfs(succ, path + [current])
                    if result:
                        return result
            return None
        
        for source in sources:
            if self.activities[source].is_critical:
                path = dfs(source, [])
                if path:
                    return path
        
        return []

    def get_project_duration(self) -> int:
        """Total project duration (length of critical path)."""
        return self.project_duration

    def get_activity_table(self) -> dict:
        """Return full CPM data for all activities."""
        return {
            act_id: {
                'duration': act.duration,
                'depends_on': act.depends_on,
                'es': act.es,
                'ef': act.ef,
                'ls': act.ls,
                'lf': act.lf,
                'slack': act.slack,
                'critical': act.is_critical
            }
            for act_id, act in self.activities.items()
        }

    def __str__(self) -> str:
        lines = ["CPM Analysis:", f"Project duration: {self.project_duration}", ""]
        lines.append(f"{'ID':>4} {'Dur':>4} {'ES':>4} {'EF':>4} {'LS':>4} {'LF':>4} {'Slack':>6} {'Critical':>8}")
        lines.append("-" * 50)
        
        for act_id in sorted(self.activities.keys()):
            act = self.activities[act_id]
            crit = "YES" if act.is_critical else ""
            lines.append(
                f"{act_id:>4} {act.duration:>4} {act.es:>4} {act.ef:>4} "
                f"{act.ls:>4} {act.lf:>4} {act.slack:>6} {crit:>8}"
            )
        
        path = self.get_critical_path()
        lines.append("")
        lines.append(f"Critical path: {' -> '.join(str(x) for x in path)}")
        
        return '\n'.join(lines)