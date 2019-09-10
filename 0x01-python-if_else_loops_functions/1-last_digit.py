#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10 if number > 10 else number % -10
print("Last digit of", number, "is ", end='')
if x > 5:
    print(x, "and is greater than 5")
elif x == 0:
    print(x, "and is 0")
elif x < 6 and x is not 0:
    print(x, "and is less than 6 and not 0")
