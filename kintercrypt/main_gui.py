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
"""Front end tkinter GUI

This module sets up the GUI for kintercrypt, including the various tkinter widgets and properties
"""

from pathlib import Path
from os.path import getsize
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import tkinter as tk
from time import ctime, time
from kintercrypt.ciphers.cipher_manager import main_cipher


# Adapted class structure from https://www.begueradj.com/tkinter-best-practices/
# too-many-ancestors is disabled since the parent class itself has too
# many ancestors
class App(tk.Frame):  # pylint: disable=too-many-ancestors
    """Configures the main window

    Attributes:

        parent: The parent class, which in this case is an instance of Tk

        width: Minimum possible window width
        height: Minimum possible window height

        file: The file to be encrypted/decrypted
        password: Password to encrypt/decrypt the file

        note: The notebook interface
        tab1: General tab
        tab2: Cipher tab

        output_area: Outputs diagnostic results of encryption
        initial_value: Initial value of the encrypt/decrypt dropdown menu

    """

    def __init__(self, parent: tk.Tk, **kw: object) -> None:
        # Suggested in the Frame docs
        # Inherit the properties of the parent class
        super().__init__(**kw)

        # Configure additional properties
        self.parent = parent

        # Minimum Dimensions are in pixels
        self.width = 400
        self.height = 200

        # File to be encrypted/decrypted and password
        self.file = ""
        self.password = ""

        # Create the tabs
        self.note = ttk.Notebook(self.parent)
        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)

        # Assign tab titles
        self.note.add(self.tab1, text="General")
        self.note.add(self.tab2, text="Cipher")

        self.note.pack(fill=tk.BOTH, expand=True)

        # Outputs diagnostic results of encryption
        # The following properties are not in the "add widgets" method
        # This is since it needs to be accessed by other methods
        self.output_area = ScrolledText(self.tab1, wrap=tk.WORD)

        # Choose between encrypt and decrypt
        # Based off http://effbot.org/tkinterbook/optionmenu.htm
        self.initial_value = tk.StringVar(self.tab1)

        # Password Input
        self.password_entry = ttk.Entry(self.tab1, show="*")
        self.password_entry.grid(
            row=0, column=1, columnspan=3, sticky="WE"
        )  # Seperate grid prevents password_entry from being None

        # Methods to arrange the app
        self.configure_app()
        self.add_widgets_tab1()

        # Beginning output messages
        self.output_area.insert(tk.INSERT, f"KINTERCRYPT LOG:\n")
        self.log_output("kintercrypt started")

    def log_output(self, text: str) -> None:
        """Formats the output to show the time

        Args:
            text: Text to be displayed in the log

        """
        self.output_area.insert(tk.INSERT, f"{ctime()} - {text}\n")

    def configure_app(self) -> None:
        """Sets up properties of the main window"""
        self.parent.title("kintercrypt")
        self.parent.geometry(f"{self.width + 100}x{self.height + 100}"
                             )  # 100x100 bigger than minimum size
        self.parent.minsize(self.width, self.height)

        # Allows the window to be resizable
        # The range denotes the number of columns and rows
        for axis in range(4):
            self.tab1.rowconfigure(axis, weight=1)
            self.tab1.columnconfigure(axis, weight=1)

        self.tab1.grid_columnconfigure(
            0, minsize=110)  # Prevents buttons from being squashed
        self.tab1.grid_rowconfigure(
            0, minsize=40)  # Prevents password area from being squashed

    def add_widgets_tab1(self) -> None:
        """Sets up widgets for the general tab"""

        # Password Label
        ttk.Label(self.tab1, text="Password:").grid(row=0, column=0)

        # Allows the buttons to be in the same grid cell
        button_area = ttk.Frame(self.tab1)
        button_area.grid(row=1, column=0)

        self.initial_value.set("Encrypt")
        # Encrypt twice since otherwise, decypt is the only option
        option_menu = ttk.OptionMenu(button_area, self.initial_value,
                                     "Encrypt", "Encrypt", "Decrypt")
        option_menu.grid(
            row=0, column=0
        )  # Separate grid so that the widget isn't assigned as None

        ttk.Button(
            button_area, text="Choose file", command=self.choose_file).grid(
                row=1, column=0, sticky="WE",
                pady=10)  # Padding for the middle button spaces all buttons

        ttk.Button(
            button_area, text="Start", command=self.start_cipher).grid(
                row=2, column=0, sticky="WE")

        self.output_area.grid(row=1, column=1, columnspan=3, sticky="WE")

    def choose_file(self) -> None:
        """Allows the user to choose a file, and detects if one has been selected"""
        # Creates a file dialog object
        self.file = askopenfilename()

        if not self.file:  # If file selector is opened, but no file is chosen
            self.log_output("No file chosen")
        else:
            # Basename only outputs the file name, not the path
            self.log_output(f"{Path(self.file).stem} chosen")

    def start_cipher(self) -> None:
        """Performs various checks before encryption begins

        After performing the checks, it retrieves the encrypted/decrypted text
        It then writes it to a new file

        """

        # Various errors that can occur
        if not self.file:
            self.log_output("ERROR: File not chosen")
            return

        if not getsize(self.file):
            self.log_output("ERROR: File is empty")
            return

        self.password = self.password_entry.get()

        if not self.password:
            self.log_output("ERROR: Password not set")
            return

        cipher_choice = (self.initial_value.get()
                         )  # Whether the user wants to encrypt or decrypt

        # Encrypt -> Encryption, etc.
        self.log_output(f"{cipher_choice}ion started")
        start_time = time()

        # Opens the chosen file as read only
        with open(self.file, "r") as chosen_file:
            file_contents = chosen_file.read()

        final_result = main_cipher(file_contents, self.password, "XOR",
                                   cipher_choice)

        with open(self.file, "w") as result_file:
            result_file.write(final_result)

        finish_time = time()
        total_duration = round(finish_time - start_time, 4)
        self.log_output(f"{cipher_choice}ion Finished in {total_duration}s!")


def main() -> None:
    """Creates an instance of the App class as the main window and monitors events"""

    # Creates the main window
    window = App(tk.Tk())

    # Runs application and helps to process events
    window.mainloop()


if __name__ == "__main__":
    main()
