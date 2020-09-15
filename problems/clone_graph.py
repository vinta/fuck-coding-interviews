# coding: utf-8
"""
https://leetcode.com/problems/clone-graph/
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # New nodes' neighbors are all empty at first,
        # we will rebuild them after we find all nodes.
        new_nodes = {node.val: Node(node.val, [])}
        visited = {node.val: node}

        # BFS
        current_level = [node, ]
        while current_level:
            next_level = []
            for v in current_level:
                for neighbor in v.neighbors:
                    if neighbor.val not in visited:
                        new_nodes[neighbor.val] = Node(neighbor.val, [])
                        visited[neighbor.val] = neighbor
                        next_level.append(neighbor)

            current_level = next_level

        # Re-build neighbors for new nodes.
        for old_node in visited.values():
            new_node = new_nodes[old_node.val]
            new_node.neighbors = [new_nodes[n.val] for n in old_node.neighbors]

        return new_nodes[1]


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # Every new node's neighbors is empty at first, we will rebuild them from old_nodes later.
        new_nodes = {node.val: Node(node.val)}
        old_nodes = {node.val: node}

        # We use BFS to find all nodes, and store them in old_nodes.
        current_level = [node, ]
        while current_level:
            next_level = []
            for v in current_level:
                for neighbor in v.neighbors:
                    if neighbor.val not in old_nodes:
                        new_nodes[neighbor.val] = Node(neighbor.val)
                        old_nodes[neighbor.val] = neighbor
                        next_level.append(neighbor)

                # Now we have all neighbors ready in new_nodes for v, it's time to re-build.
                new_node = new_nodes[v.val]
                new_node.neighbors = [new_nodes[n.val] for n in v.neighbors]

            current_level = next_level

        return new_nodes[1]
