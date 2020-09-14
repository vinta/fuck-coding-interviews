# coding: utf-8
import unittest

from data_structures.graphs.adjacency_map_undirected_weighted_graph import UndirectedGraph


class TestCase(unittest.TestCase):
    def setUp(self):
        self.graph = UndirectedGraph()
        self.edges = [
            # (source, destination, weight)
            ('A', 'B', 0),
            ('A', 'C', 0),
            ('B', 'C', 0),
            ('B', 'D', 0),
            ('C', 'D', 0),
            ('E', 'A', 0),
            ('E', 'F', 0),
            ('F', 'C', 0),
            ('F', 'G', 0),
        ]
        self.vertices = set()
        for source, destination, weight in self.edges:
            self.vertices.add(source)
            self.vertices.add(destination)
            self.graph.add_vertex(source, value=source)
            self.graph.add_vertex(destination, value=destination)
            self.graph.add_edge(source, destination, weight)

    def test_add_vertex(self):
        self.graph.add_vertex('X')
        self.assertEqual(self.graph.vertex_count(), len(self.vertices) + 1)

    def test_add_edge(self):
        self.graph.add_vertex('X', value='X')
        self.graph.add_vertex('Y', value='Y')
        self.graph.add_edge('X', 'Y', 0)
        self.assertEqual(self.graph.vertex_count(), len(self.vertices) + 2)
        self.assertEqual(self.graph.edge_count(), len(self.edges) + 1)

    def test_remove_vertex(self):
        self.graph.remove_vertex('C')
        self.assertEqual(self.graph.vertex_count(), len(self.vertices) - 1)

        edge_count = 0
        for source, destination, _ in self.edges:
            if not source == 'C' and not destination == 'C':
                edge_count += 1
        self.assertEqual(self.graph.edge_count(), edge_count)

    def test_remove_edge(self):
        self.graph.remove_edge('A', 'B')
        self.assertEqual(self.graph.edge_count(), len(self.edges) - 1)

        with self.assertRaises(ValueError):
            self.graph.remove_edge('Z', 'Z')

    def test_vertex_count(self):
        self.assertEqual(self.graph.vertex_count(), len(self.vertices))

    def test_edge_count(self):
        self.assertEqual(self.graph.edge_count(), len(self.edges))

    def test_vertices(self):
        self.assertCountEqual(self.graph.vertices(), self.vertices)

    def test_edges(self):
        edges = []
        for source, destination, weight in self.edges:
            pair = sorted([source, destination])
            edges.append((pair[0], pair[1], weight))

        self.assertCountEqual(self.graph.edges(), edges)

    def test_incident_edges(self):
        vertex = 'A'
        edges = []
        for source, destination, weight in self.edges:
            if vertex in (source, destination):
                pair = sorted([source, destination])
                edges.append((pair[0], pair[1], weight))

        self.assertCountEqual(self.graph.incident_edges(vertex, edge_type='outgoing'), edges)
        self.assertCountEqual(self.graph.incident_edges(vertex, edge_type='incoming'), edges)

    def test_edge_weight(self):
        for source, destination, weight in self.edges:
            self.assertEqual(self.graph.edge_weight(source, destination), weight)
            self.assertEqual(self.graph.edge_weight(destination, source), weight)


if __name__ == '__main__':
    unittest.main()
