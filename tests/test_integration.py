import pytest

from roman.converter import RomanError, add_roman, is_valid_roman, subtract_roman


def test_add_roman_returns_canonical_result():
    assert add_roman("II", "II") == "IV"


def test_add_roman_result_is_accepted_by_is_valid_roman():
    assert is_valid_roman(add_roman("II", "II"))


def test_subtract_roman_out_of_range():
    with pytest.raises(RomanError):
        subtract_roman("I", "I")
