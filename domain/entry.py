import tkinter

from domain.widget import Widget


class Entry(Widget):
    """Same as tkinter.Entry."""

    def __init__(self, parent):
        super().__init__(parent)
        self.variable = tkinter.StringVar(self.base)
        self.entry = tkinter.Entry(self.base, textvariable=self.variable)
        self.entry.pack()

    @property
    def value(self):
        return self.entry.get()
