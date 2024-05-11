import random
import numpy

print(random.randint(16, 275))
x = input("Enter number x: ")
y = input("Enter number y: ")
print (f"x**y = {int(x)**int(y)}")
print (f"log(x) = {numpy.log2(int(x))}")