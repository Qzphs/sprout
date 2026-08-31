import tkinter
from typing import Callable

from sprout.widget import Widget


class Image(Widget):
    """
    Basic widget that displays an image.

    This class is analogous to tkinter.Label.
    """

    def __init__(self):
        super().__init__()
        self._tk_label: tkinter.Label | None = None
        self._on_click_callback: Callable[[Widget], None] | None = None

        self._asset: Asset | None = None

    def _create(self, base: tkinter.Frame):
        super()._create(base)
        self._tk_label = tkinter.Label(self._root_frame)
        self._tk_label.bind("<Button-1>", self._on_click)
        if self.asset is not None:
            self._tk_label.configure(image=self._asset.tkinter())
        self._tk_label.pack_configure()

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

    @property
    def asset(self):
        """The image displayed by this widget."""
        return self._asset

    @asset.setter
    def asset(self, asset: "str | Asset"):
        if isinstance(asset, str):
            asset = Asset(asset)
        self._asset = asset
        if self.created:
            self._tk_label.configure(image=asset.tkinter())


class Asset:
    """Substitute tkinter.PhotoImage."""

    def __init__(self, filename: str):
        """Initialise self with filename."""
        self.filename = filename
        self.operations: list[tuple[str, int, int]] = []

    def subsample(self, x: int, y: int | None = None):
        """
        Create copy of self with decreased dimensions.

        `x` is the horizontal scale factor. `y` is the vertical scale
        factor. If `y` is missing, it is assumed to be the same as `x`.

        This method is analogous to tkinter.PhotoImage's subsample().
        """
        if y is None:
            y = x
        copy = Asset(self.filename)
        copy.operations.extend(self.operations)
        copy.operations.append(("subsample", x, y))
        return copy

    def zoom(self, x: int, y: int | None = None):
        """
        Create copy of self with increased dimensions.

        `x` is the horizontal scale factor. `y` is the vertical scale
        factor. If `y` is missing, it is assumed to be the same as `x`.

        This method is analogous to tkinter.PhotoImage's zoom().
        """
        if y is None:
            y = x
        copy = Asset(self.filename)
        copy.operations.extend(self.operations)
        copy.operations.append(("zoom", x, y))
        return copy

    def tkinter(self):
        """Convert self to tkinter.PhotoImage."""
        asset = tkinter.PhotoImage(file=self.filename)
        for operation in self.operations:
            if operation[0] == "subsample":
                asset = asset.subsample(operation[1], operation[2])
            elif operation[0] == "zoom":
                asset = asset.zoom(operation[1], operation[2])
        # Prevent tkinter.PhotoImage from being garbage collected?
        self._output = asset
        return asset
