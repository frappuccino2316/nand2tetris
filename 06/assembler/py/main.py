from lib.parser import Parser


def main():
    input_path = "../../add/Add.asm"
    output_path = "../../add/Add.hack"

    parser = Parser(input_path)

    with open(output_path, "w") as f:
        f.write(parser.delete_comment())


if __name__ == "__main__":
    main()
