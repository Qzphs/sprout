import pytest

import sprout as s


def test_font():
    font = s.Font("Sans Serif", 24, bold=True, underline=True)
    assert font.family == "Sans Serif"
    assert font.size == 24
    assert font.bold
    assert not font.italic
    assert font.underline
    assert not font.strikethrough


def test_font_copy():
    font = s.Font("Sans Serif", 24, bold=True, underline=True)
    copy = font.copy(size=18, bold=True, italic=False, underline=False)
    assert copy.size == 18
    assert copy.bold
    assert not copy.italic
    assert not copy.underline
