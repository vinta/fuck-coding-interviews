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

    def test_breadth_first_search(self):
        v = 'A'
        visited = self.graph.breadth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'H', 'I'])

        v = 'E'
        visited = self.graph.breadth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

    def test_depth_first_search(self):
        v = 'A'
        visited = self.graph.depth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'H', 'I'])

        v = 'E'
        visited = self.graph.depth_first_search(v)
        self.assertCountEqual(visited, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

    def test_has_cycles_dfs(self):
        self.assertEqual(self.graph.has_cycles_dfs(), True)

        graph = DirectedGraph()
        edges = [
            ('A', 'A', 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        self.assertEqual(graph.has_cycles_dfs(), True)

        graph = DirectedGraph()
        edges = [
            ('A', 'B', 1),
            ('B', 'C', 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        self.assertEqual(graph.has_cycles_dfs(), False)

    def test_find_shortest_paths_bfs(self):
        graph = DirectedGraph()
        edges = [  # https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
            (0, 1, 1),
            (0, 3, 1),
            (1, 0, 1),
            (1, 2, 1),
            (2, 1, 1),
            (3, 0, 1),
            (3, 4, 1),
            (3, 7, 1),
            (4, 3, 1),
            (4, 5, 1),
            (4, 6, 1),
            (4, 7, 1),
            (5, 4, 1),
            (5, 6, 1),
            (6, 4, 1),
            (6, 5, 1),
            (6, 7, 1),
            (7, 3, 1),
            (7, 4, 1),
            (7, 6, 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_paths_bfs(0)

        path = graph.construct_path(previous, 0, 5)
        self.assertEqual(path, [0, 3, 4, 5])

        path = graph.construct_path(previous, 0, 7)
        self.assertEqual(path, [0, 3, 7])

        # No such path.
        with self.assertRaises(ValueError):
            graph.construct_path(previous, 0, 10)

    def test_find_shortest_path_dijkstra(self):
        graph = DirectedGraph()
        edges = [  # https://cs.stackexchange.com/questions/18138/dijkstra-algorithm-vs-breadth-first-search-for-shortest-path-in-graph
            ('A', 'B', 1),
            ('B', 'C', 3),
            ('B', 'D', 2),
            ('B', 'E', 1),
            ('C', 'E', 4),
            ('D', 'E', 2),
            ('E', 'F', 3),
            ('G', 'D', 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_path_dijkstra('A')

        path = graph.construct_path(previous, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'D'])

        path = graph.construct_path(previous, 'A', 'E')
        self.assertEqual(path, ['A', 'B', 'E'])

        path = graph.construct_path(previous, 'A', 'F')
        self.assertEqual(path, ['A', 'B', 'E', 'F'])

        # No such path.
        with self.assertRaises(ValueError):
            graph.construct_path(previous, 'A', 'G')

        graph = DirectedGraph()
        edges = [  # https://www.youtube.com/watch?v=pVfj6mxhdMw
            ('A', 'B', 6),
            ('A', 'D', 1),
            ('B', 'A', 6),
            ('B', 'C', 5),
            ('B', 'D', 2),
            ('B', 'E', 2),
            ('C', 'B', 5),
            ('C', 'E', 5),
            ('D', 'A', 1),
            ('D', 'B', 2),
            ('D', 'E', 1),
            ('E', 'B', 2),
            ('E', 'C', 5),
            ('E', 'D', 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_path_dijkstra('A')

        path = graph.construct_path(previous, 'A', 'B')
        self.assertEqual(path, ['A', 'D', 'B'])

        path = graph.construct_path(previous, 'A', 'C')
        self.assertEqual(path, ['A', 'D', 'E', 'C'])

        path = graph.construct_path(previous, 'A', 'D')
        self.assertEqual(path, ['A', 'D'])

        path = graph.construct_path(previous, 'A', 'E')
        self.assertEqual(path, ['A', 'D', 'E'])

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

        previous, distances = graph.find_shortest_path_dijkstra('A')

        path = graph.construct_path(previous, 'A', 'I')
        self.assertEqual(path, ['A', 'B', 'D', 'E', 'H', 'I'])

        previous, distances = graph.find_shortest_path_dijkstra('E')

        path = graph.construct_path(previous, 'E', 'C')
        self.assertEqual(path, ['E', 'H', 'F', 'C'])

        previous, distances = graph.find_shortest_path_dijkstra('I')

        # No such path.
        with self.assertRaises(ValueError):
            graph.construct_path(previous, 'I', 'A')

        graph = DirectedGraph()
        edges = [  # https://www.bogotobogo.com/python/python_Prims_Spanning_Tree_Data_Structure.php
            ('A', 'B', 7),
            ('A', 'C', 9),
            ('A', 'F', 14),
            ('B', 'A', 7),
            ('B', 'C', 10),
            ('B', 'D', 15),
            ('C', 'A', 9),
            ('C', 'B', 10),
            ('C', 'D', 11),
            ('C', 'F', 2),
            ('D', 'B', 15),
            ('D', 'C', 11),
            ('D', 'E', 6),
            ('E', 'D', 6),
            ('E', 'F', 9),
            ('F', 'A', 14),
            ('F', 'C', 2),
            ('F', 'E', 9),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_path_dijkstra('A')

        path = graph.construct_path(previous, 'A', 'E')
        self.assertEqual(path, ['A', 'C', 'F', 'E'])

        path = graph.construct_path(previous, 'A', 'D')
        self.assertEqual(path, ['A', 'C', 'D'])

        graph = DirectedGraph()
        adj_list = {  # https://adityakamath.com/2018/06/17/Dijktra%27s-Algorithm-In-Python.html
            'S': {'A': 7, 'B': 2, 'C': 3},
            'A': {'S': 7, 'B': 3, 'D': 4},
            'B': {'S': 2, 'A': 3, 'D': 4, 'H': 1, 'C': 12},
            'C': {'S': 3, 'L': 2},
            'D': {'A': 4, 'B': 4, 'F': 5},
            'E': {'G': 2, 'K': 5},
            'F': {'D': 5, 'H': 3},
            'G': {'H': 2, 'I': 10, 'E': 2},
            'H': {'B': 1, 'F': 3, 'G': 2},
            'I': {'J': 6, 'K': 4, 'L': 4},
            'J': {'K': 4, 'L': 4},
            'K': {'I': 4, 'J': 4, 'E': 5},
            'L': {'C': 2, 'I': 4, 'J': 4},
        }
        for src, neighbors in adj_list.items():
            for des, weight in neighbors.items():
                graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_path_dijkstra('S')

        path = graph.construct_path(previous, 'S', 'E')
        self.assertEqual(path, ['S', 'B', 'H', 'G', 'E'])

    def test_find_shortest_path_bellman_ford(self):
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
            previous, distances = graph.find_shortest_path_bellman_ford('A')

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

        previous, distances = graph.find_shortest_path_bellman_ford('A')

        path = graph.construct_path(previous, 'A', 'A')
        self.assertEqual(path, ['A', ])

        path = graph.construct_path(previous, 'A', 'B')
        self.assertEqual(path, ['A', 'C', 'B'])

        path = graph.construct_path(previous, 'A', 'C')
        self.assertEqual(path, ['A', 'C'])

        path = graph.construct_path(previous, 'A', 'D')
        self.assertEqual(path, ['A', 'C', 'E', 'D'])

        path = graph.construct_path(previous, 'A', 'E')
        self.assertEqual(path, ['A', 'C', 'E'])

        previous, distances = graph.find_shortest_path_bellman_ford('D')

        # No such path.
        with self.assertRaises(ValueError):
            graph.construct_path(previous, 'D', 'E')

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

        previous, distances = graph.find_shortest_path_bellman_ford('A')

        path = graph.construct_path(previous, 'A', 'E')
        self.assertEqual(path, ['A', 'B', 'E'])

        path = graph.construct_path(previous, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'D'])

        # No such path.
        with self.assertRaises(ValueError):
            graph.construct_path(previous, 'A', 'G')

        graph = DirectedGraph()
        edges = [  # https://www.youtube.com/watch?v=pVfj6mxhdMw
            ('A', 'B', 6),
            ('A', 'D', 1),
            ('B', 'A', 6),
            ('B', 'C', 5),
            ('B', 'D', 2),
            ('B', 'E', 2),
            ('C', 'B', 5),
            ('C', 'E', 5),
            ('D', 'A', 1),
            ('D', 'B', 2),
            ('D', 'E', 1),
            ('E', 'B', 2),
            ('E', 'C', 5),
            ('E', 'D', 1),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_path_bellman_ford('A')

        path = graph.construct_path(previous, 'A', 'C')
        self.assertEqual(path, ['A', 'D', 'E', 'C'])

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

        previous, distances = graph.find_shortest_path_bellman_ford('A')

        path = graph.construct_path(previous, 'A', 'I')
        self.assertEqual(path, ['A', 'B', 'D', 'E', 'H', 'I'])

        previous, distances = graph.find_shortest_path_bellman_ford('E')

        path = graph.construct_path(previous, 'E', 'C')
        self.assertEqual(path, ['E', 'H', 'F', 'C'])

        previous, distances = graph.find_shortest_path_bellman_ford('I')

        # No such path.
        with self.assertRaises(ValueError):
            graph.construct_path(previous, 'I', 'A')

        graph = DirectedGraph()
        edges = [  # https://www.bogotobogo.com/python/python_Prims_Spanning_Tree_Data_Structure.php
            ('A', 'B', 7),
            ('A', 'C', 9),
            ('A', 'F', 14),
            ('B', 'A', 7),
            ('B', 'C', 10),
            ('B', 'D', 15),
            ('C', 'A', 9),
            ('C', 'B', 10),
            ('C', 'D', 11),
            ('C', 'F', 2),
            ('D', 'B', 15),
            ('D', 'C', 11),
            ('D', 'E', 6),
            ('E', 'D', 6),
            ('E', 'F', 9),
            ('F', 'A', 14),
            ('F', 'C', 2),
            ('F', 'E', 9),
        ]
        for src, des, weight in edges:
            graph.add_edge(src, des, weight)

        previous, distances = graph.find_shortest_path_bellman_ford('A')

        path = graph.construct_path(previous, 'A', 'E')
        self.assertEqual(path, ['A', 'C', 'F', 'E'])

        path = graph.construct_path(previous, 'A', 'D')
        self.assertEqual(path, ['A', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
