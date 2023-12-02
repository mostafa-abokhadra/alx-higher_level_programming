#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    Tuple = (len(sentence), sentence[0])
    return Tuple
