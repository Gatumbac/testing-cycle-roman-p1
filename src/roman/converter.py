class RomanError(ValueError):
    pass


_PAIRS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


_SINGLE = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


_VALID_SUBTRACTIVE = {"IV", "IX", "XL", "XC", "CD", "CM"}


_MIN_VALUE = 1
_MAX_VALUE = 3999


def to_roman(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise RomanError("value must be an integer")
    if n < _MIN_VALUE:
        raise RomanError("value must be >= 1")
    if n > _MAX_VALUE:
        raise RomanError("value must be <= 3999")
    out = []
    remaining = n
    for value, symbol in _PAIRS:
        while remaining >= value:
            out.append(symbol)
            remaining -= value
    return "".join(out)


def _canonical_error(text, groups):
    for symbol in "VLD":
        if text.count(symbol) > 1:
            return symbol + " appears more than once"
    run = 1
    for i in range(1, len(text)):
        run = run + 1 if text[i] == text[i - 1] else 1
        if run > 3:
            return text[i] + " appears four times in a row"
    used_pairs = []
    previous = None
    limit = None
    for value, subtracted, source in groups:
        if subtracted is not None and source in used_pairs:
            return source + " is used more than once"
        if previous is not None and value > previous:
            return source + " is worth more than the group before it"
        if limit is not None and value >= limit:
            return source + " is not smaller than the previous subtracted symbol"
        if subtracted is not None:
            used_pairs.append(source)
            limit = subtracted
        previous = value
    return None


def from_roman(s):
    if not isinstance(s, str):
        raise RomanError("value must be a string")
    text = s.strip().upper()
    if text == "":
        raise RomanError("empty string is not a roman numeral")
    for ch in text:
        if ch not in _SINGLE:
            raise RomanError("invalid roman character: " + ch)
    total = 0
    i = 0
    length = len(text)
    groups = []
    while i < length:
        if i + 1 < length:
            pair = text[i:i + 2]
            if pair in _VALID_SUBTRACTIVE:
                value = _SINGLE[pair[1]] - _SINGLE[pair[0]]
                groups.append((value, _SINGLE[pair[0]], pair))
                total += value
                i += 2
                continue
        current = _SINGLE[text[i]]
        if i + 1 < length:
            nxt = _SINGLE[text[i + 1]]
            if current < nxt:
                raise RomanError("invalid subtractive pair: " + text[i:i + 2])
        groups.append((current, None, text[i]))
        total += current
        i += 1
    if total < _MIN_VALUE or total > _MAX_VALUE:
        raise RomanError("value out of range 1..3999")
    problem = _canonical_error(text, groups)
    if problem is not None:
        raise RomanError("not a canonical roman numeral: " + problem)
    return total


def _roundtrip_differs(value, text):
    return to_roman(value) != text


def _count_char(text, ch):
    total = 0
    for c in text:
        if c == ch:
            total += 1
    return total


def is_valid_roman(s):
    try:
        from_roman(s)
        return True
    except RomanError:
        return False


def add_roman(a, b):
    return to_roman(from_roman(a) + from_roman(b))


def subtract_roman(a, b):
    return to_roman(from_roman(a) - from_roman(b))
