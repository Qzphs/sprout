import tkinter

from sprout.constants import LEFT, NW, OFFSCREEN
from sprout.widget import Container, Widget


class Application:
    """Main class for GUIs using Sprout."""

    def __init__(self, title: str, width: int, height: int):
        self.tk = tkinter.Tk()
        self.tk.title(title)
        self.tk.geometry(f"{width}x{height}+{0}+{0}")
        self.tk.createcommand("tk::mac::Quit", self._on_quit)
        self.tk.protocol("WM_DELETE_WINDOW", self._on_quit)
        self.width = width
        self.height = height
        self._screen = Screen(self)
        self._screen.base.place(x=0, y=0)

    @property
    def screen(self):
        """The screen currently being displayed."""
        return self._screen

    @screen.setter
    def screen(self, screen: "Screen"):
        self._screen.base.place(x=OFFSCREEN, y=0)
        self._screen = screen
        self._screen.base.place(x=0, y=0)

    def start(self):
        self.tk.mainloop()

    def _on_quit(self):
        if self.on_quit is not None:
            self.on_quit()
        self.tk.quit()

    def on_quit(self):
        pass


class Screen(Container):

    def __init__(self, parent: Application):
        self.parent = parent
        self.base = tkinter.Frame(
            parent.tk,
            width=parent.width,
            height=parent.height,
        )
        self.frame = self.base
        self.children: list[Widget] = []

    def pack(self, side=LEFT):
        raise NotImplementedError("cannot pack screen")

    def place(self, x, y, anchor=NW):
        raise NotImplementedError("cannot place screen")

    @property
    def background_colour(self):
        return self.base.cget("bg")

    @background_colour.setter
    def background_colour(self, background_colour: str | None):
        if background_colour is None:
            self.base.config(bg=self.parent.tk.cget("bg"))
        else:
            self.base.config(bg=background_colour)
