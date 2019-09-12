#!/usr/bin/python3
import calculator_1 as calc
a = 10
b = 5
print(a, "+", b, "=", "{:d}".format(calc.add(a, b)))
print(a, "-", b, "=", "{:d}".format(calc.sub(a, b)))
print(a, "*", b, "=", "{:d}".format(calc.mul(a, b)))
print(a, "/", b, "=", "{:d}".format(calc.div(a, b)))
