# coding: utf-8
"""
Graph
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
https://en.wikipedia.org/wiki/Directed_graph
https://en.wikipedia.org/wiki/Adjacency_list

Assume that we have V vertices and E edges in the graph G.
"""
from collections import defaultdict
import heapq


# This implementation cannot properly handle multiple edges between the same endpoints.
# For instance, (u, v, 1), (u, v, 2) and (u, v, 3).
class DirectedGraph:
    def __init__(self):
        # {
        #     'source_vertex': {
        #         'destination_vertex': edge_weight,
        #     },
        # }
        # NOTE: Since we use defaultdict(dict) here,
        # self.outgoing_edges['NON EXISTED KEY] returns an empty dict.
        # So we don't need to catch KeyError.
        self.outgoing_edges = defaultdict(dict)

        # {
        #     'vertex': data,
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
            for destination, weight in self.outgoing_edges[v].items():
                yield (v, destination, weight)
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

    def breadth_first_search(self, start):
        """
        Applications:
        https://en.wikipedia.org/wiki/Breadth-first_search
        https://cp-algorithms.com/graph/breadth-first-search.html#toc-tgt-2
        """
        current_level = [start, ]
        visited = {start, }
        while current_level:
            next_level = []
            for v in current_level:
                # The shortest path to `v` is found.
                visited.add(v)
                for neighbor in self.outgoing_edges[v].keys():
                    # A graph could contain cycles, so we may come to the same vertex multiple times.
                    # We only process unvisited vertices.
                    if neighbor not in visited:
                        next_level.append(neighbor)
            current_level = next_level

        return visited

    def depth_first_search(self, start, visited=None):
        """
        Applications:
        https://en.wikipedia.org/wiki/Depth-first_search
        https://cp-algorithms.com/graph/depth-first-search.html#toc-tgt-1
        """
        if visited is None:
            visited = set()

        # A vertex is visited means we can access its neighbors.
        visited.add(start)
        for neighbor in self.outgoing_edges[start].keys():
            if neighbor not in visited:
                # Recursion uses the call "stack".
                self.depth_first_search(neighbor, visited)

        return visited

    def has_cycles_dfs(self):
        """
        https://codereview.stackexchange.com/questions/86021/check-if-a-directed-graph-contains-a-cycle
        """
        global_visited = set()

        def has_cycles(start, visited):
            if start in global_visited:
                return False

            global_visited.add(start)
            visited.add(start)
            for des in self.outgoing_edges[start].keys():
                # If there is any visited vertex in the recursion call stack,
                # the graph has cycles.
                if des in visited:
                    return True
                else:
                    if has_cycles(des, visited):
                        return True
            visited.remove(start)
            return False

        for v in self.vertex_data.keys():
            visited = {v, }
            if has_cycles(v, visited):
                return True
        return False

    def construct_path(self, previous, start, end):
        backtrack_path = [end, ]
        last_step = previous.get(end)
        while last_step is not None:
            backtrack_path.append(last_step)
            last_step = previous[last_step]

        if backtrack_path[-1] != start:
            raise ValueError(f'No path from {start} to {end}')

        return list(reversed(backtrack_path))

    # O(V + E)
    def find_shortest_paths_bfs(self, start):
        """
        This algorithm can only work with a unweighted or equal-weighted graph.

        This algorithm is just BFS with distance relaxation.
        """
        distances = {}  # The distance from start to a vertex v.
        previous = {}  # {destination: source}
        for v in self.vertex_data.keys():
            distances[v] = float('inf')
            previous[v] = None
        distances[start] = 0

        current_level = [start, ]
        visited = {start, }
        while current_level:
            next_level = []
            for v in current_level:
                # The shortest path to `v` is found.
                visited.add(v)
                for neighbor in self.outgoing_edges[v].keys():
                    if neighbor not in visited:
                        # The distance increases 1 each level.
                        nei_distance = distances[v] + 1
                        if nei_distance < distances[neighbor]:
                            distances[neighbor] = nei_distance
                            previous[neighbor] = v
                            next_level.append(neighbor)
            current_level = next_level

        return previous, distances

    # O(E * log V)
    def find_shortest_path_dijkstra(self, start, end=None):
        """
        This algorithm can only work with a non-negative graph.
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        https://www.youtube.com/watch?v=pVfj6mxhdMw
        https://leetcode.com/problems/network-delay-time/discuss/329376/efficient-oe-log-v-python-dijkstra-min-heap-with-explanation

        This algorithm is quite like find_shortest_paths_bfs() but replacing the queue with a priority queue.
        """
        # First, we overestimate the distance from start to all other vertices.
        distances = {}
        previous = {}
        for v in self.vertex_data.keys():
            distances[v] = float('inf')
            previous[v] = None
        distances[start] = 0

        min_heap = [(0, start), ]
        visited = {start, }
        while min_heap:
            # NOTE: `v` is the nearest unvisited vertex to `start`.
            v_distance, v = heapq.heappop(min_heap)
            # There could be duplicate vertices with the same vertex index but different distances.
            # For instance, [(2, 'B'), (float('inf'), 'B')].
            if v_distance > distances[v]:
                continue
            # The shortest path to `v` is found.
            visited.add(v)
            for neighbor, weight in self.outgoing_edges[v].items():
                # We only need to update distances for unvisited vertices since visited ones are already found.
                if neighbor not in visited:
                    nei_distance = v_distance + weight
                    if nei_distance < distances[neighbor]:
                        distances[neighbor] = nei_distance
                        previous[neighbor] = v
                        heapq.heappush(min_heap, (distances[neighbor], neighbor))

        return previous, distances

    # O(V * E)
    def find_shortest_path_bellman_ford(self, start):
        """
        This algorithm can only work with a graph which has no negative weight cycles.
        https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
        """
        distances = {}
        previous = {}
        for v in self.vertex_data.keys():
            distances[v] = float('inf')
            previous[v] = None
        distances[start] = 0

        # We have to do V * E times to readjust distances.
        vertex_count = self.vertex_count()
        # The first loop, it calculates the shortest paths with at most 1 edge.
        # Then, it calculates the shortest paths with at most 2 edges, and so on.
        for i in range(vertex_count):
            for src, des, weight in self.edges():
                des_distance = distances[src] + weight  # The distance to destination.
                if des_distance < distances[des]:
                    # The final loop is to check wheter there are negative weight cycles.
                    if i == vertex_count - 1:
                        raise ValueError('Found negative weight cycles')
                    distances[des] = des_distance
                    previous[des] = src

        return previous, distances

    def find_minimum_spanning_tree_prim_jarnik(self, start):
        """
        https://en.wikipedia.org/wiki/Prim%27s_algorithm
        """
        all_vertices = set(self.vertex_data.keys())
        visited = {start, }
        tree_edges = []
        while all_vertices - visited:
            # For every visited vertex, find an edge which connects to a new vertex
            # and has the minimum weight.
            new_edge = (None, None, float('inf'))
            for v in visited:
                for neighbor, weight in self.outgoing_edges[v].items():
                    # We only consider an edge which connects to a new vertex.
                    if neighbor not in visited:
                        if weight < new_edge[2]:
                            new_edge = (v, neighbor, weight)

            visited.add(new_edge[1])
            tree_edges.append(new_edge)

        return tree_edges
