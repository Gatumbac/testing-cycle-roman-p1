import pytest

from roman.converter import RomanError, from_roman, is_valid_roman


def test_ac1_non_canonical_is_rejected():
    with pytest.raises(RomanError):
        from_roman("IIII")


def test_ac2_surrounding_whitespace_is_trimmed():
    assert from_roman("  IV  ") == 4


def test_ac3_is_valid_roman_never_raises():
    assert is_valid_roman(None) is False


def test_repeated_single_symbol_is_rejected():
    with pytest.raises(RomanError):
        from_roman("VV")


def test_group_out_of_order_is_rejected():
    with pytest.raises(RomanError):
        from_roman("XCM")


def test_repeated_subtractive_pair_is_rejected():
    with pytest.raises(RomanError):
        from_roman("IXIX")


def test_group_after_subtractive_pair_is_rejected():
    with pytest.raises(RomanError):
        from_roman("IVI")
