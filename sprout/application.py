import tkinter
from typing import Callable, TypeVar

from sprout.constants import NW
from sprout.screen import Screen
from sprout.widget import Widget


class _SproutApplication:

    def __init__(self):
        """Initialise self."""
        self._base_tk: tkinter.Tk | None = None

        self._title = ""
        self._width = 1200
        self._height = 720
        self._screen = Screen()
        self._on_exit_callbacks: list[Callable[[], None]] = []

    @property
    def started(self):
        """Whether underlying Tkinter widgets have been initialised."""
        return self._base_tk is not None

    @property
    def title(self):
        """The text that is displayed at the top of the window."""
        if not self.started:
            return self._title
        else:
            return self._base_tk.wm_title()

    @title.setter
    def title(self, title: str):
        if not self.started:
            self._title = title
        else:
            self._base_tk.wm_title(title)

    @property
    def width(self):
        """
        The pixel width of the window.

        This cannot be modified after the application starts; Exception
        is raised if such an attempt is made.
        """
        return self._width

    @width.setter
    def width(self, width: int):
        if self.started:
            raise Exception("cannot modify width after application start")
        self._width = width

    @property
    def height(self):
        """
        The pixel height of the window.

        This cannot be modified after the application starts; Exception
        is raised if such an attempt is made.
        """
        return self._height

    @height.setter
    def height(self, height: int):
        if self.started:
            raise Exception("cannot modify height after application start")
        self._height = height

    @property
    def screen(self):
        """
        The screen currently being displayed.

        This property can be set by user code to display a different
        screen.
        """
        return self._screen

    @screen.setter
    def screen(self, screen: "Screen"):
        self._screen._hide()
        self._screen = screen
        screen._show()
        if self.started and not screen.created:
            screen._create(self._base_tk, self.width, self.height)

    def start(self):
        """Initialise and run the underlying tkinter.Tk instance."""
        self._base_tk = tkinter.Tk()
        self._base_tk.wm_title(self._title)
        self._base_tk.wm_geometry(f"{self._width}x{self._height}+{0}+{0}")

        # Command+Q on macOS
        self._base_tk.createcommand("tk::mac::Quit", self._on_exit)
        # Closing window by clicking X
        self._base_tk.wm_protocol("WM_DELETE_WINDOW", self._on_exit)

        # Initialise underlying Tkinter widgets for starting screen
        if not self.screen.created:
            self.screen._create(self._base_tk, self.width, self.height)

        self._base_tk.mainloop()

    @property
    def clipboard(self):
        if not self.started:
            return ""
        return self._base_tk.clipboard_get()

    @clipboard.setter
    def clipboard(self, text: str):
        if not self.started:
            return
        self._base_tk.clipboard_clear()
        self._base_tk.clipboard_append(text)

    def navigation(self, screen: "Screen"):
        """
        Create a function that displays the given screen when called.

        This method is a convenience method intended to be used for
        navigation.
        """

        def callback(source: Widget):
            self.screen = screen

        return callback

    def on_exit(self, func: Callable[[], None]):
        """
        Register a function to be called when the application is closed.

        Multiple functions can be registered.
        """
        self._on_exit_callbacks.append(func)
        return func

    def _on_exit(self):
        for callback in self._on_exit_callbacks:
            try:
                callback()
            except Exception as error:
                print(f"{error.__class__.__name__}: {error}")
        self._base_tk.destroy()


application = _SproutApplication()
"""
Singleton that contains screens and other sprout widgets.

This object is analogous to tkinter.Tk.
"""


W = TypeVar("W", bound=Widget)


def add(widget: W, x: int = 0, y: int = 0, anchor: str = NW):
    """
    Add widget and place it at (x, y).

    Returns the same widget that was just added.

    This is a convenience function for simple Sprout applications.
    """
    return application.screen.add(widget, x, y, anchor)


def start():
    """
    Initialise and run the underlying tkinter.Tk instance.

    This is a convenience function for simple Sprout applications.
    """
    application.start()


def on_exit(func: Callable[[], None]):
    """
    Register a function to be called when the application is closed.

    Multiple functions can be registered.

    This is a convenience function for simple Sprout applications.
    """
    return application.on_exit(func)
