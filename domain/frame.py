from domain.widget import Container


class Frame(Container):
    """Same as tkinter.Frame."""

    def __init__(self, parent: Container, width: int, height: int):
        super().__init__(parent)
        self.base.config(width=width, height=height)
