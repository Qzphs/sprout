import tkinter

from sprout.constants import DEFAULT_BACKGROUND_COLOUR, OFFSCREEN
from sprout.widget import Container


class Screen(Container):
    """Container widget for the entire window."""

    @property
    def created(self):
        return self._tk_frame is not None

    def _create(self, base: tkinter.Tk, width: int, height: int):
        self._tk_frame = tkinter.Frame(
            base,
            bg=DEFAULT_BACKGROUND_COLOUR,
            width=width,
            height=height,
        )
        self._tk_frame.place_configure(x=0, y=0)
        for child in self.children:
            child._create(self._tk_frame)

    def _show(self):
        """
        Show self.

        This method is internal-facing and not intended to be called
        directly.
        """
        if not self.created:
            return
        self._tk_frame.place_configure(x=0, y=0)

    def _hide(self):
        """
        Hide self.

        This method is internal-facing and not intended to be called
        directly.
        """
        if not self.created:
            return
        self._tk_frame.place_configure(x=OFFSCREEN, y=0)
