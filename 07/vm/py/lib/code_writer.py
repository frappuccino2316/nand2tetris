from os import path

from .constants import C_ARITHMETIC, C_PUSH, C_POP, C_GOTO, C_IF, C_LABEL, C_FUNCTION, C_RETURN, C_CALL


class CodeWriter:
    def __init__(self, file_path):
        file_name = path.basename(file_path).split(".")[0]
        self.output_path = path.dirname(
            file_path) + '/' + file_name + '.asm'
        self.current_file = open(self.output_path, 'w', encoding='utf-8')
        self.current_file_name = ''

    def set_file_name(self, file_name):
        self.current_file_name = file_name

    def write_arithmetic(self, command):
        if command == "add":
            content = 'D=D+M\n'

        self.write_pop_to_a()
        self.current_file.write('D=M\n')
        self.write_pop_to_a()
        self.current_file.write(content)
        self.write_push_from_d()

    def write_push_pop(self, command, segment, index):
        if command == C_PUSH:
            if segment == 'constant':
                self.current_file.write(f'@{index}\n')
                self.current_file.write('M=A\n')
                self.write_push_from_d()

    def write_push_from_d(self):
        self.current_file.write('@SP\nM=A\nM=D\n@SP\nM=M+1\n')

    def write_pop_to_a(self):
        self.current_file.write('@SP\nM=M-1\nA=M\n')

    def close(self):
        self.current_file.close()
