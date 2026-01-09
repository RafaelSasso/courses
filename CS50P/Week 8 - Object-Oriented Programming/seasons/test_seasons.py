from seasons import format

import pytest


def test_error():
    with pytest.raises(ValueError):
        format("January 10, 2020")

    with pytest.raises(ValueError):
        format("1999/01/01")


def test_pass():
    assert format("2005-01-15") == "Eleven million, thirty-six thousand, one hundred and sixty minutes"
    assert format("1999-10-10") == "Thirteen million, eight hundred and six thousand, seven hundred and twenty minutes"

