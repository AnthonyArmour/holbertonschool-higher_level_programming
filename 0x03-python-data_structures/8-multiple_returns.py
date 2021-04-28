#!/usr/bin/python3
def multiple_returns(sentence):
    tp = tuple()
    if len(sentence) == 0:
        tp = (0, None)
    else:
        tp = (len(sentence), sentence[0])
    return tp
