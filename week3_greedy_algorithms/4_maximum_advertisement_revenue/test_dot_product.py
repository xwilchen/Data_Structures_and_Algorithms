import pytest
from dot_product import max_dot_product

def test_max_dot_product_1():
    assert(max_dot_product([23],[39]) == 897)

def test_max_dot_product_2():
    assert(max_dot_product([1,3,-5],[-2,4,1]) == 23)