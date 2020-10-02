#!/bin/python3
"""
https://www.hackerrank.com/challenges/dijkstrashortreach/problem
"""
from collections import defaultdict
import heapq
import os
import sys


class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.outgoing_edges = defaultdict(dict)

    def add_edge(self, u, v, new_weight):
        # NOTE: There could be multiple edges between the same pair of nodes with different weights,
        # so we only store the smallest weight.
        current_weight = self.outgoing_edges[u].get(v)
        if (current_weight is None) or (current_weight > new_weight):
            self.outgoing_edges[u][v] = new_weight
            self.outgoing_edges[v][u] = new_weight

    def shortest_paths(self, start):
        distances = [float('inf'), ] * self.num_vertices
        distances[start] = 0

        min_heap = [(0, start), ]
        visited = set()
        while min_heap:
            v_distance, v = heapq.heappop(min_heap)
            if v_distance > distances[v]:
                continue
            visited.add(v)
            for neighbor, weight in self.outgoing_edges[v].items():
                if neighbor not in visited:
                    nei_dis = distances[v] + weight
                    if nei_dis < distances[neighbor]:
                        distances[neighbor] = nei_dis
                        heapq.heappush(min_heap, (nei_dis, neighbor))

        def output():
            for i, dis in enumerate(distances):
                if i != start:
                    if dis == float('inf'):
                        dis = -1
                    yield dis
        return output()


def shortestReach(n, edges, s):
    graph = UndirectedGraph(n)
    for src, des, weight in edges:
        # The node indexes are 1-based.
        graph.add_edge(src - 1, des - 1, weight)

    return graph.shortest_paths(s - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for _ in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])

        # Instead of creating a list of edges, we could also build `outgoing_edges` here.
        edges = []
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((u, v, w))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
