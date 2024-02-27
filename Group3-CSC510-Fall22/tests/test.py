from src.subtraction import subtraction
import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_answer_subtraction():
    assert subtraction(5, 3) == 2