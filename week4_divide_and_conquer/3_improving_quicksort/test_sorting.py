import pytest
from sorting import randomized_quick_sort

def test_sort():
    assert(randomized_quick_sort([2,3,9,2,9],0,4) == [2,2,3,9,9])

