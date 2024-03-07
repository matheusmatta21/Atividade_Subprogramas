import db


def number_of_words(path):
    file_array = db.read_file(path)
    lenghts_sum = 0
    for index in range(0, len(file_array)):
        lenghts_sum += len(file_array[index])
    print(f"Existem {lenghts_sum} palavras.\n")


def biggest_words(path):
    file_array = db.read_file(path)
    biggest_words_list = []
    biggest_word = ""
    concatenation = ""
    for i in range(0, len(file_array)):
        for j in range(0, len(file_array[i])):
            word = file_array[i][j].strip()
            if word == biggest_word:
                continue
            elif len(word) > len(biggest_word) and len(word) != 0:
                biggest_word = word

            elif len(word) == len(biggest_word) and len(word) != 0:
                concatenation = biggest_word + " " + word  # o len dela fica imenso
    if concatenation == "":
        biggest_words_list.append(biggest_word)
    else:
        if biggest_word in concatenation:
            pass
        else:
            biggest_words_list.append(biggest_word)
        if len(biggest_word) > len(concatenation):
            pass
        else:
            concatenation_list = concatenation.split(" ")
            for i in range(0, len(concatenation_list)):
                biggest_words_list.append(concatenation_list[i])
    print("Maior(es) palavra(s):\n")
    for i in range(0, len(biggest_words_list)):
        print(f"{biggest_words_list[i]} -> {len(biggest_words_list[i])} caracteres\n")


def most_appeared_vowel(path):
    file_array = db.read_file(path)
    vowels_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for i in range(0, len(file_array)):
        for j in range(0, len(file_array[i])):
            for k in range(0, len(file_array[i][j])):
                char = file_array[i][j][k].lower()
                if char in vowels_dict:
                    vowels_dict[char] += 1
    max_vowel = max(vowels_dict, key=vowels_dict.get)
    print(f"A vogal que mais apareceu foi a vogal '{max_vowel}'.\n")


def sufix_checker(path):
    file_array = db.read_file(path)
    for i in range(0, len(file_array)):
        for j in range(0, len(file_array[i])):
            word = file_array[i][j].strip()
            if "ção" in word:
                print(f"Liteal 'ção' indentificado na linha {i + 1}\n")
