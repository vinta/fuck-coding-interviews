# coding: utf-8
"""
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
"""
from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.outgoing_edges = defaultdict(dict)

    def connect(self, u, v):
        self.outgoing_edges[u][v] = 6
        self.outgoing_edges[v][u] = 6

    def find_all_distances(self, s):
        distances = {}
        for n in range(self.num_nodes):
            distances[n] = float('inf')
        distances[s] = 0

        visited = set([s, ])
        queue = deque([s, ])
        while queue:
            n = queue.popleft()
            for des, weight in self.outgoing_edges[n].items():
                if des not in visited:
                    visited.add(des)
                    distance_to_des = distances[n] + weight
                    if distance_to_des < distances[des]:
                        distances[des] = distance_to_des
                        queue.append(des)

        def output():
            for n in range(self.num_nodes):
                if n != s:
                    distance = distances[n]
                    yield '-1' if distance == float('inf') else str(distance)

        print(' '.join(output()))


t = int(input())  # There are t graphs.
for _ in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)  # There are n nodes.
    for _ in range(m):  # There are m undirected edges.
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)

    s = int(input())  # Find shortest paths from vertex s.
    graph.find_all_distances(s - 1)
