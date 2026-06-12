from mylib import foo


def test_foo_sum():
    assert foo.sum(1, 2) == 3
    assert foo.sum(-1, 1) == 0
