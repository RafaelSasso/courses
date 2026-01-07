import pytest

from twttr import shorten

def test_vowelOnly():
    assert shorten("aaAAaa") == ""

def test_Twitter():
    assert shorten("Twitter") == "Twttr"

def test_noVowel():
    assert shorten("Shrt") == "Shrt"

def test_notLetters():
    assert shorten("12.") == "12."
