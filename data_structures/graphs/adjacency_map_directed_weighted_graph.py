# coding: utf-8
"""
Graph
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
https://en.wikipedia.org/wiki/Directed_graph
https://en.wikipedia.org/wiki/Adjacency_list
"""
from collections import defaultdict


class DirectedGraph:
    def __init__(self):
        # {
        #     'source_vertex': {
        #         'destination_vertex': 'edge_weight',
        #     },
        # }
        self.outgoing_edges = defaultdict(dict)

        # {
        #     'vertex': 'data',
        # }
        self.vertex_data = {}

    def add_vertex(self, v, value=None):
        self.vertex_data[v] = value

    def add_edge(self, u, v, weight=None):
        # Make sure that both vertices are in the graph.
        self.vertex_data.setdefault(u)
        self.vertex_data.setdefault(v)
        self.outgoing_edges[u][v] = weight

    def remove_vertex(self, v):
        # Remove associate edges.
        del self.outgoing_edges[v]
        for _, incident_vertices in self.outgoing_edges.items():
            # NOTE: We use list(dict.keys()) to avoid
            # RuntimeError: dictionary changed size during iteration.
            for destination in list(incident_vertices.keys()):
                if destination == v:
                    del incident_vertices[destination]

        # Remove associate data.
        del self.vertex_data[v]

    def remove_edge(self, u, v):
        try:
            del self.outgoing_edges[u][v]
        except KeyError:
            raise ValueError(f'No such edge: {(u, v)}')

    def vertex_count(self):
        return len(self.vertex_data.keys())

    def edge_count(self):
        count = 0
        for _ in self.edges():
            count += 1
        return count

    def vertices(self):
        for vertex in self.vertex_data.keys():
            yield vertex

    def edges(self):
        for source, incident_edges in self.outgoing_edges.items():
            for destination, weight in incident_edges.items():
                yield (source, destination, weight)

    def incident_edges(self, v, edge_type='outgoing'):
        if edge_type == 'outgoing':
            try:
                for destination, weight in self.outgoing_edges[v].items():
                    yield (v, destination, weight)
            except KeyError:
                return []
        elif edge_type == 'incoming':
            for source, incident_vertices in self.outgoing_edges.items():
                for destination, weight in incident_vertices.items():
                    if destination == v:
                        yield (source, v, weight)

    def edge_weight(self, u, v):
        try:
            return self.outgoing_edges[u][v]
        except KeyError:
            raise ValueError(f'No such edge: {(u, v)}')

    def depth_first_search(self, v, visited=None):
        if visited is None:
            visited = set()

        # NOTE: A vertex is visited means we can access its adjacent vertices.
        visited.add(v)

        for neighbor in self.outgoing_edges[v].keys():
            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)

        return visited

    def breadth_first_search(self, v, visited=None):
        if visited is None:
            visited = set()

        visited.add(v)

        current_level = [v, ]
        while current_level:
            next_level = []
            for vertex in current_level:
                for neighbor in self.outgoing_edges[vertex].keys():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_level.append(neighbor)

            current_level = next_level

        return visited
