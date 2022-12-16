"""
Bot Clean

link: https://www.hackerrank.com/challenges/botclean?isFullScreen=true&hr_b=1

"""

#!/usr/bin/python
import math
# Head ends here
def abs_distance(po1, po2):
    return math.sqrt((po1[0] - po2[0])**2 + (po1[1] - po2[1])**2)

def next_move(posr, posc, board):
    abs_dist = {}
    pos_dirty = []
    for idx, row in enumerate(board):
        for idy, char in enumerate(row):
            if char == "d":
                pos_dirty.append((idx,idy))
            
    print(pos_dirty)

    for x,y in pos_dirty:
        abs_dist[x,y] = abs_distance((posr,posc),(x,y))

    abs_dist = dict(sorted(abs_dist.items(), key = lambda item: item[1]))
    print(abs_dist)

    distance = list(abs_dist.keys())
    print(distance)

    difference_r = distance[0][0] - posr
    difference_c = distance[0][1] - posc

    print(difference_r,difference_c)
    if difference_r == difference_c == 0:
        move = "CLEAN"
    elif abs(difference_r) < abs(difference_c):
        move = move = "".join(["RIGHT" if difference_c > 0 else "LEFT"])
    else:
        move = "".join(["DOWN" if difference_r > 0 else "UP"])
                    
    print(move)


# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

