from compute_function import solve


def test_no_roots():
    assert solve(1,0,1) == []

def test_two_roots():
    assert solve(1,0,-1) == [1,-1]

def test_one_root():
    assert solve(1,2,1) == [-1,-1]

def test_a_equal_zero():
    try:
        solve(0, 1, 1)
    except ValueError:
        assert True
        
