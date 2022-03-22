def main():
    input_path = "../../add/Add.asm"
    output_path = "../../add/Add.hack"

    contents = ""

    with open(input_path) as f:
        contents = f.read()
        # print(contents)

    with open(output_path, "w") as f:
        content_of_lines = contents.splitlines()

        deleted_comment_content = []
        for line in content_of_lines:
            if line[0:2] == "//" or line.isspace() or line == "":
                continue
            deleted_comment_content.append(line)

        f.write("\n".join(deleted_comment_content))


if __name__ == "__main__":
    main()
