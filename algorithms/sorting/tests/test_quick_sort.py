# coding: utf-8
import random
import unittest

import pytest

from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.quick_sort import quick_sort_in_place


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
            [-2, 3, -5],
            [-1, 2, -8, -10],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(quick_sort(array.copy()), sorted(array))


class TestCase2(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
            [-2, 3, -5],
            [-1, 2, -8, -10],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(quick_sort_in_place(array.copy()), sorted(array))


array = [random.randint(-100, 100) for i in range(1000)]
expected = sorted(array.copy())


@pytest.mark.benchmark(group='quick_sort', disable_gc=True, warmup=False)
def test_benchmark_quick_sort(benchmark):
    assert benchmark(quick_sort, array.copy()) == expected


@pytest.mark.benchmark(group='quick_sort', disable_gc=True, warmup=False)
def test_benchmark_quick_sort_in_place(benchmark):
    assert benchmark(quick_sort_in_place, array.copy()) == expected


if __name__ == '__main__':
    unittest.main()
