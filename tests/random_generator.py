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

"""This module generates random data used for various tests"""

from random import sample, randrange
from typing import Iterator, List

# has to be less than 1114111, since there a limited number of unicode code points
max_unicode_codepoint = 100000


def generate_byte_list(number_lists: int = 1, list_length: int = 1) -> Iterator[List[int]]:
    """Generates a random list of bytes

    args:
        number_lists: An integer representing the number of lists
        list_length: The maximum length of the generated lists

    returns:
        An iterator that generates a random list of bytes
    """

    # Generates lists with a maximum value of the fixed number in the range
    for _ in range(number_lists):
        # First range represents the maximum value in the list
        # Can't be less than 32, since this results in control codes (This is accounted for from ciphers)
        # Minimum length has to be 1 (again accounted for if there is no password or file is empty)
        yield sample(range(32, max_unicode_codepoint), randrange(1, list_length))


def generate_text(number_text: int, text_length: int) -> Iterator[str]:
    """Generates a random string of unicode

    args:
        number_text: The number of strings of text to generate
        text_length: The length of each string generated

    returns:
        A random string of unicode
    """

    # Takes random lists of bytes
    for value in list(generate_byte_list(number_text, text_length)):
        # Converts the lists of bytes to unicode
        yield ''.join(chr(i) for i in value)
