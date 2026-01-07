from plates import is_valid


def test_valid():
    assert is_valid("IAMA10") == True
    assert is_valid("CS50") == True

def test_strStart():
    assert is_valid("A1") == False
    assert is_valid("12") == False

def test_lenght():
    assert is_valid("1") == False
    assert is_valid("IAMA111") == False

def test_notAlpha():
    assert is_valid("IAM !0") == False
    assert is_valid("PI3.14") == False

def test_letterAfterNumber():
    assert is_valid("IAM10A") == False
    assert is_valid("CS05") == False
