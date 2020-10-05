import pytest
from sorting import randomized_quick_sort


def test_sort():
    a = [8,7,6,5,4,3,2,1]
    randomized_quick_sort(a, 0, len(a)-1)
    assert (a == [1,2,3,4,5,6,7,8])

def test_sort_2():
    a = [9,2,3,2,9]
    randomized_quick_sort(a, 0, len(a)-1)
    assert (a == [2,2,3,9,9])


if __name__ == '__main__':
    a = [2,2,5,5,1]
    randomized_quick_sort(a, 0, len(a)-1)
    print(a)