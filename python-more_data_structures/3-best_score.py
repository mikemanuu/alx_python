#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    x = list(a_dictionary.keys())[0]
    biggest_value = a_dictionary[x]
    for i, j in a_dictionary.items():
        if j > biggest_value:
            biggest_value = j
            x = i
    return (x)
