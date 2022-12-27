"""

New Year chaos
link: https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
"""
2
5
2 1 5 3 4
5
2 5 1 3 4
"""
def minimumBribes(q):
    # Write your code here
    total_count = 0
    for i in range(len(q)-1,0,-1):
        count = 0
        for j in range(i):
            if q[j]>q[j+1]:
                count += 1
                total_count += 1
                q[j], q[j+1] = q[j+1], q[j]
            print(q)

        if count > 2:
            print("Too Chaotic")
            break

    print(total_count)




if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
