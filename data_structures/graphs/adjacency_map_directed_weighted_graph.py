# coding: utf-8
"""
Graph
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
https://en.wikipedia.org/wiki/Directed_graph
https://en.wikipedia.org/wiki/Adjacency_list

Assume that we have V vertices and E edges in the graph G.
"""
from collections import defaultdict
from collections import deque
import heapq


class NestedBreak(Exception):
    pass


# This implementation cannot properly handle multiple edges between the same endpoints.
# For instance, (u, v, 1), (u, v, 2) and (u, v, 3).
class DirectedGraph:
    def __init__(self):
        # {
        #     'source_vertex': {
        #         'destination_vertex': edge_weight,
        #     },
        # }
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

    def breadth_first_search(self, start):
        """
        Applications
        https://en.wikipedia.org/wiki/Breadth-first_search
        https://cp-algorithms.com/graph/breadth-first-search.html#toc-tgt-2
        """
        current_level = [start, ]
        visited = {start, }
        while current_level:
            next_level = []
            for v in current_level:
                for des in self.outgoing_edges[v].keys():
                    # NOTE: A vertex is visited means we can access its neighbors.
                    if des not in visited:
                        visited.add(des)
                        next_level.append(des)
            current_level = next_level

        return visited

    def breadth_first_search_queue(self, start):  # pragma: no cover
        queue = deque([start, ])
        visited = {start, }
        while queue:
            v = queue.popleft()
            for des in self.outgoing_edges[v].keys():
                if des not in visited:
                    visited.add(des)
                    queue.append(des)

        return visited

    def depth_first_search(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        for des in self.outgoing_edges[start].keys():
            if des not in visited:
                # Recursion uses the call "stack".
                self.depth_first_search(des, visited)

        return visited

    def depth_first_search_iterate(self, start):  # pragma: no cover
        stack = [start, ]
        visited = {start, }
        while stack:
            v = stack.pop()
            for des in self.outgoing_edges[v].keys():
                if des not in visited:
                    visited.add(des)
                    stack.append(des)

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
        while last_step:
            backtrack_path.append(last_step)
            last_step = previous[last_step]

        if backtrack_path[-1] != start:
            raise ValueError(f'No path from {start} to {end}')

        return list(reversed(backtrack_path))

    # O(V + E)
    def find_shortest_paths_bfs(self, start):
        """
        This algorithm can only work with a unweighted graph or a graph has the same weights.
        """
        # First, we overestimate the distance from start to all other vertices.
        distances = {}  # The distance from start to a vertex v.
        previous = {}  # {destination: source}
        for v in self.vertex_data.keys():
            distances[v] = float('inf')
            previous[v] = None
        distances[start] = 0

        # BFS with distance relaxation.
        queue = deque([start, ])
        visited = {start, }
        while queue:
            v = queue.popleft()
            # To calculate distances of the current vertex v's neighbors.
            for des, weight in self.outgoing_edges[v].items():
                # Only unvisited vertices should be calculated
                # since we already calculate visited vertices' neighbors.
                if des not in visited:
                    visited.add(des)
                    distance_to_des = distances[v] + weight
                    if distance_to_des < distances[des]:
                        # We find a shorter path to des,
                        # so its unvisited neighbors' distances should be readjust.
                        distances[des] = distance_to_des
                        previous[des] = v
                        queue.append(des)

        return previous, distances

    # O(E * log V)
    def find_shortest_path_dijkstra(self, start):
        """
        This algorithm can only work with a non-negative graph.
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        https://leetcode.com/problems/network-delay-time/discuss/329376/efficient-oe-log-v-python-dijkstra-min-heap-with-explanation
        """
        distances = {}
        previous = {}
        for v in self.vertex_data.keys():
            distances[v] = float('inf')
            previous[v] = None
        distances[start] = 0

        # We begin with a vertex v which has the minimun distance every round,
        # and calculate its neighbors' distances. The distance of a visited vertex is already the minimum.
        # To achieve that, we maintain a priority queue using a min heap.
        min_heap = [(0, start), ]  # (distance, vertex)
        visited = {start, }
        while min_heap:
            v_distance, v = heapq.heappop(min_heap)
            # There might be duplicate vertices with the same index but different distances.
            if v_distance > distances[v]:
                continue
            for des, weight in self.outgoing_edges[v].items():
                if des not in visited:
                    visited.add(des)
                    distance_to_des = v_distance + weight
                    if distance_to_des < distances[des]:
                        distances[des] = distance_to_des
                        previous[des] = v
                        heapq.heappush(min_heap, (distances[des], des))

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
                distance_to_des = distances[src] + weight  # The distance to destination.
                if distance_to_des < distances[des]:
                    # The final loop is to check wheter there are negative weight cycles.
                    if i == vertex_count - 1:
                        raise ValueError('Found negative weight cycles')
                    distances[des] = distance_to_des
                    previous[des] = src

        return previous, distances
