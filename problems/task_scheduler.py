# coding: utf-8
"""
https://leetcode.com/problems/task-scheduler/
"""
from collections import Counter
from typing import List


# TODO
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        queue = []
        task_nums = Counter(tasks)
        while task_nums:
            last_tasks = queue[-n:]
            idle = True

            for task, _ in task_nums.most_common():
                if task not in last_tasks:
                    task_nums[task] = task_nums[task] - 1
                    if task_nums[task] == 0:
                        del task_nums[task]

                    queue.append(task)
                    idle = False
                    break

            if idle and task_nums:
                queue.append('idle')

        return len(queue)
