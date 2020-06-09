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

import textwrap
from typing import Tuple


# TODO: Make sure that the file isn't empty
def string_binary(text: str) -> Tuple[int, str]:
    # This conversion is based on unicode code points
    # Technically UTF-8 and UTF-16 aren't fixed width, which makes it harder to decode
    # Although UTF-32 is, this is easier to code in python and requires less bits

    binary_list = []

    # Create a list with the binary values of each character in the text
    # It is first converted to its unicode code point, and this is converted to binary
    binary_list.extend([format(ord(i), 'b') for i in text])

    # The length of the longest binary value is determined
    longest_length = len(max(binary_list, key=len))

    # Zeros are added until its binary value is the same fixed length
    binary_list = [i.zfill(longest_length) for i in binary_list]

    return longest_length, ''.join(binary_list)


def binary_string(chunk_length: int, binary: str) -> str:
    # The chain of binary is broken down into chunks
    binary_chunks = textwrap.wrap(binary, chunk_length)
    # Each value is converted from binary into its decimal unicode code point
    # This is then converted to a character
    final_result = [chr(int(i, 2)) for i in binary_chunks]
    return ''.join(final_result)
