from data_loader.graph_loader import GraphLoader

from network_flow import NetworkFlow

def main():
    graph = GraphLoader.load("data/flow_digraph.json")
    nf = NetworkFlow(graph)
    for edge in graph.get_edges():
        print(f"{edge.u} | {edge.v} | {edge.capacity=} | {edge.weight=}")


if __name__ == "__main__":
    main()