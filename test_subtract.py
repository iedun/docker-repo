import pytest
from subtract import subtract

@pytest.mark.parametrize("a,b,result", [(3, 5, -2), (2, 4, -2), (-3, -4, 1)])
def test_subtract(a, b, result):
    c = subtract(a, b)
    assert c == result

def test_subtract_type_error():
    with pytest.raises(TypeError):
          c = subtract(4, "b")
