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
"""Bytes codec

This module contains two functions that convert between a string and a list of bytes
"""
from typing import List


def string_bytes(text: str, cryption: str = "Encrypt") -> List[int]:
    """Generates a list of bytes from a string

    Args:
        text: The text to be converted
        cryption: Whether the function is being used for encryption or decryption

    Returns:
        A list of bytes that represents the integer unicode codepoint value
    """

    if cryption == "Encrypt":
        return [ord(i) for i in text]

    # 32 is subtracted to allow 32 to be added below
    # This helps to fix an error with control codes that is described below in
    # the inverse function
    # This decrypts the string to the original bytes rather than the shifted ones
    return [ord(i) - 32 for i in text]


def bytes_string(bytes_list: List[int], cryption: str = "Encrypt") -> str:
    """The inverse function to string_bytes. Coverts a list of bytes to a string

    Args:
        bytes_list: A list of bytes that represent the integer unicode codepoint value
        cryption: Whether the function is being used for encryption or decryption

    Returns:
        A string that is the result of the conversion"""

    if cryption == "Encrypt":
        # 32 added in case some bytes that result from the various ciphers correspond to control codes
        # These control codes make things a bit difficult, so its easier to shift everything by 32
        # Values after 32 correspond to symbols that aren't control codes
        return "".join(chr(i + 32) for i in bytes_list)

    return "".join(chr(i) for i in bytes_list)
