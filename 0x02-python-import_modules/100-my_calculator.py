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
        result = mul(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == "+":
        result = add(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, result))
