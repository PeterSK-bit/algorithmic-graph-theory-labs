from graph.graph import Graph

class EulerianTrail:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.trail = []

        if not self.has_eulerian_trail():
            raise ValueError("The graph does not have an Eulerian trail.")
    
    def __str__(self):
        return " -> ".join(map(str, self.trail))

    def has_eulerian_trail(self):
        self.odd_degree_vertices = [v for v in self.graph.vertices if len(self.graph.get_neighbors(v)) % 2 != 0]
        return len(self.odd_degree_vertices) in (0, 2)

    def insertion_solve(self, start_vertex: int) -> list[int]:
        if not self.graph.contains_vertex(start_vertex):
            raise ValueError("Start vertex is not in the graph.")

        if len(self.odd_degree_vertices) == 2 and start_vertex not in self.odd_degree_vertices:
            raise ValueError(
                f"Graph has 2 odd vertices ({self.odd_degree_vertices}). "
                f"Trail must start at one of them."
            )
        
        unvisited_edges = {frozenset((edge.u, edge.v)) for edge in self.graph.get_edges()}

        self.trail = self._build_cycle(start_vertex, unvisited_edges)

        i = 0
        while unvisited_edges:
            while i < len(self.trail):
                vertex = self.trail[i]
                if self._has_unvisited_edge(vertex, unvisited_edges):
                    break
                i += 1
            else:
                raise RuntimeError("Unvisited edges remain but no insertion point found.")

            new_cycle = self._build_cycle(vertex, unvisited_edges)
            self.trail = self.trail[:i] + new_cycle + self.trail[i + 1:]
            i = 0

        return self.trail

    def _has_unvisited_edge(self, vertex: int, unvisited_edges: set[frozenset[int]]) -> bool:
        """Check if vertex has any edge remaining in unvisited_edges."""
        for edge in unvisited_edges:
            if vertex in edge:
                return True
        return False

    def _build_cycle(self, start: int, unvisited_edges: set[frozenset[int]]) -> list[int]:
        """Follow unused edges until returning to start (or getting stuck)."""
        current = start
        cycle = [current]

        while True:
            next_vertex = None
            edge_to_remove = None

            for edge in unvisited_edges:
                if current in edge:
                    u, v = tuple(edge)
                    next_vertex = v if u == current else u
                    edge_to_remove = edge
                    break

            if next_vertex is None:
                break

            unvisited_edges.remove(edge_to_remove)
            cycle.append(next_vertex)
            current = next_vertex

        return cycle
    
    def labyrinth_solve(self, start_vertex: int) -> list[int]:
        if not self.graph.contains_vertex(start_vertex):
            raise ValueError("Start vertex is not in the graph.")

        if self.odd_degree_vertices:
            raise ValueError(
                f"Labyrinth algorithm requires all vertices to have even degree. "
                f"Odd vertices: {self.odd_degree_vertices}"
            )

        class EdgeState:
            __slots__ = ('edge', 'u_to_v', 'v_to_u', 'first_arrival_for')
            def __init__(self, edge):
                self.edge = edge
                self.u_to_v = False
                self.v_to_u = False
                self.first_arrival_for = None

        edge_states = {id(e): EdgeState(e) for e in self.graph.get_edges()}

        def st(edge) -> EdgeState:
            return edge_states[id(edge)]

        # only for faster lookup
        adj = {v: [] for v in self.graph.vertices}
        for e in self.graph.get_edges():
            adj[e.u].append(e)
            adj[e.v].append(e)

        def can_traverse(edge, frm) -> int | False:
            """Can we go from frm to the other endpoint?"""
            s = st(edge)
            if frm == edge.u:
                return not s.u_to_v
            elif frm == edge.v:
                return not s.v_to_u
            return False

        def traverse(edge, frm) -> int:
            """Mark traversal from frm, return destination vertex."""
            s = st(edge)
            if frm == edge.u:
                s.u_to_v = True
                return edge.v
            else:
                s.v_to_u = True
                return edge.u

        def use_count(edge):
            """How many times this undirected edge was used (0, 1, or 2)."""
            s = st(edge)
            return int(s.u_to_v) + int(s.v_to_u)

        visited = {v: False for v in self.graph.vertices}
        visited[start_vertex] = True

        S = [start_vertex] # only used for debugging, not needed for algorithm itself
        w = start_vertex

        backward_seq = []

        while True:
            incident = adj[w]
            chosen_edge = None
            chosen_v = None

            # unused edges
            for edge in incident:
                if use_count(edge) == 0 and can_traverse(edge, w):
                    chosen_edge = edge
                    chosen_v = traverse(edge, w)
                    break

            # edges used once
            if chosen_edge is None:
                for edge in incident:
                    s = st(edge)
                    if can_traverse(edge, w) and s.first_arrival_for is None:
                        chosen_edge = edge
                        chosen_v = traverse(edge, w)
                        break

            # first arrival edge
            if chosen_edge is None:
                for edge in incident:
                    s = st(edge)
                    if s.first_arrival_for is not None and can_traverse(edge, w):
                        if s.first_arrival_for == w:
                            chosen_edge = edge
                            chosen_v = traverse(edge, w)
                            break

            if chosen_edge is None:
                break

            S.append(chosen_v)

            if use_count(chosen_edge) == 2:
                backward_seq.append(chosen_edge)

            if not visited[chosen_v]:
                visited[chosen_v] = True
                st(chosen_edge).first_arrival_for = chosen_v

            w = chosen_v

        # reconstruction of trail
        self.trail = [start_vertex]
        for edge in reversed(backward_seq):
            cur = self.trail[-1]
            if edge.u == cur:
                self.trail.append(edge.v)
            elif edge.v == cur:
                self.trail.append(edge.u)
            else:
                raise RuntimeError(
                    f"Trail broken at vertex {cur}: cannot follow edge {{{edge.u},{edge.v}}}"
                )
            
        return self.trail