#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("{}".format('Last digit of'), number, end=" ")
if number < 0:
    number = number * -1
print("{}".format('is'), "{:d}".format(number % 10), end=" ")
number = number % 10
if number > 5:
    print("{}".format('and is greater than 5'))
elif number == 0:
    print("{}".format('and is 0'))
else:
    print("{}".format('and is less than 6 and not 0'))
