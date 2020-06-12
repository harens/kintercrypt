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

"""Xor Cipher

This module contains the function that is able to both encrypt and decrypt text using the xor cipher
"""

from typing import List


def xor_cipher(text: List[int], password: List[int]) -> List[int]:
    """A function that performs the XOR operator on some text and a password

    args:
        text: A list of bytes to encrypt
        password: A list of bytes that represents the password

    returns:
        A list of bytes that represents the text ^ password
    """
    text_length = len(text)
    password_length = len(password)

    # If the password is longer than the text, that is fine
    # This is ince zip() deals with the issue

    if password_length < text_length:
        # This makes the password longer than required
        # It isn't necessary to shorten it, since zip does this for us
        password = password * (text_length // password_length + 1)

    # Performs the xor operator on each element in the two lists
    return [(a ^ b) for (a, b) in zip(text, password)]
