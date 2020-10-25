# coding: utf-8
import random

import pytest

from algorithms.sorting.quicksort import quicksort
from algorithms.sorting.quicksort import quicksort_in_place


array = [random.randint(-100, 100) for i in range(1000)]
expected = sorted(array.copy())


@pytest.mark.benchmark(group='quicksort', disable_gc=True, warmup=False)
def test_benchmark_quicksort(benchmark):
    assert benchmark(quicksort, array.copy()) == expected


@pytest.mark.benchmark(group='quicksort', disable_gc=True, warmup=False)
def test_benchmark_quicksort_in_place(benchmark):
    assert benchmark(quicksort_in_place, array.copy()) == expected
