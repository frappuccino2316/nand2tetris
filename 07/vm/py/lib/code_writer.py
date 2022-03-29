from os import path

from .constants import C_ARITHMETIC, C_PUSH, C_POP, C_GOTO, C_IF, C_LABEL, C_FUNCTION, C_RETURN, C_CALL


class CodeWriter:
    def __init__(self, file_path):
        file_name = path.basename(file_path).split(".")[0]
        self.output_path = path.dirname(
            file_path) + '/' + file_name + '.asm'
        self.current_file = open(self.output_path, 'w', encoding='utf-8')
        self.current_file_name = ''
        self.current_label = 0

    def set_file_name(self, file_name):
        self.current_file_name = file_name

    def write_sentences(self, sentences):
        for sentence in sentences:
            self.current_file.write(sentence + '\n')

    def write_arithmetic(self, command):
        if command == 'add' or command == 'sub' or command == 'and' or command == 'or':
            self.calculate_two_value(command)
        elif command == 'neg' or command == 'not':
            self.calculate_one_value(command)
        elif command == 'eq' or command == 'gt' or command == 'lt':
            self.calculate_compare(command)

    def calculate_two_value(self, command):
        if command == 'add':
            content = 'D=D+M'
        elif command == 'sub':
            content = 'D=D-M'
        elif command == 'and':
            content = 'D=D&M'
        elif command == 'or':
            content = 'D=D|M'

        self.write_pop_to_a()
        self.write_sentences(['D=M'])
        self.write_pop_to_a()
        self.write_sentences([content])
        self.write_push_from_d()

    def calculate_one_value(self, command):
        if command == 'neg':
            content = 'D=-M'
        elif command == 'not':
            content = 'D=!M'

        self.write_pop_to_a()
        self.write_sentences([content])
        self.write_push_from_d()

    def calculate_compare(self, command):
        if command == 'eq':
            mnemonic = 'JEQ'
        if command == 'gt':
            mnemonic = 'JGT'
        if command == 'lt':
            mnemonic = 'JLT'

        self.write_pop_to_a()
        self.write_sentences(['D=M'])
        self.write_pop_to_a()
        self.write_sentences([
            'D=M-D',
            f'@RETURN_{self.current_label}',
            f'D;{mnemonic}',
            'D=0',
            f'@NExT_{self.current_label}',
            '0;JMP',
            f'(RETURN_{self.current_label}',
            'D=-1',
            f'(NEXT_{self.current_label})'
        ])
        self.write_push_from_d()

        self.current_label += 1

    def write_push_pop(self, command, segment, index):
        if command == C_PUSH:
            if segment == 'constant':
                self.write_sentences([f'@{index}', 'D=A'])
                self.write_push_from_d()

    def write_push_from_d(self):
        self.write_sentences(['@SP', 'A=M', 'M=D', '@SP', 'M=M+1'])

    def write_pop_to_a(self):
        self.write_sentences(['@SP', 'M=M-1', 'A=M'])

    def close(self):
        self.current_file.close()
