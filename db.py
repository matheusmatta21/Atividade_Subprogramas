def read_file(path):
    words_list = []
    with open(path, encoding="utf-8") as file:
        words_list = [line.split(" ") for line in file.readlines()]
    return words_list
