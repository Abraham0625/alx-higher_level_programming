#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
str1 = "Last digit of"
str2 = "is"
if lastdigit > 5:
    print("{} {} {} {} and is greater than 5".format(str1, number, str2, lastdigit))
elif lastdigit == 0:
    print("{} {} {} {} and is 0".format(str1, number, str2, lastdigit))
elif lastdigit < 6:
    print("{} {} {} {} and is less than 6 and not 0".format(str1, number, str2, lastdigit))
