"""

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if i belongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints
1 <= n <= 10**5
1 <= m <= 10**5
1 <= Any integer in the input <= 10**9

Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format
Output a single integer, your total happiness.

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1

Explanation
You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. 
The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1 = 1.

"""
happy = 0

#n is the count of input array
#m is the count of both disjoint sets A and B
n, m = map(int, input().split())

#taking input array as list
array = list(map(int, input().split()))

# A and B sets 
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# !!!!!!!!!!!!!!!!!reduce time
for val in array:
    if val in A:
        happy += 1
    elif val in B:
        happy -= 1

print(happy)
