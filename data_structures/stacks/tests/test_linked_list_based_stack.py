# coding: utf-8
import unittest

from data_structures.stacks.linked_list_based_stack import LinkedListBasedStack


class TestCase(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedListBasedStack()

    def test__len__(self):
        self.assertEqual(len(self.stack), 0)

        self.stack.push(0)
        self.assertEqual(len(self.stack), 1)

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
