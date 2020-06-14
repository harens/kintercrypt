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
from kintercrypt import main_gui

# Creates a new instance of the GUI class
window = main_gui.App(tk.Tk())


def test_choose_file(mocker) -> None:

    # File not chosen
    mocker.patch('kintercrypt.main_gui.askopenfilename', return_value='')
    window.choose_file()
    window.start_cipher()

    # File chosen
    mocker.patch('kintercrypt.main_gui.askopenfilename', return_value='demo.txt')
    window.choose_file()
    window.start_cipher()
