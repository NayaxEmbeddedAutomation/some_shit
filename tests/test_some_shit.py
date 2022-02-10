from somesome.shitshit import print_equal
import pytest


@pytest.mark.parametrize("a, b, c", [
    (1, 3, False),
    (3, 3, True),
    ("a", 3, False),
    (3, "a", "False"),

])
def test_some_shit(a, b, c):
    assert print_equal(a, b) == c
