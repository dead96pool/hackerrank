"""
BotClean Partially Observable
link: https://www.hackerrank.com/challenges/botcleanv2?isFullScreen=true&hr_b=1

"""
#!!!!!!!!!!!!!!!!!!!!!!!not working yet
#!/usr/bin/python3

def next_move(posx, posy, board):
   
    #find dirty cells
    #dirty_cells = [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == "d"]
    dirty_cells = []
    dirt_found = ""
    for idx, row in enumerate(board):
        for idy, col in enumerate(board[idx]):
            if col == "d":
                dirty_cells.append((idx,idy))
                dirt_found = "found"
    
    if dirt_found == "found":
        print(dirty_cells)
        best_cell = None
        best_dist = float("inf")
        for x,y in dirty_cells:
            if abs(posx - x) + abs(posy - y) < best_dist:
                best_dist = abs(posx - x) + abs(posy - y)
                best_cell = (x,y)
        print(best_cell, best_dist)
        #find move
        if board[posx][posy] != "d":
            if posx - best_cell[0] < 0:
                print("DOWN")
            elif posx - best_cell[0] > 0:
                print("UP")
            elif posy - best_cell[1] < 0:
                print("RIGHT")
            else:
                print("LEFT")
        else:
            print("CLEAN")
    else:
        if idx <= len(board)//2 and idy <= len(board[0])//2:
            print("DOWN")
        elif idx > len(board)//2 and idy <= len(board[0])//2:
            print("RIGHT")
        elif idx > len(board)//2 and idy > len(board[0])//2:
            print("UP")
        elif idx <= len(board)//2 and idy > len(board[0])//2:
            print("LEFT")
        
        
        
if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)