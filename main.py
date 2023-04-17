"""
License: Apache
Organization: UNIR
"""

import os
import sys


DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def read_words_from_file(file_path):
    words_set = set()
    with open(file_path, "r") as file:
        for line in file:
            word = line.strip()
            if word:
                words_set.add(word)
    return sorted(words_set)


def get_word_list(filename=DEFAULT_FILENAME):
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        return read_words_from_file(file_path)
    else:
        print(f"El fichero {filename} no existe")
        return ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]


def remove_duplicates_from_list(items):
    return list(set(items))


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=(not ascending))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    word_list = get_word_list(filename)
    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
