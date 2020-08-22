import module3 as mod3


def test_foo_bar():
    assert mod3.foo_bar() == mod3.__file__
