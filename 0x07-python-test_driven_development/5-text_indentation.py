#!/usr.bin/python3
def text_indentation(text):

    """add new line at ":, ?, ." shown delims
    Args: text(str) - given string

    """

    if isinstance(text, str) is False or not text:
        raise TypeError("text must be a string")

    ret = ''
    for i in text:
        ret += i
        if i in "?.:":
            print(ret.strip())
            print('')
            ret = ""
    print(ret.strip())
