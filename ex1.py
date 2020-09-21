"""Write a program assigns an angle in degrees to variable called degrees. This program
converts this angle to radians and assigns it to a variable called radians. To convert
from degrees to radians, use the formula radians = degrees*3.14/180 (3.14 = pi). Print
angle in both degrees and radians"""
import random

def converter(deg):
    rad = deg*3.14/180
    return rad

degrees = random.randint(1,361)
radians = converter(degrees)


print("Degrees: ",degrees)
print("Radians: ",radians)

