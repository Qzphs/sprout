Mini GUI package built on top of tkinter. It's not particularly complete (and
doesn't try to be) but it covers my most common use cases.

Sample code:

```python
import sprout as s


class Application(s.Application):

    def __init__(self):
        super().__init__("sprout sample", 320, 200)

        self.text_label = s.TextLabel(
            self.screen,
            "this is a text label",
        )
        self.text_label.place(x=20, y=20)

        self.image_label = s.ImageLabel(
            self.screen,
            s.Image.from_file("icon.png"),
        )
        self.image_label.border_width = 5
        self.image_label.on_click = self.toggle_border
        self.image_label.place(x=25, y=180, anchor=s.SW)

    def toggle_border(self, source: s.ImageLabel):
        if self.image_label.border_colour is None:
            self.image_label.border_colour = "#efaf00"
        else:
            self.image_label.border_colour = None


Application().start()
```

The name Sprout doesn't mean anything. I just got the name from [@milieu-x](https://github.com/milieu-x)
and thought it sounded cool.
