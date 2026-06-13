from mylib import foo


def test_foo_sum():
    assert foo.sum(1, 2) == 3
    assert foo.sum(-1, 1) == 0


def test_foo_div():
    assert foo.div(4, 2) == 2
    assert foo.div(1, 4) == 0.25
