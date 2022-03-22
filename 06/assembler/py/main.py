import sys
from os import path

from lib.parser import Parser
from lib.code import Code
from lib.constants import A_COMMAND, C_COMMAND, L_COMMAND


def main():
    input_path = sys.argv[1]
    file_name = path.basename(input_path).split(".")[0]
    output_path = path.dirname(input_path) + "/" + file_name + ".hack"

    parser = Parser(input_path)
    code = Code()

    machine_code = []

    while parser.has_more_command():
        if parser.command_type() == C_COMMAND:
            dest_mnemonic = parser.dest()
            comp_mnemonic = parser.comp()
            jump_mnemonic = parser.jump()

            dest = code.dest(dest_mnemonic)
            comp = code.comp(comp_mnemonic)
            jump = code.jump(jump_mnemonic)
            machine_code.append("111" + comp + dest + jump)
        elif parser.command_type() == A_COMMAND:
            # machine_code.append(bin(int(parser.symbol())).split("b")[1])
            binary = bin(int(parser.symbol())).split("b")[1].zfill(16)
            machine_code.append(binary)
        parser.advance()

    with open(output_path, "w", encoding="utf-8") as f:
        for machine_line in machine_code:
            f.write(machine_line + "\n")


if __name__ == "__main__":
    main()
