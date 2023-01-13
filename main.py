import pytest

from yandex_testing_lesson import is_under_queen_attack


def test_horisontal_right():
    assert is_under_queen_attack('b2', 'e2') is True


def test_horisontal_left():
    assert is_under_queen_attack('b2', 'a2') is True


def test_vertical_up():
    assert is_under_queen_attack('b2', 'b8') is True


def test_vertical_down():
    assert is_under_queen_attack('b2', 'b1') is True


def test_diagonal_up_right():
    assert is_under_queen_attack('b2', 'c3') is True


def test_diagonal_up_left():
    assert is_under_queen_attack('b2', 'a3') is True


def test_diagonal_down_right():
    assert is_under_queen_attack('b2', 'c1') is True


def test_diagonal_down_left():
    assert is_under_queen_attack('b2', 'a1') is True


def test_not_under_attack_horse():
    assert is_under_queen_attack('b2', 'd3') is False


def test_not_under_attack_far():
    assert is_under_queen_attack('b2', 'd6') is False


def test_incorrect_position_empty():
    with pytest.raises(ValueError):
        is_under_queen_attack('', 'd6')


def test_incorrect_queen_position_empty():
    with pytest.raises(ValueError):
        is_under_queen_attack('a1', '')


def test_incorrect_position_not_on_board():
    with pytest.raises(ValueError):
        is_under_queen_attack('a9', 'd6')


def test_incorrect_queen_position_not_on_board():
    with pytest.raises(ValueError):
        is_under_queen_attack('a8', 'i2')


def test_incorrect_position_too_long():
    with pytest.raises(ValueError):
        is_under_queen_attack('c51', 'h2')


def test_incorrect_queen_position_too_long():
    with pytest.raises(ValueError):
        is_under_queen_attack('a8', 'aa2')


def test_attack_yourself():
    assert is_under_queen_attack('f6', 'f6') is False