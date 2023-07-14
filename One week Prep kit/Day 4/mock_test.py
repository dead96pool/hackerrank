"""
Truck Tour
link: https://www.hackerrank.com/test/3em71ltlfrk/questions/6sqmn1811gk

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    #first-petrol | second-dist to next pump
    #1km per liter of perol

    pos = 0

    for idx, value in enumerate(petrolpumps):

        if value[0] - value[1] < 0:
            pos = idx + 1

    return pos



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
