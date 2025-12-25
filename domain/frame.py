import tkinter
from typing import Callable

from domain.widget import Container, Widget


class Frame(Container):
    """Same as tkinter.Frame."""

    def __init__(self, parent: Container, width: int, height: int):
        super().__init__(parent)
        self.base.config(width=width, height=height)
        self.base.bind("<Button-1>", self._on_click)
        self.command: Callable[[Widget], None] | None = None

    def _on_click(self, event: tkinter.Event):
        if self.command is None:
            return
        self.command(self)

    @property
    def border_colour(self):
        return self.base.cget("bg")

    @border_colour.setter
    def border_colour(self, border_colour: str | None):
        if border_colour is None:
            self.base.config(bg=self.parent.base.cget("bg"))
        else:
            self.base.config(bg=border_colour)

    @property
    def border_width(self):
        return self.base.cget("bd")

    @border_width.setter
    def border_width(self, border_width: int):
        self.base.config(bd=border_width)
