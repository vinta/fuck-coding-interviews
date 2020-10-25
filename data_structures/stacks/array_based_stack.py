# coding: utf-8
class ArrayBasedStack:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        for item in reversed(self.array):
            yield item

    # O(1)
    def push(self, value):
        self.array.append(value)

    # O(1)
    def pop(self):
        try:
            return self.array.pop()
        except IndexError:
            raise ValueError('stack is empty')

    # O(1)
    def peek(self):
        try:
            return self.array[-1]
        except IndexError:
            raise ValueError('stack is empty')
