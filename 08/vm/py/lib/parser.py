from .constants import C_ARITHMETIC, C_PUSH, C_POP, C_GOTO, C_IF, C_LABEL, C_FUNCTION, C_RETURN, C_CALL


class Parser:
    def __init__(self, input_path):
        self.lines = []

        with open(input_path, "r", encoding="utf-8") as f:
            raw_contents = f.read()
            splitted_lines = raw_contents.splitlines()
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
        return len(self.lines) > self.line_counter

    def advance(self):
        if self.has_more_command() == False:
            pass
        self.line_counter += 1
        if self.has_more_command():
            new_command = self.lines[self.line_counter]
            self.current_command = new_command

    def command_type(self):
        if "push" in self.current_command:
            return C_PUSH
        elif "pop" in self.current_command:
            return C_POP
        elif "label" in self.current_command:
            return C_LABEL
        elif "goto" in self.current_command:
            return C_GOTO
        elif "if" in self.current_command:
            return C_IF
        elif "function" in self.current_command:
            return C_FUNCTION
        elif "return" in self.current_command:
            return C_RETURN
        elif "goto" in self.current_command:
            return C_GOTO
        elif "call" in self.current_command:
            return C_CALL
        else:
            return C_ARITHMETIC

    def arg1(self):
        if self.command_type() == C_ARITHMETIC:
            return self.current_command.strip()
        else:
            return self.current_command.strip().split(" ")[1]

    def arg2(self):
        return self.current_command.strip().split(" ")[2]
