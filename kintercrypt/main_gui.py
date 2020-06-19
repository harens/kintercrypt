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

from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror
from tkinter import ttk
import tkinter as tk
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

        # Create the tabs
        self.note = ttk.Notebook(self.parent)
        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)

        # Assign tab titles
        self.note.add(self.tab1, text="General")
        self.note.add(self.tab2, text="Settings")

        self.note.pack(fill=tk.BOTH, expand=True)

        # Allows user to input plaintext and receive ciphertext
        # The following properties are not in the "add widgets" method
        # This is since it needs to be accessed by other methods
        self.output_area = ScrolledText(self.tab1, wrap=tk.WORD)

        # Choose between encrypt and decrypt and which cipher
        # Based off http://effbot.org/tkinterbook/optionmenu.htm
        self.initial_crypt = tk.StringVar(self.tab1)
        self.initial_cipher = tk.StringVar(self.tab2)

        # Password Input
        self.password_entry = ttk.Entry(self.tab1, show="*")
        self.password_entry.grid(
            row=0, column=1, columnspan=3, sticky="WE"
        )  # Seperate grid prevents password_entry from being None

        # Methods to arrange the app
        self.configure_app()
        self.add_widgets_tab1()
        self.add_widgets_tab2()

    def configure_app(self) -> None:
        """Sets up properties of the main window"""
        self.parent.title("kintercrypt")
        self.parent.geometry(f"{self.width + 100}x{self.height + 100}"
                             )  # 100x100 bigger than minimum size
        self.parent.minsize(self.width, self.height)

        # Allows the window to be resizable
        # The range denotes the number of columns and rows
        for axis in range(2):
            self.tab1.rowconfigure(axis, weight=1)
            self.tab1.columnconfigure(axis, weight=1)

            self.tab2.rowconfigure(axis, weight=1)
            self.tab2.columnconfigure(axis, weight=1)

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
        button_area.grid(row=2, column=1, sticky='new')

        # Allows buttons to be resizable
        for axis in range(2):
            button_area.rowconfigure(axis, weight=1)
            button_area.columnconfigure(axis, weight=1)

        ttk.Button(button_area, text="Start",
                   command=self.start_cipher).grid(row=0,
                                                   column=0,
                                                   pady=10,
                                                   sticky='new')

        self.initial_crypt.set("Encrypt")
        # Encrypt twice since otherwise, decypt is the only option
        option_menu = ttk.OptionMenu(button_area, self.initial_crypt,
                                     "Encrypt", "Encrypt", "Decrypt")
        option_menu.grid(
            row=0, column=1, sticky='new',
            pady=10)  # Separate grid so that the widget isn't assigned as None

        ttk.Label(self.tab1, text="Enter text:").grid(row=1, column=0)
        self.output_area.grid(row=1, column=1, sticky="WE")

    def add_widgets_tab2(self) -> None:
        """Sets up widgets for the cipher tab"""
        ttk.Label(self.tab2, text="Choose Cipher:").grid(row=0, column=0)
        self.initial_cipher.set("XOR")

        option_menu = ttk.OptionMenu(self.tab2, self.initial_cipher, "XOR",
                                     "XOR")
        option_menu.grid(
            row=0, column=1
        )  # Separate grid so that the widget isn't assigned as None

    def start_cipher(self) -> None:
        """Performs various checks before encryption begins

        After performing the checks, it retrieves the encrypted/decrypted text
        It then writes it to a new file

        """

        # Text inputted by the user
        # First parameter indicates to read from the first line
        # Second parameter removes the last character, which is an undesired newline
        user_text = self.output_area.get("1.0", 'end-1c')

        # Various errors that can occur
        if not user_text:
            showerror('kintercrypt', "No text entered!")
            return

        user_password = self.password_entry.get()

        if not user_password:
            showerror('kintercrypt', "Password not set!")
            return

        crypt_choice = (self.initial_crypt.get()
                        )  # Whether the user wants to encrypt or decrypt

        # User's choice of encryption algorithm
        cipher_choice = (self.initial_cipher.get())

        # Determines the ciphertext/plaintext
        final_result = main_cipher(user_text, user_password, cipher_choice,
                                   crypt_choice)

        # Removes the user's input
        self.output_area.delete('1.0', tk.END)

        # Inserts the encrypted/decrypted output
        self.output_area.insert(tk.INSERT, final_result)


def main() -> None:
    """Creates an instance of the App class as the main window and monitors events"""

    # Creates the main window
    window = App(tk.Tk())

    # Runs application and helps to process events
    window.mainloop()


if __name__ == "__main__":
    main()
