#!/usr/bin/python3
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = int(argv[1])

if isinstance(N, str):
    print("N must be a number")
    exit(1)

N = int(argv[1])

if not isinstance(N, int):
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

count = 0


def solve(N, i, a, b, c):
    if i < int(N):
        for j in range(N):
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(N, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a

for solution in solve(N, 0, [], [], []):
    e1 = enumerate(solution)
    for ele in e1:
        print("{}".format(list(ele)), end='')
    print()