#!/usr/bin/python3
import sys
argname = 0
i = 0
if len(sys.argv) == 2:
    argname = "argument:"
elif len(sys.argv) == 1:
    argname = "arguments."
elif len(sys.argv) > 2:
    argname = "arguments:"
print(len(sys.argv) - 1, argname)
for i in range(1, len(sys.argv)):
    print("{}{}".format(i, ':'), sys.argv[i])
