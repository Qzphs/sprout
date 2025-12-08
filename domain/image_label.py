import tkinter
from typing import Callable

from domain.image import Image
from domain.widget import Container, Widget


class ImageLabel(Widget):
    """Same as tkinter.Label, but always has an image."""

    def __init__(self, parent: Container, image: Image):
        super().__init__(parent)
        self._label = tkinter.Label(self.base, image=image.base)
        self._image = image
        self._label.bind("<Button-1>", self._on_click)
        self._label.pack()
        self.command: Callable[[Widget], None] | None = None

    def _on_click(self, event: tkinter.Event):
        if self.command is None:
            return
        self.command(self)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image: Image):
        self._label.config(image=image.base)
        self._image = image
