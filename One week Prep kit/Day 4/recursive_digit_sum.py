"""

Recursive Digit Sum
link: https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four&h_r=next-challenge&h_v=zen

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    #fidn the total of the digits in list of string n
    #the sum should be repeated k times
    total = sum(map(int,list(n)))*k
    
    #if the digit is just 1 length long, return the digit
    if len(str(total)) == 1:
        return total
    
    #else send the sum again to the fucntions
    return superDigit(str(total),1)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
