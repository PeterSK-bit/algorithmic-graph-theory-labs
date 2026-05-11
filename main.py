from data_loader.graph_loader import GraphLoader

from graph_coloring import GraphColoring
from network_flow import NetworkFlow
from centers_and_medians import CentersAndMedians

def main():
    """
    graph = GraphLoader.load("data/flow_digraph.json")
    nf = NetworkFlow(graph)
   
    print(nf.solve_ford_fulkerson(1, 6))
    for edge in graph.get_edges():
        print(f"Edge {edge.u} -> {edge.v}: flow = {edge.flow} / capacity = {edge.capacity}")
    
    print(nf.solve_cheapest_flow(1, 6))
    """
    
    """
    graph = GraphLoader.load("data/graph_coloring.json")
    gc = GraphColoring(graph)
    print("Sequential Coloring:")
    print(gc.sequential_coloring())
    print("Parallel Coloring:")
    print(gc.parallel_coloring())
    """
    
    """
    graph = GraphLoader.load("data/centers_and_medians.json")
    cam = CentersAndMedians(graph)
    print("P-Median Solution:")
    centers, total_distance = cam.find_p_median(p=2)
    print(f"Centers: {centers}, Total Distance: {total_distance}")
    print("P-Center Solution:")
    centers, max_distance = cam.find_p_center(p=2)
    print(f"Centers: {centers}, Maximum Distance: {max_distance}")
    """


if __name__ == "__main__":
    main()