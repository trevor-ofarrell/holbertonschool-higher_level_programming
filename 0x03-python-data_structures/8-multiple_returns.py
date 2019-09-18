#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[:1] = None
    tup = (len(sentence), sentence[:1])
    return tup
