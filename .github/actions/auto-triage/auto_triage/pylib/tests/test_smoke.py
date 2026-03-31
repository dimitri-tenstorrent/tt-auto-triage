"""Smoke test to validate the pytest pipeline works."""


def test_package_imports():
    """Verify the pylib package is importable."""
    import pylib

    assert pylib is not None


def test_python_version():
    """Verify we are running Python 3.11+."""
    import sys

    assert sys.version_info >= (3, 11)
