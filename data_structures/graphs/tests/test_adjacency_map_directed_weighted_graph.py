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
            ('B', 'I', 0),
            ('C', 'D', 0),
            ('D', 'C', 0),
            ('D', 'H', 0),
            ('H', 'I', 0),
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
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'H', 'I'])

        v = 'E'
        visited = self.graph.depth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

    def test_breadth_first_search(self):
        v = 'A'
        visited = self.graph.breadth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'H', 'I'])

        v = 'E'
        visited = self.graph.breadth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

    def test_find_shortest_path_bfs(self):
        graph = DirectedGraph()
        edges = [  # https://cs.stackexchange.com/questions/18138/dijkstra-algorithm-vs-breadth-first-search-for-shortest-path-in-graph
            ['A', 'B', 0],
            ['B', 'C', 0],
            ['B', 'D', 0],
            ['B', 'E', 0],
            ['C', 'E', 0],
            ['D', 'E', 0],
            ['E', 'F', 0],
            ['G', 'D', 0],
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        path = graph.find_shortest_path_bfs('A', 'E')
        self.assertEqual(path, ['A', 'B', 'E'])

        with self.assertRaises(ValueError):
            graph.find_shortest_path_bellman('A', 'G')

    def test_find_shortest_path_bellman(self):
        graph = DirectedGraph()
        edges = [  # https://www.programiz.com/dsa/bellman-ford-algorithm
            ['A', 'B', 4],
            ['A', 'C', 2],
            ['B', 'C', 3],
            ['B', 'D', 2],
            ['B', 'E', 4],
            ['C', 'B', 1],
            ['C', 'D', 3],
            ['C', 'E', 5],
            ['E', 'D', -5],
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        path = graph.find_shortest_path_bellman('A', 'B')
        self.assertEqual(path, ['A', 'C', 'B'])

        # There is no such path.
        with self.assertRaises(ValueError):
            graph.find_shortest_path_bellman('D', 'E')

        path, distance = graph.find_shortest_path_bellman('A', 'A', return_distance=True)
        self.assertEqual(path, ['A', ])
        self.assertEqual(distance, 0)

        path, distance = graph.find_shortest_path_bellman('A', 'B', return_distance=True)
        self.assertEqual(path, ['A', 'C', 'B'])
        self.assertEqual(distance, 3)

        path, distance = graph.find_shortest_path_bellman('A', 'C', return_distance=True)
        self.assertEqual(path, ['A', 'C'])
        self.assertEqual(distance, 2)

        path, distance = graph.find_shortest_path_bellman('A', 'D', return_distance=True)
        self.assertEqual(path, ['A', 'C', 'E', 'D'])
        self.assertEqual(distance, 2)

        path, distance = graph.find_shortest_path_bellman('A', 'E', return_distance=True)
        self.assertEqual(path, ['A', 'C', 'E'])
        self.assertEqual(distance, 7)

        graph = DirectedGraph()
        edges = [  # https://www.programiz.com/dsa/bellman-ford-algorithm
            ['A', 'B', 2],
            ['B', 'C', 2],
            ['B', 'D', 1],
            ['C', 'D', -4],
            ['D', 'B', 1],
            ['D', 'E', 3],
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        # There is a negative weight cycle among {B, C, D}.
        with self.assertRaises(ValueError):
            graph.find_shortest_path_bellman('A', 'E')


if __name__ == '__main__':
    unittest.main()
