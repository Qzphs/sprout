import tkinter

from domain.widget import Container


class ScrollableFrame(Container):
    """Use tkinter.Canvas to create a scrollable frame."""

    def __init__(
        self,
        parent: Container,
        outer_width: int,
        outer_height: int,
        inner_width: int,
        inner_height: int,
    ):
        # TODO: only vertical scroll supported
        assert outer_width == inner_width
        assert outer_height < inner_height

        super().__init__(parent)

        self.scrollbar = tkinter.Scrollbar(
            self.base,
            orient=tkinter.VERTICAL,
        )
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.canvas = tkinter.Canvas(
            self.base,
            bd=0,
            highlightthickness=0,
            width=outer_width,
            height=outer_height,
            scrollregion=(0, 0, inner_width, inner_height),
            yscrollcommand=self.scrollbar.set,
        )
        self.canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar.config(command=self.canvas.yview)

        self.frame = tkinter.Frame(
            self.canvas,
            width=inner_width,
            height=inner_height,
        )
        self.frame.pack(fill=tkinter.BOTH)
        self.canvas.create_window(
            0,
            0,
            anchor=tkinter.NW,
            width=inner_width,
            height=inner_height,
            window=self.frame,
        )
