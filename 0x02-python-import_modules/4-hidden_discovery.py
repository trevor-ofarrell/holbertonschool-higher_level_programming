#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for seg in dir(hidden_4):
        if seg[:2] != "__":
            print(seg)
