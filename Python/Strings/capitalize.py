#!/bin/python3
#HackerRank > Strings > Capitalize!
"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format
A single line of input containing the full name, S.

Constraints
0 < len(S) < 1000
The string consists of alphanumeric characters and spaces.


Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format
Print the capitalized string, S.

Sample Input
chris alan

Sample Output
Chris Alan

"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = ""
    name_list = s.split(" ")

    for c in name_list:
        name += c[0:1].upper() + c[1:] + " "
    return name

if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)
