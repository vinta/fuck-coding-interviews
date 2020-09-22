# coding: utf-8
"""
https://leetcode.com/problems/course-schedule/
"""
from collections import defaultdict
from typing import List


class Graph:
    def __init__(self):
        self.vertices = set()
        self.outgoing_edges = defaultdict(dict)

    def add_edge(self, u, v):
        self.outgoing_edges[u][v] = 1
        self.vertices.add(u)
        self.vertices.add(v)

    def has_cycles(self):
        global_visited = set()

        def has_cycles_dfs(v, visited):
            if v in global_visited:
                return False

            global_visited.add(v)
            visited.add(v)
            for des in self.outgoing_edges[v].keys():
                # If there is any visited vertex in the call stack, the graph has cycles.
                if des in visited:
                    return True
                else:
                    if has_cycles_dfs(des, visited):
                        return True
            visited.remove(v)
            return False

        for v in self.vertices:
            visited = {v, }
            if has_cycles_dfs(v, visited):
                return True
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # If there is any cycle in the graph,
        # it's impossible to finish all courses.
        graph = Graph()
        for u, v in prerequisites:
            graph.add_edge(v, u)

        return not graph.has_cycles()
