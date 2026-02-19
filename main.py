from file_loader import load_file
from parser import Parser

def main():
    parser = Parser(load_file("graphs/graph1.txt"))
    g = parser.parse_to_graph()
    g.print_neighboring_edges(g.get_vertex_by_number(2))

if __name__ == "__main__":
    main()