#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
# this program is to learn more about the integer data type
#  and how to use it in Python
import random

# GET a random user integer
user_integer = int(input("Enter an integer: "))

# clear
# Check if the input is an integer
user_input = int(user_integer)
if user_input != int(user_integer):
    print("Invalid input! Please enter an integer.")

# check the nature of the integer
if user_integer < 0:
    print(f"{user_integer} is a negative integer.")
elif user_integer > 0:
    print(f"{user_integer} is a positive integer.")
else:
    print(f"{user_integer} is zero.")
