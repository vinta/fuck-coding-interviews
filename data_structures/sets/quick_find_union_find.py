# coding: utf-8
"""
Union-Find (Disjoint Set)
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class QuickFindUnionFind:
    def __init__(self):
        self.size = 0
        self.element_groups = {
            # element: group_id,
        }

    def __len__(self):
        return self.size

    # O(1)
    def make_set(self, element):
        # Initially, every element is in its own group which contains only itself.
        if element not in self.element_groups:
            # `group_id` could be arbitrary as long as each group has an unique `group_id`.
            # We use `self.size` here as an auto increment id.
            self.element_groups[element] = self.size
            self.size += 1

    # O(1)
    def find(self, p):
        return self.element_groups[p]

    # O(n)
    def union(self, p, q):
        p_group_id = self.find(p)
        q_group_id = self.find(q)
        for element, group_id in self.element_groups.items():
            if group_id == p_group_id:
                self.element_groups[element] = q_group_id

    # O(1)
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
