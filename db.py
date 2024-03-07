def read_file(path):
    words_list = []
    with open(path, encoding="utf-8") as file:
        for line in file.readlines():
            words_list.append(line.split(" "))
    return words_list
