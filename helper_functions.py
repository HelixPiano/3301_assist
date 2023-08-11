import numpy as np


def convert_text_to_index(input_text):
    latin_fragments = ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 'T', 'B', 'E',
                       'M', 'L', 'ING', 'OE', 'D', 'A', 'AE', 'Y', 'IA', 'EA']

    e2p = {}
    for i in range(0, 29):
        e2p[latin_fragments[i]] = i
    e2p["IO"] = e2p["IA"]
    e2p["K"] = e2p["C"]
    e2p["NG"] = e2p["ING"]
    e2p["Z"] = e2p["S"]
    e2p["Q"] = e2p["C"]
    e2p["V"] = e2p["U"]

    input_text = input_text.upper().replace("QU", "KW")
    input_text = input_text.replace("Q", "K")

    text_as_index = []
    skip = 0
    for index, value in enumerate(input_text):
        if skip:
            skip -= 1
            continue
        if input_text[index:index + 3] in e2p:
            text_as_index.append(e2p[input_text[index:index + 3]])
            skip = 2
            continue
        elif input_text[index:index + 2] in e2p:
            text_as_index.append(e2p[input_text[index:index + 2]])
            skip = 1
        else:
            text_as_index.append(e2p[input_text[index]])
    return np.asarray(text_as_index)
