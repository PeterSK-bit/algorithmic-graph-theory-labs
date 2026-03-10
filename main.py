from file_loader import load_file
from digraph.parser import Parser
from label_set_algorithm import LabelSetAlgorithm
from floyd_algorithm import FloydAlgorithm

def main():
    parser = Parser(load_file("graphs/digraph.txt"))
    g = parser.parse_to_graph()
    #label_set = LabelSetAlgorithm(g)
    #label_set.run(5)
    floyd = FloydAlgorithm(g)
    floyd.run()
    print("Shortest path from 5 to 1:", floyd.get_shortest_path(5, 1))
    floyd.print_distance_matrix()
    floyd.print_next_matrix()
    
if __name__ == "__main__":
    main()