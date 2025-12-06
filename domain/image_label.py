import tkinter
from typing import Callable

from domain.widget import Container, Widget


class ImageLabel(Widget):
    """Same as tkinter.Label, but always has an image."""

    def __init__(self, parent: Container, image: tkinter.PhotoImage):
        super().__init__(parent)
        self.label = tkinter.Label(self.base, image=image)
        self._image = image
        self.label.bind("<Button-1>", self._on_click)
        self.label.pack()
        self.command: Callable | None = None

    def _on_click(self, event: tkinter.Event):
        if self.command is None:
            return
        self.command(*self.parameters())

    def parameters(self) -> list:
        """
        Return a list of parameters this widget should use.

        When the widget is clicked, this method is called to get a list of
        parameters, which are then passed into self.command().

        Subclasses should override this.
        """
        return []

    @property
    def image(self) -> tkinter.PhotoImage:
        return self._image

    @image.setter
    def image(self, image: tkinter.PhotoImage):
        self.label.config(image=image)
        self._image = image
