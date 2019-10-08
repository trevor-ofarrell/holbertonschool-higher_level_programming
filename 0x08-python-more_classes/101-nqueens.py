#!/usr/bin/python3
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(argv[1])

except:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)


def solve(N, i, a, b, c):

    """function to determine squares where a queen can be placed without
       attacking another"""

    if i < int(N):
        for j in range(N):

            if j not in a and i+j not in b and i-j not in c:

                for solution in solve(N, i+1, a+[j], b+[i+j], c+[i-j]):

                    yield solution
    else:
        yield a

for solution in solve(N, 0, [], [], []):

    """function to print representaion of squares that are valid"""

    e1 = enumerate(solution)

    print("[", end='')

    for ele in e1:

        print("{}".format(list(ele)), end='')

    print("]")
