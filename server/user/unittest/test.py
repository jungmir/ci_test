import pytest

def target():
    return True

def test():
    assert target() == True