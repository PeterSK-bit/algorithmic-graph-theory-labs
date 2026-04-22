from data_loader.graph_loader import GraphLoader

from time_planning import TimePlanning

def main():
    activity_digraph = GraphLoader.load("data/activity_digraph.json")
    tp = TimePlanning(activity_digraph)
    print(tp)

if __name__ == "__main__":
    main()