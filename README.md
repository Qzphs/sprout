Mini GUI module built on top of tkinter. It's not particularly complete (and
doesn't try to be) but it covers my most common use cases.

To use this code, run main.py. This should create a new file called sprout.py.
I just drag that into whatever project I'm using it in and import it from
there.

Sample code:

```python
import sprout


application = sprout.Application("sample", 600, 600)

frame = sprout.ScrollableFrame(application.screen, 500, 300, 500, 500)
frame.place(50, 50)
button = sprout.TextLabel(frame, "hello world!")
button.place(300, 300)
button.font = sprout.Font(family="Sans Serif", size=20, bold=True)
dropdown = sprout.Dropdown(frame, ["abc", "def", "ghi"])
dropdown.place(100, 200)
entry = sprout.Entry(frame)
entry.place(200, 100)


def show_results():
    print(f"{dropdown.value=}")
    print(f"{entry.value=}")


button.command = show_results

application.start()

```

The name Sprout doesn't mean anything. I just got the name from [@milieu-x](https://github.com/milieu-x)
and thought it sounded cool.
