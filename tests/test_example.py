"""Tests for example module."""

from example import add, multiply


def test_add():
    """Test add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_multiply():
    """Test multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0


def test_version():
    """Test version is set."""
    from example import __version__
    assert __version__ == "0.1.0"
