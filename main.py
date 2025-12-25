"""Combine all modules into a single Python file."""


class File:

    def __init__(self):
        self.code_lines: list[str] = []
        self.import_lines: set[str] = set()

    def add(self, filename: str):
        with open(filename) as file:
            lines = file.read().splitlines()
        for line in lines:
            if "domain" in line:
                continue
            if "import" in line:
                self.import_lines.add(line)
                continue
            self.code_lines.append(line)

    def save(self, filename: str):
        with open(filename, "w") as file:
            file.write("# Sprout v0.2.1 https://github.com/Qzphs/sprout\n\n\n")
            file.write("\n".join(self.import_lines) + "\n")
            file.write("\n".join(self.code_lines) + "\n")


file = File()

file.add("domain/constants.py")
file.add("domain/font.py")
file.add("domain/image.py")
file.add("domain/widget.py")

file.add("domain/application.py")
file.add("domain/dropdown.py")
file.add("domain/entry.py")
file.add("domain/frame.py")
file.add("domain/image_label.py")
file.add("domain/scrollable_frame.py")
file.add("domain/text_label.py")

file.save("sprout.py")
