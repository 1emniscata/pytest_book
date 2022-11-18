import pytest


def test_this_passes():
    assert 1 == 1

@pytest.mark.xfail(reason="Deliberate fail")
def test_this_fails():
    assert 1 == 2