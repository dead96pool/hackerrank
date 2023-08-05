"""

hacker rank python challenge
link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

"""

from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)
s = sorted(s)

for comb in combinations_with_replacement(s, k):
    print("".join(comb))
