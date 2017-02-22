import os
import itertools


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    word_list = text.split()
    unique_word_list = []
    for word in word_list:
        if (word not in unique_word_list) and word.isalnum():
            unique_word_list.append(word)
    word_count = []
    for word in unique_word_list:
        word_count.append(word_list.count(word))
    freq_pairs = zip(unique_word_list, word_count)
    sorted_freq_pairs = sorted(
                        freq_pairs, key=lambda freq_pairs: freq_pairs[1],
                        reverse=True)
    return sorted_freq_pairs


if __name__ == '__main__':
    filepath = input("Введите путь до файла: ")
    if load_data(filepath) is not None:
        sorted_freq_pairs = get_most_frequent_words((load_data(filepath)))
        top_ten_words = itertools.islice(sorted_freq_pairs, 10)
        for word in top_ten_words:
            print(word)
    else:
        print("Некорректный путь до файла")
