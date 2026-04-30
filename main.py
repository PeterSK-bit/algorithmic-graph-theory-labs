from data_loader.graph_loader import GraphLoader

from eulerian_trail import EulerianTrail

def main():
    graph = GraphLoader.load("data/graph3.json")
    et = EulerianTrail(graph)
    et.labyrinth_solve(1)
    print(et)

if __name__ == "__main__":
    main()