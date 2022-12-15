"""

bot saves princess
link: https://www.hackerrank.com/challenges/saveprincess?isFullScreen=true&hr_b=1

"""

#!/usr/bin/python

def displayPathtoPrincess(m,grid):
#print all the moves here
    
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = [idx, row.index('p')]
        if 'm' in row:
            bot = [idx, row.index('m')]
    
    row_col = [x-y for (x,y) in zip(princess,bot) ]
    row = princess[0] - bot[0]
    col = princess[1] - bot[1]
    
    #positive value mean down or right

    moves = "".join(["DOWN\n"*abs(row) if row > 0 else "UP\n"*abs(row),
                    "RIGHT\n*"*abs(col) if col > 0 else "LEFT\n"*abs(col)])

    print(moves)

    """while row !=0 and col != 0:
        if row < 0:
            print("UP")
            row += 1
        else:
            print("DOWN")
            row -= 1

        if col < 0:
            print("LEFT")
            col += 1
        else:
            print("RIGHT")
            col -= 1

"""
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
