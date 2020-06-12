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


def xor_cipher(text: str, password: str) -> str:
    text_length = len(text)
    password_length = len(password)

    if password_length > text_length:
        password = password[:text_length]

    elif password_length < text_length:
        password = password * (text_length // password_length + 1)
        password = password[:text_length]

    return ''.join([str(int(char) ^ int(password[pos])) for (pos, char) in enumerate(text)])
