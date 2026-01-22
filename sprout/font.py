import tkinter.font


class Font:
    """Same as tkinter.font.Font."""

    def __init__(
        self,
        family: str = "Sans Serif",
        size: int = 12,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self.family = family
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strikethrough = strikethrough

    @classmethod
    def default(cls):
        return Font()

    @classmethod
    def from_tkinter(cls, tkinter_font: tkinter.font.Font):
        return Font(
            family=tkinter_font.actual("family"),
            size=int(tkinter_font.actual("size")),
            bold=tkinter_font.actual("weight") != tkinter.font.NORMAL,
            italic=tkinter_font.actual("slant") != tkinter.font.ROMAN,
            underline=tkinter_font.actual("underline"),
            strikethrough=tkinter_font.actual("overstrike"),
        )

    def tkinter(self):
        return tkinter.font.Font(
            family=self.family,
            size=self.size,
            weight=tkinter.font.BOLD if self.bold else tkinter.font.NORMAL,
            slant=tkinter.font.ITALIC if self.italic else tkinter.font.ROMAN,
            underline=self.underline,
            overstrike=self.strikethrough,
        )
