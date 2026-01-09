from um import count


def test_in_words():
    assert count("Um, I'll go to a forum") == 1

def test_spaces():
    assert count("Hello,um, world um") == 2
