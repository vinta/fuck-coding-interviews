# coding: utf-8
"""
https://leetcode.com/problems/task-scheduler/
"""
from collections import Counter
from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        recorded_tasks = []
        queue = []
        for task, count in Counter(tasks).items():
            # heapq is min heap, so make count negative.
            heapq.heappush(queue, (-count, task))

        # We should schedule the most frequent tasks as frequently as possible.
        while queue:
            put_backs = []
            for _ in range(n + 1):
                if queue:
                    # Pop the current most frequent task.
                    count, task = heapq.heappop(queue)
                    # We don't need to check whether the popped task is in recorded_tasks[-n:] or not.
                    recorded_tasks.append(task)
                    count += 1
                    if count < 0:
                        put_backs.append((count, task))
                else:
                    if put_backs:
                        recorded_tasks.append('idle')
                    else:
                        break

            for task_data in put_backs:
                heapq.heappush(queue, task_data)

        # print(recorded_tasks)

        return len(recorded_tasks)
