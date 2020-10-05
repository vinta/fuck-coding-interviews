#!/bin/python3
"""
https://www.hackerrank.com/challenges/kruskalmstrsub/problem
"""
import heapq
import os


class Group:
    def __init__(self, group_id, element):
        self.group_id = group_id
        self.elements = [element, ]
        self.size = 1

    def __len__(self):
        return self.size


class UnionFind:
    def __init__(self):
        self.auto_increment_id = 1
        self.element_groups = {
            # element: group
        }

    def make_group(self, p):
        group = self.element_groups.get(p)
        if group is None:
            group = Group(self.auto_increment_id, p)
            self.element_groups[p] = group
            self.auto_increment_id += 1

        return group

    def find(self, p):
        try:
            return self.element_groups[p]
        except KeyError:
            return self.make_group(p)

    def union(self, p, q):
        p_group = self.find(p)
        q_group = self.find(q)
        if p_group != q_group:
            if len(p_group) < len(q_group):
                # Merge p into q.
                for element in p_group.elements:
                    self.element_groups[element] = q_group
                    q_group.elements.append(element)
                    q_group.size += p_group.size
            else:
                # Merge q into p.
                for element in q_group.elements:
                    self.element_groups[element] = p_group
                    p_group.elements.append(element)
                    p_group.size += q_group.size


# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.

# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
def kruskals(g_nodes, min_heap):
    total_weight = 0
    num_edges = 0

    union_find = UnionFind()
    while min_heap or (num_edges < g_nodes - 1):
        weight, u, v = heapq.heappop(min_heap)
        if union_find.find(u) != union_find.find(v):
            total_weight += weight
            num_edges += 1
            union_find.union(u, v)

    return total_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    min_heap = []
    for _ in range(g_edges):
        src, des, weight = map(int, input().rstrip().split())
        min_heap.append((weight, src, des))
    heapq.heapify(min_heap)

    total_weight = kruskals(g_nodes, min_heap)

    fptr.write(str(total_weight))
    fptr.close()
