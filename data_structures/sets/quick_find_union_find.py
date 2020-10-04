# coding: utf-8
"""
Union-Find (Disjoint Set)
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class QuickFindUnionFind:
    def __init__(self, union_pairs=()):
        self.size = 0
        self.element_groups = {
            # element: group_id,
        }
        for p, q in union_pairs:
            self.union(p, q)

    def __len__(self):
        return self.size

    # O(1)
    def make_set(self, element):
        # Initially, every element is in its own group which contains only itself.
        group_id = self.element_groups.get(element)
        if group_id is None:
            # `group_id` could be arbitrary as long as each group has an unique `group_id`.
            # We use `self.size` here as an auto increment id.
            group_id = self.size
            self.element_groups[element] = group_id
            self.size += 1

        return group_id

    # O(1)
    def find(self, p):
        try:
            return self.element_groups[p]
        except KeyError:
            raise ValueError('Not found')

    # O(n)
    def union(self, p, q):
        p_group_id = self.make_set(p)
        q_group_id = self.make_set(q)
        for element, group_id in self.element_groups.items():
            if group_id == p_group_id:
                self.element_groups[element] = q_group_id

    # O(1)
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
