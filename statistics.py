import numpy as np


def count_words(text: str) -> int:
    return len(text.split())


def calculate_ioc(input_array):
    _, counts = np.unique(input_array, return_counts=True)
    ioc = 0

    for counted in counts:
        ioc += counted * (counted - 1)
    ioc = ioc / (len(input_array) * (len(input_array) - 1) / 29)

    print(ioc)


def count_doublets(input_array):
    number_of_doublets = np.sum(input_array[0:-1] == input_array[1::])
    print(f"Number of doublets: {number_of_doublets}")
    print(f"Doublets rate: {number_of_doublets / (len(input_array) - 1) * 100}%")
