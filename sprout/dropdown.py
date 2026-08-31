import tkinter
from typing import Callable

from sprout.widget import Widget


class Dropdown(Widget):
    """
    Basic widget that allows user to select an option from a list.

    This class is analogous to tkinter.OptionMenu.
    """

    def __init__(self, options: list[str]):
        super().__init__()
        if len(options) == 0:
            raise ValueError("options cannot be empty")
        self.options = options
        self._value = options[0]

        self._tk_dropdown: tkinter.OptionMenu | None = None
        self._tk_variable: tkinter.StringVar | None = None
        self._on_write_callback: Callable[[Widget], None] | None = None

    def _create(self, base: tkinter.Frame):
        super()._create(base)
        self._tk_variable = tkinter.StringVar()
        self._tk_variable.set(self.options[0])
        self._tk_variable.trace_add("write", self._on_write)
        self._tk_dropdown = tkinter.OptionMenu(
            self._root_frame,
            self._tk_variable,
            *self.options,
        )
        self._tk_dropdown.pack_configure()

    def on_write(self, func: Callable[[Widget], None]):
        """
        Register a function to be called when a selection is made.

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
        """The selected option."""
        return self._value
