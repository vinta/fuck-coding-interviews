# coding: utf-8
"""
Union-Find (Disjoint Set)
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class QuickFindUnionFind:
    def __init__(self, union_pairs=()):
        self.num_groups = 0
        self.auto_increment_id = 1
        self.element_groups = {
            # element: group_id,
        }

        for p, q in union_pairs:
            self.union(p, q)

    def __len__(self):
        return self.num_groups

    # O(1)
    def make_set(self, element):
        # Initially, every element is in its own group which contains only itself.
        group_id = self.element_groups.get(element)
        if group_id is None:
            # `group_id` could be arbitrary as long as each group has an unique `group_id`.
            group_id = self.auto_increment_id
            self.element_groups[element] = group_id
            self.num_groups += 1
            self.auto_increment_id += 1

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
        if p_group_id != q_group_id:
            for element, group_id in self.element_groups.items():
                if group_id == p_group_id:
                    self.element_groups[element] = q_group_id
            self.num_groups -= 1

    # O(1)
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
