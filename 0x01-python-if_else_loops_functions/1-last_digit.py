#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

str_number = str(number)
last_digit = str_number[-1]
int_l_digit = int(last_digit)

if int_l_digit > 5:
    print("Last digit of ", number, "is ", last_digit, " and is greater than 5.", end="\n")
elif int_l_digit < 6 and int_l_digit != 0:
    print("Last digit of ", number, "is ", last_digit, " and is less than 6 and not 0.", end="\n")
elif int_l_digit == 0:
    print("Last digit of ", number, "is ", last_digit, " and is zero", end="\n")


