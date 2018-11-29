#!usr/bin/env python3.6


import cmath
import math
import sys


SQUARED = "\N{SUPERSCRIPT TWO}"
ARROW = "\N{RIGHTWARDS ARROW}"
if not sys.platform.startswith("linux"):
    SQUARED = "^2"
    ARROW = "->"




def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
            print("zero is not allowed")
            x = None
        except ValueError as err:
            print(err)
    return x


print("ax" + SQUARED + " + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)


x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

equation = "{0}x{1} ".format(a, SQUARED)
if b != 0:
    if b < 0:
        equation += "- {0}x ".format(abs(b))
    else:
        equation += "+ {0}x ".format(b)
if c != 0:
    if c <0:
        equation += "- {0} ".format(abs(c))
    else:
        equation += "+ {0} ".format(c)
equation += "= 0 {1} x = {0}".format(x1, ARROW)
if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)
