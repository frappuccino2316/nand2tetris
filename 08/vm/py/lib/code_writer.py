from os import path

from .constants import C_PUSH, C_POP


class CodeWriter:
    def __init__(self, file_path):
        self.output_path = file_path + file_path.split('/')[-1] + '.asm'
        self.current_file = open(self.output_path, 'w', encoding='utf-8')
        self.current_file_name = ''
        self.current_label = 0
        self.label_for_return_address = 0

    def write_init(self):
        self.write_sentences([
            '@256',
            'D=A',
            '@SP',
            'M=D'
        ])
        self.write_call('Sys.init', '0')

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
            content = 'D=M-D'
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
            f'@NEXT_{self.current_label}',
            '0;JMP',
            f'(RETURN_{self.current_label})',
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
            elif segment in ['local', 'argument', 'this', 'that']:
                self.write_push_from_referenced_segment(segment, index)
            elif segment in ['pointer', 'temp']:
                self.write_push_from_fixed_segment(segment, index)
            elif segment == 'static':
                self.write_sentences([
                    f'@{self.current_file_name}.{index}',
                    'D=M'
                ])
                self.write_push_from_d()
        elif command == C_POP:
            if segment in ['local', 'argument', 'this', 'that']:
                self.write_pop_to_referenced_segment(segment, index)
            elif segment in ['pointer', 'temp']:
                self.write_pop_to_fixed_segment(segment, index)
            elif segment == 'static':
                self.write_pop_to_a()
                self.write_sentences([
                    'D=M',
                    f'@{self.current_file_name}.{index}',
                    'M=D'
                ])

    def write_push_from_referenced_segment(self, segment, index):
        label = self.get_label_by_segment(segment)
        self.write_sentences([f'@{label}', 'A=M'])

        index_number = int(index)
        if index_number > 0:
            self.write_sentences(['A=A+1'] * index_number)

        self.write_sentences(['D=M'])
        self.write_push_from_d()

    def write_push_from_fixed_segment(self, segment, index):
        label = self.get_label_by_segment(segment)
        self.write_sentences([f'@{label}'])

        index_number = int(index)
        if index_number > 0:
            self.write_sentences(['A=A+1'] * index_number)

        self.write_sentences(['D=M'])
        self.write_push_from_d()

    def write_pop_to_referenced_segment(self, segment, index):
        self.write_pop_to_a()

        label = self.get_label_by_segment(segment)
        self.write_sentences([
            'D=M',
            f'@{label}',
            'A=M'
        ])

        index_number = int(index)
        if index_number > 0:
            self.write_sentences(['A=A+1'] * index_number)

        self.write_sentences(['M=D'])

    def write_pop_to_fixed_segment(self, segment, index):
        self.write_pop_to_a()

        label = self.get_label_by_segment(segment)
        self.write_sentences(['D=M', f'@{label}'])

        index_number = int(index)
        if index_number > 0:
            self.write_sentences(['A=A+1'] * index_number)

        self.write_sentences(['M=D'])

    def get_label_by_segment(self, segment):
        labels = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
            'pointer': '3',
            'temp': '5'
        }
        return labels[segment]

    def write_label(self, label):
        self.write_sentences([f'({label})'])

    def write_goto(self, label):
        self.write_sentences([
            f'@{label}',
            '0;JMP'
        ])

    def write_if(self, label):
        self.write_pop_to_a()
        self.write_sentences([
            'D=M',
            f'@{label}',
            'D;JNE'
        ])

    def write_call(self, function_name, num_args):
        self.write_sentences([
            f'@RETURN_ADDRESS_{self.label_for_return_address}',
            'D=A'
        ])
        self.write_push_from_d()

        self.write_sentences([
            '@LCL',
            'D=M',
        ])
        self.write_push_from_d()

        self.write_sentences([
            '@ARG',
            'D=M',
        ])
        self.write_push_from_d()

        self.write_sentences([
            '@THIS',
            'D=M',
        ])
        self.write_push_from_d()

        self.write_sentences([
            '@THAT',
            'D=M',
        ])
        self.write_push_from_d()

        self.write_sentences([
            '@SP',
            'D=M',
            f'@{num_args}',
            'D=D-A',
            '@5',
            'D=D-A',
            '@ARG',
            'M=D',
            '@SP',
            'D=M',
            '@LCL',
            'M=D',
            f'@{function_name}',
            '0;JMP',
            f'(RETURN_ADDRESS_{self.label_for_return_address})'
        ])

        self.label_for_return_address += 1

    def write_return(self):
        self.write_sentences([
            '@LCL',
            'D=M',
            '@R13',
            'M=D',
            '@5',
            'D=A',
            '@R13',
            'A=M-D',
            'D=M',
            '@R14',
            'M=D'
        ])

        self.write_pop_to_a()

        self.write_sentences([
            'D=M',
            '@ARG',
            'A=M',
            'M=D',

            '@ARG',
            'D=M+1',
            '@SP',
            'M=D',

            '@R13',
            'AM=M-1',
            'D=M',
            '@THAT',
            'M=D',

            '@R13',
            'AM=M-1',
            'D=M',
            '@THIS',
            'M=D',

            '@R13',
            'AM=M-1',
            'D=M',
            '@ARG',
            'M=D',

            '@R13',
            'AM=M-1',
            'D=M',
            '@LCL',
            'M=D',

            '@R14',
            'A=M',
            '0;JMP'
        ])

    def write_function(self, function_name, num_locals):
        self.write_sentences([f'({function_name})', 'D=0'])
        for i in range(int(num_locals)):
            self.write_push_from_d()

    def write_push_from_d(self):
        self.write_sentences(['@SP', 'A=M', 'M=D', '@SP', 'M=M+1'])

    def write_pop_to_a(self):
        self.write_sentences(['@SP', 'M=M-1', 'A=M'])

    def close(self):
        self.current_file.close()
