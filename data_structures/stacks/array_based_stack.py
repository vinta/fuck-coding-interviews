# coding: utf-8
import unittest


class ArrayBasedStack:
    def __init__(self):
        self.array = []

    def __bool__(self):
        return bool(self.array)

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


class TestCase(unittest.TestCase):
    def setUp(self):
        self.stack = ArrayBasedStack()

    def test__bool__(self):
        self.assertFalse(self.stack)

        self.stack.push(0)
        self.assertTrue(self.stack)

    def test_push(self):
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(list(self.stack), [2, 1, 0])

    def test_pop(self):
        with self.assertRaises(ValueError):
            print(self.stack.pop())

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 0)
        self.assertEqual(list(self.stack), [])

        with self.assertRaises(ValueError):
            print(self.stack.pop())

    def test_peek(self):
        with self.assertRaises(ValueError):
            print(self.stack.peek())

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)


if __name__ == '__main__':
    unittest.main()
