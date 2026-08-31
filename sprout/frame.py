import tkinter
from typing import Callable

from sprout.constants import DEFAULT_BACKGROUND_COLOUR
from sprout.image import Image
from sprout.label import Label
from sprout.widget import Container, Widget


class Frame(Widget, Container):
    """
    Basic container widget.

    This class is analogous to tkinter.Frame.
    """

    def __init__(self):
        Widget.__init__(self)
        Container.__init__(self)
        self._on_click_callback: Callable[[Widget], None] | None = None

        self._width = 100
        self._height = 100
        self._background_colour = DEFAULT_BACKGROUND_COLOUR

    def _create(self, base: tkinter.Frame):
        super()._create(base)
        self._root_frame.configure(
            width=self._width,
            height=self._height,
        )
        self._tk_frame = tkinter.Frame(
            self._root_frame,
            bg=self._background_colour,
            width=self._width - self._border_width * 2,
            height=self._height - self._border_width * 2,
        )
        self._tk_frame.bind("<Button-1>", self._on_click)
        self._tk_frame.place_configure(x=0, y=0)
        for child in self.children:
            child._create(self._tk_frame)

    def on_click(self, func: Callable[[Widget], None]):
        """
        Register a function to be called when this widget is clicked.

        The function should accept as an argument the widget that was
        clicked.
        """
        self._on_click_callback = func
        return func

    def _on_click(self, event: tkinter.Event):
        if self._on_click_callback is not None:
            self._on_click_callback(self)

    def on_click_anywhere(self, func: Callable[[Widget], None]):
        """
        Register a function to be called when this widget is clicked.

        The function should accept as an argument the widget that was
        clicked.

        This is different from `on_click` in that the function is
        recursively registered to clickable children as well.
        """
        self._on_click_callback = func
        for child in self.children:
            if isinstance(child, Frame):
                child.on_click_anywhere(func)
            elif isinstance(child, (Label, Image)):
                child.on_click(func)

    @property
    def width(self):
        """The pixel width of this widget."""
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width
        if self.created:
            self._root_frame.configure(width=width)
            self._tk_frame.configure(width=width - self.border_width * 2)

    @property
    def height(self):
        """The pixel height of this widget."""
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height
        if self.created:
            self._root_frame.configure(height=height)
            self._tk_frame.configure(height=height - self.border_width * 2)

    @property
    def background_colour(self):
        """The background colour of this widget."""
        return self._background_colour

    @background_colour.setter
    def background_colour(self, background_colour: str):
        self._background_colour = background_colour
        if self.created:
            self._tk_frame.configure(bg=background_colour)
