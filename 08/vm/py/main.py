import sys
import glob

from lib.parser import Parser
from lib.code_writer import CodeWriter
from lib.constants import C_ARITHMETIC, C_CALL, C_FUNCTION, C_GOTO, C_IF, C_LABEL, C_POP, C_PUSH, C_RETURN


def main():
    input_path = sys.argv[1]
    vm_files = glob.glob(f'{input_path}/*.vm')

    code_writer = CodeWriter(input_path)

    for file in vm_files:
        translate(code_writer, file)


def translate(code_writer, file):
    parser = Parser(file)
    code_writer.set_file_name(file)

    while parser.has_more_command():
        if parser.command_type() == C_PUSH or parser.command_type() == C_POP:
            segment = parser.arg1()
            index = parser.arg2()
            code_writer.write_push_pop(parser.command_type(), segment, index)
        elif parser.command_type() == C_ARITHMETIC:
            command = parser.arg1()
            code_writer.write_arithmetic(command)
        elif parser.command_type() == C_LABEL:
            command = parser.arg1()
            code_writer.write_label(command)
        elif parser.command_type() == C_GOTO:
            command = parser.arg1()
            code_writer.write_goto(command)
        elif parser.command_type() == C_IF:
            command = parser.arg1()
            code_writer.write_if(command)
        elif parser.command_type() == C_CALL:
            command = parser.arg1()
            code_writer.write_call(command)
        elif parser.command_type() == C_RETURN:
            code_writer.write_return()
        elif parser.command_type() == C_FUNCTION:
            first_command = parser.arg1()
            second_command = parser.arg2()
            code_writer.write_function(first_command, second_command)
        parser.advance()

    code_writer.close()


if __name__ == "__main__":
    main()
