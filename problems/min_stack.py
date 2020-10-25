# coding: utf-8
"""
https://leetcode.com/problems/min-stack/
"""


class MinStack:
    def __init__(self):
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return min(self.array)


class MinStack2:
    def __init__(self):
        self.stack = []

        # We use an extra variable to track the minimum value.
        self.min_value = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min_value:
            self.min_value = x

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_value:
            if self.stack:
                self.min_value = min(self.stack)
            else:
                self.min_value = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_value == float('inf'):
            return self.stack[0]

        return self.min_value


class MinStack3:
    def __init__(self):
        self.stack = []

        # We keep track of the minimum value for each push(),
        # and push the minimum value into track_stack.
        # NOTE: The length of both stacks are always equal.
        # https://www.geeksforgeeks.org/tracking-current-maximum-element-in-a-stack/
        self.track_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        try:
            current_min = self.track_stack[-1]
        except IndexError:
            self.track_stack.append(x)
        else:
            if x < current_min:
                # There is a new minimum value.
                current_min = x
            else:
                # The minimum is still the same as the last push().
                pass
            self.track_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.track_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.track_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
