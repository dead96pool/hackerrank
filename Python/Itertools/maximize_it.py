"""

link: https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

"""

from itertools import product

def max_it(num_list, modd):

    max_sum = 0
    for comb in product(*num_list):
        cur_sum = sum(x**2 for x in comb)%modd
        max_sum = max(max_sum, cur_sum)

    return max_sum


list_count, modd = map(int, input().split())
num_list = []

for _ in range(list_count):
    num_list.append(list(map(int, input().split()))[1:])

print(max_it(num_list, modd))