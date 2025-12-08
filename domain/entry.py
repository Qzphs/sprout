import tkinter

from domain.widget import Widget


class Entry(Widget):
    """Same as tkinter.Entry."""

    def __init__(self, parent):
        super().__init__(parent)
        self._variable = tkinter.StringVar(self.base)
        self._entry = tkinter.Entry(self.base, textvariable=self._variable)
        self._entry.pack()

    @property
    def value(self):
        return self._entry.get()
