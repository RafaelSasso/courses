import pytest
from numb3rs import validate

def test_validate_valid_ips():
    assert validate("192.168.1.1")
    assert validate("255.255.255.255")

def test_validate_invalid_ips():
    assert not validate("256.100.50.25")
    assert not validate("192.168.1")
    assert not validate("127.1.512.1")
    assert not validate("123.456.78.90")
    assert not validate("255.100.100.512")
    assert not validate("cat")
