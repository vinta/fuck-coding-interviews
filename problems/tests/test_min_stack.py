# coding: utf-8
import unittest

from problems.min_stack import MinStack
from problems.min_stack import MinStack2
from problems.min_stack import MinStack3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def test(self):
        self.min_stack.push(-2)
        self.min_stack.push(0)
        self.min_stack.push(-3)
        self.assertEqual(self.min_stack.getMin(), -3)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 0)
        self.assertEqual(self.min_stack.getMin(), -2)

    def test_2(self):
        self.min_stack.push(0)
        self.min_stack.push(1)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.getMin(), 0)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 0)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack2()

    def test_1(self):
        self.min_stack.push(-2)
        self.min_stack.push(0)
        self.min_stack.push(-3)
        self.assertEqual(self.min_stack.getMin(), -3)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 0)
        self.assertEqual(self.min_stack.getMin(), -2)

    def test_2(self):
        self.min_stack.push(0)
        self.min_stack.push(1)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.getMin(), 0)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 0)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack3()

    def test_1(self):
        self.min_stack.push(-2)
        self.min_stack.push(0)
        self.min_stack.push(-3)
        self.assertEqual(self.min_stack.getMin(), -3)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 0)
        self.assertEqual(self.min_stack.getMin(), -2)

    def test_2(self):
        self.min_stack.push(0)
        self.min_stack.push(1)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.getMin(), 0)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 0)


if __name__ == '__main__':
    unittest.main()
