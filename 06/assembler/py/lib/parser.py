from .constants import A_COMMAND, C_COMMAND, L_COMMAND


class Parser:
    def __init__(self, input_path):
        self.lines = []

        with open(input_path, "r", encoding="utf-8") as f:
            raw_contents = f.read()
            splitted_lines = raw_contents.replace(" ", "").splitlines()
            for line in splitted_lines:
                if line[0:2] == "//" or line.isspace() or line == "":
                    continue
                if "//" in line:
                    index = line.find("//")
                    line = line[:index]
                self.lines.append(line)

        self.line_counter = 0
        self.current_command = self.lines[0]

    def has_more_command(self):
        return len(self.lines) - 1 > self.line_counter

    def advance(self):
        if self.has_more_command() == False:
            pass
        self.line_counter += 1
        new_command = self.lines[self.line_counter]
        self.current_command = new_command

    def command_type(self):
        if self.current_command.find("@") == 0:
            return A_COMMAND
        elif self.current_command.find("(") == 0:
            return L_COMMAND
        else:
            return C_COMMAND

    def symbol(self):
        if self.command_type() == A_COMMAND:
            return self.current_command.split("@")[1]
        else:
            return self.current_command[0:-1]

    def dest(self):
        return self.current_command.split("=")[0]

    def comp(self):
        if ";" not in self.current_command:
            return self.current_command.split("=")[1]
        else:
            return "null"

    def jump(self):
        index = self.current_command.find(";")
        if index != -1:
            return self.current_command[index:]
        else:
            return "null"
