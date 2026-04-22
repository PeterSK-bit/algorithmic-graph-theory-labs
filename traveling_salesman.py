from interfaces.graph_interface import GraphInterface
from floyd_algorithm import FloydAlgorithm


class Traveling_salesman:
    def __init__(self, graph: GraphInterface):
        self._graph = graph

        self._floyd = FloydAlgorithm(graph)
        self._floyd.run()

    def solve_greedy(self, start_vertex: int) -> list[int]:
        """
        Solves the Traveling Salesman Problem using a greedy heuristic.
        Starts from the specified vertex and repeatedly visits the nearest unvisited vertex until all vertices are visited
        Algorithm is operating like graph is complete
        so it uses the distance matrix from Floyd's algorithm to find the nearest unvisited vertex at each step.
        """

        if self._graph.num_vertices <= start_vertex < 0:
            raise ValueError("Start vertex index is out of bounds.")

        unvisited = set(range(1, self._graph.num_vertices + 1))
        tour = [start_vertex]
        unvisited.remove(start_vertex )

        for _ in range(1, self._graph.num_vertices):
            last_vertex = tour[-1]
            next_vertex = None
            min_distance = float('inf')

            for vertex in unvisited:
                distance = self._floyd.distance_matrix[last_vertex - 1][vertex - 1]
                if distance < min_distance:
                    min_distance = distance
                    next_vertex = vertex

            tour.append(next_vertex)
            unvisited.remove(next_vertex)
        tour.append(start_vertex)

        print(sum(self._floyd.distance_matrix[tour[i] - 1][tour[i + 1] - 1] for i in range(len(tour) - 1)))
        return tour
    
    def solve_cheapest_insertion(self, start_vertex: int) -> list[int]:
        """
        Solves the Traveling Salesman Problem using the cheapest insertion heuristic.
        Starts from the specified vertex and repeatedly inserts the cheapest unvisited vertex into the tour until all vertices are visited.
        Algorithm is operating like graph is complete
        so it uses the distance matrix from Floyd's algorithm to find the cheapest unvisited vertex at each step.
        """

        if self._graph.num_vertices <= start_vertex < 0:
            raise ValueError("Start vertex index is out of bounds.")

        unvisited = set(range(1, self._graph.num_vertices + 1))
        tour = [start_vertex]
        unvisited.remove(start_vertex)

        next_vertex = None
        min_distance = float('inf')
        for u in unvisited:
            distance = self._floyd.distance_matrix[start_vertex - 1][u - 1]
            if distance < min_distance:
                min_distance = distance
                next_vertex = u
        
        tour.append(next_vertex)
        unvisited.remove(next_vertex)
        tour.append(start_vertex)

        while unvisited:
            distance = float('inf')
            for vertex in unvisited:
                for i in range(1, len(tour) - 1):
                    tour.insert(i, vertex)
                    if distance > sum(self._floyd.distance_matrix[tour[i] - 1][tour[i + 1] - 1] for i in range(len(tour) - 1)):
                        distance = sum(self._floyd.distance_matrix[tour[i] - 1][tour[i + 1] - 1] for i in range(len(tour) - 1))
                        next_vertex = vertex
                        index = i
                    tour.pop(i)

            tour.insert(index, next_vertex)
            unvisited.remove(next_vertex)

        print(sum(self._floyd.distance_matrix[tour[i] - 1][tour[i + 1] - 1] for i in range(len(tour) - 1)))
        return tour