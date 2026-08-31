import tkinter
from typing import Callable

from sprout.constants import CENTRE, DEFAULT_BACKGROUND_COLOUR, DEFAULT_COLOUR
from sprout.font import Font
from sprout.widget import Widget


class Label(Widget):
    """
    Basic widget that displays some text.

    This class is analogous to tkinter.Label.
    """

    def __init__(self, text: str = ""):
        super().__init__()
        self._tk_label: tkinter.Label | None = None
        self._on_click_callback: Callable[[Widget], None] | None = None

        self._text = text
        self._font = Font.default()

        self._anchor_text = CENTRE
        self._background_colour = DEFAULT_BACKGROUND_COLOUR
        self._colour = DEFAULT_COLOUR
        self._justify = CENTRE
        self._n_columns = 0
        self._n_rows = 0
        self._wraplength = 0

    def _create(self, base: tkinter.Frame):
        super()._create(base)
        self._tk_label = tkinter.Label(
            self._root_frame,
            anchor=self._anchor_text,
            bg=self._background_colour,
            fg=self._colour,
            font=self._font.tkinter(),
            height=self._n_rows,
            justify=self._justify,
            text=self._text,
            width=self._n_columns,
            wraplength=self._wraplength,
        )
        self._tk_label.bind("<Button-1>", self._on_click)
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
    def text(self):
        """The text displayed by this widget."""
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text
        if self.created:
            self._tk_label.configure(text=text)

    @property
    def font_family(self):
        """The font family of this widget's text."""
        return self._font.family

    @font_family.setter
    def font_family(self, font_family: str):
        self._font.family = font_family
        if self.created:
            self._tk_label.configure(font=self._font.tkinter())

    @property
    def font_size(self):
        """The font size of this widget's text."""
        return self._font.size

    @font_size.setter
    def font_size(self, font_size: int):
        self._font.size = font_size
        if self.created:
            self._tk_label.configure(font=self._font.tkinter())

    @property
    def bold(self):
        """Whether this widget's text is bold."""
        return self._font.bold

    @bold.setter
    def bold(self, bold: bool):
        self._font.bold = bold
        if self.created:
            self._tk_label.configure(font=self._font.tkinter())

    @property
    def italic(self):
        """Whether this widget's text is slanted."""
        return self._font.italic

    @italic.setter
    def italic(self, italic: bool):
        self._font.italic = italic
        if self.created:
            self._tk_label.configure(font=self._font.tkinter())

    @property
    def underline(self):
        """Whether this widget's text is underlined."""
        return self._font.underline

    @underline.setter
    def underline(self, underline: bool):
        self._font.underline = underline
        if self.created:
            self._tk_label.configure(font=self._font.tkinter())

    @property
    def strikethrough(self):
        """Whether this widget's text is crossed out."""
        return self._font.strikethrough

    @strikethrough.setter
    def strikethrough(self, strikethrough: bool):
        self._font.strikethrough = strikethrough
        if self.created:
            self._tk_label.configure(font=self._font.tkinter())

    @property
    def anchor_text(self):
        """
        The direction to place text against, if there is space.

        Possible values are NW, N, NE, E, SE, S, SW, W, CENTRE.
        """
        return self._anchor_text

    @anchor_text.setter
    def anchor_text(self, anchor_text: str):
        self._anchor_text = anchor_text
        if self.created:
            self._tk_label.configure(anchor=anchor_text)

    @property
    def background_colour(self):
        """The background colour of this widget."""
        return self._background_colour

    @background_colour.setter
    def background_colour(self, background_colour: str):
        self._background_colour = background_colour
        if self.created:
            self._tk_label.configure(bg=background_colour)

    @property
    def colour(self):
        """The colour of this widget's text."""
        return self._colour

    @colour.setter
    def colour(self, colour: str):
        self._colour = colour
        if self.created:
            self._tk_label.configure(fg=colour)

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
            self._tk_label.configure(justify=justify)

    @property
    def n_columns(self):
        """
        The character height of this widget.

        If 0, fit the text instead of using a fixed value.
        """
        return self._n_columns

    @n_columns.setter
    def n_columns(self, n_columns: int):
        self._n_columns = n_columns
        if self.created:
            self._tk_label.configure(width=n_columns)

    @property
    def n_rows(self):
        """
        The character width of this widget.

        If 0, fit the text instead of using a fixed value.
        """
        return self._n_rows

    @n_rows.setter
    def n_rows(self, n_rows: int):
        self._n_rows = n_rows
        if self.created:
            self._tk_label.configure(height=n_rows)

    @property
    def wraplength(self):
        """
        The pixel width of this widget.

        Any text that exceeds this width is wrapped to the next line. If
        0, don't wrap text.
        """
        return self._wraplength

    @wraplength.setter
    def wraplength(self, wraplength: int):
        self._wraplength = wraplength
        if self.created:
            self._tk_label.configure(wraplength=self._wraplength)
