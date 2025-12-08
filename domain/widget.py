import tkinter

from domain.constants import NW


class Widget:
    """Base class for Sprout widgets."""

    def __init__(self, parent: "Container"):
        self.parent = parent
        self.base = tkinter.Frame(parent.frame)
        """
        The underlying tkinter widget.
        
        This can be accessed directly to hack in any changes not
        supported by Sprout.
        """

    def place(self, x: int, y: int, anchor: str = NW):
        self.base.place(x=x, y=y, anchor=anchor)

    def destroy(self):
        self.base.destroy()


class Container(Widget):
    """Base class for Sprout widgets that contain other widgets."""

    def __init__(self, parent: "Container"):
        super().__init__(parent)
        self.frame = self.base
        """The tkinter frame other widgets connect to."""
