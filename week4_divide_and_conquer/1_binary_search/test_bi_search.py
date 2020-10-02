import pytest
from binary_search import binary_search, linear_search, binary_search_while

def test_bi_search():
    assert(binary_search([1,5,8,12,13],8, 0, 4) == linear_search([1,5,8,12,13],8))

def test_bi_search_2():
    assert(binary_search([1,5,8,12,13],13, 0, 4) == linear_search([1,5,8,12,13],13))

def test_bi_search_3():
    assert(binary_search([1,5,8,12,13],20, 0, 4) == linear_search([1,5,8,12,13],20))

def test_bi_search_4():
    assert(binary_search([1,5,8,12,13],1, 0, 4) == linear_search([1,5,8,12,13],1))

def test_bi_search_5():
    assert(binary_search([1,5,8,12,13],-5, 0, 4) == linear_search([1,5,8,12,13],-5))

def test_binary_search_tail_eli():
    assert (binary_search_while([1, 5, 8, 12, 13], -5, 0, 4) == linear_search([1, 5, 8, 12, 13], -5))
