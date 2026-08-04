import pytest

from roman.converter import (
    RomanError,
    add_roman,
    from_roman,
    is_valid_roman,
    subtract_roman,
    to_roman,
)


def test_p1_not_an_integer():
    with pytest.raises(RomanError):
        to_roman("5")


def test_p1_bool_is_not_an_integer():
    with pytest.raises(RomanError):
        to_roman(True)


def test_p2_below_minimum():
    with pytest.raises(RomanError):
        to_roman(0)


def test_p3_above_maximum():
    with pytest.raises(RomanError):
        to_roman(4000)


def test_p5_loop_skips_every_pair_but_the_last():
    assert to_roman(1) == "I"


def test_p6_loop_body_executed_once():
    assert to_roman(1000) == "M"


def test_loop_body_executed_several_times():
    assert to_roman(3000) == "MMM"


def test_upper_boundary():
    assert to_roman(3999) == "MMMCMXCIX"


def test_from_roman_not_a_string():
    with pytest.raises(RomanError):
        from_roman(5)


def test_from_roman_empty_string():
    with pytest.raises(RomanError):
        from_roman("")


def test_from_roman_invalid_character():
    with pytest.raises(RomanError):
        from_roman("A")


def test_from_roman_subtractive_pair():
    assert from_roman("IV") == 4


def test_from_roman_invalid_subtractive_pair():
    with pytest.raises(RomanError):
        from_roman("IL")


def test_from_roman_out_of_range():
    with pytest.raises(RomanError):
        from_roman("MMMM")


def test_from_roman_mixed():
    assert from_roman("MCMXCIV") == 1994


def test_is_valid_roman_true():
    assert is_valid_roman("X") is True


def test_is_valid_roman_false():
    assert is_valid_roman("A") is False


def test_add_roman():
    assert add_roman("I", "I") == "II"


def test_subtract_roman():
    assert subtract_roman("X", "V") == "V"
