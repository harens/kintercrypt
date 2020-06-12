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

from typing import List
import pytest
from kintercrypt.ciphers.xor_cipher import xor_cipher
from tests.random_generator import generate_byte_list


# Sets the arguments to be random lists of bytes of maximum length 200
# It repeats this 200 times
@pytest.mark.parametrize(
    ("text", "password"), [*zip(generate_byte_list(200, 200), generate_byte_list(200, 200))]
)
def test_xor(text: List[int], password: List[int]) -> None:
    """Tests the XOR cipher by using the fact that (A^B)^B == A

    args:
        text: The plaintext to be encrypted and decrypted
        password: The password that is applied to the text via the xor operator
    """

    assert xor_cipher(xor_cipher(text, password), password) == text
