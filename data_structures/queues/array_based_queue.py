# coding: utf-8
class ArrayBasedQueue:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        for item in self.array:
            yield item

    # O(1)
    def enqueue(self, value):
        self.array.append(value)

    # O(n)
    def dequeue(self):
        try:
            return self.array.pop(0)
        except IndexError:
            raise ValueError('queue is empty')
