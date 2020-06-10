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

from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
import tkinter.ttk as ttk
import tkinter as tk
from time import ctime


# Adapted class structure from https://www.begueradj.com/tkinter-best-practices/
# This configures the main window
class App(tk.Frame):

    def __init__(self, parent: tk.Tk, **kw: object) -> None:
        # Suggested in the Frame docs
        # Inherit the properties of the parent class
        super().__init__(**kw)

        # Configure additional properties
        self.parent = parent

        # Minimum Dimensions are in pixels
        self.width = 400
        self.height = 200

        # File to be encrypted
        self.file = ""

        # Create the tabs
        self.note = ttk.Notebook(self.parent)
        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)
        self.tab3 = ttk.Frame(self.note)

        # Assign tab titles
        self.note.add(self.tab1, text="General")
        self.note.add(self.tab2, text="Settings")
        self.note.add(self.tab3, text="About")

        self.note.pack(fill=tk.BOTH, expand=True)

        # Outputs diagnostic results of encryption
        # It's not in an "add widgets" method since it needs to be accessed by other methods
        self.output_area = scrolledtext.ScrolledText(self.tab1,
                                                     wrap=tk.WORD)

        # Methods to arrange the app
        self.configure_app()
        self.add_widgets_tab1()

        # Beginning output messages
        self.output_area.insert(tk.INSERT, f"KINTERCRYPT LOG:\n")
        self.log_output('kintercrypt started')

    def log_output(self, text: str) -> None:
        # Formats the output to show the time
        self.output_area.insert(tk.INSERT, f"{ctime()} - {text}\n")

    def configure_app(self) -> None:
        # Sets up properties of the main window
        self.parent.title("kintercrypt")
        self.parent.geometry(f"{self.width + 100}x{self.height + 100}")  # 100x100 bigger than minimum size
        self.parent.minsize(self.width, self.height)

        # Allows the window to be resizable
        # The range denotes the number of columns and rows
        for axis in range(4):
            self.tab1.rowconfigure(axis, weight=1)
            self.tab1.columnconfigure(axis, weight=1)

        self.tab1.grid_columnconfigure(0, minsize=110)  # Prevents buttons from being squashed
        self.tab1.grid_rowconfigure(0, minsize=40)  # Prevents password area from being squashed

    def add_widgets_tab1(self) -> None:

        # Password Label
        ttk.Label(
            self.tab1,
            text="Password:",
        ).grid(row=0, column=0)

        # Password Input
        ttk.Entry(self.tab1, show="*").grid(row=0, column=1, columnspan=3, sticky='WE')

        # Allows the buttons to be in the same grid cell
        button_area = ttk.Frame(self.tab1)
        button_area.grid(row=1, column=0)

        # Choose between encrypt and decrypt
        # Based off http://effbot.org/tkinterbook/optionmenu.htm
        initial_value = tk.StringVar(self.tab1)
        initial_value.set("Encrypt")

        option_menu = ttk.OptionMenu(button_area, initial_value, "Encrypt", "Decrypt")
        option_menu.grid(row=0, column=0)  # Seperate grid so that the widget isn't assigned as None

        # TODO: Create a subclass of tk.button to simplify process
        ttk.Button(
            button_area,
            text="Choose file",
            command=self.choose_file,
        ).grid(row=1, column=0, sticky="WE", pady=10)  # Padding for the middle button spaces all buttons

        ttk.Button(
            button_area,
            text="Start",
        ).grid(row=2, column=0, sticky="WE")

        self.output_area.grid(row=1, column=1, columnspan=3, sticky='WE')

    def choose_file(self) -> None:
        # Creates a file dialog object
        self.file = askopenfilename()

        if not self.file:  # If file selector is opened, but no file is chosen
            self.log_output("No file chosen")
        else:
            self.log_output(str(self.file) + " chosen")


def main() -> None:
    # Creates the main window
    window = App(tk.Tk())

    # Runs application and helps to process events
    window.mainloop()


if __name__ == "__main__":
    main()
