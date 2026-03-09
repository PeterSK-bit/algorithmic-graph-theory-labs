from basics import *

class FloydAlgorithm:
    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.dist: list[list[float]] = [[float('inf')] * graph.num_vertices for _ in range(graph.num_vertices)]
        self.next: list[list[int | None]] = [[None] * graph.num_vertices for _ in range(graph.num_vertices)]

        # Distance setup
        for i in range(graph.num_vertices):
            self.dist[i][i] = 0
        
        for u in range(1, graph.num_vertices + 1):
            for v, weight in graph.get_neighbors(u):
                self.dist[u - 1][v.number - 1] = weight

        # Next setup
        for i in range(graph.num_vertices):
            self.next[i][i] = i + 1

        for u in range(1, graph.num_vertices + 1):
            for v, weight in graph.get_neighbors(u):
                self.next[u - 1][v.number - 1] = v.number

    def run(self) -> None:
        for k in range(self.graph.num_vertices):
            for i in range(self.graph.num_vertices):
                for j in range(self.graph.num_vertices):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next[i][j] = self.next[i][k]

    def get_shortest_path(self, u: int, v: int) -> tuple[float, list[int]] | None:
        distance = self.dist[u - 1][v - 1]
        if distance != float('inf'):
            path = [u]
            while u != v:
                u = self.next[u][v] - 1
                path.append(u)
            return distance, path
        return None