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
    graph.outgoing_edges = edges
    return graph.shortest_paths(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])

        edges = defaultdict(dict)
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())

            # Node indexes are 1-based.
            u = u - 1
            v = v - 1

            # NOTE: There could be multiple edges between the same pair of nodes with different weights,
            # so we only store the edge which has the smallest weight.
            current_weight = edges[u].get(v)
            if (current_weight is None) or (current_weight > w):
                edges[u][v] = w
                edges[v][u] = w

        s = int(input())

        result = shortestReach(n, edges, s - 1)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
