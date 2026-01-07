import pytest

from fuel import gauge, convert

def test_E():
    assert convert("0/2") == 0
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_F():
    assert convert("1/1") == 100
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_default():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"

def test_valueError():
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("cat")

def test_zeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
