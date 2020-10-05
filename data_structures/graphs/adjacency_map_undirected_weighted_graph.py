# coding: utf-8
"""
Graph
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
https://en.wikipedia.org/wiki/Adjacency_list
"""
from collections import defaultdict

from data_structures.graphs.adjacency_map_directed_weighted_graph import DirectedGraph


class UndirectedGraph(DirectedGraph):
    def __init__(self):
        super().__init__()

        # {
        #     'source_vertex': {
        #         'destination_vertex': 'edge_weight',
        #     },
        #     'destination_vertex': {
        #         'source_vertex': 'edge_weight',
        #     }
        # }
        # NOTE: outgoing_edges of an undirected graph contains both (u, v) and (v, u) for each edge.
        self.outgoing_edges = defaultdict(dict)

    def add_edge(self, u, v, weight=None):
        # Actually, we can treat a directed graph as a undirected graph.
        # As long as we add both endpoints for the same edge, for instance, `add_edge(u, v, 1)` and `add_edge(v, u, 1)`.
        self.outgoing_edges[u][v] = weight
        self.outgoing_edges[v][u] = weight

    def remove_edge(self, u, v):
        try:
            del self.outgoing_edges[u][v]
            del self.outgoing_edges[v][u]
        except KeyError:
            raise ValueError(f'No such edge: {(u, v)} or {(v, u)}')

    def edge_count(self):
        count = 0
        for _ in self.edges():
            count += 1
        return count

    def edges(self):
        deduplicate_edges = set()
        for source, incident_edges in self.outgoing_edges.items():
            for destination, weight in incident_edges.items():
                # Make sure that (u, v) and (v, u) wouldn't both exist in the results.
                pair = sorted([source, destination])
                deduplicate_edges.add((pair[0], pair[1], weight))

        return deduplicate_edges

    def incident_edges(self, v, edge_type='outgoing'):
        for destination, weight in self.outgoing_edges[v].items():
            pair = sorted([v, destination])
            yield (pair[0], pair[1], weight)
