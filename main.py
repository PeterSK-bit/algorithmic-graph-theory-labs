from file_loader import load_file
from graph.parser import Parser

from traveling_salesman import Traveling_salesman

def main():
    parser = Parser(load_file("data/graph2.txt"))
    g = parser.parse_to_graph()
    tsm = Traveling_salesman(g)
    tour = tsm.solve_greedy(1)
    print("Tour:", tour)
    
if __name__ == "__main__":
    main()