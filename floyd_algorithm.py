from basics.graph_interface import GraphInterface

class FloydAlgorithm:
    def __init__(self, graph: GraphInterface) -> None:
        self.graph: GraphInterface = graph
        self.dist: list[list[float]] = [[float('inf')] * graph.num_vertices for _ in range(graph.num_vertices)]
        self.next: list[list[int | None]] = [[None] * graph.num_vertices for _ in range(graph.num_vertices)]

        # Distance setup
        for i in range(graph.num_vertices):
            self.dist[i][i] = 0

        for u in range(1, graph.num_vertices + 1):
            for v, weight in graph.get_neighbors(u):
                self.dist[u-1][v.number-1] = weight
                self.next[u-1][v.number-1] = v.number

    def run(self) -> None:
        for k in range(self.graph.num_vertices):
            for i in range(self.graph.num_vertices):
                for j in range(self.graph.num_vertices):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next[i][j] = self.next[i][k]

    def get_shortest_path(self, u: int, v: int) -> tuple[float, list[int]]:
        distance = self.dist[u - 1][v - 1]

        if distance == float('inf'):
            return float('inf'), []

        path = [u]

        while u != v:
            u = self.next[u - 1][v - 1]
            path.append(u)

        return distance, path
    
    def print_distance_matrix(self) -> None:
        for row in self.dist:
            print(" ".join(f"{dist:7}" if dist != float('inf') else "   inf" for dist in row))
    
    def print_next_matrix(self) -> None:
        for row in self.next:
            print(" ".join(f"{next_vertex:7}" if next_vertex is not None else "   None" for next_vertex in row))