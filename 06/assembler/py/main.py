import sys
from os import path

from lib.parser import Parser
from lib.code import Code
from lib.symbol_table import SymbolTable
from lib.constants import A_COMMAND, C_COMMAND, L_COMMAND


def main():
    input_path = sys.argv[1]
    file_name = path.basename(input_path).split(".")[0]
    output_path = path.dirname(input_path) + "/" + file_name + ".hack"

    parser = Parser(input_path)
    code = Code()
    symbol_table = SymbolTable()
    rom_address = 0
    ram_address = 16

    while parser.has_more_command():
        if parser.command_type() == A_COMMAND or parser.command_type() == C_COMMAND:
            rom_address += 1
        elif parser.command_type() == L_COMMAND:
            symbol = parser.symbol()
            if not symbol_table.contains(symbol):
                address = str(rom_address).zfill(16)[-6:]
                symbol_table.add_entry(symbol, address)

        parser.advance()

    parser.line_counter = 0
    parser.current_command = parser.lines[0]

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
            print("======")
            print("C")
            print("111" + comp + dest + jump)
        elif parser.command_type() == A_COMMAND:
            symbol = parser.symbol()
            if not symbol.isnumeric():
                if symbol_table.contains(symbol):
                    address = symbol_table.get_address(symbol)
                else:
                    address = "0x" + str(ram_address).zfill(16)[-4:]
                    symbol_table.add_entry(symbol, address)
                    ram_address += 1
                machine_code.append(
                    str(bin(int(address, 16)).split("b")[1]).zfill(16))
                print("======")
                print("A-1")
                print(str(bin(int(address, 16)).split("b")[1]).zfill(16))
            else:
                binary = str(bin(int(symbol, 16)).split("b")[1]).zfill(16)
                machine_code.append(binary)
                print("======")
                print("A-2")
                print(str(bin(int(symbol, 16)).split("b")[1]).zfill(16))

        parser.advance()

    with open(output_path, "w", encoding="utf-8") as f:
        for machine_line in machine_code:
            f.write(machine_line + "\n")


if __name__ == "__main__":
    main()
