from file_loader import load_file
from parser import Parser

def main():
    parser = Parser(load_file("graphs/graph1.txt"))
    g = parser.parse_to_graph()
    g.print_info()

if __name__ == "__main__":
    main()