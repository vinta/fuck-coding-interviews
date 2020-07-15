# coding: utf-8
class ArrayBasedStack:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        for item in reversed(self.array):
            yield item

    def push(self, value):
        self.array.append(value)

    def pop(self):
        try:
            return self.array.pop()
        except IndexError:
            raise ValueError('Stack is empty')

    def peek(self):
        try:
            return self.array[-1]
        except IndexError:
            raise ValueError('Stack is empty')
