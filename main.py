from data_loader.graph_loader import GraphLoader

from eulerian_trail import EulerianTrail
from graph import graph
from traveling_salesman import TravelingSalesman

def main():
    graph = GraphLoader.load("data/graph2.json")
    ts = TravelingSalesman(graph)
    print(ts.solve_cheapest_insertion(1))


if __name__ == "__main__":
    main()