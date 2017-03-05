import os
import argparse
import collections
import re


NUMBER_OF_WORDS = 10


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, number_of_words):
    words = re.findall(r"\w+", text.lower())
    return collections.Counter(words).most_common(number_of_words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Путь до файла")
    args = parser.parse_args()
    if load_data(args.filepath) is not None:
        top_number_of_words = get_most_frequent_words(
                                load_data(args.filepath), NUMBER_OF_WORDS)
        print("{} наиболее часто употребляемых слов"
            " в данном тексте это:".format(NUMBER_OF_WORDS))
        for word in top_number_of_words:
            print(word)
    else:
        print("Некорректный путь до файла")
