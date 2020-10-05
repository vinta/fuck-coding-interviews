#!/bin/python3
"""
https://www.hackerrank.com/challenges/primsmstsub/problem
"""
from collections import defaultdict
import heapq
import os
import sys


class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices

    def find_minimum_spanning_tree_weight(self, start):
        total_weight = 0
        num_edges = 0

        min_heap = [(0, start, start), ]  # (weight, source, destination)
        visited = set()
        while min_heap or (num_edges < self.num_vertices - 1):
            # The minimum-weight edge which connects to a new vertex.
            weight, u, v = heapq.heappop(min_heap)
            if v not in visited:
                total_weight += weight
                num_edges += 1
                visited.add(v)
                for neighbor, weight in self.outgoing_edges[v].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (weight, v, neighbor))

        return total_weight


def prims(n, edges, start):
    graph = UndirectedGraph(n)
    graph.outgoing_edges = edges
    return graph.find_minimum_spanning_tree_weight(start)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    edges = defaultdict(dict)
    for _ in range(m):
        src, des, weight = list(map(int, sys.stdin.readline().split()))

        # Node indexes are 1-based.
        src = src - 1
        des = des - 1

        # the graph is undirected.
        edges[src][des] = weight
        edges[des][src] = weight

    start = int(input())

    result = prims(n, edges, start - 1)

    fptr.write(str(result) + '\n')
    fptr.close()
