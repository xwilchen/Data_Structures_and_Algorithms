import pytest
from fractional_knapsack import get_optimal_value

def test_get_optimal_value_1():
    assert (get_optimal_value(50,[60,100,120],[20,50,30]) == 180)

def test_get_optimal_value_2():
    assert (int(get_optimal_value(10,[500],[30])) == 166)

def test_get_optimal_value_3():
    assert (int(get_optimal_value(1000,[500],[30])) == 500)