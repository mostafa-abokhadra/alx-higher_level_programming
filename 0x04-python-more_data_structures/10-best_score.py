#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        listy = a_dictionary.values()
        maxy = max(listy)
        for i in a_dictionary:
            if a_dictionary[i] == maxy:
                return i
