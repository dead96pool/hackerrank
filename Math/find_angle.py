"""

https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png
is a right triangle, 90 at B.
Therefore, angleABC = 90.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and AC.
Your task is to find MBC (angle detha, as shown in the figure) in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
0 < AB <= 100
0 < BC <= 100
lengths of AB and BC are natural numbers.

Output Format
Output MBC in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input
10
10

Sample Output
45°

"""

from math import atan, degrees

ab =int(input())
bc = int(input())

angle = round(degrees(atan(ab/bc)))

print("%d\N{DEGREE SIGN}" %angle)