class Parser:
    def __init__(self, input_path):
        self.input_path = input_path

    def delete_comment(self):
        with open(self.input_path) as f:
            raw_contents = f.read()
            splitted_lines = raw_contents.replace(" ", "").splitlines()

            deleted_comment_lines = []
            for line in splitted_lines:
                if line[0:2] == "//" or line.isspace() or line == "":
                    continue
                deleted_comment_lines.append(line)

            return "\n".join(deleted_comment_lines)
