import tkinter

from domain.widget import Container, Widget


class Dropdown(Widget):
    """Same as tkinter.OptionMenu."""

    def __init__(self, parent: Container, options: list[str]):
        super().__init__(parent)
        assert len(options) > 0
        self.variable = tkinter.StringVar(self.base)
        self.variable.set(options[0])
        self.options = options
        self.dropdown = tkinter.OptionMenu(self.base, self.variable, *options)
        self.dropdown.pack()

    @property
    def value(self):
        return self.variable.get()
