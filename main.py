from file_loader import load_file
from basics.parser import Parser
from floyd_algorithm import FloydAlgorithm

def main():
    parser = Parser(load_file("graphs/graph1.txt"))
    g = parser.parse_to_graph()
    floyd = FloydAlgorithm(g)
    floyd.run()
    print("Shortest path from 1 to 3:", floyd.get_shortest_path(1, 3))

if __name__ == "__main__":
    main()