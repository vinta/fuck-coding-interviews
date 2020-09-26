# coding: utf-8
"""
https://www.hackerrank.com/challenges/simple-text-editor/problem
"""


class SimpleTextEditor:
    def __init__(self):
        self.s = ''

        # It works as a stack for storing full copies of previous s.
        # However, it might take too much memory resource if s is huge.
        self.s_history = []

    def add_history(self):
        # TODO: Other implementations:
        # https://stackoverflow.com/questions/1915907/best-practice-for-undo-redo-implementation
        self.s_history.append(self.s)

    # 1: Append string w to the end of s.
    def append(self, w):
        self.s += w

    # 2: Delete the last k characters of s.
    def delete(self, k):
        self.s = self.s[:len(self.s) - k]

    # 3: Print the k-th character of s.
    def print_(self, k):
        print(self.s[k - 1])

    # 4: Undo the last (not previously undone) operation of type 1 or 2,
    # reverting s to the state it was in prior to that operation.
    def undo(self):
        self.s = self.s_history.pop()


_ = input()
editor = SimpleTextEditor()

while True:
    try:
        line = input().split()
    except EOFError:
        break

    operation = line[0]
    if operation == '1':
        w = line[1]
        editor.add_history()
        editor.append(w)
    elif operation == '2':
        k = int(line[1])
        editor.add_history()
        editor.delete(k)
    elif operation == '3':
        k = int(line[1])
        editor.print_(k)
    elif operation == '4':
        editor.undo()
