from file_loader import load_file
from digraph.parser import Parser

def main():
    parser = Parser(load_file("graphs/digraph.txt"))
    g = parser.parse_to_graph()
    g.shortest_path_basic_algorithm(5)

if __name__ == "__main__":
    main()