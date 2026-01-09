from jar import Jar

import pytest


def test_init():
    jar1 = Jar(10)
    assert jar1.capacity == 10

    jar2 = Jar()
    assert jar2.capacity == 12

    jar3 = Jar(5)
    assert jar3.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(0)
    assert str(jar) == ""
    jar.deposit(1)
    print(jar.size)
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(0)
    assert str(jar) == "🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar.withdraw(2)
