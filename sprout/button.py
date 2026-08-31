import tkinter

from sprout.label import Label


class Button(Label):
    """
    Alias for Label.

    By default buttons are also underlined; there are no other
    differences between Sprout buttons and Sprout labels.

    This class is NOT analogous to tkinter.Button.
    """

    def _create(self, base: tkinter.Frame):
        super()._create(base)
        self.underline = True
