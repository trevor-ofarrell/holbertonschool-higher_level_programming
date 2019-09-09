#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = '{:.28}'.format(str[-90:]) + '{:.5}'.format(str[-22:]) + str[:6]
print(str)
