import sys

from lib.parser import Parser
from lib.code_writer import CodeWriter
from lib.constants import C_ARITHMETIC, C_CALL, C_FUNCTION, C_GOTO, C_IF, C_LABEL, C_POP, C_PUSH, C_RETURN


def main():
    input_path = sys.argv[1]

    parser = Parser(input_path)
    code_writer = CodeWriter(input_path)

    while parser.has_more_command():
        print(parser.command_type())
        if parser.command_type() == C_PUSH or parser.command_type() == C_POP:
            segment = parser.arg1()
            index = parser.arg2()
            code_writer.writePushPop(parser.command_type(), segment, index)
        parser.advance()

    code_writer.close()


if __name__ == "__main__":
    main()
