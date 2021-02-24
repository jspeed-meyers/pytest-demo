"""Test functions in normal.py"""

from normal import salutation, repeatName


def test_salutation():
    """Unit test for salutation()."""
    assert salutation("Kinga") == "Hello, Kinga!"


def test_repeatName():
    """Unit test for repeatName()."""
    assert repeatName("Zig", 3) == "ZigZigZig"
