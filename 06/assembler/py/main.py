import sys
from os import path
from lib.parser import Parser


def main():
    input_path = sys.argv[1]
    file_name = path.basename(input_path).split(".")[0]
    output_path = path.dirname(input_path) + "/" + file_name + ".hack"

    parser = Parser(input_path)

    with open(output_path, "w") as f:
        f.write("\n".join(parser.lines))


if __name__ == "__main__":
    main()
