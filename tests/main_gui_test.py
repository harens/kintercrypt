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
from pytest_mock import MockFixture
from kintercrypt import main_gui

# Creates a new instance of the GUI class
WINDOW = main_gui.App(tk.Tk())


# Session mocker since we want the output_area contents to be accessible to the next test
# We also want pop ups to not appear throughout
def test_user_text(session_mocker: MockFixture) -> None:
    """Runs various methods depending on whether text has been entered

    args:
        mocker: Wrapper for pytest of the mock package
    """

    # Prevents pop ups from appearing
    session_mocker.patch("kintercrypt.main_gui.showerror")

    # Text not entered
    WINDOW.start_cipher()

    # Text entered
    session_mocker.patch("tests.main_gui_test.WINDOW.output_area.get",
                         return_value="example text")
    WINDOW.start_cipher()


def test_password(mocker: MockFixture) -> None:
    """Runs the start cipher method with different passwords

            args:
                mocker: Wrapper for pytest of the mock package
        """

    # No password
    mocker.patch("tests.main_gui_test.WINDOW.password_entry.get",
                 return_value=0)

    # Sets password
    mocker.patch("tests.main_gui_test.WINDOW.password_entry.get",
                 return_value='example_password')

    WINDOW.start_cipher()
