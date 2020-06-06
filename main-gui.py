from tkinter import Tk
from tkinter.filedialog import askopenfilename
import tkinter as tk


# Adapted class structure from https://www.begueradj.com/tkinter-best-practices/
# This configures the main window
class App(tk.Frame):
    parent: Tk
    backgroundColour: str

    def __init__(self, parent: tk.Tk, **kw: object) -> None:
        # Suggested in the Frame docs
        # Inherit the properties of the parent class
        super().__init__(**kw)

        # Configure additional properties
        self.parent = parent

        # Dimensions are in pixels
        self.width = 350
        self.height = 300

        # Used to set the background colour of the main window and widgets
        # Currently a dark grey
        self.backgroundColour = "#3E4149"

        # Methods to arrange the app
        self.configure_app()
        self.add_widgets()

    def configure_app(self) -> None:
        # Sets up properties of the main window
        self.parent.title("")  # No window title
        self.parent.geometry(f"{self.width}x{self.height}")
        self.parent.resizable(0, 0)  # Not resizable
        self.parent.configure(bg=self.backgroundColour)

    def add_widgets(self) -> None:
        # Adds widgets so that the match the background colour
        # .pack() centres the elements and then places it in the parent widget

        # Use of self.parent rather than window from:
        # https://dev.to/abdurrahmaanj/building-an-oop-calculator-and-what-it-means-to-write-a-widget-library-4560z
        # This works since the first paramater represents the parent window

        # Main title
        tk.Label(
            self.parent,
            text="kintercrypt",
            background=self.backgroundColour,
            foreground="white",
        ).grid(row=0, sticky='NW')

        # Password Label
        tk.Label(
            self.parent,
            text="Password:",
            background=self.backgroundColour,
            foreground="white",
        ).grid(row=1,column=0, sticky='W')

        # Password Input
        tk.Entry(self.parent, show="*").grid(row=1, column=1, columnspan=3, sticky='WE')

        # Choose between encrypt and decrypt
        # Based off http://effbot.org/tkinterbook/optionmenu.htm
        initial_value = tk.StringVar(self.parent)
        initial_value.set("Encrypt")

        option_menu = tk.OptionMenu(self.parent, initial_value, "Encrypt", "Decrypt")
        option_menu.grid(row=2, column=1)  # Seperate grid so that the widget isn't assigned as None
        option_menu.config(bg=self.backgroundColour)

        # File input button
        # TODO: Create a subclass of tk.button to simplify process
        tk.Button(
            self.parent,
            text="Upload file",
            highlightbackground=self.backgroundColour,
            command=self.choose_file,
        ).grid(row=2, column=2)

        tk.Button(
            self.parent,
            text="Start",
            highlightbackground=self.backgroundColour,
        ).grid(row=2, column=3)


    def choose_file(self) -> None:
        # Creates a file dialog object
        file: str = askopenfilename()


def main():
    # Creates the main window
    window = App(tk.Tk())

    # Runs application and helps to process events
    window.mainloop()


if __name__ == "__main__":
    main()
