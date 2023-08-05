"""
link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

"""

import re

count = int(input())
pattern = r"^[7-9]\d{9}$"


for _ in range(count):
    number = input()

    if re.match(pattern, number):
        print("YES")
    else:
        print("NO")