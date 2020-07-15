# coding: utf-8
import unittest

from data_structures.stacks.array_based_stack import ArrayBasedStack


class TestCase(unittest.TestCase):
    def setUp(self):
        self.stack = ArrayBasedStack()

    def test_push(self):
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 3)
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
        self.assertEqual(len(self.stack), 0)
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
