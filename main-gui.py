from tkinter.filedialog import askopenfilename
import tkinter.ttk as ttk
import tkinter as tk


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
        self.height = 110

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

        # Methods to arrange the app
        self.configure_app()
        self.add_widgets()

    def configure_app(self) -> None:
        # Sets up properties of the main window
        self.parent.title("kintercrypt")
        self.parent.geometry(f"{self.width}x{self.height}")
        self.parent.minsize(self.width, self.height)

        # Allows the window to be resizable
        # The range denotes the number of columns and rows
        for axis in range(4):
            self.tab1.rowconfigure(axis, weight=1)
            self.tab1.columnconfigure(axis, weight=1)

    def add_widgets(self) -> None:
        # Adds widgets so that the match the background colour
        # .pack() centres the elements and then places it in the parent widget

        # Use of self.parent rather than window from:
        # https://dev.to/abdurrahmaanj/building-an-oop-calculator-and-what-it-means-to-write-a-widget-library-4560z
        # This works since the first paramater represents the parent window

        # Password Label
        ttk.Label(
            self.tab1,
            text="Password:",
        ).grid(row=1,column=0, sticky='WE')

        # Password Input
        ttk.Entry(self.tab1, show="*").grid(row=1, column=1, columnspan=3, sticky='WE')

        # Choose between encrypt and decrypt
        # Based off http://effbot.org/tkinterbook/optionmenu.htm
        initial_value = tk.StringVar(self.tab1)
        initial_value.set("Encrypt")

        option_menu = ttk.OptionMenu(self.tab1, initial_value, "Encrypt", "Decrypt")
        option_menu.grid(row=2, column=1, sticky="WE")  # Seperate grid so that the widget isn't assigned as None

        # File input button
        # TODO: Create a subclass of tk.button to simplify process
        ttk.Button(
            self.tab1,
            text="Upload file",
            command=self.choose_file,
        ).grid(row=2, column=2, sticky="WE")

        ttk.Button(
            self.tab1,
            text="Start",
        ).grid(row=2, column=3, sticky="WE")

    def choose_file(self) -> None:
        # Creates a file dialog object
        file: str = askopenfilename()


def main() -> None:
    # Creates the main window
    window = App(tk.Tk())

    # Runs application and helps to process events
    window.mainloop()


if __name__ == "__main__":
    main()
