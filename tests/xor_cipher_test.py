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

from random import sample
from typing import Iterator, List
import pytest
from kintercrypt.ciphers.xor_cipher import xor_cipher


def generate_byte_list(length: int) -> Iterator[List[int]]:
    """Generates a random list of bytes

    args:
        length: An integer representing the maximum length of the generated lists

    returns:
        An iterator that generates a random list of bytes
    """
    # Generates lists of every positive length upto the length stated
    for current_length in range(1, length + 1):
        # Maximum possible value in the list is set in the range
        yield sample(range(20000), current_length)


# Sets the arguments to be random lists of bytes
@pytest.mark.parametrize(
    ("text", "password"), [*zip(generate_byte_list(100), generate_byte_list(100))]
)
def test_xor(text: List[int], password: List[int]) -> None:
    """Tests the XOR cipher by using the fact that (A^B)^B == A

    args:
        text: The plaintext to be encrypted and decrypted
        password: The password that is applied to the text via the xor operator
    """

    assert xor_cipher(xor_cipher(text, password), password) == text
