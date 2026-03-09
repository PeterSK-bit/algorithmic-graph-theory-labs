from file_loader import load_file
from digraph.parser import Parser
from label_set_algorithm import LabelSetAlgorithm

def main():
    parser = Parser(load_file("graphs/digraph.txt"))
    g = parser.parse_to_graph()
    label_set = LabelSetAlgorithm(g)
    label_set.run(5)
    print("Shortest path from 5 to 3:", label_set.get_shortest_path(3))
    print("Shortest path from 5 to 1:", label_set.get_shortest_path(1))
    print("Shortest path from 5 to 6:", label_set.get_shortest_path(6))
    print("Shortest path from 5 to 7:", label_set.get_shortest_path(7))

if __name__ == "__main__":
    main()