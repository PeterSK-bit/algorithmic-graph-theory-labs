import json
from pathlib import Path
from graph.graph import Graph, Edge
from digraph.digraph import Digraph, OrientedEdge
from digraph.activity_digraph import ActivityDigraph, Activity

class GraphLoader:
    @staticmethod
    def load(path: str | Path) -> Graph | Digraph | ActivityDigraph:
        with open(path, 'r') as f:
            data = json.load(f)

        gtype = data.get("graph_structure_type")

        match gtype:
            case "graph":
                return GraphLoader._parse_graph(data)
            case "digraph":
                    return GraphLoader._parse_digraph(data)
            case "activity_digraph":
                return GraphLoader._parse_activity_digraph(data)
            case _:
                raise ValueError(f"Unknown graph_structure_type: {gtype!r}")

    @staticmethod
    def _parse_graph(data: dict) -> Graph:
        edges_data = data["edges"]
        edges = [Edge(e["u"], e["v"], e.get("weight", 1)) for e in edges_data]
        vertices = GraphLoader._extract_vertices(edges_data)
        return Graph(vertices, edges)

    @staticmethod
    def _parse_digraph(data: dict) -> Digraph:
        edges_data = data["edges"]
        edges = [OrientedEdge(e["u"], e["v"], e.get("weight", 1)) for e in edges_data]
        vertices = GraphLoader._extract_vertices(edges_data)
        return Digraph(vertices, edges)

    @staticmethod
    def _parse_activity_digraph(data: dict) -> ActivityDigraph:
        activities_data = data["activities"]
        activities = [Activity(a["id"], a["duration"], a.get("successors", [])) for a in activities_data]
        return ActivityDigraph(activities)

    @staticmethod
    def _extract_vertices(edges_data: list[dict]) -> list[int]:
        """Collect unique vertex numbers from edge list, sorted."""
        verts = set()
        for e in edges_data:
            verts.add(e["u"])
            verts.add(e["v"])
        return sorted(verts)