from file_loader import load_file
from graph.parser import Parser
from skeleton import Skeleton, SkeletonType

def main():
    parser = Parser(load_file("data/graph2.txt"))
    g = parser.parse_to_graph()
    skeleton = Skeleton(g, SkeletonType.MOST_EXPENSIVE).get_skeleton()
    print("; ".join(str(edge) for edge in skeleton.get_edges()))
    
if __name__ == "__main__":
    main()