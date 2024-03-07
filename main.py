import functions


def main():
    caminho = input("Digite o caminho do arquivo:")
    functions.number_of_words(caminho)
    functions.biggest_words(caminho)
    functions.most_appeared_vowel(caminho)
    functions.sufix_checker(caminho)


if __name__ == "__main__":
    main()
