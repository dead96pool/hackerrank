"""
Bot save princess too(2)
link: https://www.hackerrank.com/challenges/saveprincess2?isFullScreen=true&hr_b=1

"""

# n is size of the grid
# r and c is the position of the bot



def nextMove(n,r,c,grid):
    for idx, row in enumerate(grid):
        if "p" in row:
            princess = (idx, row.index("p"))

    

    row = princess[0] - r
    col = princess[1] - c

    print(row,col)
    
    if abs(row) < abs(col):
        move = "".join(["LEFT\n" if col < 0 else "RIGHT\n"])
    else:
        move = "".join(["UP\n" if row < 0 else "DOWN\n"])


    return move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))