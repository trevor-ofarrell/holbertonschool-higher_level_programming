#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[:1] = None
    tup = (len(sentence), sentence[:1])
    return tup
