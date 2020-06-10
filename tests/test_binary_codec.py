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

from kintercrypt.binary_codec import binary_string, string_binary


def test_both() -> None:
    assert binary_string(*string_binary("Hello World")) == "Hello World"
    assert binary_string(*string_binary("123ę")) == "123ę"
    assert binary_string(*string_binary(" ")) == " "

    # The following examples are from https://stackoverflow.com/a/51539774/10763533
    # Emoji
    assert binary_string(*string_binary("👱👱🏻👱🏼👱🏽👱🏾👱🏿")) == "👱👱🏻👱🏼👱🏽👱🏾👱🏿"
    assert binary_string(*string_binary("🧟‍♀️🧟‍♂️")) == "🧟‍♀️🧟‍♂️"
    assert binary_string(*string_binary("👨‍❤️‍💋‍👨👩‍👩‍👧‍👦️")) == "👨‍❤️‍💋‍👨👩‍👩‍👧‍👦️"

    # Words in different directions
    assert binary_string(*string_binary("اختبار النص")) == "اختبار النص"
    assert binary_string(*string_binary("اليسار")) == "اليسار"
