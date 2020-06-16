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
"""Cipher manager

This module contains a function to chooses which cipher is necessary
"""

import textwrap
from typing import List
from kintercrypt.ciphers.xor_cipher import xor_cipher
import kintercrypt.bytes_codec as codec


def main_cipher(text: str,
                password: str,
                algorithm: str,
                crypt: str = "Encrypt") -> str:
    """Chooses the necessary cipher and operation

    args:
        text: The text to encrypt/decrypt
        password: The password to encrypt/decrypt the text
        algorithm: The function to encrypt/decrypt the text
        crypt: Whether the user wants to encrypt or decrypt

    returns:
        The final result of the encryption/decryption process
    """

    # Newlines are added to the ciphertext to format it nicely
    # These newlines are removed when decrypting
    if crypt == 'Decrypt':
        text = text.replace('\n', '')

    # Convert both the plaintext/ciphertext and password to a list of bytes
    plaintext_bytes = codec.string_bytes(text, crypt)
    password_bytes = codec.string_bytes(password)

    bytes_result: List[int] = []

    if algorithm == "XOR":
        bytes_result = xor_cipher(plaintext_bytes, password_bytes)

    # Output of algorithm converted to a string
    final_output = codec.bytes_string(bytes_result, crypt)

    # Adds newlines to the ciphertext to format it nicely
    if crypt == 'Encrypt':
        line_break = 79
        final_output = '\n'.join(
            textwrap.wrap(final_output,
                          line_break,
                          replace_whitespace=False,
                          drop_whitespace=False))

    return final_output
