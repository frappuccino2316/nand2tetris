def main():
    # 実際はこちらを変換したい
    # path = "../../pong/Pong.asm"
    # サンプル
    path = "../../add/Add.asm"
    with open(path) as f:
        contents = f.read()
        print(contents)


if __name__ == "__main__":
    main()
