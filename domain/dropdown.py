import tkinter

from domain.widget import Container, Widget


class Dropdown(Widget):
    """Same as tkinter.OptionMenu."""

    def __init__(self, parent: Container, options: list[str]):
        super().__init__(parent)
        assert len(options) > 0
        self._variable = tkinter.StringVar(self.base)
        self._variable.set(options[0])
        self.options = options
        self._dropdown = tkinter.OptionMenu(self.base, self._variable, *options)
        self._dropdown.pack()

    @property
    def value(self):
        return self._variable.get()
