import tkinter
from typing import Callable

from domain.font import Font
from domain.widget import Container, Widget


class TextLabel(Widget):
    """Same as tkinter.Label, but always has text."""

    def __init__(self, parent: Container, text: str):
        super().__init__(parent)
        self._label = tkinter.Label(self.base, text=text)
        self._label.bind("<Button-1>", self._on_click)
        self._label.pack()
        self.command: Callable[[Widget], None] | None = None

    def _on_click(self, event: tkinter.Event):
        if self.command is None:
            return
        self.command(self)

    @property
    def text(self) -> str:
        return self._label.cget("text")

    @text.setter
    def text(self, text: str):
        self._label.config(text=text)

    @property
    def font(self):
        # TODO: return a sprout.Font instead of str
        return self._label.cget("font")

    @font.setter
    def font(self, font: Font):
        self._label.config(font=font.tkinter())

    @property
    def colour(self):
        return self._label.cget("fg")

    @colour.setter
    def colour(self, colour: str):
        self._label.config(fg=colour)
