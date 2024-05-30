import pytest
from add import add

@pytest.mark.parametrize("a,b,result", [(3, 5, 8), (2, 4, 6), (-3, -4, -7)])
def test_add(a, b, result):
    c = add(a, b)
    assert c == result
