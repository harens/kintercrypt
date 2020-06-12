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


# Since its quite difficult to test tkinter, the tests are currently very basic
def test() -> None:
    """Creates a new instance of the GUI class"""
    main_gui.App(tk.Tk())
