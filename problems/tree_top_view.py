# coding: utf-8
"""
https://www.hackerrank.com/challenges/tree-top-view/problem
"""
from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    # Write your code here
    queue = deque([(root, 0), ])
    levels = []
    while queue:
        node, pos = queue.popleft()
        if node:
            levels.append((node.info, pos))
            queue.extend([(node.left, pos - 1), (node.right, pos + 1)])

    levels.sort(key=lambda t: t[1])
    current_pos = None
    output = []
    for node_info, pos in levels:
        if current_pos != pos:
            current_pos = pos
            output.append(str(node_info))

    print(' '.join(output))


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])

topView(tree.root)
