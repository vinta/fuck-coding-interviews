# coding: utf-8
"""
https://learning.oreilly.com/library/view/Data+Structures+and+Algorithms+in+Python/9781118290279/19_chap14.html#ch014-sec051
"""


class Node:
    def __init__(self, element):
        self.element = element
        self.parent = self  # NOTE: We treat the node instance as the node id.
        self.size = 1

    def __len__(self):
        return self.size


# There is another implementation:
# https://github.com/vinta/fuck-coding-interviews/blob/master/problems/kruskal_mst_really_special_subtree.py
class WeightedQuickUnionUnionFind:
    def __init__(self, union_pairs=()):
        self.num_groups = 0
        self.element_groups = {
            # element: node_instance
        }

        for p, q in union_pairs:
            self.union(p, q)

    def __len__(self):
        return self.num_groups

    def make_group(self, element):
        node = self.element_groups.get(element)
        if node is None:
            node = Node(element)
            self.element_groups[element] = node
            self.num_groups += 1

        return node

    def find(self, p):
        try:
            node = self.element_groups[p]
        except KeyError:
            node = self.make_group(p)
        else:
            while node.parent != node:
                node = node.parent

        return node.parent

    def union(self, p, q):
        p_group = self.find(p)
        q_group = self.find(q)
        if len(p_group) < len(q_group):
            # Merge p into q.
            p_group.parent = q_group.parent
            q_group.size += p_group.size
        else:
            # Merge q into p.
            q_group.parent = p_group.parent
            p_group.size += q_group.size
        self.num_groups -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
