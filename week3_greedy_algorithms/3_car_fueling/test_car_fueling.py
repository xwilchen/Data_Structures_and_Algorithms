import pytest
from car_fueling import compute_min_refills

def test_compute_min_refills_1():
    assert(compute_min_refills(950,400,[200,375,550,750]) == 2)

def test_compute_min_refills_2():
    assert(compute_min_refills(950,400,[200,375,550,750,950]) == 2)

def test_compute_min_refills_3():
    assert(compute_min_refills(10,3,[1,2,5,9]) == -1)

def test_compute_min_refills_4():
    assert(compute_min_refills(10,3,[1,2,5,8]) == 3)

def test_compute_min_refills_5():
    assert(compute_min_refills(200,250,[100,150]) == 0)

def test_compute_min_refills_6():
    assert(compute_min_refills(200,150,[]) == -1)

def test_compute_min_refills_7():
    assert(compute_min_refills(700,100,[50, 150, 200, 275, 300, 400, 425, 525, 600, 700]) == 8)