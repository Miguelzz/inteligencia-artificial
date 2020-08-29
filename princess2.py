#


def position(n,grid):
    pos=()
    for i in range(n):
        if(pos): break
        for j in range(5):
            if(grid[i][j]=='p'):
                pos = (i, j)
                break
    return pos



def nextMove(n,br, bc, grid):
    dr, dc = position(n,grid)
    if(dc == bc and dr == br): result = 'CLEAN'

    if(br > dr): return 'UP'
    elif(br < dr): return 'DOWN'

    elif(bc > dc): return 'LEFT'
    elif(bc < dc): return 'RIGHT'

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))