import tkinter
from typing import TypeVar

from sprout.constants import DEFAULT_BACKGROUND_COLOUR, NW


class Widget:
    """Base class for all Sprout widgets."""

    def __init__(self):
        """Initialise self."""
        self._parent: Container | None = None
        self._root_frame: tkinter.Frame | None = None

        self._x = 0
        self._y = 0
        self._anchor = NW

        self._border_colour = DEFAULT_BACKGROUND_COLOUR
        self._border_width = 0

    @property
    def created(self):
        """Whether underlying Tkinter widgets have been initialised."""
        return self._root_frame is not None

    @property
    def parent(self):
        """
        The widget that contains this one.

        This property should not be modified directly. Use add() on the
        container instead.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: "Container"):
        if self._parent is not None:
            raise Exception("widget already has a parent")
        self._parent = parent

    def _create(self, base: tkinter.Frame):
        """
        Initialise underlying Tkinter widgets.

        This method is internal-facing and not intended to be called
        directly.
        """
        self._root_frame = tkinter.Frame(
            base,
            bd=self._border_width,
            bg=self._border_colour,
        )
        self.place()

    @property
    def x(self):
        """The x-coordinate of this widget."""
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x
        self.place()

    @property
    def y(self):
        """The y-coordinate of this widget."""
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y
        self.place()

    def place(
        self,
        x: int | None = None,
        y: int | None = None,
        anchor: str | None = None,
    ):
        """
        Place widget at (x, y).

        Any arguments not given are assumed to be the same as their
        current values.
        """
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        if anchor is not None:
            self._anchor = anchor

        if self.created:
            self._root_frame.place_configure(
                x=self._x,
                y=self._y,
                anchor=self._anchor,
            )

    def destroy(self):
        """Recursively destroy this widget and its children."""
        self.parent.children.remove(self)
        self._root_frame.destroy()

    @property
    def border_colour(self):
        """The border colour of this widget."""
        return self._border_colour

    @border_colour.setter
    def border_colour(self, border_colour: str):
        self._border_colour = border_colour
        if self.created:
            self._root_frame.configure(bg=border_colour)

    @property
    def border_width(self):
        """The pixel border width of this widget."""
        return self._border_width

    @border_width.setter
    def border_width(self, border_width: int):
        self._border_width = border_width
        if self.created:
            self._root_frame.configure(bd=border_width)


W = TypeVar("W", bound=Widget)


class Container:
    """Base class for Sprout widgets that contain other widgets."""

    # This is almost Composite pattern. No inheritance because Screen
    # does not want to inherit from Widget.

    def __init__(self):
        self._tk_frame: tkinter.Frame | None = None

        self.children: list[Widget] = []
        """
        The widgets contained by this one.
        
        This list should not be modified directly. Use add() instead.
        """

    def add(self, widget: W, x: int = 0, y: int = 0, anchor: str = NW):
        """
        Add widget as a child of self and place it at (x, y).

        Returns the same widget that was just added.
        """
        widget.parent = self
        widget.place(x, y, anchor)
        if self._tk_frame is not None:
            widget._create(self._tk_frame)
        self.children.append(widget)
        return widget
