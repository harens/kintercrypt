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
"""Main GUI Tests

This script tests various aspects of the front end tkinter gui
"""

import tkinter as tk
from pytest_mock import MockFixture, pytest

from kintercrypt import main_gui

# Creates a new instance of the GUI class
WINDOW = main_gui.App(tk.Tk())


def test_choose_file(mocker: MockFixture) -> None:
    """Runs various methods depending on whether a file has been chosen

    args:
        mocker: Wrapper for pytest of the mock package
    """

    # File not chosen
    mocker.patch("kintercrypt.main_gui.askopenfilename", return_value="")
    WINDOW.choose_file()
    WINDOW.start_cipher()

    # File chosen
    mocker.patch(
        "kintercrypt.main_gui.askopenfilename",
        return_value="example_file.txt")
    WINDOW.choose_file()


# Session scope since we still want the file to have some contents for the next tests
def test_file_contents(session_mocker: MockFixture) -> None:
    """Runs the start cipher method with different file contents

        args:
            mocker: Wrapper for pytest of the mock package
    """

    # File is empty
    session_mocker.patch("kintercrypt.main_gui.getsize", return_value=0)
    WINDOW.start_cipher()

    # File has contents
    session_mocker.patch("kintercrypt.main_gui.getsize", return_value=1)
    WINDOW.start_cipher()


def test_password(mocker: MockFixture) -> None:
    """Runs the start cipher method with different passwords

            args:
                mocker: Wrapper for pytest of the mock package
        """
    # No password
    mocker.patch(
        "tests.main_gui_test.WINDOW.password_entry.get", return_value=0)
    WINDOW.start_cipher()

    # Sets password
    mocker.patch(
        "tests.main_gui_test.WINDOW.password_entry.get",
        return_value='example_password')

    # Contents of file
    mocker.patch('builtins.open',
                 mocker.mock_open(read_data='example content'))
    WINDOW.start_cipher()
