import module2 as mod2
from hypothesis import given, example
from hypothesis.strategies import text


def test_func2():
    assert mod2.func2() == "This is a random return string"


@given(s=text())
@example(s="")
# @example(s="hi")
def test_tail(s):
    if len(s) > 0:
        assert s[0] + mod2.tail(s) == s
    else:
        assert mod2.tail(s) == s
