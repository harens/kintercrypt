# /usr/bin/env python

# This file is part of kintercrypt.

# kintercrypt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# kintercrypt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with kintercrypt.  If not, see <http://www.gnu.org/licenses/>.

"""Binary Codec Tests

This script tests various aspects of the two binary codec functions
Tests codec with characters of varying difficulty
Both are tested simultaneously, be encoding a value and then decoding it
"""

import pytest
from kintercrypt.bytes_codec import bytes_string, string_bytes
from tests.random_generator import generate_text


def test_simple() -> None:
    """More Simple characters"""
    assert bytes_string(string_bytes("Hello World")) == "Hello World"
    assert bytes_string(string_bytes("123ę")) == "123ę"
    assert bytes_string(string_bytes(" ")) == " "


# The following examples are from https://stackoverflow.com/a/51539774/10763533


def test_emoji() -> None:
    """Unicode Emojis"""
    assert bytes_string(string_bytes("👱👱🏻👱🏼👱🏽👱🏾👱🏿")) == "👱👱🏻👱🏼👱🏽👱🏾👱🏿"
    assert bytes_string(string_bytes("🧟‍♀️🧟‍♂️")) == "🧟‍♀️🧟‍♂️"
    assert bytes_string(string_bytes("👨‍❤️‍💋‍👨👩‍👩‍👧‍👦️")) == "👨‍❤️‍💋‍👨👩‍👩‍👧‍👦️"


def test_other() -> None:
    """Characters that do not match the other groups"""

    # Words in different directions
    assert bytes_string(string_bytes("اختبار النص")) == "اختبار النص"
    assert bytes_string(string_bytes("اليسار")) == "اليسار"


# Generates 200 strings of max length 200 of random unicode
@pytest.mark.parametrize("text", [*(generate_text(200, 200))])
def test_random(text: str) -> None:
    """Tests with randomly generated strings"""
    assert bytes_string(string_bytes(text)) == text
