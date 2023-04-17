"""
License: Apache
Organization: UNIR
"""

import os
import sys


DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER_ASCENDING = True


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
    order_ascending = DEFAULT_ORDER_ASCENDING

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order_ascending = sys.argv[3].lower() == "yes"
    else:
        print("The file must be specified as the first argument") #= print("Se debe indicar el fichero como primer argumento")
        print("The second argument indicates whether you want to remove duplicates") #= print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)


    print(f"The words of the file {filename} will be read.") #= print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist") #= print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, order_ascending))
