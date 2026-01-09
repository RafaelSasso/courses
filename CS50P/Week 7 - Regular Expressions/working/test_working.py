# I didn't really understand what those 2 errors meant
# and couldn't fix them so I just upload with them triggered:

#   :( test_working.py catches working.py printing hours off by one
#       expected exit code 1, not 0
#   :( test_working.py catches working.py printing minutes off by five
#       expected exit code 1, not 0

import pytest
from working import convert

def test_error():
    with pytest.raises(ValueError):
        convert("9 AM 10 AM")
    with pytest.raises(ValueError):
        convert("9AM to 10AM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 10:60 AM")

def test_working():
    assert convert("9 AM to 5 PM")
    assert convert("12:30 AM to 12:30 PM")
    assert convert("11 AM to 12 PM")
    assert convert("9:55 AM to 10 AM")
