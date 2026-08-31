import tkinter
from typing import Callable

from sprout.constants import DEFAULT_BACKGROUND_COLOUR, DEFAULT_COLOUR, LEFT
from sprout.widget import Widget


class Entry(Widget):
    """
    Basic widget that displays some text.

    This class is analogous to tkinter.Entry.
    """

    def __init__(self):
        super().__init__()
        self._value = ""

        self._tk_entry: tkinter.Entry | None = None
        self._tk_variable: tkinter.StringVar | None = None
        self._on_write_callback: Callable[[Widget], None] | None = None

        self._justify = LEFT
        self._width = 20

    def _create(self, base: tkinter.Frame):
        super()._create(base)
        self._tk_variable = tkinter.StringVar()
        self._tk_variable.trace_add("write", self._on_write)
        self._tk_entry = tkinter.Entry(
            self._root_frame,
            bg=DEFAULT_BACKGROUND_COLOUR,
            fg=DEFAULT_COLOUR,
            highlightthickness=0,
            justify=self._justify,
            textvariable=self._tk_variable,
            width=self._width,
        )
        self._tk_entry.pack_configure()

    def on_write(self, func: Callable[[Widget], None]):
        """
        Register a function to be called when text is entered.

        The function should accept as an argument the widget that was
        interacted with.
        """
        self._on_write_callback = func
        return func

    def _on_write(self, var: str, index: str, mode: str):
        self._value = self._tk_variable.get()
        if self._on_write_callback is not None:
            self._on_write_callback(self)

    @property
    def value(self):
        """The value written in this entry."""
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value
        if self.created:
            self._tk_variable.set(value)

    @property
    def justify(self):
        """
        The alignment of lines relative to each other within the text.

        Possible values are LEFT, CENTRE, RIGHT.
        """
        return self._justify

    @justify.setter
    def justify(self, justify: str):
        self._justify = justify
        if self.created:
            self._tk_entry.configure(justify=justify)

    @property
    def width(self):
        """The character width of this widget."""
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width
        if self.created:
            self._tk_entry.configure(width=width)
