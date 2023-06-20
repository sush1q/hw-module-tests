from compute_function import solve


def test_no_roots():
    assert solve(1,0,1) == []

def test_equal_roots():
    assert solve(1,0,-1) == [1,-1]

def test_():
    assert solve(1,2,1) == [1,-1]
