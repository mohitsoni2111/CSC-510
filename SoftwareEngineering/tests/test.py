import pytest

from code import add


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_answer_addition():
    assert add(5, 3) == 8
