import functions
import pytest


def test_is_solved():
    board = [x for x in range(1, 16)] + [0]
    assert functions.is_solved(board) == 0


def test_is_win_1():
    board = [x for x in range(1, 16)] + [0]
    assert functions.is_win(board) == 1


def test_is_win_2():
    board = [x for x in range(16)]
    assert functions.is_win(board) == 0
