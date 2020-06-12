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

"""XOR Cipher Tests

Generates a random password and text and checks if it is encrypted/decrypted successfully
"""

from random import randint
import pytest
from kintercrypt.ciphers.xor_cipher import xor_cipher


def generate_binary(length: int) -> str:
    """Generates random binary numbers upto some length"""

    # Generates 'length' amount of numbers
    # If current_length was 0, the output would be ''
    for current_length in range(1, length + 1):
        # Generates a number between 0 and 1 that is the same length as current_length
        yield ''.join(str(randint(0, 1)) for _ in range(current_length))


# Sets the text and password as random binary digits upto some length
@pytest.mark.parametrize(('text', 'password'), [*zip(generate_binary(100), generate_binary(100))])
def test_xor(text: str, password: str) -> None:
    """Tests the XOR cipher by using the fact that (A^B)^B == A"""
    assert xor_cipher(xor_cipher(text, password), password) == text
