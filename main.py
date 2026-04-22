from file_loader import load_file
from digraph.parser import Parser

from time_planning import TimePlanning

def main():
    parser = Parser(load_file("data/graph2.txt"))
    g = parser.parse_to_graph()
    activities = parser.parse_to_activities() #TODO implement this method
    tp = TimePlanning(g, activities)

if __name__ == "__main__":
    main()