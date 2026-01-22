import tkinter
import tkinter.font
from typing import Callable

from sprout.font import Font
from sprout.widget import Container, Widget


class Dropdown(Widget):
    """Same as tkinter.OptionMenu."""

    def __init__(self, parent: Container, options: list[str]):
        super().__init__(parent)
        assert len(options) > 0
        self._variable = tkinter.StringVar(self.base)
        self._variable.set(options[0])
        self._variable.trace_add("write", self._on_write)
        self.options = options
        self._dropdown = tkinter.OptionMenu(self.base, self._variable, *options)
        self._dropdown.pack()
        self.on_write: Callable[[Widget], None] | None = None
        self.font = Font.default()

    def _on_write(self, *args):
        if self.on_write is None:
            return
        self.on_write(self)

    @property
    def value(self):
        return self._variable.get()

    @property
    def font(self):
        tkinter_font = tkinter.font.nametofont(self._dropdown.cget("font"))
        return Font.from_tkinter(tkinter_font)

    @font.setter
    def font(self, font: Font):
        self._dropdown.config(font=font.tkinter())
