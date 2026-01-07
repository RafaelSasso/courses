import pytest

from bank import value


def test_hello():
    assert value("Hello, John") == 0

def test_H():
    assert value("How are you?") == 20

def test_other():
    assert value("Long time no see!") == 100
