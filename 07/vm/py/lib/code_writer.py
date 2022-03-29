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

    def write_sentences(self, sentences):
        for sentence in sentences:
            self.current_file.write(sentence + '\n')

    def write_arithmetic(self, command):
        if command == "add":
            content = 'D=D+M'

        self.write_pop_to_a()
        self.write_sentences(['D=D+M'])
        self.write_pop_to_a()
        self.write_sentences([content])
        self.write_push_from_d()

    def write_push_pop(self, command, segment, index):
        if command == C_PUSH:
            if segment == 'constant':
                self.write_sentences([f'@{index}', 'M=A'])
                self.write_push_from_d()

    def write_push_from_d(self):
        self.write_sentences(['@SP', 'M=A', 'M=D', '@SP', 'M=M+1'])

    def write_pop_to_a(self):
        self.write_sentences(['@SP', 'M=M-1', 'A=M'])

    def close(self):
        self.current_file.close()
