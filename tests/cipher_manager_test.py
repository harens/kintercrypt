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
"""Cipher manager test

Tests the encryption and decryption of the ciphers with unicode rather than a list of bytes
"""

import pytest
from kintercrypt.ciphers.cipher_manager import main_cipher
from tests.random_generator import generate_text


@pytest.mark.parametrize(
    ("text", "password"),
    [*zip(generate_text(200, 200), generate_text(200, 200))])
def test_xor(text: str, password: str) -> None:
    """Tests the XOR cipher by using the fact that (A^B)^B == A

    args:
        text: Plaintext to be encrypted and decrypted
        password: Password to encrypt and decrypt the plaintext
    """
    assert main_cipher(main_cipher(text, password, "XOR"), password,
                       "XOR") == text
