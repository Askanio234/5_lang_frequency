import os
import argparse
import collections
import re


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r"\w+", text.lower())
    return collections.Counter(words).most_common(10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Путь до файла")
    args = parser.parse_args()
    if load_data(args.filepath) is not None:
        top_ten_words = get_most_frequent_words((load_data(args.filepath)))
        print("Десять наиболее часто употребляемых слов в данном тексте это:")
        for word in top_ten_words:
            print(word)
    else:
        print("Некорректный путь до файла")
