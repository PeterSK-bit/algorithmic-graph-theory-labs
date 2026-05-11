from typing import Set
import math

from graph.graph import Graph
from floyd_algorithm import FloydAlgorithm

class CentersAndMedians:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.floyd: FloydAlgorithm = FloydAlgorithm(graph)
        self.floyd.run()

    def _assign(self, centers: Set[int], non_centers: Set[int]) -> tuple[float, float]:
        """
        For every vertex, find distance to its nearest center.
        Returns (max_distance, total_distance) over ALL vertices.
        """

        max_d = 0.0
        total_d = 0.0

        for v in non_centers:
            min_d = min(self.floyd.dist[v-1][c-1] for c in centers)
            max_d = max(max_d, min_d)
            total_d += min_d

        return max_d, total_d
    
    def _interchange(self, initial_centers: Set[int], minimize_max: bool):
        """
        Generic local search using 1-exchange neighborhood.
        minimize_max=True  -> p-center (minimize maximum distance)
        minimize_max=False -> p-median (minimize total distance)
        """
        n = self.graph.num_vertices
        centers = set(initial_centers)
        non_centers = set(range(1, n + 1)) - centers

        current_max, current_total = self._assign(centers, non_centers)
        current_obj = current_max if minimize_max else current_total

        improved = True
        while improved:
            improved = False
            best_obj = current_obj
            best_swap = None

            for c in list(centers):
                for v in list(non_centers):
                    new_centers = set(centers)
                    new_centers.remove(c)
                    new_centers.add(v)

                    new_non_centers = set(non_centers)
                    new_non_centers.remove(v)
                    new_non_centers.add(c)

                    new_max, new_total = self._assign(new_centers, new_non_centers)
                    new_obj = new_max if minimize_max else new_total

                    if new_obj < best_obj:
                        best_obj = new_obj
                        best_swap = (c, v)

            if best_swap is not None:
                c_out, v_in = best_swap
                centers.remove(c_out)
                centers.add(v_in)
                non_centers.remove(v_in)
                non_centers.add(c_out)
                current_obj = best_obj
                improved = True

        return centers, current_obj

    def find_p_median(self, p: int) -> tuple[Set[int], float]:
        if not (1 <= p <= self.graph.num_vertices):
            raise ValueError("p must be between 1 and num_vertices")

        initial = set(range(1, p + 1))
        centers, obj = self._interchange(initial, minimize_max=False)
        return centers, obj

    def find_p_center(self, p: int) -> tuple[Set[int], float]:
        if not (1 <= p <= self.graph.num_vertices):
            raise ValueError("p must be between 1 and num_vertices")

        initial = set(range(1, p + 1))
        centers, obj = self._interchange(initial, minimize_max=True)
        return centers, obj