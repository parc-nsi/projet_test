from exo import *
import pytest


def test_somme():
    """test"""
    assert somme([0]) == 0
    assert somme([1, 2]) == 3
