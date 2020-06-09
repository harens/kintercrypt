from kintercrypt import main_gui
import tkinter as tk


# TODO: Improve gui testing
# Since its quite difficult to test tkinter, the tests are currently very basic
def test():
    main_gui.App(tk.Tk())
