#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if op == '\*':
        result = mul(int(a), int(b))
    elif op == '-':
        result = sub(int(a), int(b))
    elif op == "+":
        result = add(int(a), int(b))
    elif op == '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(int(a), op, int(b), '=', int(result))
