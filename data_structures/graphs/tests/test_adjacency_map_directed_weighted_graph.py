# coding: utf-8
import unittest

from data_structures.graphs.adjacency_map_directed_weighted_graph import DirectedGraph


class TestCase(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.edges = [
            # (source, destination, weight)
            ('A', 'B', 1),
            ('A', 'C', 1),
            ('B', 'C', 1),
            ('B', 'D', 1),
            ('B', 'I', 1),
            ('C', 'D', 1),
            ('D', 'C', 1),
            ('D', 'H', 1),
            ('H', 'I', 1),
            ('E', 'A', 1),
            ('E', 'F', 1),
            ('F', 'C', 1),
            ('F', 'G', 1),
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
            ('A', 'B', 1),
            ('B', 'C', 1),
            ('B', 'D', 1),
            ('B', 'E', 1),
            ('C', 'E', 1),
            ('D', 'E', 1),
            ('E', 'F', 1),
            ('G', 'D', 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        path = graph.find_shortest_path_bfs('A', 'E')
        self.assertEqual(path, ['A', 'B', 'E'])

        with self.assertRaises(ValueError):
            graph.find_shortest_path_bfs('A', 'G')

    def test_find_shortest_path_dijkstra(self):
        graph = DirectedGraph()
        edges = [  # https://www.chegg.com/homework-help/questions-and-answers/8-4-14-10-2-figure-2-directed-graph-computing-shortest-path-3-dijkstra-s-algorithm-computi-q25960616#question-transcript
            ('A', 'B', 4),
            ('B', 'C', 11),
            ('B', 'D', 9),
            ('C', 'A', 8),
            ('D', 'C', 7),
            ('D', 'E', 2),
            ('D', 'F', 6),
            ('E', 'B', 8),
            ('E', 'G', 7),
            ('E', 'H', 4),
            ('F', 'C', 1),
            ('F', 'E', 5),
            ('G', 'H', 14),
            ('G', 'I', 9),
            ('H', 'F', 2),
            ('H', 'I', 10),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        # There is no such path.
        with self.assertRaises(ValueError):
            graph.find_shortest_path_dijkstra('I', 'A')

        path = graph.find_shortest_path_dijkstra('A', 'I')
        self.assertEqual(path, ['A', 'B', 'D', 'E', 'H', 'I'])

        path = graph.find_shortest_path_dijkstra('E', 'C')
        self.assertEqual(path, ['E', 'H', 'F', 'C'])

    def test_find_shortest_path_bellman_ford(self):
        graph = DirectedGraph()
        edges = [  # https://www.programiz.com/dsa/bellman-ford-algorithm
            ('A', 'B', 4),
            ('A', 'C', 2),
            ('B', 'C', 3),
            ('B', 'D', 2),
            ('B', 'E', 4),
            ('C', 'B', 1),
            ('C', 'D', 3),
            ('C', 'E', 5),
            ('E', 'D', -5),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        # There is no such path.
        with self.assertRaises(ValueError):
            graph.find_shortest_path_bellman_ford('D', 'E')

        path = graph.find_shortest_path_bellman_ford('A', 'B')
        self.assertEqual(path, ['A', 'C', 'B'])

        path = graph.find_shortest_path_bellman_ford('A', 'A')
        self.assertEqual(path, ['A', ])

        path = graph.find_shortest_path_bellman_ford('A', 'B')
        self.assertEqual(path, ['A', 'C', 'B'])

        path = graph.find_shortest_path_bellman_ford('A', 'C')
        self.assertEqual(path, ['A', 'C'])

        path = graph.find_shortest_path_bellman_ford('A', 'D')
        self.assertEqual(path, ['A', 'C', 'E', 'D'])

        path = graph.find_shortest_path_bellman_ford('A', 'E')
        self.assertEqual(path, ['A', 'C', 'E'])

        graph = DirectedGraph()
        edges = [  # https://www.programiz.com/dsa/bellman-ford-algorithm
            ('A', 'B', 2),
            ('B', 'C', 2),
            ('B', 'D', 1),
            ('C', 'D', -4),
            ('D', 'B', 1),
            ('D', 'E', 3),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        # There is a negative weight cycle among {B, C, D}.
        with self.assertRaises(ValueError):
            graph.find_shortest_path_bellman_ford('A', 'E')


if __name__ == '__main__':
    unittest.main()
