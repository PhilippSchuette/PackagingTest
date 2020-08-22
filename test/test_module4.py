import sub_module.module4 as mod4


def test_func3():
    assert mod4.func3() == mod4.__package__
