import pytest
import cr

def test_health():
    assert cr.health() == '200'

