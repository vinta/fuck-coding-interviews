# coding: utf-8
import random

import pytest

from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.quick_sort import quick_sort_in_place


array = [random.randint(-100, 100) for i in range(1000)]
expected = sorted(array.copy())


@pytest.mark.benchmark(group='quick_sort', disable_gc=True, warmup=False)
def test_benchmark_quick_sort(benchmark):
    assert benchmark(quick_sort, array.copy()) == expected


@pytest.mark.benchmark(group='quick_sort', disable_gc=True, warmup=False)
def test_benchmark_quick_sort_in_place(benchmark):
    assert benchmark(quick_sort_in_place, array.copy()) == expected
