with open("en-ru.txt", "r", encoding="utf-8") as dict_file:
    en_ru_dict = dict_file.readlines()

ru_en_dict = {}

for line in en_ru_dict:
    en_word, ru_word = line.strip().split(" - ")
    for ru_word_item in ru_word.split(", "):
        if ru_word_item in ru_en_dict:
            ru_en_dict[ru_word_item] += ", " + en_word
        else:
            ru_en_dict[ru_word_item] = en_word

sorted_ru_en_dict = sorted(ru_en_dict.items(), key=lambda x: x[0])

with open("ru-en.txt", "w", encoding="utf-8") as new_dict_file:
    for ru_word, en_word in sorted_ru_en_dict:
        new_dict_file.write(f"{ru_word} - {en_word}\n")