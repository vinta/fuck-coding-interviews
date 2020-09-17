# coding: utf-8
import unittest

from data_structures.graphs.adjacency_map_directed_weighted_graph import DirectedGraph


class TestCase(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.edges = [
            # (source, destination, weight)
            ('A', 'B', 0),
            ('A', 'C', 0),
            ('B', 'C', 0),
            ('B', 'D', 0),
            ('C', 'D', 0),
            ('D', 'C', 0),
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
        self.assertCountEqual(self.graph.edges(), self.edges)

    def test_incident_edges(self):
        vertex = 'A'
        outgoing_edges = [edge for edge in self.edges if edge[0] == vertex]
        self.assertCountEqual(self.graph.incident_edges(vertex, edge_type='outgoing'), outgoing_edges)
        incoming_edges = [edge for edge in self.edges if edge[1] == vertex]
        self.assertCountEqual(self.graph.incident_edges(vertex, edge_type='incoming'), incoming_edges)

        self.assertCountEqual(self.graph.incident_edges('NOT EXIST', edge_type='outgoing'), [])
        self.assertCountEqual(self.graph.incident_edges('NOT EXIST', edge_type='incoming'), [])

    def test_edge_weight(self):
        for source, destination, weight in self.edges:
            self.assertEqual(self.graph.edge_weight(source, destination), weight)

        with self.assertRaises(ValueError):
            self.graph.edge_weight('NOT EXIST', 'NOT EXIST')

    def test_depth_first_search(self):
        v = 'A'
        visited = self.graph.depth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D'])

        v = 'E'
        visited = self.graph.depth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_breadth_first_search(self):
        v = 'A'
        visited = self.graph.breadth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D'])

        v = 'E'
        visited = self.graph.breadth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])


if __name__ == '__main__':
    unittest.main()
