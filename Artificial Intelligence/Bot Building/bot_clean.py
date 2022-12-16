"""
Bot Clean
link: https://www.hackerrank.com/challenges/botclean?isFullScreen=true&hr_b=1

"""
#!/usr/bin/python
# Head ends here
"""
1 2
--d-d
-db-d
--dd-
--d--
----d

b - - - d 
- d - - d
- - d d -
- - d - -
- - - - d
"""


def next_move(posr, posc, board):
    min_move = len(board[0])
    
    for idc, char in enumerate(board[posr]):
        if char == "d":
            dirt_dist = idc - posc
            
            #print("idc:%d,pos:%d,dirt_dist:%d"%(idc,posc,dirt_dist))
        
            if abs(dirt_dist) < abs(min_move):
                min_move = dirt_dist
                #print("min_move:",min_move)

    if min_move < len(board[0]):
        if min_move == 0:
            print("CLEAN")
        elif min_move > 0:
            print("RIGHT")
        else:
            print("LEFT")
    else:
        print("DOWN")
            

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
