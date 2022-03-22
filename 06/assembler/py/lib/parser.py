A_COMMAND = "A_COMMAND"
C_COMMAND = "C_COMMAND"
L_COMMAND = "L_COMMAND"


class Parser:
    def __init__(self, input_path):
        self.lines = []
        self.line_counter = 0

        with open(input_path) as f:
            raw_contents = f.read()
            splitted_lines = raw_contents.replace(" ", "").splitlines()

            for line in splitted_lines:
                if line[0:2] == "//" or line.isspace() or line == "":
                    continue
                if "//" in line:
                    index = line.find("//")
                    line = line[:index]
                self.lines.append(line)
