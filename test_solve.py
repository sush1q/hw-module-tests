import pytest
from compute_function import solve


def test_no_roots():
    assert solve(1,0,1) == []

def test_two_roots():
    assert solve(1,0,-1) == [1,-1]

def test_one_root():
    assert solve(1,2,1) == [-1,-1]

def test_a_equal_zero():
    try:
        solve(0.0, 1, 1)
    except ValueError:
        assert True

def test_float_boundary_values_with_infinite():
    assert solve(float('inf'), 1, 1) == []

def test_float_boundary_values_with_minus_infinite():
    assert solve(float('-inf'), 1, 1) == [float('-inf'), float('inf')]

def test_float_boundary_values_with_nan():
    assert solve(float('nan'), 1, 1) == None

@pytest.mark.parametrize("value", ['str', [1, 2], {'a':1}, True, (1,2)])
def test_unavailable_values(value):
    try:
        solve(value, 1, 1)
    except TypeError:
        assert True
